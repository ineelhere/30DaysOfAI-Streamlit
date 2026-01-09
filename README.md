# 30 Days of AI Challenge

A Streamlit application exploring Snowflake Cortex AI capabilities as part of the [30 Days of AI Challenge](https://discuss.streamlit.io/t/the-30-days-of-ai-challenge-starts-today/120455).

## Overview

This project demonstrates different AI and LLM features using Streamlit and Snowflake Cortex, building up skills over 8 days:

- **Day 1**: Basic AI completion with Cortex
- **Day 2**: Hello, Cortex! - Simple prompt interaction with usage management
- **Day 3**: Write Streams - Streaming responses with multiple methods
- **Day 4**: Caching - Optimizing performance with cached LLM calls
- **Day 5**: LinkedIn Post Generator - Practical application combining all concepts
- **Day 6**: LinkedIn Post Generator v2 - Enhanced version with usage management
- **Day 7**: LinkedIn Post Generator v3 - Advanced version with usage management and status indicators
- **Day 8**: Chat Interface - Interactive chat with Cortex AI and usage management
- **Day 8**: Chat Interface - Interactive chat with Cortex AI and usage management

## Features

### Core Functionality
- Integration with **Snowflake Cortex AI** models
- Support for multiple LLM models (Claude 3.5 Sonnet, Mistral Large, Llama 3.1)
- Streaming response support with `st.write_stream()`
- Response caching for improved performance
- Built-in usage tracking and rate limiting

### Usage Management
- Per-session and daily usage tracking via `UsageManager`
- Configurable rate limits with environment variables or secrets
- Daily limit bypass option for testing
- File-backed persistence of usage data

## Project Structure

```
├── app.py                 # Main Streamlit app with day selector
├── usage.py              # Usage tracking and rate limiting module
├── requirements.txt      # Python dependencies
├── day1/
│   └── day1.py          # AI completion basics
├── day2/
│   └── day2.py          # Basic LLM interaction
├── day3/
│   └── day3.py          # Streaming responses
├── day4/
│   └── day4.py          # Cached LLM calls
├── day5/
│   └── day5.py          # LinkedIn post generator
├── day6/
│   └── day6.py          # LinkedIn post generator v2
├── day7/
│   └── day7.py          # LinkedIn post generator v3
└── day8/
    └── day8.py          # Chat interface with usage management
└── day8/
    └── day8.py          # Chat interface with Cortex AI
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ineelhere/30DaysOfAI-Streamlit.git
   cd 30DaysOfAI-Streamlit
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Snowflake connection**:
   - Create `.streamlit/secrets.toml` with your Snowflake credentials:
     ```toml
     [connections.snowflake]
     account = "your-account-identifier"
     user = "your-username"
     password = "your-password"
     warehouse = "your-warehouse"
     database = "your-database"
     schema = "your-schema"
     
     [max_daily_calls]
     max_daily_calls = 10
     ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser. Select a day from the sidebar to explore that day's demonstration.

## Configuration

### Environment Variables
- `MAX_DAILY_CALLS`: Maximum daily API calls (default: 10)
- `BYPASS_DAILY_LIMIT`: Set to "true" to bypass daily limits
- `USAGE_FILE_PATH`: Custom path for usage tracking file (default: `.daily_usage.tmp`)

### Secrets Configuration
Add to `.streamlit/secrets.toml`:
```toml
[connections.snowflake]
# Snowflake connection details

max_daily_calls = 10
bypass_daily_limit = false
```

## Key Components

### UsageManager
Manages API call limits and tracks usage:
- `get_status()`: Returns remaining calls and daily limits
- `can_generate(prompt)`: Checks if a call is allowed
- `register_call()`: Records a successful API call

### Models Supported
- claude-3-5-sonnet (default)
- mistral-large
- llama3.1-8b

## Requirements

- Python 3.8+
- Streamlit 1.52.2+
- Snowflake Snowpark
- Snowflake Cortex access

See `requirements.txt` for full dependency list.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
