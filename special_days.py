import pandas as pd
from datetime import datetime
from typing import List
from typing import Union

def is_holiday(date: str) -> int:
    # print(type(date))
    holidays = [
        # January 2021
        '2021-01-01',  # New Year's Day
        # April 2021
        '2021-04-02',  # Good Friday
        '2021-04-05',  # Easter Monday
        # May 2021
        '2021-05-01',  # Labor Day
        '2021-05-13',  # Driveway
        '2021-05-24',  # Whit Monday
        # August 2021
        '2021-08-01',  # Swiss National Holiday
        # December 2021
        '2021-12-25',  # Christmas
        '2021-12-26',  # St. Stephen's Day
        # January 2022
        '2022-01-01',  # New Year's Day
        # April 2022
        '2022-04-15',  # Good Friday
        '2022-04-18',  # Easter Monday
        # May 2022
        '2022-05-01',  # Labor Day
        '2022-05-26',  # Driveway
        '2022-06-06',  # Whit Monday
        # August 2022
        '2022-08-01',  # Swiss National Holiday
        # December 2022
        '2022-12-25',  # Christmas
        '2022-12-26',  # St. Stephen's Day
        # January 2023
        '2023-01-01',  # New Year's Day
        # April 2023
        '2023-04-07',  # Good Friday
        '2023-04-10',  # Easter Monday
        # May 2023
        '2023-05-01',  # Labor Day
        '2023-05-18',  # Driveway
        '2023-05-29',  # Whit Monday
        # August 2023
        '2023-08-01',  # Swiss National Holiday
        # December 2023
        '2023-12-25',  # Christmas
        '2023-12-26',  # St. Stephen's Day
        # March 2024
        '2024-03-29',  # Good Friday
        # April 2024
        '2024-04-01',  # Easter Monday
        # May 2024
        '2024-05-01',  # Labor Day
        '2024-05-09',  # Driveway
        '2024-05-20',  # Whit Monday
        # August 2024
        '2024-08-01',  # Swiss National Holiday
        # December 2024
        '2024-12-25',  # Christmas
        '2024-12-26'   # St. Stephen's Day
    ]
    date = date[:10]
    if date in holidays:
        return 1
    return 0


def is_special_day(date: str) -> int:
    # print(type(date))
    special_days = [
        '2021-11-25', #christmas lights
        '2022-04-25', #sechselauten
        '2022-06-18',  #pride
        '2022-08-13', #street parade
        '2022-11-24', #christmas lights
        '2023-04-17',  #sechselauten
        '2023-06-17',  #frauenstreik
        '2023-07-07',  #zurifest
        '2023-07-08',  #zurifest
        '2023-07-09',  #zurifest
        '2023-08-12',  #parade
        '2023-10-28',  #palestine demo
        '2023-11-23', #christmas lights
        '2023-12-31',
        '2024-01-01' #nye party
    ]
    date = date[:10]
    if date in special_days:
        return 1
    return 0


if __name__ == '__main__':
    date_array = [
        '2024-05-01 12:00:00',
        '2024-08-01 15:30:00',
        '2024-12-28 09:45:00',
        '2023-12-31 09:45:00',
        '2023-12-31 09:45:00'
    ]

    results = [is_holiday(date) for date in date_array]
    print(results)

    results = [is_special_day(date) for date in date_array]
    print(results)



