from datetime import datetime

from flask import Blueprint

filters_bp = Blueprint('filters', __name__)


@filters_bp.app_template_filter('time_ago')
def time_ago_filter(dt):
    now = datetime.now()
    diff = now - dt

    periods = [
        ('год', 'года', 'лет'),
        ('месяц', 'месяца', 'месяцев'),
        ('день', 'дня', 'дней'),
        ('час', 'часа', 'часов'),
        ('минуту', 'минуты', 'минут')
    ]

    seconds = diff.total_seconds()
    if seconds <= 0:
        return "только что"

    time_ranges = [
        (365 * 24 * 60 * 60, periods[0]),
        (30 * 24 * 60 * 60, periods[1]),
        (24 * 60 * 60, periods[2]),
        (60 * 60, periods[3]),
        (60, periods[4])
    ]

    for seconds_in_unit, unit_names in time_ranges:
        if seconds >= seconds_in_unit:
            value = int(seconds // seconds_in_unit)
            if value % 10 == 1 and value % 100 != 11:
                return f"{value} {unit_names[0]} назад"
            elif 2 <= value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20):
                return f"{value} {unit_names[1]} назад"
            else:
                return f"{value} {unit_names[2]} назад"

    return "меньше минуты назад"

@filters_bp.app_template_filter('format_datetime')
def format_datetime(value, format='medium'):
    if not value:
        return ""

    if format == 'full':
        format = "%d.%m.%Y %H:%M:%S"
    elif format == 'medium':
        format = "%d.%m.%Y %H:%M"
    elif format == 'date':
        format = "%d.%m.%Y"
    elif format == 'time':
        format = "%H:%M"

    return value.strftime(format)
