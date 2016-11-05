"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file,delimiter):
    """ Parses a raw CSV file to a JSON-line object"""

    #open CSV file
    opened_file = open(raw_file)
    #read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    
    # setup an empty list    
    parsed_data =[]

    #skip first line of the file for headers
    fields = csv_data.next()

    #iterate over each row of the csv, zip together the field and value

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    #close the csv
    opened_file.close()


    return parsed_data

def visualize_days():
    """ Visualise data by day of the week"""

    # grab our parsed data that we parsed earlier 
    data_file = parse(MY_FILE, ",")



    # make a new variable "counter" from iterating through each line of data 
    # in the parsed data, and count how many incidents happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # separate the x-axis data (the days of the week) from the "counter" variable from 
    #the y-axis data (number of incidents per year)
    data_list = [
                counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
                ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    #with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
    #create the amount of ticks needed for our x-axis and assign the labels 
    plt.xticks(range(len(day_tuple)), day_tuple)
    # save the plot
    plt.savefig("Days.png")
    #close plot file
    plt.clf()


def visualize_type():
    """Visualize data by category in a bar graph"""

    # grab our parsed data
    data_file = parse(MY_FILE, ",")
    # make a new variable, 'counter', from iterating through each line
    # of data in the parsed data, and count how many incidents happen
    # by category
    counter = Counter(item["Category"] for item in data_file)
    # Set the labels which are based on the keys of our counter.
    # Since order doesn't matter, we can just used counter.keys()
    labels = tuple(counter.keys())
    # Set exactly where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5
    # Width of each bar that will be plotted
    width = 0.5
    # Assign data to a bar plot (similar to plt.plot()!)
    plt.bar(xlocations, counter.values(), width = width)
    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width/2, labels, rotation = 90)

    # Give some more room so the x-axis labels aren't cut off in the
    # graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure is larger
    plt.rcParams("figure.figsize") = 12, 8
    # Save the graph!
    plt.savefig("Type.png")

    # Close plot figure
    plt.clf()

def main():
   # visualize_days()
   visualize_type()

"""
def main():
    new_data = parse(MY_FILE, ",")

    print new_data
"""
if __name__ == "__main__":
    main()
