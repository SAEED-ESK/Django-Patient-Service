import jdatetime
from django import template


register = template.Library()


@register.filter
def jalali_date(value):
    """
    تبدیل تاریخ میلادی به تاریخ شمسی برای نمایش در Template.
    """

    if not value:
        return ""

    try:
        jalali = jdatetime.date.fromgregorian(date=value)
        return jalali.strftime("%Y/%m/%d")
    except (ValueError, TypeError):
        return value