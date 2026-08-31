from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

chat = ChatOpenAI(temperature=0.1)


messages = [
    SystemMessage(
        content="You are a great geography expert. And You only reply in Korean"
    ),
    AIMessage(content="Hi, Your name is Hyunmoo"),
    HumanMessage(
        content="What is distance between Korean and England. Also, what is your name?"
    ),
]

result = chat.predict_messages(messages)
print(result)
