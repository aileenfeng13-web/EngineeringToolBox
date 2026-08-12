def convert_length(value, unit):
    """
    Convert a length to metres.
    """
    conversions = {
        "m":1,
        "cm":0.01,
        "km":1000,
        "in":0.0254,
        "ft":0.3048,
    }
    return value * conversions[unit]

def convert_pressure(value, unit):
    """
    Convert pressure to Pascals.
    """
    conversions = {
        "Pa":1,
        "kPa":1000,
        "MPa":1_000_000,
        "bar":100_000,
        "psi":6894.757,
    }
    return value * conversions[unit]

def convert_velocity(value, unit):
    """
    Convert velocity to metres per second.
    """
    conversions = {
        "m/s":1,
        "cm/s":0.01, 
        "ft/s":0.3048,
        "km/h":1000/3600,
        "mph":0.44704,
    }
    return value * conversions[unit]

def from_pa(value, unit):
    """
    Convert pressure from Pascals to the selected unit.
    """
    conversions = {
        "Pa":1, 
        "kPa":1000, 
        "MPa":1_000_000, 
        "bar":100_000, 
        "psi":6894.757,
    }
    return value / conversions[unit]

