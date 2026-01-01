import streamlit as st
import os
import requests

st.set_page_config(
    page_title="AI Financial Statement Analyzer",
    layout="centered"
)

st.title("📊 AI Financial Statement Analyzer")
st.caption("Investment-grade analysis | UAE Corporate Finance Standard")

financials = st.text_area(
    "📥 Paste Income Statement, Balance Sheet & Cash Flow",
    height=280
)

if st.button("🔍 Analyze Financials"):
    if financials.strip() == "":
        st.warning("Please paste financial statements first.")
    else:
        api_key = os.getenv("OPENAI_API_KEY")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a UAE senior financial analyst. Produce investment-grade analysis."
                },
                {
                    "role": "user",
                    "content": financials
                }
            ]
        }

        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if r.status_code != 200:
            st.error(r.text)
        else:
            st.subheader("📈 Analysis Result")
            st.write(r.json()["choices"][0]["message"]["content"])
