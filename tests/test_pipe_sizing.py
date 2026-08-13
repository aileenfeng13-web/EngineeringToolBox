import pytest

from calculators.pipe_sizing import find_pipe_diameter

def test_pipe_sizing_finds_solution():
    diameter, pressure_drop = find_pipe_diameter(
        pipe_length=20, 
        density=1000, 
        velocity=2,
        viscosity=0.001,
        roughness=0.000045,
        max_pressure_drop=50000
        )

    assert diameter is not None
    assert pressure_drop <= 50000

def test_negative_velocity():
    with pytest.raises(ValueError): 
        find_pipe_diameter(
            pipe_length=20,
            density=1000,
            velocity=-2,
            viscosity=0.001,
            roughness=0.000045,
            max_pressure_drop=50000
        )

def test_zero_pipe_length():
    with pytest.raises(ValueError):
        find_pipe_diameter(
            pipe_length=0,
            density=1000,
            velocity=2,
            viscosity=0.001,
            roughness=0.000045,
            max_pressure_drop=50000
        )
