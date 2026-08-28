from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

llm = OpenAI()
chat = ChatOpenAI()

a = llm.predict("How many planets are there?")
b = chat.predict("How many planets are there?")

print(a)
print(b)
