# Email Generator with LangChain

This project is a simple email generator that uses the LangChain library and OpenAI's language models to generate creative email content based on customizable prompts.

## Features
- Uses LangChain's prompt templates for flexible email generation
- Integrates with OpenAI LLMs (e.g., GPT-3, GPT-4, or compatible models)
- Supports environment variable configuration for API keys
- Adjustable model parameters for creativity and response control

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
Run the email generator script:
```bash
python email_generator.py
```

You can customize the prompt and model parameters in `email_generator.py` to fit your needs.

## File Structure
- `email_generator.py` — Main script for generating emails
- `.env` — Environment variables (not included in version control)
- `README.md` — Project documentation

## License
This project is for educational and personal use. Please check the licenses of LangChain and OpenAI for commercial usage.
