import streamlit as st
from datetime import time, date
from st_copy import copy_button

st.title("Market Analyst Prompt Generator")

st.sidebar.title("Input Parameters")

index_choice = st.sidebar.selectbox(
    "Select Instrument Type",
    ["Nifty 50", "Bank Nifty", "FinNifty", "Stock F&O"]
)

if index_choice == "Stock F&O":
    stock_name = st.sidebar.text_input("Enter Stock Name", value="Tata Motors")
    current_price = st.sidebar.number_input(f"Current Price of {stock_name}", min_value=0.0, value=900.0)
else:
    current_price = st.sidebar.number_input("Current Index Price", min_value=0.0, value=25000.0)

current_time = st.sidebar.time_input("Current Time (IST)", value=time(9, 30), step=60)
current_date = st.sidebar.date_input("Current Date", value=date.today())
expiry_date = st.sidebar.date_input("Expiry Date")
risk_appetite = st.sidebar.slider("Risk Appetite (% of premium)", min_value=10, max_value=70, value=50)

st.markdown("---")

def generate_prompt(instrument, price, time_val, date_val, expiry, risk, stock_name=None):
    if instrument == "Stock F&O":
        heading = f"""
You are an expert financial analyst specializing in the Indian equity and derivatives markets, with a focus on F&O trading for **{stock_name}**.
The current price of **{stock_name}** is **{price}** as of **{time_val} IST, {date_val}**.
"""
        factors = f"""
Analyze the following for **{stock_name}**:
- Technical indicators: candlestick patterns, intraday trends, support/resistance, OI at key strikes, option Greeks, IV from NSE live data.
- Fundamental drivers: sector-specific news, earnings reports, company announcements, macroeconomic cues.
- Real-time sentiment: market news, management commentary, industry trends, geopolitical impact.

"""
        probability = f"""
### 1️⃣ Intraday Closing Probability Estimates (Total 100%):
- Upside Close (above **{price}**): ___%
- Downside Close (below **{price}**): ___%
- Neutral/Flat Close (within ±0.5%): ___%

"""
        option_section = f"""
### 2️⃣ Option Buying Recommendation (ATM – {expiry} Expiry):
- Best Call Option strike with expected intraday return (%)
- Best Put Option strike with expected intraday return (%)
- Key risks (IV crush, reversal risk, news events)

"""
    else:
        heading = f"""
You are an expert financial analyst specializing in the Indian equity and derivatives markets, with a focus on **{instrument} options**.
The current **{instrument}** index level is **{price}** as of **{time_val} IST, {date_val}**.
"""
        factors = """
Use a combination of:
- Technical factors: candlestick patterns, intraday indicators, key support/resistance levels, open interest (OI) build-up, option Greeks, IV based on live data.
- Fundamental cues: macroeconomic events, sector news, FII/DII flows, global market trends.
- Real-time sentiment: news headlines, RBI commentary, corporate actions, geopolitical factors.

"""
        probability = f"""
### 1️⃣ {instrument} Intraday Closing Probability Estimates (Total 100%):
- Upside Close (above **{price}**): ___%
- Downside Close (below **{price}**): ___%
- Neutral/Flat Close (within ±0.2%): ___%

"""
        option_section = f"""
### 2️⃣ Option Buying Recommendation (ATM – {expiry} Expiry):
- Best Call Option strike with expected intraday return (%)
- Best Put Option strike with expected intraday return (%)
- Key risk factors (IV crush, reversal risk, news impact)

"""

    risk_section = f"""
⚠️ **Risk Appetite:**
Willing to risk up to **{risk}% of premium** for potential high intraday gains.

📊 **OI Sensitivity:**
Evaluate live OI build-up and unwinding — especially at ATM and nearby strikes.

✅ **Actionable Summary:**
- Recommended strategy for today (Buy Call, Buy Put, Both, or Wait)
- Suggested strike(s) with approx. premium per lot (₹)
- Expected probability of success (%)
- Rationale covering technicals, OI, and sentiment.

💡 *Base your analysis on live market behavior — avoid static assumptions.*
"""

    return heading + factors + probability + option_section + risk_section


if st.sidebar.button("Generate Prompt"):
    if index_choice == "Stock F&O":
        prompt = generate_prompt(index_choice, current_price, current_time, current_date, expiry_date, risk_appetite, stock_name)
    else:
        prompt = generate_prompt(index_choice, current_price, current_time, current_date, expiry_date, risk_appetite)

    st.markdown("### ✅ Generated Prompt")
    copy_button(prompt, icon="📋", tooltip="Copy prompt", copied_label="Copied!")
    st.markdown(prompt)
