import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    iso_date = datetime.fromisoformat(iso_string)

                # Format the datetime object as a human-readable string
    human_readable_date = iso_date.strftime("%A %d %B %Y")
    return human_readable_date


# human_readable_date = iso_to_human(iso_string)


"""Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    celcius = (float(temp_in_farenheit) - 32) * 5/9
    return round(celcius,1)

def calculate_mean(weather_data):

    total_sum = 0
    for number in weather_data:
        total_sum += float(number)

    result = len(weather_data)
    calculate_mean = total_sum/result
    return float(calculate_mean)

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file, encoding="utf-8") as weather_data:
       reader = csv.reader(weather_data)
       next(reader)
       csv_data = []
       for data in reader:
         if data != []:
          sub_list = [data[0], float(data[1]), float(data[2])]
          csv_data.append (sub_list)

       return csv_data

# my_list = [1, 2, 3, 2, 4, 3, 5, 6, 1]
# duplicates = find_duplicate_positions(my_list)

# for item, positions in duplicates.items():
#     print(f"Item {item} is duplicated at positions {positions}")

def find_min(weather_data):
    if weather_data == []:
        return ()
    min_value = min(weather_data)
    index_list = []

    for index,value in enumerate(weather_data):
     if value == min_value:
      index_list.append(index)

    return float((min_value)), max(index_list)


"""Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """


def find_max(weather_data):
    
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data == []:
        return ()
    max_value = max(weather_data)
    index_list = []

    for index,value in enumerate(weather_data):
     if value == max_value:
      index_list.append(index)

    return float((max_value)), max(index_list)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
