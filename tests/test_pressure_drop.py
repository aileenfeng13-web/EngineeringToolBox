from calculators.pressure_drop import calculate_pressure_drop

def test_pressure_drop():
    result = calculate_pressure_drop(
        friction_factor=0.02, 
        pipe_length=10,
        diameter=0.1,
        density=1000,
        velocity=1
    )

    assert abs(result - 1000) < 0.001