"""
April 14th, 2021

A program that separates the raw data out of a list,
and puts it in all into neatly organized tables
"""

import re

""" Function that will split up a string
and place each part into an appropiate list """
def dataSorter(rawData):
    
    # list where sorted items will go
    sortedList = []

    #classCode = re.split('[^a-zA-Z]', rawData)

    # Separates the class code and puts it in the sortedList
    classCode = rawData[:5]
    sortedList.append(classCode)


    # Finds every 
    classTitle = re.findall('[^0-9][a-zA-Z]+', rawData[5:])
    classTitle = classTitle.pop(0)
    

    # Adds back in spaces
    classTitle = re.sub("to", " to ", classTitle)

    print(classTitle)

    sortedList.append(classTitle)

    classNumber = re.findall('[^a-zA-Z][0-9]+', rawData[5:])
    classNumber = classNumber.pop(0)
    sortedList.append(classNumber)


    print(sortedList)




def main():
    courses = ['CS152Introduction to Python Programming21',
               'CS369Operating Systems Administration8',
               'CS352Data Structures19',
               'CS208Discrete Mathematics124',
               'CS319Computer Architecture14',
               'MA221Calculus and Analytical Geometry for Majors I12',
               'MA311Linear Algebra7',
               'MA150Precalculus Mathematics27',
               'CS335Introduction to Cybersecurity20',
               'IS361Data Management Systems22',
               'MG315Advanced Business Statistics6' ]
               
            
    testTable = "CS155IntrotoButt21"
    testTableTwo = "CS111SpecialVictimsUnit69"

    dataSorter(testTableTwo)

main()
