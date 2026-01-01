import streamlit as st
import os
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Financial Statement Analyzer",
    layout="centered"
)

# ---------------- UI ----------------
st.title("📊 AI Financial Statement Analyzer")
st.caption("Investment-grade analysis | UAE Corporate Finance Standard")

financials = st.text_area(
    "📥 Paste Income Statement, Balance Sheet & Cash Flow",
    height=280,
    placeholder="Paste structured financial data here..."
)

analyze = st.button("🔍 Analyze Financials")

# ---------------- PROMPT ----------------
FINANCE_PROMPT = """
You are a Senior Financial Analyst working in the UAE with experience in:
- Financial Statement Analysis
- FP&A
- Credit & Investment Analysis
- Corporate Finance (Bank / Big-4 standard)

TASK:
Analyze the financial information provided and produce an
INVESTMENT-GRADE FINANCIAL ANALYSIS.

STRUCTURE:
1. Executive Summary
2. Performance Analysis
3. Key Financial Ratios
4. Cash Flow Quality
5. Risks & Red Flags
6. Management & Investor Insights

RULES:
- Be professional and concise
- Use bullet points
- Do NOT assume missing data
"""

# ---------------- AI CALL ----------------
if analyze:
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
                {"role": "system", "content": FINANCE_PROMPT},
                {"role": "user", "content": financials}
            ]
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            st.error("OpenAI API error")
            st.write(response.text)
        else:
            result = response.json()
            st.subheader("📈 Analysis Result")
            st.write(result["choices"][0]["message"]["content"])