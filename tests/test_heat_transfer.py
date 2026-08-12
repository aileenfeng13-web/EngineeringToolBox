from calculators.heat_transfer import calculate_heat_transfer

def test_heat_transfer():
    result = calculate_heat_transfer(0.8, 10, 20, 0.1)
    assert result == 1600
