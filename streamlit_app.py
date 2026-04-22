import streamlit as st
from market_data import get_market_data
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os
import json

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
search = TavilySearch(max_results=3, tavily_api_key=os.getenv("TAVILY_API_KEY"))

st.set_page_config(page_title="AlphaTrade", page_icon="📈")
st.title("📈 AlphaTrade — AI Options Strategy Analyzer")
st.subheader("Real-time Nifty 50 options strategy powered by AI")

if st.button("🔍 Analyze Market Now"):
    with st.spinner("Fetching live market data..."):
        data = get_market_data()

    st.subheader("📊 Live Market Data")
    col1, col2, col3 = st.columns(3)
    col1.metric("Nifty 50", f"₹{data['current_price']}", f"{data['percentage_change']:.2f}%")
    col2.metric("VIX", data['vix_level'])
    col3.metric("52W High", f"₹{data['fiftytwo_week_high']}")

    with st.spinner("Searching latest news..."):
        news_result = search.invoke("Nifty 50 latest news today")
        news_text = " ".join([r["content"] for r in news_result["results"]])

    with st.spinner("Generating strategy..."):
        response = llm.invoke(f"""You are an expert Nifty 50 options trading advisor.
Market Data: {json.dumps(data)}
Latest News: {news_text}

Suggest the best options strategy. Return as structured text with:
Strategy, Rationale, Risk, Potential Profit, Strike Prices.""")

    st.subheader("🎯 Recommended Strategy")
    st.write(response.content)

    st.caption("⚠️ This is not financial advice. Always do your own research.")