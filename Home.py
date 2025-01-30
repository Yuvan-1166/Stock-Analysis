import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def get_stock_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, group_by=ticker) 
    if data.empty:
        st.error(f"No data found for {ticker} between {start} and {end}.")
    return data

def plot_stock_data(data, title, ticker):
    fig = go.Figure()
    if (ticker, 'Close') in data.columns:
        fig.add_trace(go.Scatter(x=data.index, y=data[(ticker, 'Close')], mode='lines', name=title))
    else:
        st.error(f"Missing 'Close' column in the data for {title}.")
    fig.update_layout(title=title, xaxis_title='Date', yaxis_title='Price')
    return fig

def get_top_gainers_losers(data, ticker):
    if (ticker, 'Close') not in data.columns or (ticker, 'Open') not in data.columns:
        st.error("Data is missing required 'Close' or 'Open' columns.")
        return pd.DataFrame(), pd.DataFrame()
     
    data[(ticker, 'Daily Change %')] = (data[(ticker, 'Close')] - data[(ticker, 'Open')]) / data[(ticker, 'Open')] * 100
    data['Stock Symbol'] = data.index
    top_gainers = data.nlargest(5, (ticker, 'Daily Change %'))[[(ticker, 'Open'), (ticker, 'Close'), (ticker, 'Daily Change %')]]
    top_losers = data.nsmallest(5, (ticker, 'Daily Change %'))[[(ticker, 'Open'), (ticker, 'Close'), (ticker, 'Daily Change %')]]

    return top_gainers, top_losers

st.set_page_config(page_title='Stock Analyzer!', page_icon="📈")

st.title("Stock Analyzer 📈")
st.sidebar.success("") 

start_date = st.date_input('Start Date', pd.to_datetime('2023-01-01'))
end_date = st.date_input('End Date', pd.to_datetime('today'))

sensex_tickers = ["RELIANCE.BO", "TCS.BO", "HdataCBANK.BO", "INFY.BO", "HINDUNILVR.BO"]
nifty_tickers = ["RELIANCE.NS", "TCS.NS", "HdataCBANK.NS", "INFY.NS", "HINDUNILVR.NS"]

bsesn, nsei = '^BSESN', '^NSEI'

sensex_data = get_stock_data(bsesn, start=start_date, end=end_date)
nifty_data = get_stock_data(nsei, start=start_date, end=end_date)

top_gainers_sensex, top_losers_sensex = get_top_gainers_losers(sensex_data, bsesn)
top_gainers_nifty, top_losers_nifty = get_top_gainers_losers(nifty_data, nsei)

sensex_tab, nifty_tab = st.tabs(["Sensex", "Nifty"])

# Sensex Tab
with sensex_tab:
    st.subheader("Sensex Data")
    sensex_chart_tab, sensex_gainers_tab, sensex_losers_tab = st.tabs(["Sensex Chart", "Top Gainers", "Top Losers"])
    
    with sensex_chart_tab:
        st.plotly_chart(plot_stock_data(sensex_data, "Sensex", bsesn))

    with sensex_gainers_tab:
        st.subheader("Top 5 Gainers in Sensex")
        st.dataframe(top_gainers_sensex)

    with sensex_losers_tab:
        st.subheader("Top 5 Losers in Sensex")
        st.dataframe(top_losers_sensex)

with nifty_tab:
    st.subheader("Nifty Data")
    
    nifty_chart_tab, nifty_gainers_tab, nifty_losers_tab = st.tabs(["Nifty Chart", "Top Gainers", "Top Losers"])
    
    with nifty_chart_tab:
        st.plotly_chart(plot_stock_data(nifty_data, "Nifty", nsei))

    with nifty_gainers_tab:
        st.subheader("Top 5 Gainers in Nifty")
        st.dataframe(top_gainers_nifty)

    with nifty_losers_tab:
        st.subheader("Top 5 Losers in Nifty")
        st.dataframe(top_losers_nifty)
