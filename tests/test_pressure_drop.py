from calculators.pressure_drop import calculate_pressure_drop
from utils.unit_conversions import(
    convert_length, convert_velocity, convert_pressure, from_pa
)

def test_pressure_drop():
    result = calculate_pressure_drop(
        friction_factor=0.02, 
        pipe_length=10,
        diameter=0.1,
        density=1000,
        velocity=1
    )

    assert abs(result - 1000) < 0.001

def test_inches_to_metres():
    result = convert_length(4, "in")
    assert abs(result - 0.1016) < 0.000001

def test_feet_per_second_to_metres_per_second():
    result = convert_velocity(10, "ft/s")
    assert abs(result - 3.048 ) < 0.000001

def test_kpa_to_pa():
    result = convert_pressure(100, "kPa")
    assert result == 100000

def test_pa_to_kpa(): 
    result = from_pa(100000, "kPa")
    assert result == 100
    