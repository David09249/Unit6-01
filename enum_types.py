# Created by: David Wang
# Created on: 28-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit6-01
# This program displays an enumerated type

from enum import Enum

# an enumerated type of planets
Days = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

print('Sunday(1), Monday(2), Tuesday(3), Wednesday(4), Thursday(5), Friday(6), Saturday(7)')

day_of_the_week_selected = int(input('Enter the number that corresponds to your favorite day of the week: '))

try:
    if Days[day_of_the_week_selected-1] in Days:
        print('Your favorite day of the week is: ')
        print(Days[day_of_the_week_selected-1])
except:
    print("Please enter a valid number")
