import streamlit as st
import numpy as np

# Markdown and Headings
html_temp = """ 
<div style="background-color: lightblue; padding: 16px">
<h2 style="color: black; text-align: center;">Drex Dang Income Statement Template (IFRS Standard) Web App</h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)
st.write('')
st.write('')
st.markdown("##### A Simple Income Statement Computation\n##### Let's Ascertain The Much Of Net Profit/Loss")

# Input Fields
revenue = st.number_input("Total Revenue", step=1.0, format="%f")
cost_of_goods_sold = st.number_input("Cost of Goods Sold (COGS)", step=1.0, format="%f")
gross_profit = revenue - cost_of_goods_sold

operating_expenses = st.number_input("Operating Expenses", step=1.0, format="%f")
income_tax = st.number_input("Income Tax", step=1.0, format="%f")
other_income = st.number_input("Other Income", step=1.0, format="%f")
other_expenses = st.number_input("Other Expenses", step=1.0, format="%f")

# Calculate Operating Profit
operating_profit = gross_profit - operating_expenses

# Calculate Net Profit
net_profit = operating_profit + other_income - other_expenses - income_tax

# Display Income Statement
st.header("Income Statement (IFRS Compliant)")

st.write(f"Total Revenue: {revenue}")
st.write(f"Cost of Goods Sold (COGS): {cost_of_goods_sold}")
st.write(f"Gross Profit: {gross_profit}")
st.write(f"Operating Expenses: {operating_expenses}")
st.write(f"Income Tax: {income_tax}")
st.write(f"Other Income: {other_income}")
st.write(f"Other Expenses: {other_expenses}")
st.write(f"Operating Profit: {operating_profit}")
st.write(f"Net Profit Or Loss: {net_profit}")
