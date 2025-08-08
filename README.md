
# LangChain Utilities: Email Generator & Wikipedia Research Agent


This project contains two main utilities using the LangChain library and OpenAI's language models:
- **Email Generator**: Generate creative email content based on customizable prompts.
- **Wikipedia Research Agent**: Perform research tasks using Wikipedia and LLM-powered tools.


## Features
### Email Generator
- Uses LangChain's prompt templates for flexible email generation
- Integrates with OpenAI LLMs (e.g., GPT-3, GPT-4, or compatible models)
- Supports environment variable configuration for API keys
- Adjustable model parameters for creativity and response control

### Wikipedia Research Agent
- Uses LangChain's agent tools for Wikipedia and math
- Allows interactive research via command line
- Integrates OpenAI LLMs for reasoning and summarization

## Requirements
- Python 3.8+
- `langchain`
- `langchain_community` (if required by your code or dependencies)
- `openai`
- `python-dotenv`

## Installation
1. Clone this repository or download the project files.
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install langchain openai python-dotenv langchain_community
   ```

## Configuration
1. Create a `.env` file in the project root with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```


## Usage

### Email Generator
Run the email generator script:
```bash
python email_generator.py
```
You can customize the prompt and model parameters in `email_generator.py` to fit your needs.

### Wikipedia Research Agent
Run the Wikipedia research agent script:
```bash
python wikipedia_research.py
```
You will be prompted to enter a research task/question. The agent will use Wikipedia and LLM tools to answer it interactively.


## File Structure
- `email_generator.py` — Main script for generating emails
- `wikipedia_research.py` — Wikipedia research agent using LangChain tools
- `.env` — Environment variables (not included in version control)
- `README.md` — Project documentation

## License
This project is for educational and personal use. Please check the licenses of LangChain and OpenAI for commercial usage.
