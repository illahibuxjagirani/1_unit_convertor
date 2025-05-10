import streamlit as st


  
print("Hello World")
# conversion value for Area
area_conversion_factors = {
    "square kilometre": 1000000,      # 1 sq km = 1,000,000 sq m
    "square metre": 1,                # Base unit
    "square mile": 2589988.11,        # 1 sq mile ≈ 2,589,988.11 sq m
    "square yard": 0.83612736,        # 1 sq yard ≈ 0.83612736 sq m
    "square foot": 0.09290304,        # 1 sq ft ≈ 0.09290304 sq m
    "square inch": 0.00064516,        # 1 sq in ≈ 0.00064516 sq m
    "hectare": 10000,                 # 1 hectare = 10,000 sq m
    "acre": 4046.8564224              # 1 acre ≈ 4,046.8564224 sq m
}

# Conversion value for Data Transfer Rate
data_transfer_rate_conversion_factors = {
    "bit per second": 1,
    "kilobit per second": 1000,
    "kilobyte per second": 8000,
    "kibibit per second": 1024,
    "megabit per second": 1000000,
    "megabyte per second": 8000000,
    "mebibit per second": 1048576,
    "gigabit per second": 1000000000,
    "gigabyte per second": 8000000000,
    "gibibit per second": 1073741824,
    "terabit per second": 1000000000000,
    "terabyte per second": 8000000000000,
    "tebibit per second": 1099511627776
}


# Conversion value for Digital Storage
digital_storage_conversion_factors = {
    "kilobit": 125,              # 1 kilobit = 125 bytes
    "kibibit": 128,              # 1 kibibit = 128 bytes
    "megabit": 125000,           # 1 megabit = 125,000 bytes
    "mebibit": 131072,           # 1 mebibit = 131,072 bytes
    "gigabit": 125000000,        # 1 gigabit = 125,000,000 bytes
    "gibibit": 134217728,        # 1 gibibit = 134,217,728 bytes
    "terabit": 125000000000,     # 1 terabit = 125,000,000,000 bytes
    "tebibit": 137438953472,     # 1 tebibit = 137,438,953,472 bytes
    "petabit": 125000000000000,  # 1 petabit = 125,000,000,000,000 bytes
    "pebibit": 140737488355328,  # 1 pebibit = 140,737,488,355,328 bytes
    "byte": 1,                   # Base unit
    "kilobyte": 1000,            # 1 kilobyte = 1,000 bytes
    "kibibyte": 1024,            # 1 kibibyte = 1,024 bytes
    "megabyte": 1000000,         # 1 megabyte = 1,000,000 bytes
    "mebibyte": 1048576,         # 1 mebibyte = 1,048,576 bytes
    "gigabyte": 1000000000,      # 1 gigabyte = 1,000,000,000 bytes
    "gibibyte": 1073741824       # 1 gibibyte = 1,073,741,824 bytes
}

# Conversion value for Energy
energy_conversion_factors = {
    "joule": 1,                        # Base unit
    "kilojoule": 1000,                 # 1 kJ = 1,000 J
    "gram calorie": 4.184,             # 1 cal = 4.184 J
    "kilocalorie": 4184,               # 1 kcal = 4,184 J
    "watt hour": 3600,                 # 1 Wh = 3,600 J
    "kilowatt-hour": 3600000,          # 1 kWh = 3,600,000 J
    "electronvolt": 1.60218e-19,       # 1 eV = 1.60218 × 10⁻¹⁹ J
    "british thermal unit": 1055.05585, # 1 BTU = 1,055.05585 J
    "us therm": 105505585.2,           # 1 US therm = 105,505,585.2 J
    "foot-pound": 1.35581795           # 1 ft-lb = 1.35581795 J
}

# Conversion value for Frequency
frequency_conversion_factors = {
    "hertz": 1,            # Base unit
    "kilohertz": 1000,     # 1 kHz = 1,000 Hz
    "megahertz": 1000000,  # 1 MHz = 1,000,000 Hz
    "gigahertz": 1000000000  # 1 GHz = 1,000,000,000 Hz
}

# conversion Fuel Economy
fuel_economy_conversion_factors = {
    "kilometer per liter": 1,              # Base unit
    "mile per us gallon": 0.425144,        # 1 mpg (US) ≈ 0.425144 km/L
    "mile per gallon": 0.425144            # Assuming US gallon, same as above
}

# conversion Value for length 
length_conversion_factors = {
        "nautical mile": 1852,        # 1 nautical mile = 1852 meters
        "kilometre": 1000,           # 1 kilometer = 1000 meters
        "metre": 1,                  # Base unit
        "centimetre": 0.01,          # 1 centimeter = 0.01 meters
        "millimetre": 0.001,         # 1 millimeter = 0.001 meters
        "micrometre": 0.000001,      # 1 micrometer = 0.000001 meters
        "nanometre": 0.000000001,    # 1 nanometer = 0.000000001 meters
        "mile": 1609.344,            # 1 mile = 1609.344 meters
        "yard": 0.9144,              # 1 yard = 0.9144 meters
        "foot": 0.3048,              # 1 foot = 0.3048 meters
        "inch": 0.0254               # 1 inch = 0.0254 meters
    }

# Conversion value for mass
mass_conversion_factors = {
    "tonne": 1000000,         # 1 tonne = 1,000,000 g
    "kilogram": 1000,         # 1 kg = 1,000 g
    "gram": 1,                # Base unit
    "milligram": 0.001,       # 1 mg = 0.001 g
    "microgram": 0.000001,    # 1 µg = 0.000001 g
    "imperial ton": 1016046.9088,  # 1 imperial ton ≈ 1,016,046.9088 g
    "us ton": 907184.74,      # 1 US ton = 907,184.74 g
    "stone": 6350.29318,      # 1 stone = 6,350.29318 g
    "pound": 453.59237,       # 1 lb = 453.59237 g
    "ounce": 28.349523125     # 1 oz = 28.349523125 g
}

# conversion value for plane angle
plane_angle_conversion_factors = {
    "arcsecond": 0.000004848,     # 1 arcsec ≈ 0.000004848 rad
    "degree": 0.0174533,          # 1 deg ≈ 0.0174533 rad
    "gradian": 0.015708,          # 1 grad ≈ 0.015708 rad
    "milliradian": 0.001,         # 1 mrad = 0.001 rad
    "minute of arc": 0.000290888, # 1 arcmin ≈ 0.000290888 rad
    "radian": 1                   # Base unit
}

# conversion value for Pressure
pressure_conversion_factors = {
    "bar": 100000,          # 1 bar = 100,000 Pa
    "pascal": 1,            # Base unit
    "pound per square inch": 6894.75729,  # 1 psi ≈ 6,894.75729 Pa
    "standard atmosphere": 101325,  # 1 atm = 101,325 Pa
    "torr": 133.322368      # 1 torr ≈ 133.322368 Pa
}

# conversion value for speed
speed_conversion_factors = {
    "mile per hour": 0.44704,      # 1 mph ≈ 0.44704 m/s
    "foot per second": 0.3048,      # 1 ft/s = 0.3048 m/s
    "metre per second": 1,          # Base unit
    "kilometre per hour": 0.277778, # 1 km/h ≈ 0.277778 m/s
    "knot": 0.514444               # 1 knot ≈ 0.514444 m/s
}

# conversion value for temperature
temperature_conversion_factors = {
    "degree celsius": 1,      # Scaling factor (offset: +273.15 K)
    "fahrenheit": 0.555556,   # Scaling factor (offset: -459.67°F = 0 K)
    "kelvin": 1               # Base unit (no offset)
}

# conversion value for time
time_conversion_factors = {
    "nanosecond": 0.000000001,    # 1 ns = 10⁻⁹ s
    "microsecond": 0.000001,      # 1 µs = 10⁻⁶ s
    "millisecond": 0.001,         # 1 ms = 10⁻³ s
    "second": 1,                  # Base unit
    "minute": 60,                 # 1 min = 60 s
    "hour": 3600,                 # 1 h = 3,600 s
    "day": 86400,                 # 1 d = 86,400 s
    "week": 604800,               # 1 week = 604,800 s
    "month": 2628000,             # 1 month ≈ 2,628,000 s (average)
    "calendar year": 31536000,    # 1 year ≈ 31,536,000 s (365.25 days)
    "decade": 315360000,          # 1 decade ≈ 315,360,000 s
    "century": 3153600000         # 1 century ≈ 3,153,600,000 s
}

# conversion value for volume
volume_conversion_factors = {
    "us liquid gallon": 3.78541,         # 1 US gallon = 3.78541 liters
    "us liquid quart": 0.946353,         # 1 US quart = 0.946353 liters
    "us liquid pint": 0.473176,          # 1 US pint = 0.473176 liters
    "us legal cup": 0.24,                # 1 US legal cup = 0.24 liters
    "us fluid ounce": 0.0295735,         # 1 US fluid ounce = 0.0295735 liters
    "us tablespoon": 0.0147868,          # 1 US tablespoon = 0.0147868 liters
    "us teaspoon": 0.00492892,           # 1 US teaspoon = 0.00492892 liters
    "cubic meter": 1000,                 # 1 cubic meter = 1,000 liters
    "liter": 1,                          # Base unit
    "milliliter": 0.001,                 # 1 milliliter = 0.001 liters
    "imperial gallon": 4.54609,          # 1 Imperial gallon = 4.54609 liters
    "imperial quart": 1.13652,           # 1 Imperial quart = 1.13652 liters
    "imperial pint": 0.568261,           # 1 Imperial pint = 0.568261 liters
    "imperial cup": 0.284131,            # 1 Imperial cup = 0.284131 liters
    "imperial fluid ounce": 0.0284131,   # 1 Imperial fluid ounce = 0.0284131 liters
    "imperial tablespoon": 0.0177582     # 1 Imperial tablespoon = 0.0177582 liters
}



main_options = ["Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"]


# Area Units
area_units = ["Square kilometre", "Square metre", "Square mile", "Square yard", "Square foot", "Square inch", "Hectare", "Acre"]

# data transfer rate units
data_transfer_rate_units = [
    "Bit per second","Kilobit per second","Kilobyte per second","Kibibit per second", "Megabit per second","Megabyte per second","Mebibit per second","Gigabit per second","Gigabyte per second","Gibibit per second","Terabit per second","Terabyte per second","Tebibit per second"
]

# digital storage units
digital_storage_units = [
    "Kilobit",
    "Kibibit",
    "Megabit",
    "Mebibit",
    "Gigabit",
    "Gibibit",
    "Terabit",
    "Tebibit",
    "Petabit",
    "Pebibit",
    "Byte",
    "Kilobyte",
    "Kibibyte",
    "Megabyte",
    "Mebibyte",
    "Gigabyte",
    "Gibibyte"
]

# Energy units
energy_units = [
    "Joule",
    "Kilojoule",
    "Gram calorie",
    "Kilocalorie",
    "Watt hour",
    "Kilowatt-hour",
    "Electronvolt",
    "British thermal unit",
    "US therm",
    "Foot-pound"
]

# Frequency units
frequency_units = [
    "Hertz",
    "Kilohertz",
    "Megahertz",
    "Gigahertz"
]

# Fuel Economy units
fuel_economy_units = [
    "Kilometer per liter",
    "Mile per US gallon",
    "Mile per gallon",
]

# Length Units
length_units = [ "Kilometre", "Metre", "Centimetre", "Millimetre", "Micrometre", "Nanometre", "Mile", "Yard", "Foot", "Inch", "Nautical mile"]

# mass units
mass_units = [
    "Tonne",
    "Kilogram",
    "Gram",
    "Milligram",
    "Microgram",
    "Imperial ton",
    "US ton",
    "Stone",
    "Pound",
    "Ounce"
]

# Plane angle units
plane_angle_units = [
    "Arcsecond",
    "Degree",
    "Gradian",
    "Milliradian",
    "Minute of arc",
    "Radian"
]

#Pressure units
pressure_units = [
    "Bar",
    "Pascal",
    "Pound per square inch",
    "Standard atmosphere",
    "Torr"
]

# Speed units
speed_units = [
    "Mile per hour",
    "Foot per second",
    "Metre per second",
    "Kilometre per hour",
    "Knot"
]

# Temperature units
temperature_units = [
    "Degree Celsius",
    "Fahrenheit",
    "Kelvin"
]

# time units
time_units = [
    "Nanosecond",
    "Microsecond",
    "Millisecond",
    "Second",
    "Minute",
    "Hour",
    "Day",
    "Week",
    "Month",
    "Calendar year",
    "Decade",
    "Century"
]

# Volume units
volume_units = [
    "US liquid gallon",
    "US liquid quart",
    "US liquid pint",
    "US legal cup",
    "US fluid ounce",
    "US tablespoon",
    "US teaspoon",
    "Cubic meter",
    "Liter",
    "Milliliter",
    "Imperial gallon",
    "Imperial quart",
    "Imperial pint",
    "Imperial cup",
    "Imperial fluid ounce",
    "Imperial tablespoon"
]

st.markdown("<h1 style='text-align: center;'>Unit convertor</h1>", unsafe_allow_html=True)

select_main_options = st.selectbox("", main_options)

col1, col2, col3 = st.columns([2, .25, 2], vertical_alignment="center")



main_options_dict = {"Area": area_units,"Data Transfer Rate": data_transfer_rate_units,"Digital Storage": digital_storage_units, "Energy": energy_units,"Frequency": frequency_units,"Fuel Economy": fuel_economy_units, "Length": length_units, "Mass": mass_units, "Plane Angle": plane_angle_units, "Pressure": pressure_units, "Speed": speed_units, "Temperature": temperature_units, "Time": time_units, "Volume": volume_units}

options_dict = {"Area": area_conversion_factors, "Data Transfer Rate": data_transfer_rate_conversion_factors, "Digital Storage": digital_storage_conversion_factors,"Energy": energy_conversion_factors, "Frequency": frequency_conversion_factors,"Fuel Economy": fuel_economy_conversion_factors, "Length": length_conversion_factors, "Mass": mass_conversion_factors, "Plane Angle": plane_angle_conversion_factors, "Pressure": pressure_conversion_factors, "Speed": speed_conversion_factors, "Temperature": temperature_conversion_factors, "Time": time_conversion_factors, "Volume": volume_conversion_factors}



to_product:float = 1
from_product:float = 1.0
with col1:
   to_box = st.selectbox("", main_options_dict[select_main_options], key="to_box" )
   to_value = (st.number_input("", key="to", value=to_product))
   if to_value > 0:
      to_product = (options_dict[select_main_options])[to_box.lower()] * to_value
   
with col2:
   st.title("=")



with col3:
   from_box = st.selectbox("", main_options_dict[select_main_options], key="from_box")
   from_product = (options_dict[select_main_options])[from_box.lower()]
   result = round((to_product/from_product), 4)
   from_value = st.text_input("", key="from", value=result)


