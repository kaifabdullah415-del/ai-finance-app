import streamlit as st
from openai import OpenAI
import os

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(
    page_title="AI Financial Statement Analyzer",
    layout="centered"
)

# ---------------- OPENAI CLIENT ----------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------- UI ----------------
st.title("📊 AI Financial Statement Analyzer")
st.caption("Investment-grade analysis | UAE Corporate Finance Standard")

st.markdown("### 📥 Paste Financial Statements")

financials = st.text_area(
    "Income Statement, Balance Sheet & Cash Flow",
    height=280,
    placeholder="Paste structured financial data here..."
)

analyze = st.button("🔍 Analyze Financials")

st.markdown("---")

# ---------------- PROMPT ----------------
FINANCE_PROMPT = """
You are a Senior Financial Analyst working in the UAE with experience in:
- Financial Statement Analysis
- FP&A
- Credit & Investment Analysis
- Corporate Finance (Bank / Big-4 standard)

TASK:
Analyze the financial information provided and produce an
INVESTMENT-GRADE FINANCIAL ANALYSIS suitable for:
• Bank credit committee
• Private equity / investor review
• Senior management decision-making

OUTPUT STRUCTURE:
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
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": FINANCE_PROMPT},
                {"role": "user", "content": financials}
            ]
        )

        st.subheader("📈 Analysis Result")
        st.write(response.choices[0].message.content)