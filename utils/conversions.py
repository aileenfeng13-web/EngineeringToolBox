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