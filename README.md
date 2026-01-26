# 30 Days of AI Challenge

A Streamlit application exploring Snowflake Cortex AI capabilities as part of the [30 Days of AI Challenge](https://discuss.streamlit.io/t/the-30-days-of-ai-challenge-starts-today/120455).

## Overview

This project demonstrates different AI and LLM features using Streamlit and Snowflake Cortex, building up skills over 30 days (in progress):

- **Day 1**: Basic AI completion with Cortex
- **Day 2**: Hello, Cortex! - Simple prompt interaction with usage management
- **Day 3**: Write Streams - Streaming responses with multiple methods
- **Day 4**: Caching - Optimizing performance with cached LLM calls
- **Day 5**: LinkedIn Post Generator - Practical application combining all concepts
- **Day 6**: LinkedIn Post Generator v2 - Enhanced version with usage management
- **Day 7**: LinkedIn Post Generator v3 - Advanced version with usage management and status indicators
- **Day 8**: Chat Interface - Interactive chat with Cortex AI and usage management
- **Day 9**: Understanding Session State - Demonstrating the difference between standard variables and session state
- **Day 10**: Your First Chatbot - A stateful chatbot with session state and usage management
- **Day 11**: Chatbot with History - Enhanced chatbot with conversation history and usage management
- **Day 12**: Chatbot with Streaming - Streaming responses in chat with usage management
- **Day 13**: System Prompts - Customizable chatbot personalities with usage management
- **Day 14**: Avatars & Error Handling - Custom avatars and robust error handling with usage management
- **Day 15**: Model Comparison Arena - Side-by-side model comparison with usage management
- **Day 16**: Batch Document Text Extractor - Extracting text from multiple files (PDF, TXT, MD) and saving to Snowflake for RAG
- **Day 17**: Data Preparation & Chunking - Loading, processing, and chunking customer reviews for RAG applications
- **Day 18**: Generating Embeddings for Customer Reviews - Converting text into 768-dimensional vectors to enable semantic search for RAG applications
- **Day 19**: Cortex Search for Customer Reviews - Creating a semantic search service for processed customer reviews
- **Day 20**: Querying Cortex Search - Searching and retrieving relevant text chunks using the search service
- **Day 21**: RAG with Cortex Search - Combining search results with LLM generation for grounded answers (Retrieve-Augment-Generate)
- **Day 22**: Chat with Your Documents - A conversational RAG chatbot powered by Cortex Search for interactive Q&A
- **Day 23**: LLM Evaluation & AI Observability - Measuring RAG quality (Context Relevance, Groundedness, Answer Relevance) using TruLens and Snowflake AI Observability
- **Day 24**: Working with Images (Multimodality) - Analyzing images using Snowflake Cortex `AI_COMPLETE` and stages
- **Day 25**: Voice Interface - Transcribing audio and interacting with AI using `AI_TRANSCRIBE` and Streamlit `audio_input`

## Features

### Core Functionality
- Integration with **Snowflake Cortex AI** models
- Support for multiple LLM models (Claude 3.5 Sonnet, Mistral Large, Llama 3.1)
- Multimodal capabilities (Image analysis and OCR)
- Voice processing (Audio transcription and interaction)
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
├── day8/
│   └── day8.py          # Chat interface with Cortex AI
├── day9/
│   └── day9.py          # Understanding Session State
├── day10/
│   └── day10.py         # First chatbot with state and usage management
├── day11/
│   └── day11.py         # Chatbot with history and usage management
├── day12/
│   └── day12.py         # Chatbot with streaming responses
├── day13/
│   └── day13.py         # Customizable chatbot with system prompts and usage management
├── day14/
│   └── day14.py         # Avatars and error handling with usage management
├── day15/
│   └── day15.py         # Model comparison arena with usage management
├── day16/
│   └── day16.py         # Batch document text extractor for RAG
├── day17/
│   └── day17.py         # Data preparation and chunking for RAG
├── day18/
│   └── day18.py         # Generating embeddings for customer reviews
├── day19/
│   └── day19.py         # Cortex Search for customer reviews
├── day20/
│   └── day20.py         # Querying Cortex Search
├── day21/
│   └── day21.py         # RAG with Cortex Search
├── day22/
│   └── day22.py         # Chat with documents using RAG
├── day23/
│   └── day23.py         # LLM evaluation and AI observability
├── day24/
│   └── day24.py         # Image analysis with multimodal AI
└── day25/
    └── day25.py         # Voice-enabled AI assistant
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
- claude-3-5-sonnet (Recommended default)
- mistral-large / mixtral-8x7b
- llama3.1-8b / llama3-70b
- pixtral-large (Vision)
- openai-gpt-4.1 / o4-mini

## Requirements

- Python 3.8+
- Streamlit 1.52.2+
- Snowflake Snowpark
- Snowflake Cortex access

See `requirements.txt` for full dependency list.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
