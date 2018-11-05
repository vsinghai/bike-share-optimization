import csv
from collections import Counter
#import numpy as np 
from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import matplotlib.pyplot as plt
from mapsplotlib import mapsplot as mplt
import numpy as np 


#Winter = 20161221 to 20160320 (do the same for 2017)
#Spring = 20160320 to 20160620 (do the same for 2017)
#Summer = 20160620 to 20160922 (do the same for 2017)
#Fall   = 20160922 to 20161221 (do the same for 2017)

class AverageTime():
    def getTime(self):
        denominatorSum = 0

        #opening csv file 
        with open('metro-bike-share-trip-data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',') #creating an iterable reader object
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                    #These are the headers
                else:
                    denominatorSum+= int(row[1])
                    line_count += 1
                    #These are the rows 
            #print(f'Processed {line_count} lines.')
            return (denominatorSum/line_count)

time = AverageTime()
# print("Average time in seconds: {}".format(time.getTime()))

class Distance():
    distanceList = []
    line_count = 0
    def listofDistances(self):
        
        with open('metro-bike-share-trip-data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if self.line_count == 0:
                    self.line_count += 1
                else:
                    if row[5] == '' or row[6] == '' or row[8] == '' or row[9] == '':
                        self.distanceList.append(0)
                        self.line_count += 1
                    else: 
                        #print("{}, {}, {}, {}".format(row[5],row[6], row[8], row[9]))
                        R = 6373.0

                        lat1 = radians(float(row[5]))
                        lon1 = radians(float(row[6]))
                        lat2 = radians(float(row[8]))
                        lon2 = radians(float(row[9]))

                        dlon = lon2 - lon1
                        dlat = lat2 - lat1

                        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                        c = 2 * atan2(sqrt(a), sqrt(1 - a))

                        distance = R * c
                        miles = distance * 0.621371

                        #print("Final Result: {}".format(miles))
                        #print("Final Result Miles: ", miles)
                        self.line_count += 1
                        self.distanceList.append(miles)
            return self.distanceList
    def averageDistance(self):
        sumDistanceList = sum(self.distanceList)
        print("The sum of the distance in miles is: {}".format(sumDistanceList))
        print("The line count is: {}".format(self.line_count))
        return sumDistanceList/self.line_count
coordinateDistance = Distance()
coordinateDistance.listofDistances()
print("The average distance in miles is: {}".format(coordinateDistance.averageDistance()))


class Season():
    
    
    def __init__(self):
        self.winterList = []
        self.springList = []
        self.fallList = []
        self.summerList = []
        
    def getUsedBike(self): 
        #opening csv file
        season = [] 
        with open('metro-bike-share-trip-data.csv') as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',') #creating an iterable reader object
            line_count = 0
            for row in csv_reader: 
                if line_count == 0:
                    line_count += 1
                else: 
                    dashReplace = row[2].replace("-", "")
                    indexT = dashReplace.index("T")
                    seasonInt = int(dashReplace[0:indexT])
                    season.append(seasonInt)
                    
            
        return(season)

    def winter(self, number):
        winterList = []
    
        if (number >= 20161221 and number <= 20161231) or (number <= 20160320)  or (number >= 20171221 and number <= 20171231)  or (number <= 20170320 and number >= 20170101):
            winterList.append(number)
            return True

        return False

    def spring(self, number):
        springList = []
        if (number >= 20160320 and number <= 20160620) or (number >= 20170320 and number <= 20170620):
            springList.append(number)
            return True

        return False

    def summer(self, number):
        summerList = []
        if (number >= 20160620 and number <= 20160922) or (number >= 20170620 and number <= 20170922):
            summerList.append(number)
            return True
    
        return False
    
    def fall(self, number):
        fallList = []
    
        if (number >= 20160922 and number <= 20161221) or (number >= 20170922 and number <= 20171221):
            fallList.append(number)
            return True

        return False
    
    def lists(self):
        yo = Season()
        with open('metro-bike-share-trip-data.csv') as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',') #creating an iterable reader object
            line_count = 0
            for row in csv_reader: 
                if line_count == 0:
                    line_count += 1
                else: 
                    dashReplace = row[2].replace("-", "")
                    indexT = dashReplace.index("T")
                    seasonInt = int(dashReplace[0:indexT])
                    if (yo.winter(seasonInt)):
                        self.winterList.append(row)
                    elif (yo.spring(seasonInt)):
                        self.springList.append(row)
                    elif(yo.summer(seasonInt)):
                        self.summerList.append(row)
                    else:
                        self.fallList.append(row)
        return(self.winterList)

    def winterL(self):
        yo = Season()
        sum = 0
        line_count = 0
        for row in yo.lists():
            if row[5] != '' and row[6] != '' and row[8] != '' and row[9] != '':
                R = 6373.0

                lat1 = radians(float(row[5]))
                lon1 = radians(float(row[6]))
                lat2 = radians(float(row[8]))
                lon2 = radians(float(row[9]))

                dlon = lon2 - lon1
                dlat = lat2 - lat1

                a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))

                distance = R * c
                miles = distance * 0.621371
                sum += miles
                line_count += 1
        
        print(sum/line_count)

        # cleanedLat = []
        # for row in yo.lists():
        #     try:
        #         if (row[5] != '' and row[5] != 'Starting Station Latitude' and float(row[5]) != 0 and 
        #             row[6] != '' and row[6] != 'Starting Station Longitude' and float(row[6]) != 0):
        #             cleanedLat.append((float(row[5]), float(row[6])))
        #     except ValueError:
        #         print("Error: {}".format(type(row[5])))
        #         print(row[5])

        # for i, j in cleanedLat:
        #     print("new google.maps.LatLng({}, {}), ".format(i, j))


season  = Season()
print(season.winterL())
