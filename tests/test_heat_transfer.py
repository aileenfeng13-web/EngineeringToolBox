import pytest

from calculators.heat_transfer import calculate_heat_transfer

def test_heat_transfer():
    result = calculate_heat_transfer(0.8, 10, 20, 0.1)
    assert result == 1600

def test_zero_thickness(): 
    with pytest.raises(ValueError):
        calculate_heat_transfer(0.8, 10, 20, 0)

def test_negative_area():
    with pytest.raises(ValueError):
        calculate_heat_transfer(0.8,-10,20,0.1)
        
