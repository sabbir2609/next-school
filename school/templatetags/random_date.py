import random
from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter(name="random_date")
def random_date(start_date, end_date):
    try:
        # Convert the start_date and end_date to datetime objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Calculate the range of days between start_date and end_date
        days_difference = (end_date - start_date).days

        # Generate a random number of days within the range
        random_days = random.randint(0, days_difference)

        # Calculate the random date
        random_date = start_date + timedelta(days=random_days)

        # Format the random date as a string
        return random_date.strftime("%Y-%m-%d")
    except Exception as e:
        return str(e)
