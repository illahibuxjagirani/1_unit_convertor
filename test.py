length_units = ["Nautical mile", "Kilometre", "Metre", "Centimetre", "Millimetre", "Micrometre", "Nanometre", "Mile", "Yard", "Foot", "Inch"]

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

options_dict = { "Length": length_conversion_factors}

print(options_dict["Length"]["metre"])