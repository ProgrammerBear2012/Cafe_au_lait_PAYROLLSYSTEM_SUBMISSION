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


# ======================================================================================================================
#                                                 TO-BE COMPLETED FUNCTIONS                                            #
# ======================================================================================================================

def GenerateEmployeeID(EmployeeLoginArray):
    newEmployeeID = int(ArrayLengthCalculator(EmployeeLoginArray)) + 1
    return newEmployeeID

def RandomGenerateEmployeePass():
    print("TBA")

def ArrayValidationAndDeletion(SpecificValueToBeDeleted, Array):
    print("TBA")


def ArrayValidationAndAddition(SpecificValueToBeAdded, Array):
    print("TBA")


def FindPaymentForRole(EmployeeRole):
    print("TBA")


def CalculateBasePay(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours, SundayHours,
                     HourlyRate):
    print("TBA")


def OvertimeCalculator(DayHours):
    print("TBA")


def WeekOvertimeCalculator(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours,
                           SundayHours):
    print("TBA")


def CalculateOvertimePay(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours,
                         SundayHours):
    print("TBA")


def CalculatePublicHolidayPay(PublicHolidayHours, HourlyPay):
    print("TBA")


def CalculateTotalPay(BasePay, OvertimePay, PublicHolidayPay, PublicHolidayHours):
    print("TBA")


def CalculateTax(GrossPay, Role):
    print("TBA")


def CalculateNetPay(GrossPay, Tax):
    print("TBA")


def SortData(DataArray):
    print("TBA")


def StoreData(DataArray):
    print("TBA")


def CalculateAndPrint(DataArray):
    print("TBA")


def readInFile():
    print("TBA")


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
    length = 1
    for entities in array:
        length = length + 1
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
        myRecord_list = myRecord_list + readCSVline2List(currentLine)  # put each line of the file into the array/list object
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
        myRecord_list = readCSVline2List(currentLine)  # put each line of the file into the array/list object
        twoDimensionalList[counter] = myRecord_list
        counter = counter + 1
    # end for
    myRecord_Array = convertListTo2DArray(twoDimensionalList)
    inputFileObject.close()
    return myRecord_Array
# end def

def FindCurrentEmployee(EmployeeID, array):
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
    outputTime = int(ClockOutTime) - int(ClockInTime)
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
    Header("Navigation", "")
    print("|Please select the required mode to be used:")
    print("|")
    print("|[T]est mode/[I]nteractive mode (default)")
    optionSelected = input("::")
    return optionSelected.lower()
    # end if
# end def


def Display_InteractiveLogin(array):
    EmployeeID = ''
    Password = ''
    Header("Interactive: Log-in", "Interactive mode selected")
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



def Display_InteractiveClockIn(EmployeeID, EmployeeArray, LoginArray):
    timeStamp = 0000
    timeStampValidation = False
    daySelection = ""
    daySelectionValidation = False
    clockSelection = ""
    clockSelectionValidation = False
    HoursWorked = 0
    employeeFirstName = LoginArray[int(EmployeeID)][1]
    employeeLastName = LoginArray[int(EmployeeID)][2]
    EmployeeWelcome = "Welcome Employee: " + employeeFirstName + " " + employeeLastName
    Header("Interactive: Employee", EmployeeWelcome)
    print("| ")
    clockSelection = input("| Clock - [I]n / [O]ut(default)")
    if clockSelection.lower() != 'i':
        clockSelectionValidation = 'o'
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
                print(isSameString(daySelection, dayString))
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
        TimeChecker(timeStamp)
        if TimeChecker(timeStamp) == True:
            if clockSelection.lower() == 'o':
                if TimeCalculator(EmployeeArray[6], timeStamp) != False:
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
            elif daySelection.lower() == 'tue':
                EmployeeArray[5] = 'TUESDAY'
            elif daySelection.lower() == 'wed':
                EmployeeArray[5] = 'WEDNESDAY'
            elif daySelection.lower() == 'thu':
                EmployeeArray[5] = 'THURSDAY'
            elif daySelection.lower() == 'fri':
                EmployeeArray[5] = 'FRIDAY'
            elif daySelection.lower() == 'sat':
                EmployeeArray[5] = 'SATURDAY'
            elif daySelection.lower() == 'sun':
                EmployeeArray[5] = 'SUNDAY'
            # end if
        else:
            EmployeeArray[4] = False
            EmployeeArray[7] = timeStamp
            HoursWorked = TimeCalculator(EmployeeArray[2], EmployeeArray[3])
            if daySelection.lower() == 'mon':
                EmployeeArray[8] = HoursWorked
            elif daySelection.lower() == 'tue':
                EmployeeArray[9] = HoursWorked
            elif daySelection.lower() == 'wed':
                EmployeeArray[10] = HoursWorked
            elif daySelection.lower() == 'thu':
                EmployeeArray[11] = HoursWorked
            elif daySelection.lower() == 'fri':
                EmployeeArray[12] = HoursWorked
            elif daySelection.lower() == 'sat':
                EmployeeArray[13] = HoursWorked
            elif daySelection.lower() == 'sun':
                EmployeeArray[14] = HoursWorked
            # end if
        # end if
        return True
    # end if
    return False
# end def

def Display_Clockin(EmployeeID, CurrentEmployeeArray, LoginArray):
    employeeFirstName = LoginArray[int(EmployeeID)][1]
    employeeLastName = LoginArray[int(EmployeeID)][2]
    status = None
    if CurrentEmployeeArray[4] == True:
        status = 'Shift in progress'
    else:
        status = 'Not on shift'
    # end if
    Header("Interactive: Employee", "Have a good day employee: " + employeeFirstName + " " + employeeLastName)
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
        print("| Hours:  " + TimeCalculator(CurrentEmployeeArray[6], CurrentEmployeeArray[7]))
        print("| ")
        print("-----------------------------------------------------------")
    # end if
# end def

def Display_ClerkOptions(EmployeeID, EmployeeLoginArray, EmployeeDetailsArray):
    specificEmployee = int(EmployeeID) - 1
    employeeFirstName = EmployeeNameArray[specificEmployee][1]
    employeeLastName = EmployeeNameArray[specificEmployee][2]
    ClerkSelection = ''
    Header("Interactive: Clerk", "Welcome Clerk: " + employeeFirstName + " " + employeeLastName)
    print("| ")
    print("| [P]ayment / [F]inancial / [E]mployee options(default)")
    ClerkSelection = input("| User input:")
    print("| ")
    if Footer() == True:
        if ClerkSelection.lower() == 'p':
            Display_ClerkPaymentOptions(ClerkID=EmployeeID, EmployeeLoginArray=EmployeeLoginArray,
                                        EmployeeDetailsArray=EmployeeDetailsArray)
        elif ClerkSelection.lower() == 'f':
            print("ClerkFinancialOptions")
            # Display_ClerkFinancialOptions(EmployeeID)
        else:
            Display_ClerkEmployeeOptions(ClerkID=EmployeeID)
        # end if
    # end if
# end def

def Display_ClerkPaymentOptions(ClerkID, EmployeeLoginArray, EmployeeDetailsArray):
    clerkPaymentEmployeeID = ''
    employeeFound = False
    Header("Interactive: Clerk", "Payment")
    print("| ")
    if Footer() == True:
        while employeeFound == False:
            clerkPaymentEmployeeID = input("| Enter employee ID: ")
            print("| ")
            if FindCurrentEmployee(clerkPaymentEmployeeID, EmployeeLoginArray) == False:
                print("ERROR! Invalid employee")
                print("Please input a valid employee ID")
            else:
                employeeFound = True
            # end if
        # end while
    # end if
# end def

def Display_ClerkEmployeeOptions(ClerkID):
    clerkSelection = ''
    Header("Interactive: Clerk", "Employee Options")
    print("| ")
    clerkSelection = input("| [A]dd / [R]emove / [E]dit Employee(default): ")
    print("| ")
    if Footer() == True:
        if clerkSelection.lower() == 'a':
            print("Add Employee")
            # Display_AddEmployee(ClerkID)
        elif clerkSelection.lower() == 'r':
            print("remove employee")
            # Display_RemoveEmployee()
        else:
            print("edit Employee")
            # Display_EditEmployee()
        # end if
    # end if
# end def


def Display_AddEmployee(ClerkID, RolePaymentArray, EmployeeDetailsArray):
    newEmployeeID = ''
    newEmployeePass = ''
    newEmployeeHourlyRate = 0
    employeeGivenName = ''
    employeeSurname = ''
    employeeRole = ''
    employeeSuperannuation = ''
    employeeHealthInsurance = ''
    employeeRoleValidation = False
    Header("Interactive: Clerk", "Add Employee")
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
        newEmployeeHourlyRate = FindPaymentForRole(EmployeeRole)
        newEmployeeID = GenerateEmployeeID()
        newEmployeePass = RandomGenerateEmployeePass()
        # EmployeeFileArray.append(NewEmployeeID)
        # NewEmployeeArray = [NewEmployeeID, NewEmployeePass, EmployeeGivenName,
        #                     EmployeeSurname, EmployeeRole, NewEmployeeHourlyRate,     ### FIX OUTPUT TO FILE
        #                     EmployeeSuperannuation, EmployeeHealthInsurance,
        #                     Finished, 0000, 0000, Monday, 0, 0, 0, 0, 0, 0, 0]
        print("-----------------------------------------------------------")
        print("| ")
        print("| Generated Employee ID: " + NewEmployeeID)
        print("| ")
        print("| Generated Employee Password: " + NewEmployeePass)
        print("| ")
        print("-----------------------------------------------------------")
        Display_ClerkOptions(EmployeeID)


# def Display_RemoveEmployee(EmployeeArrayFile):
#     EmployeetoDelete = ""
#     Header("Interactive: Clerk", "Remove Employee")
#     print("| ")
#     print("| Enter employee's details")
#     print("| ")
#     print("| Employee - ID:")
#     input("EmployeeIDtoRemove")
#     print("| ")
#     print("| Clerk - ID:")
#     input(ClerkID)
#     print("| ")
#     print("| Clerk - Password:")
#     input(ClerkPassword)
#     print("| ")
#     Footer(Display_EmployeeOptions)
#     if Footer(Display_EmployeeOptions) == 'C':
#         # Repeat loop
#         FindCurrentEmployee(EmployeeIDtoRemove)
#         if FindCurrentEmployee(EmployeeIDtoRemove) == 'False':
#             print("ERROR EMPLOYEE NOT FOUND!")
#             print("Enter Valid Employee: ")
#             input(EmployeeIDtoRemove)
#         # Repeat loop condition: Until(FindCurrentEmployee(EmployeeIDtoRemove) != 'False')
#         # Second Repeat loop
#         FindEmployee(ClerkID, ClerkPassword)
#         if FindEmployee(ClerkID, ClerkPassword) == 'No':
#             print("ERROR CLERK NOT FOUND!")
#             print("Enter Valid Clerk - ID: ")
#             input(ClerkID)
#             print("Enter Valid Clerk - Password: ")
#             input(ClerkPassword)
#         # Repeat loop condition: Until(FindEmployee(ClerkID, ClerkPassword) == 'Yes')
#         EmployeetoDelete = FindCurrentEmployee(EmployeeIDtoRemove)
#         # Delete EmployeetoDelete
#         # Delete EmployeeArrayFile(EmployeeID)
#         Display_ClerkOptions(EmployeeID)
#
#
# def Display_EditEmployee(ClerkID):
#     EmployeeArray = []
#     Header("Interactive: Clerk", "Edit Employee")
#     print("| ")
#     print("| Café - Au - Lait - ID:")
#     input(EmployeeID)
#     print("| ")
#     print("| Password:")
#     input(EmployeePassword)
#     print("| ")
#     print("| Role: [B]arista / [M]anager / [C]lerk")
#     input(EmployeeRole)
#     print("| ")
#     print("| Superannuation: [1]4% / [2]6% / [3]8%")
#     input(EmployeeSuperannuation)
#     print("| ")
#     print("| Health Insurance:")
#     print("| [A]ncillery / [SU]perior / [ST]andard(default)")
#     print("| ")
#     input(EmployeeHealthInsurance)
#     Footer(Display_ClerkEmployeeOptions(ClerkID))
#     if Footer(Display_ClerkEmployeeOptions(ClerkID)) == 'C':
#         FindCurrentEmployee(EmployeeID)
#         # Repeat loop
#         if FindCurrentEmployee(EmployeeID) == 'Not found':
#             print("ERROR: PLEASE DO NOT EDIT EMPLOYEE ID")
#             input(EmployeeID)
#         # Repeat loop condition: Until(FindCurrentEmployee(EmployeeID) != 'Not found')
#         EmployeeArray = FindCurrentEmployee(EmployeeID)
#         EmployeeArray[1] = EmployeePassword
#         EmployeeArray[4] = EmployeeRole
#         EmployeeArray[6] = EmployeeSuperannuation
#         EmployeeArray[7] = EmployeeHealthInsurance
#
#
# def Display_FinancialOptions(EmployeeID):
#     ClerkFinancialOption = ''
#     Header("Interactive: Clerk", "Financial Options")
#     print("| ")
#     print("| [T]ax rate / [S]uperannuation / [H]ealth insurance /")
#     print("| [P]ay rates(default)")
#     input(ClerkFinancialOption)
#     print("| ")
#     Footer(Display_ClerkOptions(EmployeeID))
#     if Footer(Display_ClerkOptions(EmployeeID)) == 'C':
#         if ClerkFinancialOption == 'T':
#             Display_Financial_TaxRates()
#         elif ClerkFinancialOption == 'S':
#             Display_Financial_Superannuation()
#         elif ClerkFinancialOption == 'H':
#             Display_Financial_HealthInsurance()
#         else:
#             Display_Financial_PayRates()
#
#
# def Display_Financial_TaxRates(TaxRateArray, EmployeeID):
#     TaxRateToBeAdded = 0
#     TaxRateToBeDeleted = 0
#     LoopCalculator = ArrayLengthCalculator(TaxRateArray)
#     LoopCounter = 0
#     TaxRateprintStringBegin = " | Tax rates: "
#     TaxRateprintStringEnd = ""
#     Header("Interactive: Clerk", "Tax Adjustment")
#     # Repeat loop
#     TaxRateprintString = "[" + LoopCounter + "]" + TaxRateArray[LoopCounter] + " % "
#     LoopCounter = LoopCounter + 1
#     # Repeat loop condition: Until(LoopCounter==LoopCalculator)
#     print("| ")
#     print("| " + TaxRateprintStringBegin + TaxRateprintStringEnd)
#     print("| ")
#     print("| Delete tax rate: // using options 1, 2, 3 etc.")
#     input(TaxRateToBeDeleted)
#     print("| ")
#     print("| Add tax rate: // using number without percentage tag")
#     input(TaxRateToBeAdded)
#     print("| ")
#     Footer(Display_FinancialOptions(EmployeeID))
#     if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
#         # Repeat loop
#         if ArrayValidationAndDeletion(TaxRateToBeDeleted, TaxRateArray) == 'InvalidEntry':
#             print("ERROR INVALID TAX RATE: NOT ON Array")
#             print("Please input a valid tax rate to be deleted:")
#             input(TaxRateToBeDeleted)
#         # Repeat loop condition: Until(ArrayValidationAndDeletion(TaxRateToBeDeleted, TaxRateArray) == 'Complete')
#         # Second Repeat loop
#         if ArrayValidationAndAddition(TaxRateToBeAdded, TaxRateArray) == 'InvalidEntry':
#             print("ERROR INVALIDTAX RATE: INVALID INTEGER ENTRY")
#             print("Please input a valid tax rate, using an integer without a percentage sign:")
#             input(TaxRateToBeAdded)
#         # Repeat loop condition: Until(ArrayValidationAndAdded(TaxRateToBeAdded, TaxRateArray) == 'Complete')
#
#
# def Display_Financial_Superannuation(SuperArray, EmployeeID):
#     LoopCalculator = ArrayLengthCalculator(SuperArray)
#     LoopCounter = 0
#     SuperprintStringBegin = " | Superannuation: "
#     SuperprintString = ""
#     Header("Interactive: Clerk", "Superannuation Adjustment")
#     # Repeat loop
#     SuperprintString = "[" + LoopCounter + "]" + "$" + SuperArray[LoopCounter]
#     LoopCounter = LoopCounter + 1
#     # Repeat loop condition: Until(LoopCounter==LoopCalculator)
#     print("|")
#     print("| " + SuperprintStringBegin + SuperprintStringEnd)
#     print("| ")
#     print("| Delete Superannuation Rate: // using options 1, 2, 3 etc.")
#     input(SuperToBeDeleted)
#     print("|")
#     print("| Add Superannuation: // using number without percentage tag")
#     input(SuperToBeAdded)
#     print("|")
#     Footer(Display_FinancialOptions(EmployeeID))
#     if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
#         # Repeat loop
#         if ArrayValidationAndDeletion(SuperToBeDeleted, SuperArray) == 'InvalidEntry':
#             print("ERROR INVALID SUPERANNUATION RATE: NOT ON Array")
#             print("Please input a valid superannuation rate to be deleted:")
#             input(SuperToBeDeleted)
#     # Repeat loop condition: Until(ArrayValidationAndDeletion(SuperToBeDeleted, SuperArray) == 'Complete')
#     # Second Repeat loop
#     if ArrayValidationAndAddition(SuperToBeAdded, SuperArray) == 'InvalidEntry':
#         print("ERROR INVALID SUPERANNUATION: INVALID INTEGER ENTRY")
#         print("Please input a valid superannuation rate, using an integer without a percentage sign:")
#         input(SuperToBeAdded)
#     # Second loop condition: Until(ArrayValidationAndAdded(SuperToBeAdded, SuperArray) == 'Complete')
#
#
# def Display_Financial_HealthInsurance(HealthInsuranceArray, EmployeeID):
#     LoopCalculator = ArrayLengthCalculator(HealthInsuranceArray)
#     LoopCounter = 0
#     HealthInsuranceprintStringBegin = " | Health Insurance Deductions: "
#     HealthInsuranceprintString = ""
#     Header("Interactive: Clerk", "Health Insurance Adjustment")
#     # Repeat loop
#     HealthInsuranceprintString = "[" + LoopCounter + "]" + "$" + HealthInsuranceArray[LoopCounter]
#     LoopCounter = LoopCounter + 1
#     # Repeat loop condition: Until(LoopCounter==LoopCalculator)
#     print("|")
#     print("|" + HealthInsuranceprintStringBegin + HealthInsuranceprintStringEnd)
#     print("|")
#     print("| Delete Health Insurance Plan: // using options 1, 2, etc.")
#     input(HealthInsuranceToBeDeleted)
#     print("|")
#     print("| Add Health Insurance Plan: // using the price")
#     input(HealthInsuranceToBeAdded)
#     print("|")
#     Footer(Display_FinancialOptions(EmployeeID))
#     if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
#         # Repeat loop
#         if ArrayValidationAndDeletion(HealthInsuranceToBeDeleted, HealthInsuranceArray) == 'InvalidEntry':
#             print("ERROR INVALID HEALTH CARE PLAN: NOT ON Array")
#             print("Please input a valid health care plan to be deleted:")
#             input(HealthInsuranceToBeDeleted)
#         # Repeat loop condition: Until(ArrayValidationAndDeletion(HealthInsuranceToBeDeleted, HealthInsuranceArray) == 'Complete')
#         # Second Repeat loop
#         if ArrayValidationAndAddition(HealthInsuranceToBeAdded, HealthInsuranceArray) == 'InvalidEntry':
#             print("ERROR: INVALID HEALTH CARE PLAN: INVALID INTEGER ENTRY")
#             print("Please input a valid health care plan, inputting the cost:")
#             input(HealthInsuranceToBeAdded)
#         # Repeat loop condition: Until(ArrayValidationAndAdded(HealthInsuranceToBeAdded, HealthInsuranceArray) == 'Complete')
#
#
# def Display_Financial_PayRates(RolePaymentArray, RoleNameArray, EmployeeID):
#     LoopCalculator = ArrayLengthCalculator(RolePaymentArray)
#     LoopCounter = 0
#     RolePaymentprintStringBegin = " | Payrates: "
#     HealthInsuranceprintString = ""
#     Header("Interactive: Clerk", "Payrates Adjustment")
#     # Repeat loop
#     PayRateprintString = "[" + LoopCounter + "]" + RoleNameArray[LoopCounter] + "($" + PayRateArray[
#         LoopCounter] + " / hour)"
#     LoopCounter = LoopCounter + 1
#     # Repeat loop condition: Until(LoopCounter==LoopCalculator)
#     print("|")
#     print("|" + PayRateprintStringBegin + PayRateprintStringEnd)
#     print("|")
#     print("| Delete Payrate: // using options 1, 2, etc.")
#     input(PayRateToBeDeleted)
#     print("|")
#     print("| Add Role: // Enter the name")
#     input(RoleToBeAdded)
#     print("|")
#     print("| Add Pay Rate: // Enter the hourly rate as an integer")
#     input(PayRateToBeAdded)
#     print("|")
#     Footer(Display_FinancialOptions(EmployeeID))
#     if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
#         # Repeat loop
#         if ArrayValidationAndDeletion(PayRateToBeDeleted, PayRateArray) == 'InvalidEntry':
#             print("ERROR INVALID PAY RATE: NOT ON Array")
#             print("Please input a valid pay rate to be deleted:")
#             input(PayRateToBeDeleted)
#     # Repeat loop condition: Until(ArrayValidationAndDeletion(PayRateToBeDeleted, PayRateArray) == 'Complete')
#     # Second Repeat loop
#     if ArrayValidationAndAddition(PayRateToBeAdded, PayRateArray) == 'InvalidEntry':
#         print("ERROR: INVALID ROLE PAY: INVALID INTEGER ENTRY")
#         print("Please input a valid payment, inputting the hourly rate:")
#         input(PayRateToBeAdded)
#     # Repeat loop condition: Until(ArrayValidationAndAdded(PayRateToBeAdded, PayRateArray) == 'Complete')
#     # Third Repeat loop
#     if ArrayValidationAndAddition(RoleToBeAdded, RoleNameArray) == 'InvalidEntry':
#         print("ERROR: VALIDATION AND ADDITION OF ROLE ERROR")
#     # Repeat loop condition: Until ArrayValidationAndAddition(RoleToBeAdded, RoleNameArray) == 'Complete'
#
#
# def Display_EmployeePaymentScreen(EmployeeID, EmployeeFileArray, EmployeeArray):
#     CorrectEmployeeArray = FindCurrentEmployee(EmployeeID)
#     EmployeeName = CorrectEmployeeArray[2]
#     EmployeeSurname = CorrectEmployeeArray[3]
#     Role = CorrectEmployeeArray[4]
#     HourlyPay = CorrectEmployeeArray[5]
#     DescriptiveIntroduction = "Employee" + EmployeeName + EmployeeID
#     HoursWorked = CalculateHoursWorked(CorrectEmployeeArray[12], CorrectEmployeeArray[13], CorrectEmployeeArray[14],
#                                        CorrectEmployeeArray[15], CorrectEmployeeArray[16], CorrectEmployeeArray[17],
#                                        CorrectEmployeeArray[18])
#     BasePay = CalculateBasePay(CorrectEmployeeArray[12], CorrectEmployeeArray[13], CorrectEmployeeArray[14],
#                                CorrectEmployeeArray[15], CorrectEmployeeArray[16], CorrectEmployeeArray[17],
#                                CorrectEmployeeArray[18], HourlyPay)
#     PublicHolidayOvertimeHours = OvertimeCalculator(CorrectEmployeeArray[12])
#     WeekOvertimeHours = WeekOvertimeCalculator(CorrectEmployeeArray[12], CorrectEmployeeArray[13],
#                                                CorrectEmployeeArray[14], CorrectEmployeeArray[15],
#                                                CorrectEmployeeArray[16], CorrectEmployeeArray[17],
#                                                CorrectEmployeeArray[18])
#     SaturdayOvertime = OvertimeCalculator(CorrectEmployeeArray[17])
#     SundayOvertime = OvertimeCalculator(CorrectEmployeeArray[18])
#     OvertimePay = CalculateOvertimePay(CorrectEmployeeArray[12], CorrectEmployeeArray[13], CorrectEmployeeArray[14],
#                                        CorrectEmployeeArray[15], CorrectEmployeeArray[16], CorrectEmployeeArray[17],
#                                        CorrectEmployeeArray[18], HourlyPay)
#     PublicHolidayPay = CalculatePublicHolidayPay(CorrectEmployeeArray[12], HourlyPay)
#     GrossPay = CalculateTotalPay(BasePay, OvertimePay, PublicHolidayPay, CorrectEmployeeArray[12])
#     Tax = CalculateTax(GrossPay, Role)
#     NetPay = CalculateNetPay(GrossPay, Tax)
#     Header("Interactive: Clerk", DescriptiveIntroduction)
#     print("|")
#     print("| Employee Given name:" + EmployeeName)
#     print("|")
#     print("| Employee surname:" + EmployeeSurname)
#     print("|")
#     print("| Role: " + Role)
#     print("| Hourly rate: " + Role)
#     print("|")
#     print("| Monday: " + CorrectEmployeeArray[12])
#     print("| Tuesday: " + CorrectEmployeeArray[13])
#     print("| Wednesday: " + CorrectEmployeeArray[14])
#     print("| Thursday: " + CorrectEmployeeArray[15])
#     print("| Friday: " + CorrectEmployeeArray[16])
#     print("| Saturday: " + CorrectEmployeeArray[17])
#     print("| Sunday: " + CorrectEmployeeArray[18])
#     print("| Public holiday hours: " + CorrectEmployeeArray[12])
#     print("| Public holiday overtime hours: " + PublicHolidayOvertimeHours)
#     print("| Overtime hours:" + WeekOvertimeCalculator)
#     print("| Saturday overtime hours:" + SaturdayOvertime)
#     print("| Sunday overtime hours:" + SundayOvertime)
#     print("|")
#     print("| Total hours worked:" + HoursWorked)
#     print("|")
#     print("| Base pay:" + BasePay)
#     print("| Overtime pay:" + OvertimePay)
#     print("| Public holiday pay:" + PublicHolidayPay)
#     print("|")
#     print("| Gross pay:" + GrossPay)
#     print("| Superannuation deduction:" + CorrectEmployeeArray[6])
#     print("| Health insurance deduction:" + CorrectEmployeeArray[7])
#     print("| Tax:" + Tax)
#     print("|")
#     print("| Net pay:" + NetPay)
#     print("|")
#     Footer(Display_Navigation())
#     if Footer(Display_Navigation()) == 'C':
#         Display_Navigation()
#
#
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
else:
    employeeLoginArray = readCSVto2DArray('EmployeeLoginDetails.csv')

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
else:
    superannuationArray = readCSV2Array('SuperannuationRates.csv')

if file_exists("TaxRates.csv") == False:
    f = open('TaxRates.csv', 'a+')
    f.write("30")
    f.write("\n")
    f.write("40")
    f.write("\n")
    print("CREATED FILE: TaxRates")
    f.close()
else:
    taxRatesArray = readCSV2Array('TaxRates.csv')

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
else:
    healthInsuranceArray = readCSV2Array('HealthInsurance.csv')

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
else:
    rolePaymentArray = readCSVto2DArray('RolePaymentRecord.csv')

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
else:
    employeeFileArray = readCSVto2DArray('EmployeeFile.csv')


# ======================================================================================================================
# mainline code begins below
# ======================================================================================================================

loginGuesses = 0
guessLimit = 3
guessesLeft = guessLimit - loginGuesses
confirmation = False
display_Navigation_Loop = False
display_InteractiveClockIn_Return = False
loginOutput = None
employeeID = '0'
employeeIDArrayPlacement = 0

while display_Navigation_Loop == False:
    if Display_Navigation() == 't':
        clearconsole()
        print("")
        print(employeeLoginArray)
        print(superannuationArray)
        print(taxRatesArray)
        print(healthInsuranceArray)
        print(rolePaymentArray)
        print(employeeFileArray)
        # Display_TestMode(FileToBeRead)
    else:
        clearconsole()
        while loginGuesses < guessLimit:
            loginOutput = Display_InteractiveLogin(array=employeeLoginArray)
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
            exit()
        else:
            clearconsole()
            employeeID = loginOutput
            specificEmployeeArray = employeeFileArray[FindCurrentEmployee(loginOutput, employeeFileArray)]
            while display_InteractiveClockIn_Return == False:
                employeeIDArrayPlacement = int(employeeID) - 1
                if employeeFileArray[employeeIDArrayPlacement][1] != 'Clerk':
                    if Display_InteractiveClockIn(EmployeeID=employeeID, EmployeeArray=specificEmployeeArray,
                                                  LoginArray=employeeLoginArray) == True:
                        clearconsole()
                        Display_Clockin(EmployeeID=employeeID,CurrentEmployeeArray=specificEmployeeArray,
                                        LoginArray=employeeLoginArray)
                        time.sleep(5)
                        exit()
                    else:
                        display_InteractiveClockIn_Return == True
                else:
                    Display_ClerkOptions(EmployeeID=employeeID)
                # end if
            # end while
        # end if
    # end if
# end while

# end mainline code
# ======================================================================================================================
