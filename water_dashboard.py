import streamlit as st
import pandas as pd # data manipulation
import plotly.express as px # data visualization

# to run: streamlit run name_of_file.py
# if it doesn't work, try: python -m streamlit run name_of_file.py

st.title("Water Quality Dashboard")
st.header("CIS 3590 - Internship-Ready Software Development")
st.subheader("Prof. Gregory Reis")

st.divider()

st.sidebar.header("File Upload")
st.sidebar.info("Upload a CSV file "
                "with water quality data")
uploaded_file=st.sidebar.file_uploader("Upload a CSV file",
                         type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("2021-oct21.csv")

tables, plots, maps = st.tabs(["Data",
                               "Charts",
                               "Maps"])
with tables:
    st.dataframe(df)
    st.caption("Raw Data")
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")
    # TODO: add a multiselect box to select multiple columns to display

with plots:
    st.subheader("Line Chart")
    parameter = st.selectbox("Select a parameter",options=df.columns.tolist())
    # TODO: add all possible parameters to list of parameters in the selectbox above
    #  and dynamically change the y axis in the plot below to the selected parameter
    fig1 = px.line(df,
                   x="Time",
                   y=parameter,
                   title=f"{parameter} over Time")
    st.plotly_chart(fig1)