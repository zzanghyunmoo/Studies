from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(temperature=0.1)
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a geography expert. And you only reply in {language}."),
        ("ai", "Hi your name is {name}"),
        (
            "human",
            "What is the distance between {country_src} and {country_dst}. Also what is your name?",
        ),
    ]
)

prompt = template.format_messages(
    language="Korean", name="Hyunmoo", country_src="Korean", country_dst="England"
)
result = chat.predict_messages(prompt)
print(result)
