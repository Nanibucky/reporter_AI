# 📰 Reporter_AI using CrewAI

This project leverages CrewAI to build a collaborative AI-powered news reporting agent capable of researching, writing, and fact-checking articles.

## 🚀 Features
- **Automated Research**: Finds and synthesizes information on trending topics using Gemini (VertexAI) or any LLM.
- **Content Writing**: Generates insightful and engaging markdown articles.
- **Fact Verification**: Ensures accuracy and reliability of generated articles through automated verification.

## ⚙️ Tech Stack
- **CrewAI**: Manages collaborative AI agent workflows.
- **LiteLLM Integration**: Access to Gemini 1.5 Pro through Vertex AI or you can use the Openai.
- **Serper Dev Tool**: Enables advanced internet search capabilities.
- **Pydantic**: Data validation and settings management.

## 📁 Project Structure
```
.
├── agents.py        # AI agent definitions
├── tasks.py         # Task definitions for agents
├── tools.py         # External tool configurations
├── crew.py          # Main script to run CrewAI workflow
├── reported_data.md # Generated article output
└── .env             # Environment variables (API keys)
|_  requirements.txt # Install the required libraries and packages
```

## ⚙️ Setup
1. Clone this repository.
```bash
git clone https://github.com/Nanibucky/reporter_AI.git
cd reporter_AI
```



3. Create a `.env` file with your API keys:

```env
SERPER_API_KEY=your_serper_api_key
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the AI Agent:
```bash
python crew.py
```

## 💡 Usage
Edit `crew.py` to customize the topic:
```python
article_result = research_write_crew.kickoff(inputs={'topic': 'Your topic here'})
```

## 📝 License
This project is licensed under the MIT License.
```
Feel free to customize it further to match your project's specifics!

