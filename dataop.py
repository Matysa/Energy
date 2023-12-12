import csv
from datetime import datetime


date_format = '%d-%m-%Y'

def validate_date(date_text):
    try:
        datetime.strptime(date_text, date_format)
        return True
    except ValueError:
        return False
def format_date(year, month, day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        formatted_date = datetime(year, month, day).strftime(date_format)
        return formatted_date
    except ValueError as e:
        print("Invalid date inputs:", e)
        return None
    
def insert_data_to_csv(date, value1, value2):
    if validate_date(date):
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, value1, value2])
        print("Data inserted successfully!")
    else:
        print("Invalid date format. Please use YYYY-MM-DD.")

insert_data_to_csv(format_date(2020,12,12),234,34)