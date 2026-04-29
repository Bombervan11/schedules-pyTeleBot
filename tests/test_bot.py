def test_unknown_day():
    result = get_day_schedule("Sunday")
    assert result == "Wrong text"  # навмисно неправильно