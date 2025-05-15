import streamlit as st
from duckduckgo_search import DDGS
from datetime import datetime

# Set up the Streamlit app configuration
st.set_page_config(page_title="Real-Time News Fetcher", page_icon="📰")
st.title("📰 Real-Time News Fetcher")

# Instructions for the user
st.write("Select a topic from the dropdown and click 'Fetch News' to get the latest news articles.")

# Define a list of news topics for the dropdown
topics = ["Technology", "Politics", "Sports", "Entertainment", "Business"]

# Dropdown for selecting a news topic
selected_topic = st.selectbox("Select a news topic:", topics)

# Function to search for news using DuckDuckGo
def search_news(topic):
    with DDGS() as ddg:
        # Search for news articles with the current month and year to get recent results
        query = f"{topic} news {datetime.now().strftime('%Y-%m')}"
        results = ddg.text(query, max_results=5)  # Fetch up to 5 news articles
        if results:
            return results
        else:
            return None

# Button to fetch news when clicked
if st.button("Fetch News"):
    with st.spinner("Fetching news..."):
        news_results = search_news(selected_topic)
        if news_results:
            # Display the time when the news was fetched
            fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success(f"Found {len(news_results)} articles on {selected_topic} (Fetched at {fetch_time})")
            
            # Display each news article in an expander for better user experience
            for i, result in enumerate(news_results, 1):
                with st.expander(f"Article {i}: {result['title']}"):
                    st.markdown(f"**URL:** [{result['href']}]({result['href']})")
                    st.write(f"**Summary:** {result['body']}")
        else:
            st.warning(f"No news found for {selected_topic}.")
