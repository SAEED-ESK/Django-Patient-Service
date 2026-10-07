from datetime import date

import jdatetime


def gregorian_to_jalali(value):
    """
    تبدیل تاریخ میلادی به تاریخ شمسی
    """

    if not value:
        return ""

    jalali_date = jdatetime.date.fromgregorian(date=value)

    return jalali_date.strftime("%Y/%m/%d")


def jalali_to_gregorian(value):
    """
    تبدیل تاریخ شمسی به تاریخ میلادی
    """

    if not value:
        return None

    value = value.replace("-", "/")

    try:
        year, month, day = map(int, value.split("/"))

        jalali_date = jdatetime.date(year, month, day)

        return jalali_date.togregorian()

    except (ValueError, TypeError):
        return None


def calculate_duration(start_date, end_date=None):
    """
    محاسبه مدت زمان بین دو تاریخ.

    نتیجه به صورت سال، ماه و روز برگردانده می‌شود.
    """

    if not start_date:
        return ""

    if end_date is None:
        end_date = date.today()

    if end_date < start_date:
        return ""

    start_jalali = jdatetime.date.fromgregorian(date=start_date)
    end_jalali = jdatetime.date.fromgregorian(date=end_date)

    years = end_jalali.year - start_jalali.year

    if (
        end_jalali.month < start_jalali.month
        or (
            end_jalali.month == start_jalali.month
            and end_jalali.day < start_jalali.day
        )
    ):
        years -= 1

    adjusted_year = start_jalali.year + years

    if adjusted_year <= 0:
        adjusted_year = start_jalali.year

    try:
        anniversary = jdatetime.date(
            adjusted_year,
            start_jalali.month,
            start_jalali.day,
        )
    except ValueError:
        # برای تاریخ‌هایی که روز موردنظر در سال مقصد وجود ندارد
        anniversary = jdatetime.date(
            adjusted_year,
            start_jalali.month,
            1,
        )

    remaining_days = (
        end_jalali.togregorian() - anniversary.togregorian()
    ).days

    months = remaining_days // 30
    days = remaining_days % 30

    return {
        "years": years,
        "months": months,
        "days": days,
    }

def format_duration(duration):
    """
    تبدیل نتیجه calculate_duration به متن قابل نمایش.
    """

    if not duration:
        return ""

    parts = []

    if duration["years"]:
        parts.append(f'{duration["years"]} سال')

    if duration["months"]:
        parts.append(f'{duration["months"]} ماه')

    if duration["days"]:
        parts.append(f'{duration["days"]} روز')

    if not parts:
        return "کمتر از یک روز"

    return " و ".join(parts)