import os
from dotenv import load_dotenv
from groq import Groq
import requests
import streamlit as st
from datetime import datetime, timedelta

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_groq_summary(article_text):
    system_behavior = """You are a specific AI Assistant that summarize information about AI News from NewsAPI in simple, 
structured summaries for non-technical people.
Summarize with this exact format:
    What    :
    Who     :
    For     :
    Big News:
    Summary :

ONLY respond in the format given, no extra commentary and no preamble like "Here is the summary...". Just directly to the summarization.
Avoid the technical jargon, write it like explaining to a friend.
If something is unclear from the article, say "unclear", not guess.
If information is not available in the article , write "Not mentioned".
You will receive a news article title, description, and available content text. Summarize it based on that information only.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[{
                "role": "system", 
                "content": system_behavior
            }, {
                "role": "user", 
                "content": article_text
            }], 
            temperature=0.1
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating summary: {e}"
    
st.set_page_config(page_title="Daily AI News", page_icon="🤖")
st.title("Daily AI News Digest")
st.subheader("Your morning coffee brief on Artificial Intelligence")

if st.button("🚀Get Today's News", use_container_width=True):
    
    # A. Call NewsPI
    two_days_ago = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
    
    url = (f"https://newsapi.org/v2/everything")
    query_params = {
        "q": "artificial intelligence", 
        "language": "en",
        "sortBy": "popularity",
        "from": two_days_ago,
        "pageSize": 5,
        "apiKey": os.getenv("NEWSAPI_KEY")
    }
    
    try:
        response = requests.get(url, params=query_params)
        raw_data = response.json()
        
        if raw_data.get("status") == "error":
            st.error(f"NewsAPI Error: {raw_data.get('message')}")
        
        raw_articles = raw_data.get("articles", [])
        st.write(f"DEBUG: NewsAPI returned {len(raw_articles)} articles.")
        
        if not raw_articles:
            st.warning("No articles found of API limit reached.")
            
        # B. Loop through each article
        for art in raw_articles:
            title= art.get("title")
            source= art.get("source", {}).get("name", "Unknown Source")
            url= art.get("url")
            description = art.get("description", "")    
            content = art.get("content", "")
            
            raw_date = art.get("publishedAt")
            if raw_date:
                clean_date_obj = datetime.strptime(raw_date.replace('Z', ''), '%Y-%m-%dT%H:%M:%S')
                readable_date = clean_date_obj.strftime('%B %d, %Y at %H:%M')
            else:
                readable_date = "Unknown Time"
            
            # Bundle the next for Groq context
            text_for_groq= f"Title: {title}\nDesctiption: {description}\nContent: {content}"
            
            # C. Call Groq
            summary = get_groq_summary(text_for_groq)
            
            # D. Render the Card in Streamlit
            with st.container(border=True):
                st.subheader(title)
                st.caption(f"Source: **{source}** | Published: *{readable_date}*")
                st.text(summary)
                st.markdown(f"[🔗 Read Full Article]({url})")
    except Exception as e:
        st.error(f"An error occurred: {e}")