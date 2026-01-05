import streamlit as st
from snowflake.snowpark.functions import ai_complete
import json

st.title(":material/smart_toy: Hello, Cortex!")

# Connect to Snowflake
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create() 

# Model and prompt
model = "claude-3-5-sonnet"
prompt = st.text_input("Enter your prompt:")

# Usage management (moved to module)
from usage import UsageManager

usage_mgr = UsageManager(st)
# app will show warnings when limits are reached.
session_remaining, daily_remaining, BYPASS_DAILY = usage_mgr.get_status()

# Run LLM inference
if st.button("Generate Response"):
    allowed, msg = usage_mgr.can_generate(prompt)
    if not allowed:
        st.warning(msg)
    else:
        usage_mgr.register_call()

        df = session.range(1).select(
            ai_complete(model=model, prompt=prompt).alias("response")
        )

        # Get and display response
        response_raw = df.collect()[0][0]
        response = json.loads(response_raw)
        st.write(response)


# Footer
st.divider()
st.caption("Day 2: Hello, Cortex! | 30 Days of AI")