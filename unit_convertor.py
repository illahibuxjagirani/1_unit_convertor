
import streamlit as st

st.set_page_config(page_title="Unit Convertor")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #a8e6cf;
    }
    </style>
    """,
    unsafe_allow_html=True
)



def convert_units(value, unit_from, unit_to):
  conversions = {
    # Length Conversions
    "meter_kilometer": 0.001,    # 1 meter = 0.001 kilometers
    "meter_meter": 1,            # 1 meter = 1 meter (identity conversion)
    "kilometer_kilometer": 1,    # 1 kilometer = 1 kilometer (identity)
    "kilometer_meter": 1000,     # 1 kilometer = 1000 meters
    "meter_centimeter": 100,     # 1 meter = 100 centimeters
    "centimeter_meter": 0.01,    # 1 centimeter = 0.01 meters
    "meter_millimeter": 1000,    # 1 meter = 1000 millimeters
    "millimeter_meter": 0.001,   # 1 millimeter = 0.001 meters
    "kilometer_centimeter": 100000,  # 1 kilometer = 100,000 centimeters
    "centimeter_kilometer": 0.00001, # 1 centimeter = 0.00001 kilometers
    "meter_inch": 39.3701,       # 1 meter = 39.3701 inches
    "inch_meter": 0.0254,        # 1 inch = 0.0254 meters
    "meter_feet": 3.28084,       # 1 meter = 3.28084 feet
    "feet_meter": 0.3048,        # 1 foot = 0.3048 meters
    "kilometer_mile": 0.621371,  # 1 kilometer = 0.621371 miles
    "mile_kilometer": 1.60934,   # 1 mile = 1.60934 kilometers

    # Weight/Mass Conversions
    "gram_gram": 1,              # 1 gram = 1 gram (identity)
    "kilogram_kilogram": 1,      # 1 kilogram = 1 kilogram (identity)
    "gram_kilogram": 0.001,      # 1 gram = 0.001 kilograms
    "kilogram_gram": 1000,       # 1 kilogram = 1000 grams
    "gram_milligram": 1000,      # 1 gram = 1000 milligrams
    "milligram_gram": 0.001,     # 1 milligram = 0.001 grams
    "kilogram_milligram": 1000000,  # 1 kilogram = 1,000,000 milligrams
    "milligram_kilogram": 0.000001, # 1 milligram = 0.000001 kilograms
    "kilogram_pound": 2.20462,   # 1 kilogram = 2.20462 pounds
    "pound_kilogram": 0.453592,  # 1 pound = 0.453592 kilograms
    "gram_ounce": 0.035274,      # 1 gram = 0.035274 ounces
    "ounce_gram": 28.3495,       # 1 ounce = 28.3495 grams

    # Volume Conversions
    "liter_liter": 1,            # 1 liter = 1 liter (identity)
    "liter_milliliter": 1000,    # 1 liter = 1000 milliliters
    "milliliter_liter": 0.001,   # 1 milliliter = 0.001 liters
    "liter_cubicmeter": 0.001,   # 1 liter = 0.001 cubic meters
    "cubicmeter_liter": 1000,    # 1 cubic meter = 1000 liters
    "liter_gallon": 0.264172,    # 1 liter = 0.264172 gallons (US)
    "gallon_liter": 3.78541,     # 1 gallon (US) = 3.78541 liters
    "milliliter_cubiccentimeter": 1,  # 1 milliliter = 1 cubic centimeter (identity)
    "cubiccentimeter_milliliter": 1,  # 1 cubic centimeter = 1 milliliter (identity)

    # Area Conversions
    "squaremeter_squaremeter": 1,  # 1 square meter = 1 square meter (identity)
    "squaremeter_squarekilometer": 0.000001,  # 1 square meter = 0.000001 square kilometers
    "squarekilometer_squaremeter": 1000000,   # 1 square kilometer = 1,000,000 square meters
    "squaremeter_squarecentimeter": 10000,    # 1 square meter = 10,000 square centimeters
    "squarecentimeter_squaremeter": 0.0001,   # 1 square centimeter = 0.0001 square meters
    "squaremeter_squarefeet": 10.7639,        # 1 square meter = 10.7639 square feet
    "squarefeet_squaremeter": 0.092903,       # 1 square foot = 0.092903 square meters
    "squarekilometer_squaremile": 0.386102,   # 1 square kilometer = 0.386102 square miles
    "squaremile_squarekilometer": 2.58999,    # 1 square mile = 2.58999 square kilometers

    # Time Conversions
    "second_second": 1,          # 1 second = 1 second (identity)
    "second_minute": 0.0166667,  # 1 second = 0.0166667 minutes (1/60)
    "minute_second": 60,         # 1 minute = 60 seconds
    "minute_minute": 1,          # 1 minute = 1 minute (identity)
    "minute_hour": 0.0166667,    # 1 minute = 0.0166667 hours (1/60)
    "hour_minute": 60,           # 1 hour = 60 minutes
    "hour_hour": 1,              # 1 hour = 1 hour (identity)
    "hour_second": 3600,         # 1 hour = 3600 seconds
    "second_hour": 0.000277778,  # 1 second = 0.000277778 hours (1/3600)
    "day_hour": 24,              # 1 day = 24 hours
    "hour_day": 0.0416667,       # 1 hour = 0.0416667 days (1/24)

    # Speed Conversions
    "meterpersecond_kilometerperhour": 3.6,     # 1 m/s = 3.6 km/h
    "kilometerperhour_meterpersecond": 0.277778, # 1 km/h = 0.277778 m/s
    "kilometerperhour_mileperhour": 0.621371,    # 1 km/h = 0.621371 mph
    "mileperhour_kilometerperhour": 1.60934,     # 1 mph = 1.60934 km/h

    # Energy Conversions
    "joule_joule": 1,            # 1 joule = 1 joule (identity)
    "joule_kilojoule": 0.001,    # 1 joule = 0.001 kilojoules
    "kilojoule_joule": 1000,     # 1 kilojoule = 1000 joules
    "joule_calorie": 0.2398459,  # 1 joule = 0.2398459 calories
    "calorie_joule": 4.184,      # 1 calorie = 4.184 joules
    "kilojoule_kilocalorie": 0.2398459,  # 1 kilojoule = 0.2398459 kilocalories
    "kilocalorie_kilojoule": 4.184,      # 1 kilocalorie = 4.184 kilojoules

    # Pressure Conversions
    "pascal_pascal": 1,          # 1 pascal = 1 pascal (identity)
    "pascal_kilopascal": 0.001,  # 1 pascal = 0.001 kilopascals
    "kilopascal_pascal": 1000,   # 1 kilopascal = 1000 pascals
    "pascal_bar": 0.00001,       # 1 pascal = 0.00001 bars
    "bar_pascal": 100000,        # 1 bar = 100,000 pascals
    "pascal_atm": 0.00000986923, # 1 pascal = 0.00000986923 atmospheres
    "atm_pascal": 101325,        # 1 atmosphere = 101,325 pascals

    # Data Storage Conversions
    "byte_byte": 1,              # 1 byte = 1 byte (identity)
    "byte_kilobyte": 0.001,      # 1 byte = 0.001 kilobytes
    "kilobyte_byte": 1000,       # 1 kilobyte = 1000 bytes
    "kilobyte_megabyte": 0.001,  # 1 kilobyte = 0.001 megabytes
    "megabyte_kilobyte": 1000,   # 1 megabyte = 1000 kilobytes
    "megabyte_gigabyte": 0.001,  # 1 megabyte = 0.001 gigabytes
    "gigabyte_megabyte": 1000,   # 1 gigabyte = 1000 megabytes
    "byte_bit": 8,               # 1 byte = 8 bits
    "bit_byte": 0.125,           # 1 bit = 0.125 bytes
    }
  units = f"{unit_from}_{unit_to}".lower()
  if units in conversions:
      conversion = conversions[units]
      return value * conversion
  else:
      return "Conversion not supported"
    
    
    
    
    

st.title("Unit Converter")
value1 = st.number_input("**Enter the Value to Convert**", min_value=0)
col1, col2, = st.columns(2)

    

with col1:
    unit_from1 = st.selectbox(label="**Convert From**", options=[
        "Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Feet", "Mile",
        "Gram", "Kilogram", "Milligram", "Pound", "Ounce",
        "Liter", "Milliliter", "Cubicmeter", "Gallon", "Cubiccentimeter",
        "Squaremeter", "Squarekilometer", "Squarecentimeter", "Squarefeet", "Squaremile",
        "Second", "Minute", "Hour", "Day",
        "Meterpersecond", "Kilometerperhour", "Mileperhour",
        "Joule", "Kilojoule", "Calorie", "Kilocalorie",
        "Pascal", "Kilopascal", "Bar", "Atm",
        "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Bit"
    ], index=None, key=1)
    
with col2:
    unit_to1 = st.selectbox(label="**Convert To**", options=[
        "Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Feet", "Mile",
        "Gram", "Kilogram", "Milligram", "Pound", "Ounce",
        "Liter", "Milliliter", "Cubicmeter", "Gallon", "Cubiccentimeter",
        "Squaremeter", "Squarekilometer", "Squarecentimeter", "Squarefeet", "Squaremile",
        "Second", "Minute", "Hour", "Day",
        "Meterpersecond", "Kilometerperhour", "Mileperhour",
        "Joule", "Kilojoule", "Calorie", "Kilocalorie",
        "Pascal", "Kilopascal", "Bar", "Atm",
        "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Bit"
    ], index=None, key=2)
    
    

if st.button("Convert") and value1 and unit_to1 and unit_from1:
    result = convert_units(value1, unit_from1, unit_to1)
    st.markdown(f"""Converted Value:  <strong style="font-size: 25px; color: red "> {round(result, 3)}</strong>""", unsafe_allow_html=True)
else:
    st.markdown(f"""Please insert the <strong style="color: red "> Value </strong> and select <strong style="color: red ">Units</strong>""", unsafe_allow_html=True)
    