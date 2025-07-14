
import streamlit as st
from datetime import datetime
from datetime import datetime, time, date

st.title("Market Analyst Prompt Generator")

st.sidebar.title("Input Parameters")

current_price = st.sidebar.number_input("Current Price", min_value=0.0, value=25000.0)
# current_time = st.sidebar.time_input("Select Time", value=datetime.now().time(), step=60)
current_time = st.sidebar.time_input("Select Current Time", value=time(9, 30), step=60)
current_date = st.sidebar.date_input("Select Date", value=date.today())
expiry_date = st.sidebar.date_input("Expiry Date")
index_choice = st.sidebar.selectbox("Select Index", ["Nifty 50", "Bank Nifty"])

st.markdown("---")

if st.sidebar.button("Generate Prompt"):
    if index_choice == "Bank Nifty":
        prompt = f"""
You are an expert financial analyst specializing in the Indian equity and derivatives markets, with a focus on Bank Nifty options.
The current Bank Nifty index level is **{current_price}** as of **{current_time} IST, {current_date}**.

Using a combination of:
- Technical analysis (candlestick patterns, intraday indicators, key support/resistance, OI build-up at strikes, implied volatility, option Greeks)
- Fundamental analysis (macroeconomic cues, RBI policies, FII/DII flows, sectoral banking news, global financial market impact)
- Real-time news sentiment (financial headlines, corporate banking news, RBI commentary, geopolitical developments affecting financials)

Please analyze and provide:

1️⃣ **Intraday Probability Estimates (in %)** for Bank Nifty closing today:
- Upside probability (above **{current_price}**)
- Downside probability (below **{current_price}**)

2️⃣ **Option Buying Recommendation (ATM – {expiry_date} Expiry):**
- Best ATM Call Option to buy — with expected intraday return (%)
- Best ATM Put Option to buy — with expected intraday return (%)
- Major risk factors for both strategies (volatility crush, unexpected reversals, sudden news impact)

⚠️ **Risk Appetite:**
Willing to risk up to **15% of premium** for potential **50%+ intraday gains**

📊 **Assumed Implied Volatility (ATM):**
**17-18%**

📈 **Open Interest (OI) Sensitivity:**
Consider current OI build-up and unwinding at key strikes for directional bias

✅ **Actionable Summary Needed:**
- Which strategy is recommended today (Buy Call, Buy Put, or Both)?
- Exact strike(s) to consider for intraday trade
- Approximate premium per lot (₹) and estimated probability of success (%)
        """
    else:
        prompt = f"""
You are an expert financial analyst specializing in the Indian equity and derivatives markets, with a focus on Nifty 50 options.
The current Nifty 50 index level is **{current_price}** as of **{current_time} IST, {current_date}**.

Using a combination of:
- Technical analysis (candlestick patterns, intraday indicators, support/resistance, OI build-up, IV, option Greeks)
- Fundamental analysis (macroeconomic cues, FII/DII flows, sectoral news, global markets impact)
- Real-time news sentiment (headlines, corporate actions, RBI commentary, geopolitical events)

Please analyze and provide:

1️⃣ **Intraday Probability Estimates (in %)** for Nifty 50 closing:
- Upside (above **{current_price}**)
- Downside (below **{current_price}**)

2️⃣ **Option Buying Recommendation (ATM – {expiry_date} Expiry):**
- Best call option to buy with expected intraday return (%)
- Best put option to buy with expected intraday return (%)
- Major risk factors for each scenario (volatility crush, sharp reversals, news risks)

⚠️ **Risk Appetite:**
Willing to risk up to **70% of premium** for potential **100%+ intraday gains**

📊 **Assumed IV:**
**17-18% ATM**

📈 **OI Sensitivity:**
Consider current OI build-up for directional bias

✅ **Actionable Summary Needed:**
- Which strategy to execute today (buy call, buy put, or both)
- Exact strike(s) recommended
- Approximate premium per lot (₹) and probability of success (%)
        """

    st.markdown("### ✅ Generated Prompt")
    # st.code(prompt, language='markdown')
    st.markdown(prompt)
