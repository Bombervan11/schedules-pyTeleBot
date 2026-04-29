def get_day_schedule(day: str) -> str:
    if day == "Monday":
        return "Monday schedule: Math, Physics"
    return "No schedule found"

def test_monday_schedule():
    result = get_day_schedule("Monday")
    assert "Monday" in result

def test_unknown_day():
    result = get_day_schedule("Sunday")
    assert result == "No schedule found"