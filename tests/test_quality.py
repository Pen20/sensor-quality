from src.quality import valid_temperature

def test_temperature_limits():
    assert valid_temperature(20.0)
    assert valid_temperature(-40.0)
    assert valid_temperature(125.0)
    assert not valid_temperature(126.0)

def test_missing_temperature():
    assert not valid_temperature(None)