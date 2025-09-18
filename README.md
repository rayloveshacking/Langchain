# AI Travel Agent

An AI-powered travel assistant that helps users find information about destinations, attractions, weather, and more.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set API Keys**:
   You need to set up API keys for the services used by the agent:
   
   - **Google API Key**: For the Gemini model
     - Get one from [Google AI Studio](https://aistudio.google.com/)
     - Set as environment variable: `GOOGLE_API_KEY=your_key_here`
   
   - **Tavily API Key**: For web search functionality
     - Get one from [Tavily AI](https://tavily.com/)
     - Set as environment variable: `TAVILY_API_KEY=your_key_here`

3. **Environment Variables**:
   Create a `.env` file in the project directory with your actual API keys:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```
   
   Alternatively, you can set the environment variables in your system.

## Usage

1. **Set your API keys** in the `.env` file (copy `.env.example` to `.env` and add your keys)

2. **Run the agent** with:
   ```bash
   python tools.py
   ```

To modify the query, edit the `tools.py` file and change the content in:
```python
inputs = {"messages": [HumanMessage(content="What are the top attractions in Paris?")]}
```

## Features

- Web search for travel information
- Weather information
- Destination recommendations
- Attraction details
- Travel tips and advice

## Customization

You can modify the agent's behavior by:
1. Changing the query in the main execution block
2. Updating the tool descriptions for more specific travel-related tasks
3. Adding new tools for specific travel functionalities

## Troubleshooting

If the agent is not working:
1. Check that you have set your API keys in the `.env` file
2. Verify that you have installed all required dependencies with `pip install -r requirements.txt`
3. Check the console output for error messages
4. Ensure your API keys are valid and have not exceeded their usage limits