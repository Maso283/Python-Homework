"""
Justin L. Roberts
April 14th, 2021

A program that separates the raw data out of a list,
and puts it in all into neatly organized tables
"""

""" Function that will split up a string
and place each part into an appropiate list """
def dataSorter(rawData):
    
    # list where sorted items will go
    sortedList = []


    #Sorts sections of the raw data into separate values in the sortedList
    sortedList.append(rawData[:5])
    sortedList.append(rawData[5:])
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

    dataSorter(testTable)

main()
