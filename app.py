import streamlit as st
from datetime import time, date
from st_copy import copy_button

st.title("Nifty & Stock Options Intraday Prompt Generator")

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
expiry_date = st.sidebar.date_input("Options Expiry Date")
risk_appetite = st.sidebar.slider("Risk Appetite (% of premium)", min_value=10, max_value=70, value=50)

st.markdown("---")

def generate_prompt(instrument, price, time_val, date_val, expiry, risk, stock_name=None):
    if instrument == "Stock F&O":
        prompt = f"""
You are an expert financial analyst specializing in the Indian equity and derivatives markets, especially **{stock_name} options**.
The current price of **{stock_name}** is **{price}** as of **{time_val} IST, {date_val}**.

Using a combination of:
  • Technical analysis (candlestick patterns, intraday indicators, support/resistance, implied volatility, option Greeks, etc.)  
  • Fundamental analysis (macroeconomic cues, sectoral news, earnings impact, global markets)  
  • Real-time sentiment (news headlines, company announcements, management commentary, geopolitical factors)

Produce a short report with intraday probability estimates (in %) for whether **{stock_name}** will move:
  1. Upside  
  2. Downside  
  3. Volatile move (big move either way)

Specifically:
  1. Starting from the current price of **{price}**, calculate the probability (in %) that **{stock_name}** will finish the trading day higher, lower, or roughly flat. Clearly state your assumptions (technical patterns, news emphasis).  
  2. Based on those probabilities, recommend which *option‑buying* near ATM call and put is likely to yield the highest expected profit today:
     - Buying call options only near ATM  
     - Buying put options only near ATM  

     For each strategy, estimate the expected return (%) and mention any major risks (e.g., sudden volatility spikes, unexpected news).

I want to trade between **9:30 am and 3:00 pm** with a **high‑risk** approach.  
I will take the expiry as **{expiry}**.

At the end, provide a concise **“Actionable Summary”**:

  • Which specific strategy should I execute today **{date_val}** — buy calls, buy puts, or both buy?  
  • Which strike(s) would you choose if you were trading intraday?  
  • Approximately what premium (₹) and probability (%) does each recommended position carry?

⚠️ I am willing to risk up to **{risk}% of premium** on this high-risk intraday strategy.
"""
    else:
        prompt = f"""
You are an expert financial analyst specializing in the Indian equity and derivatives markets, especially **{instrument} options**.
The current **{instrument}** index level is **{price}** as of **{time_val} IST, {date_val}**.

Using a combination of:
  • Technical analysis (candlestick patterns, intraday indicators, support/resistance, implied volatility, option Greeks, etc.)  
  • Fundamental analysis (macroeconomic cues, FII/DII flows, sectoral news, global markets impact)  
  • Real-time news sentiment (headlines, corporate announcements, RBI commentary, geopolitical developments)

Produce a short report with intraday probability estimates (in %) for whether **{instrument}** will move:
  1. Upside  
  2. Downside  
  3. Volatile move (big move either way)

Specifically:
  1. Starting from the current index level of **{price}**, calculate the probability (in %) that the index will finish the trading day higher, lower, or roughly flat. Clearly state your assumptions (technical patterns, news emphasis).  
  2. Based on those probabilities, recommend which *option‑buying* near ATM call and put is likely to yield the highest expected profit today:
     - Buying call options only near ATM  
     - Buying put options only near ATM  

     For each strategy, estimate the expected return (%) and mention any major risks (e.g., sudden volatility spikes, unexpected news).

I want to trade between **9:30 am and 3:00 pm** with a **high‑risk** approach.  
I will take the expiry as **{expiry}**.

At the end, provide a concise **“Actionable Summary”**:

  • Which specific strategy should I execute today **{date_val}** — buy calls, buy puts, or both buy?  
  • Which strike(s) would you choose if you were trading intraday?  
  • Approximately what premium (₹) and probability (%) does each recommended position carry?

⚠️ I am willing to risk up to **{risk}% of premium** on this high-risk intraday strategy.
"""
    return prompt

if st.sidebar.button("Generate Prompt"):
    if index_choice == "Stock F&O":
        prompt = generate_prompt(index_choice, current_price, current_time, current_date, expiry_date, risk_appetite, stock_name)
    else:
        prompt = generate_prompt(index_choice, current_price, current_time, current_date, expiry_date, risk_appetite)

    st.markdown("### ✅ Generated Prompt")
    copy_button(prompt, icon="📋", tooltip="Copy prompt", copied_label="Copied!")
    st.markdown(prompt)
