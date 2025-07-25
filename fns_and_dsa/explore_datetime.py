# The Use of Datetime in Python
from datetime import datetime
from datetime import timedelta


def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))


number_of_days = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    future_date = datetime + timedelta(days="number_of_days")
    print("Future date: ", future_date.strftime("%Y-%m-%d"))
