from datetime import datetime, timedelta

def convert_to_datetime(time_str, format_str='%H:%M'):
    """
    Convert a string representing time to a datetime object.

    Args:
    time_str (str): The time string to be converted.
    format_str (str): Format of the time string (default is '%H:%M').

    Returns:
    datetime: The corresponding datetime object or None if conversion fails.
    """
    try:
        return datetime.strptime(time_str, format_str)
    except ValueError as e:
        print(f"Error converting time string to datetime: {e}")
        return None

def shift_time(time_str, shift_hours):
    """
    Shifts a time string by a specified number of hours.

    Args:
    time_str (str): The current time of the surgery in 'HH:MM' format.
    shift_hours (int): Number of hours to shift the surgery time.

    Returns:
    str: The new time in 'HH:MM' format, or None if the shift results in invalid time.
    """
    time_obj = convert_to_datetime(time_str)
    if time_obj:
        shifted_time = time_obj + timedelta(hours=shift_hours)
        return shifted_time.strftime('%H:%M')
    return None

# Additional utility functions can be added here...
