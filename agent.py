from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os
load_dotenv()

search = TavilySearch(max_results=3, tavily_api_key=os.getenv("TAVILY_API_KEY"))

result = search.run("Nifty 50 latest news today")
print(result)