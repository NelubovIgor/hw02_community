import datetime


def year(request):
    year = datetime.date.today()
    """Добавляет переменную с текущим годом."""
    return {
        'year': year.year,
    }
