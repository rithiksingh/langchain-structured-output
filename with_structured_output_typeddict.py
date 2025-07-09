from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model= ChatOpenAI()

#scema of output structure
class SentimentAnalysis(TypedDict):
    sentiment: str
    score: int


# telling the model to use structure output and giving it the defined schema
structured_model= model.with_structured_output(SentimentAnalysis)



response= structured_model.invoke("This phone is amazing! Super fast and great camera quality")

print(response)