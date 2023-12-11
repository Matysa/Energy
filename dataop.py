import csv
from datetime import datetime

# Připravit input a ošetřit vstupy. Separovat input na jednotlivé položky a automatizovat
def get_user_input():
    date_input = input("Enter date in format YYYY-MM-DD: ")
    time_input = input("Enter time HH:MM:SS: ")
    value_input = input("Enter the value of water: ")

    return date_input, time_input, value_input


def parse_date_time(date_str, time_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        time = datetime.strptime(time_str, '%H:%M:%S').time()
        return datetime.combine(date, time)
    except ValueError:
        print("Invalid format of date or time")
        return None

date_input, time_input, value_input = get_user_input()

datetime_input = parse_date_time(date_input, time_input)


print(datetime_input, value_input)



