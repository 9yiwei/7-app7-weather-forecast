import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ").title()
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecast days.")
option = st.selectbox("Select data to view: ",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [i["main"]["temp"] / 10 for i in filtered_data]
            date = [i["dt_txt"] for i in filtered_data]
            figure = px.line(x=date, y=temperature, labels={"x": "Date", "y": "Temp (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [i["weather"][0]["main"] for i in filtered_data]
            img = [images[condition] for condition in sky_conditions]
            st.image(img, width=115)

    except KeyError:
        st.info("That place does not exist.")


