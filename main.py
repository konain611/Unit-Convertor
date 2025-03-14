import streamlit as st

st.title("Unit Converter Application")
st.write("A simple web-based unit converter that allows users to convert between Length, Weight, Temperature, Volume, and Time.")

st.write("### Choose a Conversion Category")

units = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": ["Liters", "Milliliters", "Gallons"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"]
}

category = st.selectbox("Select a Category", list(units.keys()))

from_unit = st.selectbox("Convert From", ["-- Select Unit --"] + units[category], index=0)
to_unit = st.selectbox("Convert To", ["-- Select Unit --"] + units[category], index=0)

st.markdown(
    """
    <script>
    function selectAllOnClick() {
        document.querySelectorAll('input[type="number"]').forEach(el => {
            el.addEventListener('focus', function(event) {
                event.target.select();
            });
        });
    }
    document.addEventListener("DOMContentLoaded", selectAllOnClick);
    </script>
    """,
    unsafe_allow_html=True
)

value = st.number_input("Enter value to convert", min_value=0.0, format="%.2f")

def convert(value, from_unit, to_unit):
    length = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084}
    weight = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    volume = {"Liters": 1, "Milliliters": 1000, "Gallons": 0.264172}
    time = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400}

    if from_unit == "-- Select Unit --" or to_unit == "-- Select Unit --":
        return None

    if category == "Length":
        return value * (length[to_unit] / length[from_unit])
    elif category == "Weight":
        return value * (weight[to_unit] / weight[from_unit])
    elif category == "Volume":
        return value * (volume[to_unit] / volume[from_unit])
    elif category == "Time":
        return value * (time[to_unit] / time[from_unit])
    elif category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

if st.button("Convert"):
    if from_unit == "-- Select Unit --" or to_unit == "-- Select Unit --":
        st.warning("Please select valid units before converting.")
    else:
        result = convert(value, from_unit, to_unit)
        st.write(f"### Result: {value} {from_unit}  =  {result:.2f} {to_unit}")
