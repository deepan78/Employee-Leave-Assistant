
from datetime import datetime, timedelta


HOLIDAYS = {
    datetime(2026, 1, 1).date(),
    datetime(2026, 8, 14).date(),
    datetime(2026, 12, 25).date(),
}


def calculate_leave_days(start_date: str, end_date: str) -> dict:
    """Calculate leave days for a date range within 2026."""

    # Validate the exact YYYY-MM-DD format and actual dates.
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()

        if start.strftime("%Y-%m-%d") != start_date:
            raise ValueError

        if end.strftime("%Y-%m-%d") != end_date:
            raise ValueError

    except (ValueError, TypeError):
        return {
            "error": "Invalid date. Use YYYY-MM-DD format."
        }

    # Only dates within 2026 are supported.
    if start.year != 2026 or end.year != 2026:
        return {
            "error": "Only date ranges within 2026 are supported."
        }

    # End date must not precede start date.
    if end < start:
        return {
            "error": "End date cannot be before the start date."
        }

    calendar_days = (end - start).days + 1
    leave_days = 0
    weekend_days = 0
    holiday_days = 0

    current = start

    while current <= end:
        if current.weekday() >= 5:
            # Saturday or Sunday
            weekend_days += 1
        elif current in HOLIDAYS:
            # Holiday on a weekday
            holiday_days += 1
        else:
            leave_days += 1

        current += timedelta(days=1)

    return {
        "calendar_days": calendar_days,
        "leave_days": leave_days,
        "weekend_days": weekend_days,
        "holiday_days": holiday_days,
    }
