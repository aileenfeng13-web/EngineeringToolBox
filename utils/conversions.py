LENGTH_TO_METERS = {
    "Meters": 1, 
    "Centimeters": 0.01, 
    "Milimeters": 0.001, 
    "Kilometers": 1000, 
    "Inches": 0.0254, 
    "Feet": 0.3048

}

def convert_length(value, from_unit, to_unit): 
    """
    Convert between different length units
    """

    value_in_meters = value * LENGTH_TO_METERS[from_unit]

    result = value_in_meters / LENGTH_TO_METERS[to_unit]

    return result

MASS_TO_KILOGRAMS = {
    "Kilograms": 1, 
    "Grams": 0.001, 
    "Pounds": 0.45359237
}

def convert_mass(value, from_unit, to_unit):
    """
    Convert between differnt mass units.
    """
    value_in_kilogram = value * MASS_TO_KILOGRAMS[from_unit]

    result = value_in_kilogram / MASS_TO_KILOGRAMS[to_unit]

    return result 

def convert_temperature(value, from_unit, to_unit): 
    """
    Convert between celsius, farenheit, and kelvin. 
    """
    # Step 1: Convert to celsius
    if from_unit == "Celsius": 
        celsius = value 

    elif from_unit == "Fahrenheit": 
        celsius = (value - 32)*5/9

    elif from_unit == "Kelvin": 
        celsius = value -273.15 

    # Step 2: Convert from celsius to respective unit
    if to_unit == "Celsius": 
        return celsius 

    elif to_unit == "Fahrenheit": 
        return celsius * 9 / 5 + 32 

    elif to_unit == "Kelvin": 
        return celsius + 273.15