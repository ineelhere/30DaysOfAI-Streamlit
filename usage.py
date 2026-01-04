import os
import logging
from datetime import date
from pathlib import Path
import streamlit as st


# Configure module logger
logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
logger.setLevel(logging.INFO)


class UsageManager:
    """Manage per-session and global daily usage with file-backed persistence."""

    def __init__(self, st_module=st, max_daily=None):
        self.st = st_module
        try:
            self.MAX_DAILY = int(
                os.environ.get("MAX_DAILY_CALLS", self.st.secrets.get("max_daily_calls", 10))
            ) if max_daily is None else int(max_daily)
        except Exception:
            self.MAX_DAILY = 10

        bypass_env = os.environ.get("BYPASS_DAILY_LIMIT")
        bypass_secret = self.st.secrets.get("bypass_daily_limit", False)
        self.BYPASS_DAILY = str(bypass_env if bypass_env is not None else bypass_secret).lower() in (
            "1",
            "true",
            "yes",
        )

        # Use temp file in working directory for usage tracking
        self.usage_file = Path(os.environ.get("USAGE_FILE_PATH", ".daily_usage.tmp"))
        self.today_str = date.today().isoformat()

        logger.info(
            "Initializing UsageManager: max_daily=%s, bypass=%s, usage_file=%s",
            self.MAX_DAILY,
            self.BYPASS_DAILY,
            str(self.usage_file),
        )

        # load or initialize
        self.usage = self._load_usage()
        if self.usage.get("date") != self.today_str:
            self.usage = {"date": self.today_str, "count": 0}
            self._save_usage()

    def _load_usage(self):
        """Load usage from temp file; format: date on line 1, count on line 2."""
        if not self.usage_file.exists():
            logger.info("Usage file not found; starting fresh for %s", self.today_str)
            return {"date": self.today_str, "count": 0}
        try:
            content = self.usage_file.read_text(encoding="utf-8").strip()
            lines = content.split("\n")
            if len(lines) >= 2:
                file_date = lines[0].strip()
                file_count = int(lines[1].strip())
                if file_date != self.today_str:
                    logger.info("Usage file is for a different date (%s); resetting", file_date)
                    return {"date": self.today_str, "count": 0}
                data = {"date": file_date, "count": file_count}
                logger.info("Loaded usage data: %s", data)
                return data
            else:
                logger.warning("Usage file format invalid; resetting")
                return {"date": self.today_str, "count": 0}
        except Exception as exc:
            logger.exception("Failed to load usage file: %s", exc)
            return {"date": self.today_str, "count": 0}

    def _save_usage(self):
        """Save usage to temp file; format: date on line 1, count on line 2."""
        try:
            # ensure parent exists
            if self.usage_file.parent and not self.usage_file.parent.exists():
                try:
                    self.usage_file.parent.mkdir(parents=True, exist_ok=True)
                except Exception:
                    logger.warning("Failed to create parent directory for usage file: %s", self.usage_file.parent)
            content = f"{self.usage['date']}\n{self.usage.get('count', 0)}"
            self.usage_file.write_text(content, encoding="utf-8")
            logger.info("Saved usage data: %s", self.usage)
        except Exception as exc:
            logger.exception("Failed to save usage data: %s", exc)

    def ensure_session(self):
        if "uses" not in self.st.session_state:
            self.st.session_state["uses"] = 0

    def get_status(self):
        self.ensure_session()
        session_remaining = 3 - self.st.session_state.get("uses", 0)
        daily_remaining = self.MAX_DAILY - self.usage.get("count", 0)
        logger.debug("Status: session_remaining=%s, daily_remaining=%s, bypass=%s", session_remaining, daily_remaining, self.BYPASS_DAILY)
        return session_remaining, daily_remaining, self.BYPASS_DAILY

    def can_generate(self, prompt: str):
        """Return (allowed: bool, message: str)."""
        if not self.BYPASS_DAILY and self.usage.get("count", 0) >= self.MAX_DAILY:
            logger.info("Blocked generate: daily limit reached (%s/%s)", self.usage.get("count", 0), self.MAX_DAILY)
            return False, "You have reached the daily limit. Please try again later."
        if self.st.session_state.get("uses", 0) >= 3:
            logger.info("Blocked generate: session limit reached (%s/3)", self.st.session_state.get("uses", 0))
            return False, "You've reached the 3-use limit for this session. Please try again later."
        if not prompt:
            logger.debug("Blocked generate: empty prompt")
            return False, "Please enter a prompt before generating a response."
        logger.debug("Allowed to generate: prompt present and within limits")
        return True, ""

    def register_call(self):
        prev_session = self.st.session_state.get("uses", 0)
        prev_count = self.usage.get("count", 0)
        self.st.session_state["uses"] = prev_session + 1
        if not self.BYPASS_DAILY:
            self.usage["count"] = prev_count + 1
            self._save_usage()
        logger.info("Registered call: session=%s->%s, daily=%s->%s", prev_session, self.st.session_state["uses"], prev_count, self.usage.get("count", "(bypassed)"))
