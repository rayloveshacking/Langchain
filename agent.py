import getpass
import os
from click import prompt
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

template = ChatPromptTemplate.from_messages([
('system', 'You are a helpful assistant.'),
('human', '{question}'),
])

@chain
def chatbot(values):
  prompt = template.invoke(values)
  return model.invoke(prompt)
# use it
response = chatbot.invoke({"question": "Which model providers offer LLMs?"})
print(response)