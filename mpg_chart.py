"""MPG Chart Display by Brady Esplin.

Program reads vehicle data from the Enviromental Protection Agency csv
list. Program error checks input against available data. Program displays
data using Matplotlib.
"""


# Start here
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


def get_data():
    """Read file, write as tuples into list."""
    data = []
    with open('vehicles.csv', 'r') as epa_file:
        csv_reader = csv.DictReader(epa_file)
        for row in csv_reader:
            vehicle_tuple = (
                row["id"],  # [0]
                int(row["year"]),  # [1]
                row["make"],  # [2]
                row["model"],  # [3]
                row["VClass"],  # [4]
                int(row["comb08"])  # [5]
            )
            data.append(vehicle_tuple)
        return data


def get_years(data):
    """Get possible years for error-checking."""
    years = []
    for row in data:
        years.append(row[1])

    return set(years)


def get_VClasses(data):
    """Get possible vehice classes for error-checking."""
    VClasses = []
    for row in data:
        VClasses.append(row[4])

    return set(VClasses)


def get_makes(data):
    """Get manufacturers for error-testing."""
    makes = []
    for row in data:
        makes.append(row[2])

    return set(makes)


def main():
    """Handle I/O.

    Error-checks user input.
    """
    data = get_data()
    # temp_function(data)

    print("Hello User! I will show you vehicle fuel efficiencies in the\
 form of a graph!")
    print("Lets start by selecting what year you would like to look at!")
    # years = get_years(data)

    while True:
        year = int(input("Please type your four number year (1984-2020)\
 and press ENTER:"))
        if 1984 > year < 2020:
            print("That is not a valid year, please try again!")
            continue
        break

    print("You can select from the following vehicle classes:")
    VClasses = get_VClasses(data)
    print(VClasses)

    while True:
        VClass = input("Please input your vehicle class and press ENTER:")
        if VClass not in VClasses:
            print("That is not a vaild Vehicle Class, please try again!")
            continue
        break

    print("I have information about the following vehicle manufacturing\
 companies:")
    makes = get_makes(data)
    print(makes)

    while True:
        make = input("Please input the name of the manufacturer and press\
 ENTER:")
        if make not in makes:
            print("That is not a valid manufacturer, please try again!")
            continue
        break

# Using list intersections to filter out all but the user-selected entries

    new_year = [year]
# Compares list:data to user-input: year, writes all matches into new list
    new_year_list = [tup for tup in data if any(i in tup for i in new_year)]
    new_make = [make]
# Compares list:new_year_list to user-input: make, writes all matches into
# a new list
    new_make_list = [tup for tup in new_year_list if any(i in tup for i
                     in new_make)]
    new_VClass = [VClass]
# Compares list:new_make_list to user-input: VClass, writes all matches
# into a new list
    new_vehicle_list = [tup for tup in new_make_list if any(i in tup
                        for i in new_VClass)]


# Iterates through new_vehicle_list for models
    display_models = [line[3] for line in new_vehicle_list]
# Iterates through new_vehicle_list for mpg
    display_mpg = [line[5] for line in new_vehicle_list]

    print(f'Display Models: {display_models}')
    print(f'Display MPG: {display_mpg}')


# matplotlib

# I don't know how I got this to work. I will take a stab at it
# but I copied and pasted from a tutorial, then messed around with it
# until I accidentaly got it to do what I wanted

# sets the display objects to my list of display models
    objects = (display_models)
# makes the y values have the same number as by objects
    y_pos = np.arange(len(objects))
# displays range of numbers in my range of mpg values
    performance = (display_mpg)

# this makes the graph cetered on the screen?
    plt.barh(y_pos, performance, align='center', alpha=0.5)
# This sets the reference numbers on the y axis around my range of mpg
# values
    plt.yticks(y_pos, objects)
# Labels the graph
    plt.xlabel('Miles Per Gallon')
# Titles the graph
    plt.title('Miles per Gallon of Fuel for Model of Vehicle')
# Displays the graph
    plt.show()


# execute program
if __name__ == "__main__":
    main()

# Things I could have done better:
# There is not enough vehicle description on the graph
# I could have taken engine displacement and transmission type and graphed
# those as well, it would have differentiated the same models of vehicle
# from each other better.
# At this point I don't know that I should go back and try to implement
# that as I have a whole other final project to complete, due tomorrow and
# I am already having trouble stringing along enough coherent thought to
# type these comments.
