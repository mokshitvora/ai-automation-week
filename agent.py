from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os
load_dotenv()
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
search = TavilySearch(max_results=3, tavily_api_key=os.getenv("TAVILY_API_KEY"))

result = search.run("Nifty 50 latest news today")
print(result)