def valid_temperature(value: float | None) -> bool:
    """Return True for plausible equipment temperatures."""
    if value is None:
        return False

    return -40.0 <= value <= 125.0