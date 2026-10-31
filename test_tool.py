
from tools import calculate_leave_days


def test_leave_calculator():
    result = calculate_leave_days(
        "2026-08-13",
        "2026-08-17"
    )

    assert result == {
        "calendar_days": 5,
        "leave_days": 2,
        "weekend_days": 2,
        "holiday_days": 1,
    }

    result = calculate_leave_days(
        "2026-01-01",
        "2026-01-01"
    )

    assert result == {
        "calendar_days": 1,
        "leave_days": 0,
        "weekend_days": 0,
        "holiday_days": 1,
    }

    result = calculate_leave_days(
        "2026-08-17",
        "2026-08-13"
    )

    assert "error" in result

    result = calculate_leave_days(
        "2025-12-31",
        "2026-01-01"
    )

    assert "error" in result

    print("All leave calculator tests passed!")


if __name__ == "__main__":
    test_leave_calculator()
