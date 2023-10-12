import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecast days.")
option = st.selectbox("Select data to view: ",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2002-10-12", "2002-10-13", "2002-10-14"]
    temp = [10, 12, 13]
    temp = [days * i for i in temp]
    return dates, temp


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temp (C)"})
st.plotly_chart(figure)