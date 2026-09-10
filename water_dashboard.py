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
    df = pd.read_csv("biscayneBay_waterquality.csv") # please use this csv file

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

    fig2 = px.scatter(df,
                      x="Temperature (c)",
                      y="Salinity (ppt)",
                      title="Temperature vs Salinity")
    st.plotly_chart(fig2)

    fig3 = px.scatter_3d(df,
                         x="Longitude",
                         y="Latitude",
                         z="Total Water Column (m)",
                         color="Temperature (c)",
                         title="3D Visualization of the Bay Floor")
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with maps:
    st.subheader("Maps")
    first_map = px.scatter_map(
        df,
        lat="Latitude",
        lon="Longitude",
        title="Vehicle Track on a Map",
        center={"lat":25.9121,"lon":-80.1371},
        zoom=16,
        color="Temperature (c)",
        color_continuous_scale="viridis")
    st.plotly_chart(first_map)