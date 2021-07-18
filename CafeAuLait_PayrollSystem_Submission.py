# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Program Name: CafeAuLait_PayrollSystem_Submission.py
# Author:       Uzziah Smith
# Purpose:      Allows employees to clock in and out, calculates and pays employees and holds company information.
# Version:      3.0   (increment the decimal every editing session. Increment integer every major feature milestone)
# Last Revison: 20210630_1901 date format
# Dependencies: (1)os - note any libraries, APIs etc used by the code in this file
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import os.path
import csv
import time
from random import randint

# ======================================================================================================================
#                                                 TO-BE COMPLETED FUNCTIONS                                            #
# ======================================================================================================================

# ======================================================================================================================
#                                                          ARRAYS                                                      #
# ======================================================================================================================

# (1) employeeLogin
# (2) superannuation
# (3) taxRates
# (4) healthInsurance
# (5) rolePayment
# (6) employeeFile

# ======================================================================================================================
#                                                  ALGORITHMIC FUNCTIONS                                               #
# ======================================================================================================================

def ArrayLengthCalculator(array):
    length = 0
    for entities in array:
        length = length + 1
    return length
    # end for
# end def

def isInt(number):
    if number - int(number) == 0:
        return True
    else:
        return False
    # end if
# end def

def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')
# end def

def file_exists(filename):
    result = os.path.isfile(filename)
    return result
# end def

def writeList2CSVFile(listObject, fileObject):
    # This function writes an array/list of items/values to a single line in a text file object
    # Note that this function's arguments are objects, not strings/names
    # Assumes fileObject has been opened for writing
    itemCount = 0
    listLength = len(listObject)  # The length of a list/array is the number of items/elements in the list/array
    for item in listObject:
        itemCount = itemCount + 1  # iterate over each item in the list/array data structure
        fileObject.write(str(item))  # write the string version of the item to the file
        if itemCount != listLength:
            fileObject.write(',')  # write a comma to separate the values unless it is the last item
        else:
            fileObject.write('\n')  # write a newline character sequence (CR/LF) to end the line after the last item
        # end if
    # end for
# end def

def readCSVline2List(fileLineString):
    listObject = fileLineString.split(",")
    return listObject
# end def


def readCSVline2List(fileLineString):
    # This function takes a string argument representing a line from a csv formatted file and returns the populated
    # the named listobject (array/list) of items/values
    # uses Python's .split method to divide the fileLineString into separate values/items at each "," delimitation
    # list = fileLineString.strip()
    listObject = fileLineString.split(",")
    return listObject
# end def

def convertListToArray(list):
    pos = 0
    arrayLength = 0
    outputArray = [None]
    for item in list:
        arrayLength = arrayLength + 1
    # end for
    outputArray = [None]*arrayLength
    for item in list:
        outputArray[pos] = str(list[pos])
        pos = pos + 1
    # end for
    return outputArray
# end def

def readCSV2Array(filename):
    myRecord_list = []
    inputFileObject = open(filename, "r")                   # open the file for reading lines from
    #myHeader_list = readCSVline2List(currentLine)          # place first line of file into list object, myHeaderList
    #print(myHeader_list)                                    # display the header line of the csv file on the console
    for currentLine in inputFileObject:                     # iterate over each line in the input file
        currentLine = currentLine.strip()
        myRecord_list = myRecord_list + readCSVline2List(fileLineString=currentLine)  # put each line of the file into the array/list object
    # end for
    myRecord_Array = convertListToArray(myRecord_list)
    inputFileObject.close()
    return myRecord_Array
# end def

def convertListTo2DArray(list_of_lists):
    arrayPos = 0
    subItemPos = 0
    listPos = 0
    arrayLength = 0
    subArrayLength = 0
    outputArray = [None]
    for list in list_of_lists:
        arrayLength = arrayLength + 1
    # end for
    for list in list_of_lists:
        for item in list:
            subArrayLength = subArrayLength + 1
    # end for
    subArrayLength = int((subArrayLength + 1) / arrayLength)
    outputArray = [None] * arrayLength
    for list in list_of_lists:
        subArray = [None] * subArrayLength
        for item in list:
            subArray[subItemPos] = str(list[subItemPos])
            subItemPos = subItemPos + 1
        # end for
        outputArray[arrayPos] = subArray
        arrayPos = arrayPos + 1
        subItemPos = 0
    # end for
    return outputArray
# end def

def readCSVto2DArray(filename):
    lineCounter = 0
    counter = 0
    twoDimensionalList = [None]
    myRecord_list = []
    inputFileObject = open(filename, "r")  # open the file for reading lines from
    # myHeader_list = readCSVline2List(currentLine)          # place first line of file into list object, myHeaderList
    # print(myHeader_list)                                    # display the header line of the csv file on the console
    for line in inputFileObject:
        if line != "\n":
            lineCounter = lineCounter + 1
        # end if
    # end for
    inputFileObject.close
    inputFileObject = open(filename, "r")
    twoDimensionalList = [None]*lineCounter
    for currentLine in inputFileObject:  # iterate over each line in the input file
        currentLine = currentLine.strip()
        myRecord_list = readCSVline2List(fileLineString=currentLine)  # put each line of the file into the array/list object
        twoDimensionalList[counter] = myRecord_list
        counter = counter + 1
    # end for
    myRecord_Array = convertListTo2DArray(twoDimensionalList)
    inputFileObject.close()
    return myRecord_Array
# end def

def FindCurrentEmployee(EmployeeID, array, file):
    array = readCSVto2DArray(file)
    arrayCounter = 0
    for employees in array:
        if employees[0] != str(EmployeeID):
            arrayCounter = arrayCounter + 1
        else:
            return True
        # end if
    return False
    # end for
# end def

def TimeCalculator(ClockInTime, ClockOutTime):
    outputTime = float(ClockOutTime) - float(ClockInTime)
    if outputTime < 0:
        return False
    else:
        outputTime = outputTime / 100
        return outputTime
# end def

def TimeChecker(time):
    if int(time) == False:
        return False
    elif int(time) > 2400:
        return False
    elif int(time) < 0:
        return False
    elif int(str(time[2] + time[3])) > 60:
        return False
    else:
        return True
    # end if
# end def

def ValidateRole(EmployeeRole, RolePayArray):
    for role in RolePayArray:
        if EmployeeRole.lower() == str(role[0][0]).lower():
            return str(role)
        else:
            return False
        # end if
    # end for
# end def

def GenerateEmployeeID(EmployeeLoginArray):
    newEmployeeID = int(ArrayLengthCalculator(array=EmployeeLoginArray)) + 1
    return newEmployeeID
# end def

def GenerateEmployeePass(EmployeeLoginArray, Role):
    arrayLength = ArrayLengthCalculator(array=EmployeeLoginArray)
    validatePass = False
    validationCounter = 0
    employeePass = ''
    endingNum = 0
    while validatePass == False:
        endingNum = randint(100, 999)
        employeePass = Role + "Pass" + str(endingNum)
        for password in EmployeeLoginArray:
            if password[3] != employeePass:
                validationCounter = validationCounter + 1
            # end if
        # end for
        if validationCounter == arrayLength:
            return employeePass
        validationCounter = 0
        #end if
    # end while
# end def

def CalculateTotalHours(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours, SundayHours):
    hoursWorked = MondayHours + TuesdayHours + WednesdayHours + ThursdayHours + FridayHours + SaturdayHours + SundayHours
    return hoursWorked
# end def

def OvertimeCalculator(DayHours):
    overTime = 0
    if DayHours > 8:
        overTime = int(DayHours) + 1
    # end def
    return overTime
# end def

def CalculateBasePay(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours, SundayHours,
                     HourlyRate):
    basePay = CalculateTotalHours(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours,
                                  SundayHours) * HourlyRate
    return basePay

def WeekOvertimeCalculator(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours,
                           SundayHours):
    MondayOvertime = OvertimeCalculator(DayHours=MondayHours)
    TuesdayOvertime = OvertimeCalculator(DayHours=TuesdayHours)
    WednesdayOvertime = OvertimeCalculator(DayHours=WednesdayHours)
    ThurdayOvertime = OvertimeCalculator(DayHours=ThursdayHours)
    FridayOvertime = OvertimeCalculator(DayHours=FridayHours)
    SaturdayOvertime = OvertimeCalculator(DayHours=SaturdayHours)
    SundayOvertime = OvertimeCalculator(DayHours=SundayHours)
    TotalOvertime = MondayOvertime + TuesdayOvertime + WednesdayOvertime + ThurdayOvertime + FridayOvertime + \
                    SaturdayOvertime + SundayOvertime
    return TotalOvertime

def CalculateTax(GrossPay, HourlyRate, TaxRatesArray):
    taxRate = 0
    totalTax = 0
    taxArray = sorted(TaxRatesArray)
    if HourlyRate < 30:
        taxRate = int(TaxRatesArray[0])/100
    elif HourlyRate < 60:
        taxRate = int(TaxRatesArray[1])/100
    else:
        if ArrayLengthCalculator(TaxRatesArray) > 2:
            taxRate = int(TaxRatesArray[2])/100
        else:
            taxRate = int(TaxRatesArray[1])/100
        # end if
    # end if
    totalTax = GrossPay*taxRate
    totalTax = round(totalTax, 2)
    return totalTax
# end def

def CalculateNetPay(GrossPay, Tax, SuperRate, HealthInsurnace):
    SuperDeduction = GrossPay*(SuperRate/100)
    netPay = GrossPay - Tax - SuperDeduction - HealthInsurnace
    return netPay
# end def

def CalculateOvertimePay(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours,
                         SundayHours, HourlyRate):
    MondayOvertime = OvertimeCalculator(DayHours=MondayHours)
    TuesdayOvertime = OvertimeCalculator(DayHours=TuesdayHours)
    WednesdayOvertime = OvertimeCalculator(DayHours=WednesdayHours)
    ThursdayOvertime = OvertimeCalculator(DayHours=ThursdayHours)
    FridayOvertime = OvertimeCalculator(DayHours=FridayHours)
    SaturdayOvertime = OvertimeCalculator(DayHours=SaturdayHours)
    SundayOvertime = OvertimeCalculator(DayHours=SundayHours)
    MondayOvertimePay = 0
    TuesdayOvertimePay = 0
    WednesdayOvertimePay = 0
    ThursdayOvertimePay = 0
    FridayOvertimePay = 0
    SaturdayOvertimePay = 0
    SundayOvertimePay = 0
    totalOvertimePay = 0
    if TuesdayOvertime > 0 and TuesdayOvertime <= 3:
        TuesdayOvertimePay = TuesdayOvertime*(HourlyRate*1.25)
    elif TuesdayOvertime > 3:
        TuesdayOvertimePay = TuesdayOvertime*(HourlyRate*1.45)
    # end if
    if WednesdayOvertime > 0 and WednesdayOvertime <= 3:
        WednesdayOvertimePay = WednesdayOvertime*(HourlyRate*1.25)
    elif WednesdayOvertime > 3:
        WednesdayOvertimePay = WednesdayOvertime*(HourlyRate*1.45)
    # end if
    if ThursdayOvertime > 0 and ThursdayOvertime <= 3:
        ThursdayOvertimePay = ThursdayOvertime*(HourlyRate*1.25)
    elif ThursdayOvertime > 3:
        ThursdayOvertimePay = ThursdayOvertime*(HourlyRate*1.45)
    # end if
    if FridayOvertime > 0 and FridayOvertime <= 3:
        FridayOvertimePay = FridayOvertime*(HourlyRate*1.25)
    elif FridayOvertime > 3:
        FridayOvertimePay = FridayOvertime*(HourlyRate*1.45)
    if MondayOvertime > 0:
        MondayOvertimePay = MondayOvertime*(HourlyRate*1.5)
    # end if
    if SaturdayOvertime > 0:
        SaturdayOvertimePay = SaturdayOvertime*(HourlyRate*1.5)
    # end if
    if SundayOvertime > 0:
        SundayOvertimePay = SundayOvertime*(HourlyRate*1.5)
    # end if
    totalOvertimePay = MondayOvertimePay + TuesdayOvertimePay + WednesdayOvertimePay + ThursdayOvertimePay +\
                       FridayOvertimePay + SaturdayOvertimePay + SundayOvertimePay
    return totalOvertimePay
# end def

def CalculatePublicHolidayPay(PublicHolidayHours, hourlyPay):
    publicHolidayOvertime = OvertimeCalculator(DayHours=PublicHolidayHours)
    publicHolidayOvertimePay = 0
    publicHolidayPay = 0
    if publicHolidayOvertime > 0:
        publicHolidayOvertimePay = publicHolidayOvertime*(hourlyPay*1.5)
    # end if
    if PublicHolidayHours > 8:
        publicHolidayPay = 8*(hourlyPay + 4) + publicHolidayOvertimePay
    else:
        publicHolidayPay = PublicHolidayHours*(hourlyPay + 4)
    # end if
    return publicHolidayPay
# end def

def CalculateTotalPay(BasePay, OvertimePay, PublicHolidayHours, SaturdayHours, SundayHours):
    totalPay = 0
    publicHolidayBenefits = 0
    saturdayBenefits = 0
    sundayBenefits = 0
    if PublicHolidayHours > 8:
        publicHolidayBenefits = 8*4 #max amount of hours that can be worked without overtime multiplied by public holiday bonus
    else:
        publicHolidayBenefits = PublicHolidayHours*4
    #end if
    if SaturdayHours > 8:
        saturdayBenefits = 8*4 #max amount of hours that can be worked without overtime multiplied by public holiday bonus
    else:
        saturdayBenefits = SaturdayHours*3
    #end if
    if SundayHours > 8:
        sundayBenefits = 8*4 #max amount of hours that can be worked without overtime multiplied by public holiday bonus
    else:
        sundayBenefits = SundayHours*4
    #end if
    totalPay = BasePay + OvertimePay + publicHolidayBenefits + saturdayBenefits + sundayBenefits
    return totalPay
# end def

def TwoDimensionalArrayToFile(array, file):
    outputString = ''
    arrayLastPos = ArrayLengthCalculator(array=array[0])-1
    pos = 0
    f = open(file, 'w+')
    f.write("")
    f.close()
    f = open(file, 'a+')
    for item in array:
        for entity in item:
            if pos == arrayLastPos:
                outputString = outputString + str(entity)
            else:
                outputString = outputString + str(entity) + ','
            pos = pos + 1
            # end if
        # end for
        f.write(outputString)
        f.write("\n")
        outputString = ''
    # end for
    f.close()
# end def

def ArrayToFile(array, file):
    f = open(file, 'w+')
    for item in array:
        f.write(str(item))
        f.write("\n")
    # end for
    f.close()

def ArrayValidationAndDeletion(SpecificValueToBeDeleted, Array, File, TwoDimensionalArray):
    pos = 0
    for item in Array:
        if item == SpecificValueToBeDeleted:
            Array.delete(pos)
            if TwoDimensionalArray == False:
                ArrayToFile(array=Array, file=File)
            else:
                TwoDimensionalArrayToFile(array=Array, file=File)
            # end if
            return True
        # end if
        pos = pos + 1
    # end for
    return False
# end def

def ArrayValidationAndAddition(SpecificValueToBeAdded, Array, File):
    pos = 0
    arrayLength = ArrayLengthCalculator(array=Array)
    outputArray = [None]*(arrayLength + 1)
    if SpecificValueToBeAdded.isnumeric() == False:
        return False
    else:
        for item in Array:
            outputArray[pos] = item
            pos = pos + 1
        # end for
        outputArray[pos] = SpecificValueToBeAdded
        ArrayToFile(array=Array, file=File)
        return True
    # end if
# end def

def FindPaymentForRole(Role, RolePayArray):
    payRate = 0
    for item in RolePayArray:
        if str(Role) == item[0]:
            payRate = item[1]
        # end if
    # end for
    if payRate == 0:
        return False
    else:
        return payRate
    # end if
# end def

# ======================================================================================================================
#                                                 DEBUGGING FUNCTIONS                                                  #
# ======================================================================================================================

def isSameString(stringA, stringB):
    pos = 0
    for character in stringA:
        if character.lower() != stringB[pos].lower():
            return False
        pos = pos + 1
        # end if
    # end for
    return True
# end def

# ======================================================================================================================
#                                                   DISPLAY FUNCTIONS                                                  #
# ======================================================================================================================

def Header(SystemHeader, HeaderMessage):
    print("--------------------------------------------------------------------------------")
    print("| Cafe au Lait – Payment System: " + SystemHeader)
    print("--------------------------------------------------------------------------------")
    print("| " + HeaderMessage)
    print("--------------------------------------------------------------------------------")
# end module

def Footer():
    SelectedNavigation = ''
    Breakout = False
    print("----------------------------------------------------------------------------------------")
    print("| [R]eturn")
    print("| [C]onfirm")
    print("----------------------------------------------------------------------------------------")
    while Breakout == False:
        SelectedNavigation = input("::")
        if SelectedNavigation.lower() == 'r':
            return False
        elif SelectedNavigation.lower() == 'c':
            return True
        elif SelectedNavigation.lower() != 'c' and SelectedNavigation.lower() != 'r':
            print("Please select a valid option")
        # end if
    # end while
# end module

def Display_Navigation():
    optionSelected = ''
    Header(SystemHeader="Navigation", HeaderMessage="")
    print("|Please select the required mode to be used:")
    print("|")
    print("|[T]est mode/[I]nteractive mode (default)")
    optionSelected = input("::")
    return optionSelected.lower()
    # end if
# end def

def Display_InteractiveLogin(array, file):
    array = readCSVto2DArray(file)
    EmployeeID = ''
    Password = ''
    Header(SystemHeader="Interactive: Log-in", HeaderMessage="Interactive mode selected")
    print("|")
    EmployeeID = input("| Café-Au-Lait-ID:")
    print("|")
    Password = input("| Password:")
    print("|")
    if Footer() == True:
        EmployeeID = str(EmployeeID)
        Password = str(Password)
        for employees in array:
            if employees[0] == EmployeeID and employees[3] == Password:
                return EmployeeID
            # end if
        # end for
        return False
    # end if
# end def

def Display_InteractiveClockIn(EmployeeID, EmployeeDetailsArray, LoginArray, EmployeeDetailsFile, LoginFile):
    EmployeeDetailsArray = readCSVto2DArray(EmployeeDetailsFile)
    LoginArray = readCSVto2DArray(LoginFile)
    EmployeeArray = EmployeeDetailsArray[int(EmployeeID)-1]
    timeStamp = 0000
    timeStampValidation = False
    daySelection = ""
    daySelectionValidation = False
    clockSelection = ""
    clockSelectionValidation = False
    hoursWorked = 0
    employeeFirstName = str(LoginArray[int(EmployeeID)-1][1])
    employeeLastName = str(LoginArray[int(EmployeeID)-1][2])
    EmployeeWelcome = "Welcome Employee: " + employeeFirstName + " " + employeeLastName
    Header(SystemHeader="Interactive: Employee", HeaderMessage=EmployeeWelcome)
    print("| ")
    clockSelection = input("| Clock - [I]n / [O]ut(default)")
    if clockSelection.lower() != 'i':
        clockSelectionValidation = 'o'
    else:
        EmployeeArray[7] = '0000'
        EmployeeArray[5] = 'MONDAY'
        EmployeeArray[4] = False
    # end if
    print("| ")
    print("| ")
    print("| // input the day using the designated 3 letter shortened word")
    print("| ")
    print("| [MON]day, [TUE]day, [WED]day, [THU]day, [FRI]day, [SAT]day, [SUN]day")
    while daySelectionValidation == False:
        daySelection = input("| Day:")
        if daySelection.lower() != 'mon' and daySelection.lower() != 'tue' and daySelection.lower() != 'wed' and \
                daySelection.lower() != 'thu' and daySelection.lower() != 'fri' and\
                daySelection.lower() != 'sat' and daySelection.lower() != 'sun':
            print(" ")
            print("ERROR: Please enter a valid day")
        else:
            if clockSelection.lower() == 'o':
                dayString = str((EmployeeArray[5][0] + EmployeeArray[5][1] + EmployeeArray[5][2])).lower()
                if daySelection.lower() == dayString:
                    daySelectionValidation = True
                else:
                    print("ERROR: MUST CLOCK OUT ON SAME DAY")
                # end if
            else:
                daySelectionValidation = True
            # end if
        # end if
    # end while
    print("| ")
    print("| ")
    print("| // input time using the time code hhmm e.g. 11:00am is 1100")
    print("| ")
    while timeStampValidation == False:
        timeStamp = input("| Time:")
        TimeChecker(time=timeStamp)
        if TimeChecker(time=timeStamp) == True:
            if clockSelection.lower() == 'o':
                if TimeCalculator(ClockInTime=EmployeeArray[6], ClockOutTime=timeStamp) != False:
                    timeStampValidation = True
                else:
                    print("ERROR: Please enter a valid time")
                    # end if
            else:
                timeStampValidation = True
            # end if
        else:
            print("")
            print("ERROR: Please enter valid time")
        # end if
    # end while
    if Footer() == True:
        if clockSelection.lower() == 'i':
            EmployeeArray[4] = True
            EmployeeArray[6] = timeStamp
            if daySelection.lower() == 'mon':
                EmployeeArray[5] = 'MONDAY'
                EmployeeArray[8] = '0'
            elif daySelection.lower() == 'tue':
                EmployeeArray[5] = 'TUESDAY'
                EmployeeArray[9] = '0'
            elif daySelection.lower() == 'wed':
                EmployeeArray[5] = 'WEDNESDAY'
                EmployeeArray[10] = '0'
            elif daySelection.lower() == 'thu':
                EmployeeArray[5] = 'THURSDAY'
                EmployeeArray[11] = '0'
            elif daySelection.lower() == 'fri':
                EmployeeArray[5] = 'FRIDAY'
                EmployeeArray[12] = '0'
            elif daySelection.lower() == 'sat':
                EmployeeArray[5] = 'SATURDAY'
                EmployeeArray[13] = '0'
            elif daySelection.lower() == 'sun':
                EmployeeArray[5] = 'SUNDAY'
                EmployeeArray[14] = '0'
            # end if
        else:
            EmployeeArray[4] = False
            EmployeeArray[7] = timeStamp
            hoursWorked = TimeCalculator(ClockInTime=EmployeeArray[2], ClockOutTime=EmployeeArray[3])
            if daySelection.lower() == 'mon':
                EmployeeArray[8] = hoursWorked
            elif daySelection.lower() == 'tue':
                EmployeeArray[9] = hoursWorked
            elif daySelection.lower() == 'wed':
                EmployeeArray[10] = hoursWorked
            elif daySelection.lower() == 'thu':
                EmployeeArray[11] = hoursWorked
            elif daySelection.lower() == 'fri':
                EmployeeArray[12] = hoursWorked
            elif daySelection.lower() == 'sat':
                EmployeeArray[13] = hoursWorked
            elif daySelection.lower() == 'sun':
                EmployeeArray[14] = hoursWorked
            # end if
        # end if
        print(EmployeeArray)
        EmployeeDetailsArray[int(EmployeeID)-1] = EmployeeArray
        print(EmployeeDetailsArray)
        TwoDimensionalArrayToFile(array=EmployeeDetailsArray, file=EmployeeDetailsFile)
        return True
    # end if
    return False
# end def

def Display_Clockin(EmployeeID, LoginArray, LoginFile, EmployeeDetailsArray, EmployeeDetailsFile):
    LoginArray = readCSVto2DArray(LoginFile)
    EmployeeDetailsArray = readCSVto2DArray(EmployeeDetailsFile)
    CurrentEmployeeArray = EmployeeDetailsArray[int(employeeID)-1]
    employeeFirstName = LoginArray[int(EmployeeID)][1]
    employeeLastName = LoginArray[int(EmployeeID)][2]
    status = None
    if CurrentEmployeeArray[4] == True:
        status = 'Shift in progress'
    else:
        status = 'Not on shift'
    # end if
    Header(SystemHeader="Interactive: Employee",
           HeaderMessage="Have a good day employee: " + employeeFirstName + " " + employeeLastName)
    print("| ")
    print("| Status: " + status)
    print("| ")
    print("| Day: " + CurrentEmployeeArray[5])
    print("| ")
    if CurrentEmployeeArray[4] == True:
        print("| Time:  " + CurrentEmployeeArray[6])
        print("| ")
        print("| Hours: Shift in progress")
        print("| ")
        print("-----------------------------------------------------------")
    else:
        print("| Time:  " + CurrentEmployeeArray[7])
        print("| ")
        print("| Hours:  " + str(TimeCalculator(ClockInTime=CurrentEmployeeArray[6], ClockOutTime=CurrentEmployeeArray[7])))
        print("| ")
        print("-----------------------------------------------------------")
    # end if
# end def

def Display_ClerkOptions(EmployeeID, EmployeeLoginArray, LoginFile, EmployeeDetailsArray, EmployeeDetailsFile):
    EmployeeLoginArray = readCSVto2DArray(LoginFile)
    EmployeeDetailsArray = readCSVto2DArray(EmployeeDetailsFile)
    specificEmployee = int(EmployeeID) - 1
    employeeFirstName = EmployeeLoginArray[specificEmployee][1]
    employeeLastName = EmployeeLoginArray[specificEmployee][2]
    ClerkSelection = ''
    Header(SystemHeader="Interactive: Clerk",
           HeaderMessage="Welcome Clerk: " + employeeFirstName + " " + employeeLastName)
    print("| ")
    print("| [P]ayment / [F]inancial / [E]mployee options(default)")
    ClerkSelection = input("| User input:")
    print("| ")
    if Footer() == True:
        if ClerkSelection.lower() == 'p':
            return 'Payment'
        elif ClerkSelection.lower() == 'f':
            return 'Financial'
        else:
            return 'Employee'
        # end if
    # end if
# end def

def Display_ClerkPaymentOptions(EmployeeLoginArray, LoginFile):
    EmployeeLoginArray = readCSVto2DArray(LoginFile)
    clerkPaymentEmployeeID = ''
    employeeFound = False
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Payment")
    print("| ")
    clerkPaymentEmployeeID = input("| Enter employee ID: ")
    print("| ")
    if Footer() == True:
        while employeeFound == False:
            if FindCurrentEmployee(EmployeeID=clerkPaymentEmployeeID, array=EmployeeLoginArray, file=LoginFile) == False:
                print("ERROR! Invalid employee")
                print("Please input a valid employee ID")
                clerkPaymentEmployeeID = input("| Enter employee ID: ")
                print("| ")
            else:
                employeeFound = True
                return clerkPaymentEmployeeID
            # end if
        # end while
    # end if
    return False
# end def

def Display_ClerkEmployeeOptions():
    clerkSelection = ''
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Employee Options")
    print("| ")
    clerkSelection = input("| [A]dd / [R]emove / [E]dit Employee(default): ")
    print("| ")
    if Footer() == True:
        if clerkSelection.lower() == 'a':
            return 'Add'
        elif clerkSelection.lower() == 'r':
            return 'Remove'
        else:
            return 'Edit'
        # end if
    # end if
    return False
# end def


def Display_AddEmployee(EmployeeLoginArray, EmployeeLoginFile, EmployeeDetailsArray, EmployeeDetailsFile):
    EmployeeLoginArray = readCSVto2DArray(EmployeeLoginFile)
    EmployeeDetailsArray = readCSVto2DArray(EmployeeDetailsFile)
    newEmployeeID = ''
    newEmployeePass = ''
    newEmployeeHourlyRate = 0
    employeeGivenName = ''
    employeeSurname = ''
    employeeRole = ''
    employeeSuperannuation = ''
    employeeHealthInsurance = ''
    employeeRoleValidation = False
    outputArray = [None]*2
    newEmployeeLoginArray = [None]*4
    newEmployeeDetailsArray = [None]*15
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Add Employee")
    print("| ")
    print("| Enter employee's details")
    print("| ")
    employeeGivenName = input("Given Name: ")
    print("| ")
    employeeSurname = input("Surname: ")
    print("| ")
    print("| Role: ")
    employeeRole = input("| [M]anager / [C]lerk / [B]arista (default) :: ")
    print("| ")
    print("| Superannuation: ")
    employeeSuperannuation = input("| [1]4 % / [2]6 % / [3]8 % (default) :: ")
    print("| ")
    print("| HealthInsurance:")
    employeeHealthInsurance = print("| [A]ncillery / [SU]perior / [ST]andard(default) :: ")
    print("| ")
    Footer()
    if Footer() == True:
        while employeeRoleValidation == False:
            employeeRole = ValidateRole(employeeRole)
            if employeeRole == False:
                print("ERROR INVALID ROLE")
                print("Please input valid role: ")
                employeeRole = input("| [M]anager / [C]lerk / [B]arista (default) :: ")
            else:
                employeeRoleValidation = True
            # end if
        # end while
        newEmployeeHourlyRate = FindPaymentForRole(employeeRole)
        newEmployeeID = GenerateEmployeeID()
        newEmployeePass = GenerateEmployeePass(EmployeeLoginArray=EmployeeLoginArray, Role=employeeRole)
        newEmployeeDetailsArray[0] = newEmployeeID
        newEmployeeDetailsArray[1] = employeeRole
        newEmployeeDetailsArray[2] = employeeSuperannuation
        newEmployeeDetailsArray[3] = employeeHealthInsurance
        newEmployeeDetailsArray[4] = False
        newEmployeeDetailsArray[5] = 'MONDAY'
        newEmployeeDetailsArray[6] = '0000'
        newEmployeeDetailsArray[7] = '0000'
        newEmployeeDetailsArray[8] = '0'
        newEmployeeDetailsArray[9] = '0'
        newEmployeeDetailsArray[10] = '0'
        newEmployeeDetailsArray[11] = '0'
        newEmployeeDetailsArray[12] = '0'
        newEmployeeDetailsArray[13] = '0'
        newEmployeeDetailsArray[14] = '0'
        newEmployeeLoginArray[0] = newEmployeeID
        newEmployeeLoginArray[1] = employeeGivenName
        newEmployeeLoginArray[2] = employeeSurname
        newEmployeeLoginArray[3] = employeeRole
        EmployeeLoginArray.append(newEmployeeLoginArray)
        EmployeeDetailsArray.append(newEmployeeDetailsArray)
        TwoDimensionalArrayToFile(array=EmployeeLoginArray, file=EmployeeLoginFile)
        TwoDimensionalArrayToFile(array=EmployeeDetailsArray, file=EmployeeDetailsFile)
        print("-----------------------------------------------------------")
        print("| ")
        print("| Generated Employee ID: " + newEmployeeID)
        print("| ")
        print("| Generated Employee Password: " + newEmployeePass)
        print("| ")
        print("-----------------------------------------------------------")
        return outputArray
    # end if 
# end def

def Display_RemoveEmployee(EmployeeDetailsArray, EmployeeLoginArray, EmployeeLoginFile, EmployeeDetailsFile):
    EmployeeLoginArray = readCSVto2DArray(EmployeeLoginFile)
    EmployeeDetailsArray = readCSVto2DArray(EmployeeDetailsFile)
    employeeIDtoRemove = ''
    clerkID = ''
    clerkPassword = ''
    employeePos = 0
    employeeFoundValidation = False
    clerkLoginValidation = False
    if file_exists(EmployeeLoginFile) == False:
        print("ERROR: EmployeeLoginFile Invalid")
        return False
    # end if
    if file_exists(EmployeeDetailsFile) == False:
        print("ERROR: EmployeeDetailsFile Invalid")
        return False
    # end if
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Remove Employee")
    print("| ")
    print("| Enter employee's details")
    print("| ")
    employeeIDtoRemove = input("| Employee - ID:")
    print("| ")
    clerkID = input("| Clerk - ID:")
    print("| ")
    clerkPassword = input("| Clerk - Password:")
    print("| ")
    if Footer() == True:
        while employeeFoundValidation == False:
            if FindCurrentEmployee(EmployeeID=employeeIDtoRemove, array=EmployeeLoginArray, file=EmployeeLoginFile) == 'False':
                print("ERROR EMPLOYEE NOT FOUND!")
                print(" ")
                employeeIDtoRemove = input("| Enter Valid Employee: ")
            else:
                employeeFoundValidation = True
            # end if
        # end while
        while clerkLoginValidation == False:
            clerkID = str(clerkID)
            clerkPassword = str(clerkPassword)
            for employee in EmployeeLoginArray:
                if employee[0] == clerkID and employee[3] == clerkPassword:
                    clerkLoginValidation = True
                # end if
            # end for
            if clerkLoginValidation == False:
                print("ERROR CLERK NOT FOUND!")
                clerkID = input("| Enter Valid Clerk - ID: ")
                print("|")
                clerkPassword = input("| Enter Valid Clerk - Password: ")
            # end if
        EmployeeLoginArray.delete(int(employeeID)-1)
        EmployeeDetailsArray.delete(int(employeeID)-1)
        employeePos = int(employeeID)-1
        for employee in EmployeeLoginArray:
            employee[employeePos][0] = str(int(employeeID) - 1)
            employeePos = employeePos + 1
        # end for
        employeePos = int(employeeID) - 1
        for employee in EmployeeDetailsArray:
            employee[employeePos][0] = str(int(employeeID) - 1)
            employeePos = employeePos + 1
        # end for
        TwoDimensionalArrayToFile(array=EmployeeLoginArray, file=EmployeeLoginFile)
        TwoDimensionalArrayToFile(array=EmployeeDetailsArray, file=EmployeeDetailsFile)
        return True
        # end while
    # end if
    return False
# end def

def Display_EditEmployee(EmployeeLoginArray, EmployeeDetailsArray, EmployeeLoginFile, EmployeeDetailsFile):
    EmployeeLoginArray = readCSVto2DArray(EmployeeLoginFile)
    EmployeeDetailsArray = readCSVto2DArray(EmployeeDetailsFile)
    EmployeeArray = []
    employeeID = ''
    employeePassword = ''
    employeeSuperannuation = ''
    employeeHealthInsurance = ''
    employeeFoundValidation = False
    roleValidation = False
    superValidation = False
    healthInsuranceValidation = False
    if file_exists(EmployeeLoginFile) == False:
        print("ERROR: EmployeeLoginFile Invalid")
        return False
    # end if
    if file_exists(EmployeeDetailsFile) == False:
        print("ERROR: EmployeeDetailsFile Invalid")
        return False
    # end if
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Edit Employee")
    print("| ")
    employeeID = input("| Café - Au - Lait - ID: ")
    print("| ")
    employeePassword = input("| Password: ")
    print("| ")
    print("| Role")
    employeeRole = input("| [B]arista / [M]anager / [C]lerk: ")
    print("| ")
    print("| Superannuation")
    employeeSuperannuation = input("| [1]4% / [2]6% / [3]8%: ")
    print("| ")
    print("| Health Insurance")
    employeeHealthInsurance = input("| [A]ncillery / [SU]perior / [ST]andard(default): ")
    print("| ")
    if Footer() == True:
        while employeeFoundValidation == False:
            if FindCurrentEmployee(EmployeeID=employeeID, array=EmployeeLoginArray, file=EmployeeLoginFile) == False:
                print("ERROR: PLEASE DO NOT EDIT EMPLOYEE ID")
                employeeID = input("| Café - Au - Lait - ID: ")
            else:
                employeeFoundValidation = True
            # end if
        # end while
        while roleValidation == False:
            if employeeRole.lower() != 'b' and employeeRole.lower() != 'm' and employeeRole.lower() != 'c':
                print("ERROR: PLEASE INPUT A VALID ROLE")
                print("| Role")
                employeeRole = input("| [B]arista / [M]anager / [C]lerk: ")
            else:
                if str(employeeRole).lower() == 'b':
                    employeeRole = 'Barista'
                elif str(employeeRole).lower() == 'm':
                    employeeRole = 'Manager'
                else:
                    employeeRole = 'Clerk'
                # end if
                roleValidation = True
            # end if
        # end while
        while superValidation == False:
            if str(employeeSuperannuation) != '1' and str(employeeSuperannuation) != '2' and \
                    str(employeeSuperannuation) != '3':
                print("ERROR: PLEASE INPUT A VALID SUPERANNUATION PLAN")
                print("| Superannuation")
                employeeSuperannuation = input("| [1]4% / [2]6% / [3]8%: ")
            else:
                if str(employeeSuperannuation) == '1':
                    employeeSuperannuation = 4
                elif str(employeeSuperannuation) == '2':
                    employeeSuperannuation = 6
                elif str(employeeSuperannuation) == '3':
                    employeeSuperannuation = 8
                # end if
                superValidation = True
            # end if
        # end while
        while employeeHealthInsurance == False:
            if employeeHealthInsurance.lower() != 'a' and employeeHealthInsurance.lower() != 'st' and \
                    employeeHealthInsurance != 'su':
                print("ERROR: PLEASE INPUT A VALID HEALTH INSURANCE PLAN")
                print("| Health Insurance")
                employeeHealthInsurance = input("| [A]ncillery / [SU]perior / [ST]andard(default): ")
            else:
                if str(employeeHealthInsurance).lower() == 'a':
                    employeeHealthInsurance = 15
                elif str(employeeHealthInsurance).lower() == 'st':
                    employeeHealthInsurance = 25
                else:
                    employeeHealthInsurance = 45
                # end if
                employeeHealthInsurance = True
            # end if
        # end while
        EmployeeLoginArray[int(employeeID)-1][1] = employeePassword
        EmployeeDetailsArray[int(employeeID)-1][1] = employeeRole
        EmployeeDetailsArray[int(employeeID)-1][2] = employeeSuperannuation
        EmployeeDetailsArray[int(employeeID)-1][3] = employeeHealthInsurance
        TwoDimensionalArrayToFile(array=EmployeeLoginArray, file=EmployeeLoginFile)
        TwoDimensionalArrayToFile(array=EmployeeDetailsArray, file=EmployeeDetailsFile)
    # end if
    return True
# end def

def Display_FinancialOptions():
    clerkFinancialOption = ''
    returnStatement = ''
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Financial Options")
    print("| ")
    print("| Select from the following options: ")
    clerkFinancialOption = input("| [T]ax rate / [S]uperannuation / [H]ealth insurance / | [P]ay rates(default): ")
    print("| ")
    if Footer() == True:
        if clerkFinancialOption.lower() == 't':
            returnStatement = 'TaxRates'
        elif clerkFinancialOption.lower() == 's':
            returnStatement = 'Superannuation'
        elif clerkFinancialOption.lower() == 'h':
            returnStatement = 'HealthInsurance'
        else:
            returnStatement = 'PayRates'
        # end if
        return returnStatement
    # end if
    return False
# end while

def Display_Financial_TaxRates(TaxRateArray, TaxRatesFile):
    TaxRateArray = readCSV2Array(TaxRatesFile)
    taxRateToBeAdded = 0
    taxRateToBeDeleted = 0
    deletionValidation = False
    additionValidation = False
    loopCounter = 1
    taxRatePrintStringBegin = " | Tax rates: "
    taxRatePrintStringEnd = ''
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Tax Adjustment")
    for item in TaxRateArray:
        taxRatePrintStringEnd = taxRatePrintStringEnd + "[" + str(loopCounter) + "]" + TaxRateArray[loopCounter-1] + \
                                " % " + ", "
        loopCounter = loopCounter + 1
    # end for
    print("| ")
    print(taxRatePrintStringBegin + taxRatePrintStringEnd)
    print("| ")
    taxRateToBeDeleted = input("| Delete tax rate: // using options 1, 2, 3 etc.")
    print("| ")
    taxRateToBeAdded = input("| Add tax rate: // using number without percentage tag")
    print("| ")
    if Footer() == True:
        while deletionValidation == False:
            if deletionValidation.isnumeric() == False:
                if deletionValidation.lower() == 'next':
                    deletionValidation = True
                else:
                    print("ERROR INVALID TAX RATE: NOT ON Array")
                    taxRateToBeDeleted = input("Please input a valid tax rate to be deleted:")
            elif ArrayValidationAndDeletion(SpecificValueToBeDeleted=taxRateToBeDeleted, Array=TaxRateArray,
                                          File=TaxRatesFile) == False:
                print("ERROR INVALID TAX RATE: NOT ON Array")
                taxRateToBeDeleted = input("Please input a valid tax rate to be deleted:")
            else:
                deletionValidation = True
            # end if
        # end while
        while additionValidation == False:
            if taxRateToBeAdded.isnumeric() == False:
                if taxRateToBeAdded.lower() == 'next':
                    additionValidation = True
                else:
                    print("ERROR INVALID TAX RATE: INVALID INTEGER ENTRY")
                    taxRateToBeAdded = input("Please input a valid tax rate, using an integer without a "
                                             "percentage sign: ")
            elif ArrayValidationAndAddition(SpecificValueToBeAdded=taxRateToBeAdded, Array=TaxRateArray,
                                                            File=TaxRatesFile) == False:
                print("ERROR INVALID TAX RATE: INVALID INTEGER ENTRY")
                taxRateToBeAdded = input("Please input a valid tax rate, using an integer without a percentage sign: ")
            else:
                additionValidation = True
            # end if
        # end while
        return True
    # end if
    return False
# end def

def Display_Financial_Superannuation(SuperArray, SuperFile):
    SuperArray = readCSV2Array(SuperFile)
    loopCounter = 0
    superprintStringBegin = " | Superannuation: "
    superprintStringEnd = ""
    superToBeDeleted = ''
    superToBeAdded = ''
    deletionValidation = False
    additionValidation = False
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Superannuation Adjustment")
    for item in SuperArray:
        superprintStringEnd = superprintStringEnd + "[" + str(loopCounter) + "]" + "$" + SuperArray[loopCounter-1] + \
                              ", "
        loopCounter = loopCounter + 1
    # end for
    print("|")
    print(superprintStringBegin + superprintStringEnd)
    print("| ")
    print("| Delete Superannuation Rate: // using options 1, 2, 3 etc. or 'next' to skip")
    superToBeDeleted = input(":: ")
    print("|")
    print("| Add Superannuation: // using number without percentage tag or use 'next' to skip")
    superToBeAdded = input(":: ")
    print("|")
    if Footer() == True:
        while deletionValidation == False:
            if superToBeDeleted.isnumeric() == False:
                if superToBeDeleted.lower() == 'next':
                    deletionValidation = True
                else:
                    print("ERROR INVALID SUPERANNUATION RATE: NOT ON Array")
                    superToBeDeleted = input("Please input a valid superannuation rate to be deleted: ")
            elif ArrayValidationAndDeletion(SpecificValueToBeDeleted=superToBeDeleted,
                                            Array=SuperArray, File=SuperFile) == False:
                print("ERROR INVALID SUPERANNUATION RATE: NOT ON Array")
                superToBeDeleted = input("Please input a valid superannuation rate to be deleted:")
            else:
                deletionValidation = True
            # end if
        # end while
        while additionValidation == False:
            if superToBeAdded.isnumeric() == False:
                if superToBeAdded.loewr() == 'next':
                    additionValidation = True
                else:
                    print("ERROR INVALID SUPERANNUATION RATE: INVALID INTEGER ENTRY")
                    superToBeAdded = input("Please input a superannuation rate, using an integer without a"
                                           " percentage sign: ")
            elif ArrayValidationAndAddition(SpecificValueToBeAdded=superToBeAdded,
                                            Array=SuperArray, File=SuperFile) == False:
                print("ERROR INVALID SUPERANNUATION RATE: INVALID INTEGER ENTRY")
                superToBeAdded = input("Please input a superannuation rate, using an integer without a"
                                         " percentage sign: ")
            else:
                additionValidation = True
            # end if
        # end while
        return True
    # end if
    return False

def Display_Financial_HealthInsurance(HealthInsuranceArray, HealthFile):
    HealthInsuranceArray = readCSV2Array(HealthFile)
    healthInsuranceprintStringBegin = " | Health Insurance Deductions: "
    healthInsuranceprintStringEnd = ""
    healthInsuranceToBeDeleted = ''
    healthInsuranceToBeAdded = ''
    deletionValidation = False
    additionValidation = False
    loopCounter = 1
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Health Insurance Adjustment")
    for HealthPlans in HealthInsuranceArray:
        healthInsuranceprintStringEnd = healthInsuranceprintStringEnd + "[" + str(loopCounter) + "]" + "$" + \
                                        HealthInsuranceArray[loopCounter-1] + ", "
        loopCounter = loopCounter + 1
    # end for
    print("|")
    print(healthInsuranceprintStringBegin + healthInsuranceprintStringEnd)
    print("|")
    print("| Delete Health Insurance Plan: // using options 1, 2, etc. or 'next' to skip")
    healthInsuranceToBeDeleted = input(":: ")
    print("|")
    print("| Add Health Insurance Plan: // using the price or 'next' to skip")
    healthInsuranceToBeAdded = input(":: ")
    print("|")
    if Footer() == True:
        while deletionValidation == False:
            if healthInsuranceToBeDeleted.isnumeric() == False:
                if healthInsuranceToBeDeleted.lower() == 'next':
                    deletionValidation = True
                else:
                    print("ERROR INVALID HEALTH CARE PLAN: NOT ON Array")
                    healthInsuranceToBeDeleted = input("Please input a valid health care plan to be deleted: ")
            elif ArrayValidationAndDeletion(specificValueToBeDeleted=healthInsuranceToBeDeleted,
                                            Array=HealthInsuranceArray, File=HealthFile) == False:
                print("ERROR INVALID HEALTH CARE PLAN: NOT ON Array")
                healthInsuranceToBeDeleted = input("Please input a valid health care plan to be deleted: ")
            else:
                deletionValidation = True
            # end if
        # end while
        while additionValidation == False:
            if healthInsuranceToBeAdded.isnumeric() == False:
                if healthInsuranceToBeAdded.lower() == 'next':
                    additionValidation = True
                else:
                    print("ERROR: INVALID HEALTH CARE PLAN: INVALID INTEGER ENTRY")
                    healthInsuranceToBeAdded = input("Please input a valid health care plan, inputting the cost"
                                                     " (to skip type 'next'): ")
                # end if
            elif ArrayValidationAndAddition(specificValueToBeAdded=healthInsuranceToBeAdded,
                                            Array=HealthInsuranceArray, File=HealthFile) == False:
                print("ERROR: INVALID HEALTH CARE PLAN: INVALID INTEGER ENTRY")
                healthInsuranceToBeAdded = input("Please input a valid health care plan, inputting the cost"
                                                 " (to skip type 'next'): ")
            else:
                additionValidation = True
            # end if
        # end while
        return True
    return False
    # end if
# end def

def Display_Financial_PayRates(RolePaymentArray, RolePayFile):
    RolePaymentArray = readCSVto2DArray(RolePayFile)
    loopCounter = 1
    rolePaymentprintStringBegin = " | Roles: "
    rolePaymentprintStringEnd = ""
    roleToBeDeleted = ''
    roleToBeAdded = ''
    payRateToBeAdded = ''
    roleToBeAddedArray = [None]*2
    arrayValidation = False
    additionValidation = False
    deletionValidation = False
    Header(SystemHeader="Interactive: Clerk", HeaderMessage="Payrates Adjustment")
    for role in RolePaymentArray:
        rolePaymentprintStringEnd = rolePaymentprintStringEnd + "[" + str(loopCounter) + "] " + \
                                    str(RolePaymentArray[loopCounter-1][0]) + " ($" +\
                                    str(RolePaymentArray[loopCounter-1][1]) + " / hour), "
        loopCounter = loopCounter + 1
    # Repeat loop condition: Until(loopCounter==loopCalculator)
    print("|")
    print("|" + rolePaymentprintStringBegin + rolePaymentprintStringEnd)
    print("|")
    print("| Delete role: // using options 1, 2, etc. or use 'next' to skip")
    roleToBeDeleted = input("| :: ")
    print("|")
    print("| Add Role: // Enter the name or use 'next' to skip")
    roleToBeAdded = input("| :: ")
    print("|")
    print("| Add Payrate: // Enter the payrate to correlate with the new role, if you have skipped "
          "the add role option please do not add a payrate, to skip type 'next'")
    payRateToBeAdded = input("| :: ")
    print("")
    if Footer() == True:
        while arrayValidation == False:
            if payRateToBeAdded.isnumeric() == False and payRateToBeAdded != 'next':
                if roleToBeAdded != 'next':
                    print("ERROR: MISMATCH, there is not a corresponding payrate to the role or vice versa.")
                    print("| Add Role: // Enter the name or use 'next' to skip")
                    roleToBeAdded = input("| :: ")
                    print("| Add Payrate: // Enter the payrate to correlate with the new role, if you have skipped "
                          "the add role option please do not add a payrate, to skip type 'next'")
                    payRateToBeAdded = input("| :: ")
                else:
                    if roleToBeDeleted != 'next':
                        while deletionValidation == False:
                            if ArrayValidationAndDeletion(specificValidToBeDeleted=roleToBeDeleted,
                                                          Array=RolePaymentArray, File=RolePayFile) == False:
                                print("ERROR INVALID ROLE: NOT ON Array")
                                roleToBeDeleted = input("Please input a valid role to be deleted: ")
                            else:
                                print("|")
                                print("| ROLE: " + str(roleToBeDeleted) + " was deleted")
                                print("|")
                                deletionValidation = True
                            # end if
                        # end while
                    else:
                        print("NO ACTIONS TAKEN")
                        return True
                    # end if
                # end if
            elif roleToBeAdded.lower() == 'next':
                while deletionValidation == False:
                    if roleToBeDeleted.lower() == 'next':
                        print("NO ACTIONS TAKEN")
                        return True
                    elif ArrayValidationAndDeletion(specificValidToBeDeleted=roleToBeDeleted,
                                                  Array=RolePaymentArray, File=RolePayFile) == False:
                        print("ERROR INVALID ROLE: NOT ON Array")
                        roleToBeDeleted = input("Please input a valid role to be deleted: ")
                    else:
                        print("|")
                        print("| ROLE: " + str(roleToBeDeleted) + " was deleted")
                        print("|")
                        deletionValidation = True
                    # end if
                # end while
            else:
                while additionValidation == False:
                    roleToBeAddedArray[0] = roleToBeAdded
                    roleToBeAddedArray[1] = payRateToBeAdded
                    if ArrayValidationAndAddition(specificValidToBeAdded=roleToBeAddedArray,
                                                  Array=RolePaymentArray, File=RolePayFile) == False:
                        print(" ")
                        print("PROGRAM ERROR")
                        print(" ")
                        time.sleep(2)
                        exit()
                    else:
                        print("|")
                        print("| ROLE: " + str(roleToBeAddedArray[0]) + " was added, paying $" +
                              str(roleToBeAddedArray[1]) + " an hour")
                        return True
                    # end if
                # end while
            # end if
        # end while
    return False

def Display_EmployeePaymentScreen(EmployeeID, EmployeeDetailsArray, EmployeeDetailsFile, EmployeeLoginArray,
                                  EmployeeLoginFile, RolePayArray, RolePayFile, TaxArray, TaxFile, PaymentArray,
                                  PaymentFile, TestingUse):
    if TestingUse == False:
        EmployeeLoginArray = readCSVto2DArray(EmployeeLoginFile)
        EmployeeDetailsArray = readCSVto2DArray(EmployeeDetailsFile)
        PaymentArray = readCSVto2DArray(PaymentFile)
        RolePayFile = readCSVto2DArray(RolePayFile)
        TaxFile = readCSV2Array(TaxFile)
    outputPaymentArray = [None]*21
    mondayHours = 0
    tuesdayHours = 0
    wednesdayHours = 0
    thursdayHours = 0
    fridayHours = 0
    saturdayHours = 0
    sundayHours = 0
    specificEmployeeDetailsArray = ''
    specificEmployeeLoginArray = ''
    employeeArrayPosition = int(EmployeeID) - 1
    employeeName = ''
    employeeSurname = ''
    employeeRole = ''
    hourlyPay = 0
    descriptiveIntroduction = ''
    hoursWorked = 0
    basePay = 0
    publicHolidayOvertimeHours = 0
    weekOvertimeHours = 0
    saturdayOvertime = 0
    sundayOvertime = 0
    overtimePay = 0
    publicHolidayPay = 0
    grossPay = 0
    taxRate = 0
    tax = 0
    netPay = 0
    employeeSuperRate = 0
    employeeSuperDeduction = 0
    employeeHealthPlan = 0
    employeeHealthDeduction = 0
    normalHours = 0
    if FindCurrentEmployee(EmployeeID=EmployeeID, array=EmployeeLoginArray, file=EmployeeLoginFile) == True:
        specificEmployeeDetailsArray = EmployeeDetailsArray[employeeArrayPosition]
        specificEmployeeLoginArray = EmployeeLoginArray[employeeArrayPosition]
        employeeName = str(specificEmployeeLoginArray[1])
        employeeSurname = str(specificEmployeeLoginArray[2])
        employeeRole = str(specificEmployeeDetailsArray[1])
        descriptiveIntroduction = "Employee: " + employeeName + " "  + employeeSurname + " :: EmployeeID: " + EmployeeID
        employeeSuperRate = specificEmployeeDetailsArray[2]
        employeeHealthPlan = specificEmployeeDetailsArray[3]
    # end if
    mondayHours = float(specificEmployeeDetailsArray[8])
    tuesdayHours = float(specificEmployeeDetailsArray[9])
    wednesdayHours = float(specificEmployeeDetailsArray[10])
    thursdayHours = float(specificEmployeeDetailsArray[11])
    fridayHours = float(specificEmployeeDetailsArray[12])
    saturdayHours = float(specificEmployeeDetailsArray[13])
    sundayHours = float(specificEmployeeDetailsArray[14])
    if mondayHours > 8:
        normalHours = normalHours + 8
    else:
        normalHours = normalHours + mondayHours
    # end if
    if tuesdayHours > 8:
        normalHours = normalHours + 8
    else:
        normalHours = normalHours + tuesdayHours
    # end if
    if wednesdayHours > 8:
        normalHours = normalHours + 8
    else:
        normalHours = normalHours + wednesdayHours
    # end if
    if thursdayHours > 8:
        normalHours = normalHours + 8
    else:
        normalHours = normalHours + thursdayHours
    # end if
    if fridayHours > 8:
        normalHours = normalHours + 8
    else:
        normalHours = normalHours + fridayHours
    # end if
    if saturdayHours > 8:
        normalHours = normalHours + 8
    else:
        normalHours = normalHours + saturdayHours
    # end if
    if sundayHours > 8:
        normalHours = normalHours + 8
    else:
        normalHours = normalHours + sundayHours
    # end if
    for role in RolePayArray:
        if employeeRole == str(role[0]):
            hourlyPay = int(role[1])
        # end if
    # end for
    hoursWorked = CalculateTotalHours(MondayHours=mondayHours,
                                      TuesdayHours=tuesdayHours,
                                      WednesdayHours=wednesdayHours,
                                      ThursdayHours=thursdayHours,
                                      FridayHours=fridayHours,
                                      SaturdayHours=saturdayHours,
                                      SundayHours=sundayHours)
    basePay = CalculateBasePay(MondayHours=mondayHours,
                               TuesdayHours=tuesdayHours,
                               WednesdayHours=wednesdayHours,
                               ThursdayHours=thursdayHours,
                               FridayHours=fridayHours,
                               SaturdayHours=saturdayHours,
                               SundayHours=sundayHours,
                               HourlyRate=hourlyPay)

    publicHolidayOvertimeHours = OvertimeCalculator(DayHours=mondayHours)
    weekOvertimeHours = WeekOvertimeCalculator(MondayHours=mondayHours,
                                               TuesdayHours=tuesdayHours,
                                               WednesdayHours=wednesdayHours,
                                               ThursdayHours=thursdayHours,
                                               FridayHours=fridayHours,
                                               SaturdayHours=saturdayHours,
                                               SundayHours=sundayHours)
    saturdayOvertime = OvertimeCalculator(DayHours=saturdayHours)
    sundayOvertime = OvertimeCalculator(DayHours=sundayHours)
    overtimePay = CalculateOvertimePay(MondayHours=mondayHours,
                                       TuesdayHours=tuesdayHours,
                                       WednesdayHours=wednesdayHours,
                                       ThursdayHours=thursdayHours,
                                       FridayHours=fridayHours,
                                       SaturdayHours=saturdayHours,
                                       SundayHours=sundayHours,
                                       HourlyRate=hourlyPay)
    publicHolidayPay = CalculatePublicHolidayPay(mondayHours, hourlyPay)
    grossPay = CalculateTotalPay(BasePay=basePay,
                                 OvertimePay=overtimePay,
                                 PublicHolidayHours=mondayHours,
                                 SaturdayHours=saturdayHours,
                                 SundayHours=sundayHours)
    employeeSuperDeduction = grossPay * (int(employeeSuperRate)/100)
    tax = CalculateTax(GrossPay=(float(grossPay)-float(employeeSuperDeduction)-float(employeeHealthPlan)),
                       HourlyRate=hourlyPay,
                       TaxRatesArray=TaxArray)
    netPay = CalculateNetPay(GrossPay=grossPay,
                             Tax=tax,
                             SuperRate=int(specificEmployeeDetailsArray[2]),
                             HealthInsurnace=int(specificEmployeeDetailsArray[3]))
    clearconsole()
    Header(SystemHeader="Interactive: Clerk", HeaderMessage=descriptiveIntroduction)
    print("|")
    print("| Employee Given name:" + str(employeeName))
    print("|")
    print("| Employee surname:" + str(employeeSurname))
    print("|")
    print("| Role: " + str(employeeRole))
    print("| Hourly rate: $" + str(hourlyPay))
    print("|")
    print("| Monday: " + str(mondayHours))
    print("| Tuesday: " + str(tuesdayHours))
    print("| Wednesday: " + str(wednesdayHours))
    print("| Thursday: " + str(thursdayHours))
    print("| Friday: " + str(fridayHours))
    print("| Saturday: " + str(saturdayHours))
    print("| Sunday: " + str(sundayHours))
    print("| Public holiday hours: " + str(mondayHours))
    print("| Public holiday overtime hours: " + str(publicHolidayOvertimeHours))
    print("| Total Overtime hours: " + str(weekOvertimeHours))
    print("| Saturday overtime hours: " + str(saturdayOvertime))
    print("| Sunday overtime hours: " + str(sundayOvertime))
    print("|")
    print("| Total hours worked: " + str(hoursWorked))
    print("|")
    print("| Base pay: $" + str(basePay))
    print("| Overtime pay: $" + str(overtimePay))
    print("| Public holiday pay: $" + str(publicHolidayPay))
    print("|")
    print("| Gross pay: $" + str(grossPay))
    print("| Superannuation deduction: " + str(employeeSuperRate) + "%")
    if float(netPay) < float(employeeHealthPlan):
        netPay = netPay + int(employeeHealthPlan) + float(tax)
        employeeHealthPlan = 0
        tax = 0
    # end if
    print("| Health insurance deduction: $" + str(employeeHealthPlan))
    print("| Tax: $" + str(tax))
    print("|")
    print("| Net pay: $" + str(netPay))
    print("|")
    print("-----------------------------------------------------------")
    print("")
    if hourlyPay < 30:
        taxRate = taxRatesArray[0]
    elif ArrayLengthCalculator(taxRatesArray) > 2 and hourlyPay >= 50:
        taxRate = taxRatesArray[2]
    else:
        taxRate = taxRatesArray[1]
    # end if
    if employeeHealthPlan == 0:
        employeeHealthPlan = 'Unpaid'
        employeeHealthDeduction = 0
    elif employeeHealthPlan == 15:
        employeeHealthPlan = 'Ancillery'
        employeeHealthDeduction = 15
    elif employeeHealthPlan == 25:
        employeeHealthPlan = 'Standard'
        employeeHealthDeduction = 25
    else:
        employeeHealthPlan = 'Superior'
        employeeHealthDeduction = 45
    # end if
    if TestingUse == False:
        outputPaymentArray[0] = EmployeeID
        outputPaymentArray[1] = employeeName
        outputPaymentArray[2] = employeeSurname
        outputPaymentArray[3] = employeeRole
        outputPaymentArray[4] = taxRate
        outputPaymentArray[5] = employeeSuperRate
        outputPaymentArray[6] = employeeHealthPlan
        outputPaymentArray[7] = mondayHours
        outputPaymentArray[8] = tuesdayHours
        outputPaymentArray[9] = wednesdayHours
        outputPaymentArray[10] = thursdayHours
        outputPaymentArray[11] = fridayHours
        outputPaymentArray[12] = saturdayHours
        outputPaymentArray[13] = sundayHours
        outputPaymentArray[14] = normalHours
        outputPaymentArray[15] = weekOvertimeHours
        outputPaymentArray[16] = grossPay
        outputPaymentArray[17] = employeeSuperDeduction
        outputPaymentArray[18] = employeeHealthDeduction
        outputPaymentArray[19] = tax
        outputPaymentArray[20] = netPay
        returnSelection = input("Enter anything to return: ")
    else:
        clearconsole()
    # end if
    PaymentArray.append(outputPaymentArray)
    TwoDimensionalArrayToFile(array=PaymentArray, file=PaymentFile)
    return False
# end def

# def Display_TestMode(FileToBeRead):
#     DataArray = []
#     ##ReadIn FileToBeRead to DataArray
#     SortData(DataArray)
#     StoreData(DataArray)
#     CalculateAndPrint(DataArray)
#     print("|")
#     print("| Thankyou for using the test mode.")
#     print("|")


# ======================================================================================================================
# File Setup
# ======================================================================================================================

if file_exists("EmployeeLoginDetails.csv") == False:
    f = open('EmployeeLoginDetails.csv', 'a+')
    f.write("1,Billy,Bob,EmployeePass123")
    f.write("\n")
    f.write("2,Timmy,Tom,EmployeePass456")
    f.write("\n")
    f.write("3,Charlie,Chaplin,ClerkPass432")
    f.write("\n")
    f.write("4,Telina,Swarez,ManagerPass123")
    f.write("\n")
    print("CREATED FILE: EmployeeLoginDetails")
    f.close()
    employeeLoginArray = readCSVto2DArray('EmployeeLoginDetails.csv')
else:
    employeeLoginArray = readCSVto2DArray('EmployeeLoginDetails.csv')
# end if

if file_exists("SuperannuationRates.csv") == False:
    f = open('SuperannuationRates.csv', 'a+')
    f.write("4")
    f.write("\n")
    f.write("6")
    f.write("\n")
    f.write("8")
    f.write("\n")
    print("CREATED FILE: SuperannuationRates")
    f.close()
    superannuationArray = readCSV2Array('SuperannuationRates.csv')
else:
    superannuationArray = readCSV2Array('SuperannuationRates.csv')
# end if

if file_exists("TaxRates.csv") == False:
    f = open('TaxRates.csv', 'a+')
    f.write("30")
    f.write("\n")
    f.write("40")
    f.write("\n")
    print("CREATED FILE: TaxRates")
    f.close()
    taxRatesArray = readCSV2Array('TaxRates.csv')
else:
    taxRatesArray = readCSV2Array('TaxRates.csv')
# end if

if file_exists("HealthInsurance.csv") == False:
    f = open('HealthInsurance.csv', 'a+')
    f.write("15")
    f.write("\n")
    f.write("25")
    f.write("\n")
    f.write("45")
    f.write("\n")
    print("CREATED FILE: HealthInsurance")
    f.close()
    healthInsuranceArray = readCSV2Array('HealthInsurance.csv')
else:
    healthInsuranceArray = readCSV2Array('HealthInsurance.csv')
# end if

if file_exists("RolePaymentRecord.csv") == False:
    f = open('RolePaymentRecord.csv', 'a+')
    f.write("Barista,23")
    f.write("\n")
    f.write("Manager,30")
    f.write("\n")
    f.write("Clerk,50")
    f.write("\n")
    print("CREATED FILE: RolePaymentRecord")
    f.close()
    rolePaymentArray = readCSVto2DArray('RolePaymentRecord.csv')
else:
    rolePaymentArray = readCSVto2DArray('RolePaymentRecord.csv')
# end if

if file_exists("EmployeeFile.csv") == False:
    f = open('EmployeeFile.csv', 'a+')
    f.write("1,Barista,4,15,False,MONDAY,0000,0000,0,0,0,0,0,0,0")
    f.write("\n")
    f.write("2,Manager,4,15,False,MONDAY,0000,0000,0,0,0,0,0,0,0")
    f.write("\n")
    f.write("3,Clerk,6,45,False,MONDAY,0000,0000,0,0,0,0,0,0,0")
    f.write("\n")
    f.write("4,Barista,8,25,False,MONDAY,0000,0000,0,0,0,0,0,0,0")
    f.write("\n")
    print("CREATED FILE: EmployeeFile")
    f.close()
    EmployeeDetailsArray = readCSVto2DArray('EmployeeFile.csv')
else:
    EmployeeDetailsArray = readCSVto2DArray('EmployeeFile.csv')
# end if

if file_exists("PaymentFile.csv") == False:
    f = open('PaymentFile.csv', 'a+')
    f.write("ID,GNAME,SNAME,ROLE,TRATE,SUPER,HLTH,MON,TUE,WED,THU,FRI,SAT,SUN,NHRS,OHRS,GROSS,SDED,HDED,TAX,NETT")
    f.write("\n")
    print("CREATED FILE: PaymentFile")
    f.close
    PaymentArray = readCSVto2DArray('PaymentFile.csv')
else:
    PaymentArray = readCSVto2DArray('PaymentFile.csv')
# end if

# ======================================================================================================================
# mainline code begins below
# ======================================================================================================================

#### VARIABLES ####

loginGuesses = 0
guessLimit = 3
guessesLeft = guessLimit - loginGuesses
loginOutput = None
employeeID = '0'
employeeIDArrayPlacement = 0
clerkOptionsReturn = ''
clerkPaymentOptionsReturn = ''

# Loop conditions #

confirmation = False
display_Navigation_Loop = False
display_InteractiveClockIn_Return = False
display_ClerkPaymentOptions_loop = True
display_ClerkOptions_loop = True
display_FinancialOptions_loop = True
display_ClerkEmployeeOptions_loop = True

# Main body #

while display_Navigation_Loop == False:
    display_Navigation_Loop == False
    if Display_Navigation() == 't':
        clearconsole()
        #VARIABLES
        fileFound = False
        # tax array
        sameTaxFound = False
        taxPos = 0
        taxFileSize = 0
        taxHolder = 0
        TestTaxArray = None
        # login array
        TestLoginArray = None
        testLoginArrayLength = 0
        # employee details array
        TestEmployeeDetailsArray = None
        testEmployeeDetailsArrayLength = 0
        # health array
        TestHealthArray = None
        testHealthArrayLength = 0
        sameHealthFound = False
        healthPos = 0
        healthHolder = 0
        # super array
        TestSuperArray = None
        testSuperArrayLength = 0
        sameSuperFound = False
        superPos = 0
        superHolder = 0
        # other variables
        testWhileCounter = 0
        personFileLength = 0
        TestDetailsSubArray = [None]*15             # "4,Barista,8,25,False,MONDAY,0000,0000,0,0,0,0,0,0,0"
        TestLoginSubArray = [None]*3
        employeeIDCounter = 0
        while fileFound == False:
            fileToBeRead = input("| Please input the name of the file to be read: ")
            if file_exists(str(fileToBeRead)) == True:
                fileFound = True
            else:
                print("|")
                print("| ERROR: File could not be found")
                print("|")
            # end if
        # end while
        FileArray = readCSVto2DArray(str(fileToBeRead))
        personFileLength = ArrayLengthCalculator(FileArray)
        for item in FileArray:
            if str(item[2]).lower() == 'Administator':
                item[2] = 'Clerk'
            # end if
            for tax in TestTaxArray:
                if item[3] == tax:
                    sameTaxFound = True
                # end if
            # end for
            if sameTaxFound == False:
                taxFileSize = taxFileSize + 1
            # end if
            for super in TestSuperArray:
                if item[4] == super:
                    sameSuperFound = True
                # end if
            # end for
            if sameSuperFound == False:
                testSuperArrayLength = testSuperArrayLength + 1
            # end if
            for health in TestHealthArray:
                if item[5] == health:
                    sameHealthFound = True
                # end if
            # end for
            if sameHealthFound == False:
                testHealthArrayLength = testHealthArrayLength + 1
            # end if
        # end for
        TestTaxArray = [None]*taxFileSize
        TestSuperArray = [None]*testSuperArrayLength
        TestHealthArray = [None]*testHealthArrayLength
        for item in FileArray:
            for tax in TestTaxArray:
                if item[3] == tax:
                    sameTaxFound = True
                else:
                    taxHolder = item[3]
                # end if
            # end for
            if sameTaxFound == False:
                TestTaxArray[taxPos] = taxHolder
            # end if
            taxPos = taxPos + 1
        # end for
        for item in FileArray:
            for super in TestSuperArray:
                if item[4] == super:
                    sameSuperFound = True
                else:
                    superHolder = item[4]
                # end if
            # end for
            if sameSuperFound == False:
                TestSuperArray[superPos] = superHolder
            # end if
            superPos = superPos + 1
        # end for
        for item in FileArray:
            for health in TestHealthArray:
                if item[5] == health:
                    sameHealthFound = True
                else:
                    healthHolder = item[5]
                # end if
            # end for
            if sameHealthFound == False:
                TestHealthArray[healthPos] = healthHolder
            # end if
            healthPos = healthPos + 1
        # end for
        for item in FileArray:
            loginArrayLength = loginGuesses + 1
            testEmployeeDetailsArrayLength = testEmployeeDetailsArrayLength + 1
        # end for
        TestLoginArray = [None]*loginArrayLength
        TestEmployeeDetailsArray = [None]*testEmployeeDetailsArrayLength
        for item in FileArray:
            TestLoginSubArray[0] = employeeIDCounter
            TestLoginSubArray[1] = item[1]
            TestLoginSubArray[2] = item[2]
            TestDetailsSubArray[0] = employeeIDCounter
            TestDetailsSubArray[1] = item[2]
            TestDetailsSubArray[2] = item[4]
            TestDetailsSubArray[3] = item[5]
            TestDetailsSubArray[4] = False
            TestDetailsSubArray[5] = 'MONDAY'
            TestDetailsSubArray[6] = 0000
            TestDetailsSubArray[7] = 0000
            TestDetailsSubArray[8] = item[6]
            TestDetailsSubArray[9] = item[7]
            TestDetailsSubArray[10] = item[8]
            TestDetailsSubArray[11] = item[9]
            TestDetailsSubArray[12] = item[10]
            TestDetailsSubArray[13] = item[11]
            TestDetailsSubArray[14] = item[12]
            TestLoginArray[employeeIDCounter] = TestLoginSubArray
            TestEmployeeDetailsArray[employeeIDCounter] = TestDetailsSubArray
            employeeIDCounter = employeeIDCounter + 1
        # end for
        while testWhileCounter < personFileLength:
            Display_EmployeePaymentScreen(EmployeeID=int(testWhileCounter+1),
                                          EmployeeDetailsArray=TestEmployeeDetailsArray,
                                          EmployeeDetailsFile=False,
                                          EmployeeLoginArray=TestLoginArray,
                                          EmployeeLoginFile=False,
                                          RolePayArray=rolePaymentArray,
                                          RolePayFile=False,
                                          TaxArray=TestTaxArray,
                                          TaxFile=False,
                                          PaymentArray=PaymentArray,
                                          PaymentFile='PaymentFile.csv',
                                          TestingUse=True)
            testWhileCounter = testWhileCounter + 1
        # end while
        clearconsole()
    else:
        clearconsole()
        loginGuesses = 0
        while loginGuesses < guessLimit:
            loginOutput = Display_InteractiveLogin(array=employeeLoginArray, file='EmployeeLoginDetails.csv')
            if loginOutput == False:
                loginGuesses = loginGuesses + 1
                guessesLeft = guessesLeft - 1
                clearconsole()
                incorrectGuessLeftString = "Incorrect: guesses left -- [{}]".format(guessesLeft)
                print(incorrectGuessLeftString)
                print("")
            else:
                loginGuesses = guessLimit + 1
            # end if
        # end while
        if loginGuesses == guessLimit:
            print("Account lockout: please contact administrator")
            time.sleep(3)
            exit()
        else:
            clearconsole()
            employeeID = loginOutput
            specificEmployeeArray = EmployeeDetailsArray[FindCurrentEmployee(EmployeeID=loginOutput,
                                                                             array=EmployeeDetailsArray,
                                                                             file='EmployeeFile.csv')]
            while display_InteractiveClockIn_Return == False:
                display_InteractiveClockIn_Return = False
                employeeIDArrayPlacement = int(employeeID) - 1
                if EmployeeDetailsArray[employeeIDArrayPlacement][1] != 'Clerk':
                    if Display_InteractiveClockIn(EmployeeID=employeeID,
                                                  LoginArray=employeeLoginArray,
                                                  LoginFile='EmployeeLoginDetails.csv',
                                                  EmployeeDetailsArray=EmployeeDetailsArray,
                                                  EmployeeDetailsFile='EmployeeFile.csv') == True:
                        clearconsole()
                        Display_Clockin(EmployeeID=employeeID,
                                        LoginArray=employeeLoginArray,
                                        LoginFile='EmployeeLoginDetails.csv',
                                        EmployeeDetailsArray=EmployeeDetailsArray,
                                        EmployeeDetailsFile='EmployeeFile.csv')
                        time.sleep(5)
                        exit()
                    else:
                        display_InteractiveClockIn_Return = True
                else:
                    while display_ClerkOptions_loop == True:
                        display_ClerkOptions_loop = True
                        clearconsole()
                        clerkOptionsReturn = Display_ClerkOptions(EmployeeID=employeeID,
                                                                  EmployeeLoginArray=employeeLoginArray,
                                                                  LoginFile='EmployeeLoginDetails.csv',
                                                                  EmployeeDetailsArray=EmployeeDetailsArray,
                                                                  EmployeeDetailsFile='EmployeeFile.csv')
                        if clerkOptionsReturn == 'Payment':
                            while display_ClerkPaymentOptions_loop == True:
                                display_ClerkPaymentOptions_loop = True
                                clearconsole()
                                clerkPaymentOptionsReturn = Display_ClerkPaymentOptions(EmployeeLoginArray=
                                                                                        employeeLoginArray,
                                                                                        LoginFile=
                                                                                        'EmployeeLoginDetails.csv')
                                if clerkPaymentOptionsReturn != False:
                                    clearconsole()
                                    Display_EmployeePaymentScreen(EmployeeID=clerkPaymentOptionsReturn,
                                                                  EmployeeDetailsArray=EmployeeDetailsArray,
                                                                  EmployeeDetailsFile='EmployeeFile.csv',
                                                                  EmployeeLoginArray=employeeLoginArray,
                                                                  EmployeeLoginFile='EmployeeLoginDetails.csv',
                                                                  RolePayArray=rolePaymentArray,
                                                                  RolePayFile='RolePaymentRecord.csv',
                                                                  TaxArray=taxRatesArray,
                                                                  TaxFile='TaxRates.csv',
                                                                  PaymentArray=PaymentArray,
                                                                  PaymentFile='PaymentFile.csv',
                                                                  TestingUse=False)
                                # end if
                                display_ClerkPaymentOptions_loop = False
                                display_ClerkOptions_loop = False
                                display_InteractiveClockIn_Return = True
                                clearconsole()
                        elif clerkOptionsReturn == 'Financial':
                            while display_FinancialOptions_loop == True:
                                display_FinancialOptions_loop = True
                                clearconsole()
                                display_FinancialOptions_return = Display_FinancialOptions()
                                clearconsole()
                                if display_FinancialOptions_return == 'TaxRates':
                                    Display_Financial_TaxRates(TaxRateArray=taxRatesArray,
                                                               TaxRatesFile='TaxRates.csv')
                                elif display_FinancialOptions_return == 'Superannuation':
                                    Display_Financial_Superannuation(SuperArray=superannuationArray,
                                                                     SuperFile='SuperannuationRates.csv')
                                elif display_FinancialOptions_return == 'HealthInsurance':
                                    Display_Financial_HealthInsurance(HealthInsuranceArray=healthInsuranceArray,
                                                                      HealthFile='HealthInsurance.csv')
                                else:
                                    Display_Financial_PayRates(RolePaymentArray=rolePaymentArray,
                                                               RolePayFile='RolePaymentRecord.csv')
                                # end if
                                display_FinancialOptions_loop = False
                                display_ClerkOptions_loop = False
                                display_InteractiveClockIn_Return = True
                                clearconsole()
                            # end while
                        elif clerkOptionsReturn == 'Employee':
                            while display_ClerkEmployeeOptions_loop == True:
                                display_ClerkEmployeeOptions_loop = True
                                clearconsole()
                                display_ClerkEmployeeOptions_return = Display_ClerkEmployeeOptions()
                                if display_ClerkEmployeeOptions_return == 'Add':
                                    Display_AddEmployee(EmployeeLoginArray=employeeLoginArray,
                                                         EmployeeDetailsArray=EmployeeDetailsArray,
                                                         EmployeeLoginFile='EmployeeLoginDetails.csv',
                                                         EmployeeDetailsFile='EmployeeFile.csv')
                                elif display_ClerkEmployeeOptions_return == 'Remove':
                                    Display_RemoveEmployee(EmployeeLoginArray=employeeLoginArray,
                                                         EmployeeDetailsArray=EmployeeDetailsArray,
                                                         EmployeeLoginFile='EmployeeLoginDetails.csv',
                                                         EmployeeDetailsFile='EmployeeFile.csv')
                                else:
                                    Display_EditEmployee(EmployeeLoginArray=employeeLoginArray,
                                                         EmployeeDetailsArray=EmployeeDetailsArray,
                                                         EmployeeLoginFile='EmployeeLoginDetails.csv',
                                                         EmployeeDetailsFile='EmployeeFile.csv')
                                # end if
                                display_ClerkEmployeeOptions_loop = False
                                display_ClerkOptions_loop = False
                                display_InteractiveClockIn_Return = True
                                clearconsole()
                            # end while
                        else:
                            display_ClerkOptions_loop = False
                        # end if
                    # end while
                # end if
            # end while
        # end if
    # end if
# end while

# end mainline code
# ======================================================================================================================
