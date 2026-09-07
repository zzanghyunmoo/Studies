from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseOutputParser
from langchain.prompts import ChatPromptTemplate


class CommaOutputParser(BaseOutputParser):
    def parse(self, text: str):
        items = text.strip().split(",")
        return list(map(str.strip, items))


p = CommaOutputParser()
result = p.parse("Hello, how, are, you")
print(result)

chat = ChatOpenAI(temperature=0.1)
template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a list generating machine. Everything you are asked will be answerd with a comma seperated list of max {max_items}. Do NOT reply with anything else.",
        ),
        ("human", "{question}"),
    ]
)

prompt = template.format_messages(max_items=10, question="What are the planets")
result = chat.predict_messages(prompt)
p = CommaOutputParser()
parsed_res = p.parse(str(result.content))
print(parsed_res)

chain = template | chat | CommaOutputParser()
print(chain.invoke({"max_items": 5, "question": "What are poketmons?"}))
