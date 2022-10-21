import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y/%m/%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y/%m/%d")
start_date = d2
import streamlit as st
st.title("Real-time Stock Price Data")
a = st.text_input("Enter Any Company >>:")
data = web.DataReader(name=a, data_source='yahoo', start=start_date, end=end_date)
fig, ax = plt.subplots() 
ax = data["Close"].plot(figsize=(12, 8), title=a+" Stock Prices", fontsize=20, label="Close Price")
plt.legend()
plt.grid()
st.pyplot(fig)