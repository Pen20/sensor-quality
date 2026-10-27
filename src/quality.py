def valid_temperature(value: float) -> bool:
    """Return True for plausible equipment temperatures."""
    return -40.0 <= value <= 125.0