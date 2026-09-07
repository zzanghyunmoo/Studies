from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler


chat = ChatOpenAI(
    temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler()]
)
chef_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a world-class international chef. You create easy to follow reciepies for any type of cuisine with easy to find ingredients.",
        ),
        ("human", "I want to cook {cuisine} food."),
    ]
)

chef_chain = chef_prompt | chat

veg_chef_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a vegeterian chef specialized on making traditional reciepies vegeterian. You find alternative ingredients and explain their preparation. You don't redically modify the recipe. If There is no alternative for a food just say you don't know how to replace it.",
        ),
        ("human", "{recipe}"),
    ]
)

veg_chain = veg_chef_prompt | chat

final_chain = {"recipe": chef_chain} | veg_chain
print(
    final_chain.invoke(
        {
            "cuisine": "indian",
        }
    )
)
