# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Program Name: CafeAuLait_PayrollSystem_Submission.py
# Author:       Uzziah Smith
# Purpose:      Allows employees to clock in and out, calculates and pays employees and holds company information.
# Version:      3.0   (increment the decimal every editing session. Increment integer every major feature milestone)
# Last Revison: 20210630_1901 date format
# Dependencies: (1)os - note any libraries, APIs etc used by the code in this file
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os

# ======================================================================================================================
#                                                 TO-BE COMPLETED FUNCTIONS                                            #
# ======================================================================================================================

def TimeCalculator(ClockInTime, ClockOutTime):
    print("TBA")


def TimeChecker(time):
    print("TBA")


def FindEmployee(EmployeeID, Password):
    print("TBA")


def FindCurrentEmployee(EmployeeID):
    print("TBA")


def RandomGenerateEmployeeID():
    print("TBA")


def RandomGenerateEmployeePass():
    print("TBA")


def ValidateRole(EmployeeRole):
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


# ======================================================================================================================
#                                                          ARRAYS                                                      #
# ======================================================================================================================


# ======================================================================================================================
#                                                  ALGORITHMIC FUNCTIONS                                               #
# ======================================================================================================================

def ArrayLengthCalculator(array):
    length = 1
    for entities in array:
        length = length + 1
    # End For
# End Module

def isInt(number):
    if number - int(number) == 0:
        return True
    else:
        return False
    # End if
# End Module

def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')
# End Module

# ======================================================================================================================
#                                                   DISPLAY FUNCTIONS                                                  #
# ======================================================================================================================


def Header(SystemHeader, HeaderMessage):
    print("--------------------------------------------------------------------------------")
    print("| Cafe au Lait – Payment System: " + SystemHeader)
    print("--------------------------------------------------------------------------------")
    print("| " + HeaderMessage)
    print("--------------------------------------------------------------------------------")
# End Module

def Footer(PreviousPageFunction):
    SelectedNavigation = ''
    Confirmation = 0
    print("----------------------------------------------------------------------------------------")
    print("| [R]eturn")
    print("| [C]onfirm")
    print("----------------------------------------------------------------------------------------")
    input(SelectedNavigation)
    while (Confirmation != 1):
        if SelectedNavigation == 'R':
            Confirmation = 1
            PreviousPageFunction
        elif SelectedNavigation == 'C':
            return 'C'
        elif SelectedNavigation != 'C' and SelectedNavigation != 'R':
            print("Please select a valid option")
        # End if
    # End While
# End Module

def Display_Navigation():
    optionSelected = ''
    Header("Navigation", "")
    print("|Please select the required mode to be used:")
    print("|")
    print("|[T]est mode/[I]nteractive mode (default)")
    input(optionSelected)
    if optionSelected == 'T' or optionSelected == 't':
        return 'test'
    # End if
# End Module


def Display_InteractiveLogin():
    outputArray = [None, None]
    EmployeeID = ''
    Password = ''
    Guesses = 0
    Header("Interactive: Log-in", "Interactive mode selected")
    print("|")
    print("| Café-Au-Lait-ID:")
    input(EmployeeID)
    print("|")
    print("| Password:")
    input(Password)
    print("|")
    if Footer(Display_Navigation()) == C:
        EmployeeID = str(EmployeeID)
        outputArray[0] = EmployeeID
        outputArray[1] = Password
        print(outputArray)
        return outputArray
    if Guesses == 3:
        print("ERROR: INVALID EMPLOYEE")
        Display_Navigation()


def Display_InteractiveMode(EmployeeID, EmployeeArray):
    Confirmation = 0
    HoursWorked = 0
    EmployeeName = EmployeeArray[1]
    EmployeeWelcome = "Welcome Employee" + EmployeeName
    Header("Interactive: Employee", EmployeeName)
    print(" | ")
    print(" | Clock - [I]n / [O]ut(default)")
    input(clockSelection)
    print(" | ")
    print(" | // input the day using the designated 3 letter shortened word")
    print(" | ")
    print(" | [MON]day, [TUE]day, [WED]day, [THU]day, [FRI]day, [SAT]day, [SUN]day")
    print("Day:")
    # Repeat loop here
    input(DaySelection)
    if DaySelection != "MON" and DaySelection != "TUE" and DaySelection != "WED" and DaySelection != "THU" and DaySelection != "FRI" and DaySelection != "SAT" and DaySelection != "SUN":
        print(" ")
        print("ERROR: Please enter a valid day")
    else:
        Confirmation = 1
    # Loop condition: Until(Confirmation = 1)
    Confirmation = 0
    print(" | ")
    print(" | ")
    print(" | // input day using the time code hhmm e.g. 11:00am is 1100")
    print(" | ")
    print("Time:")
    # Repeat loop here
    input(TimeStamp)
    TimeChecker(TimeStamp)
    if TimeChecker == Y:
        Confirmation = 1
    else:
        print("")
        print("ERROR: Please enter valid time")
    # Repeat condition: Until(Confirmation==1)
    Confirmation = 0
    Footer(Display_InteractiveLogin(EmployeeFileArray))
    if Footer(Display_InteractiveLogin(EmployeeFileArray)) == 'C':
        if clockSelection == 'I':
            EmployeeArray[8] = "CLOCK - IN"
            EmployeeArray[9] = TimeStamp
            EmployeeArray[10] = "Shift in progress"
        else:
            EmployeeArray[8] = "CLOCK - OUT"
            EmployeeArray[9] = TimeStamp
            HoursWorked = TimeCalculator(EmployeeArray[2], EmployeeArray[3])
        if DaySelection == "MON":
            EmployeeArray[12] = HoursWorked
            EmployeeArray[11] = "MONDAY"
        elif DaySelection == "TUE":
            EmployeeArray[13] = HoursWorked
            EmployeeArray[11] = "TUESDAY"
        elif DaySelection == "WED":
            EmployeeArray[14] = HoursWorked
            EmployeeArray[11] = "WEDNESDAY"
        elif DaySelection == "THU":
            EmployeeArray[15] = HoursWorked
            EmployeeArray[11] = "THURSDAY"
        elif DaySelection == "FRI":
            EmployeeArray[16] = HoursWorked
            EmployeeArray[11] = "FRIDAY"
        elif DaySelection == "SAT":
            EmployeeArray[17] = HoursWorked
            EmployeeArray[11] = "SATURDAY"
        elif DaySelection == "SUN":
            EmployeeArray[18] = HoursWorked
            EmployeeArray[19] = "SUNDAY"


def Display_Clockinprint(EmployeeID, EmployeeFileArray, EmployeeArray):
    CurrentEmployee = FindCurrentEmployee(EmployeeID)
    Header("Interactive: Employee", "Have a good day employee" + CurrentEmployee[1])
    print(" | ")
    print(" | Status: " + CurrentEmployee[8])
    print(" | ")
    print("Day:  " + CurrentEmployee[11])
    print(" | ")
    if CurrentEmployee[Status] == "CLOCK - IN":
        print(" | Time:  " + CurrentEmployee[9])
        print(" | ")
        print(" | Hours: In - progress")
    else:
        print(" | Time:  " + CurrentEmployee[10])
        print(" | ")
        print(" | Hours:  " + TimeCalculator(CurrentEmployee[9], CurrentEmployee[10]))
        print(" | ")
        print("-----------------------------------------------------------")


def Display_ClerkOptions(EmployeeID):
    Header("Interactive: Clerk", "Welcome Clerk" + EmployeeID)
    print(" | ")
    print(" | [P]ayment / [F]inancial / [E]mployee options(default)")
    input(ClerkSelection)
    print(" | ")
    Footer(Display_InteractiveLogin(EmployeeFileArray))
    if Footer(Display_InteractiveLogin(EmployeeFileArray)) == 'C':
        if ClerkSelection == P:
            Display_ClerkPaymentOptions(EmployeeID)
        elif ClerkSelection == F:
            Display_ClerkFinancialOptions(EmployeeID)
        else:
            Display_ClerkEmployeeOptions(EmployeeID)


def Display_ClerkPaymentOptions(EmployeeFileArray, ClerkID):
    Header("Interactive: Clerk", "Payment")
    print(" | ")
    print(" | Enter employee ID")
    print(" | ")
    print(" | Employee - ID:")
    input(EmployeeID)
    print(" | ")
    Footer(Display_ClerkOptions(ClerkID))
    if Footer(Display_ClerkOptions(ClerkID)) == 'C':
        # Repeat loop
        FindCurrentEmployee(EmployeeID)
        if FindCurrentEmployee(EmployeeID) == 'Not found':
            print("ERROR! Invalid employee")
            print("Please input a valid employee ID")
            input(EmployeeID)
        # Repeat loop condition: Until(FindCurrentEmployee(EmployeeID) != 'Not found')


def Display_ClerkEmployeeOptions(ClerkID):
    Header("Interactive: Clerk", "Employee Options")
    print(" | ")
    print(" | [A]dd / [R]emove / [E]dit Employee(default)")
    input(ClerkSelection)
    print(" | ")
    Footer(Display_ClerkOptions(EmployeeID))
    if Display_ClerkOptions(EmployeeID) == 'C':
        if ClerkSelection == 'A':
            Display_AddEmployee(ClerkID)
        elif ClerkSelection == 'R':
            Display_RemoveEmployee()
        else:
            Display_EditEmployee()


def Display_AddEmployee(RolePaymentArray, ClerkID, EmployeeFileArray):
    NewEmployeeHourlyRate = 0
    Header("Interactive: Clerk", "Add Employee")
    print(" | ")
    print(" | Enter employee's details")
    print(" | ")
    print("Given Name: ")
    input(EmployeeGivenName)
    print(" | ")
    print("Surname: ")
    input(EmployeeSurname)
    print(" | ")
    print("Role: [B]arista / [M]anager / [C]lerk")
    input(EmployeeRole)
    print(" | ")
    print("Superannuation: [1]4 % / [2]6 % / [3]8 % (default)")
    input(EmployeeSuperannuation)
    print(" | ")
    print("HealthInsurance:")
    print("[A]ncillery / [SU]perior / [ST]andard(default)")
    input(EmployeeHealthInsurance)
    print(" | ")
    Footer(Display_EmployeeOptions)
    if Footer(Display_EmployeeOptions) == 'C':
        # Repeat loop
        ValidateRole(EmployeeRole)
        if ValidateRole == False:
            print("ERROR INVALID ROLE")
            print("Please input valid role: ")
            input(EmployeeRole)
        # Repeat loop condition: Until(ValidateRole== 'Barista' OR 'Manager' OR 'Clerk')
        NewEmployeeHourlyRate = FindPaymentForRole(EmployeeRole)
        NewEmployeeID = RandomGenerateEmployeeID()
        NewEmployeePass = RandomGenerateEmployeePass()
        EmployeeFileArray.append(NewEmployeeID)
        NewEmployeeArray = [NewEmployeeID, NewEmployeePass, EmployeeGivenName,
                            EmployeeSurname, EmployeeRole, NewEmployeeHourlyRate,
                            EmployeeSuperannuation, EmployeeHealthInsurance,
                            Finished, 0000, 0000, Monday, 0, 0, 0, 0, 0, 0, 0]
        print("-----------------------------------------------------------")
        print(" | ")
        print(" | Generated Employee ID: " + NewEmployeeID)
        print(" | ")
        print(" | Generated Employee Password: " + NewEmployeePass)
        print(" | ")
        print("-----------------------------------------------------------")
        Display_ClerkOptions(EmployeeID)


def Display_RemoveEmployee(EmployeeArrayFile):
    EmployeetoDelete = ""
    Header("Interactive: Clerk", "Remove Employee")
    print(" | ")
    print(" | Enter employee's details")
    print(" | ")
    print(" | Employee - ID:")
    input("EmployeeIDtoRemove")
    print(" | ")
    print(" | Clerk - ID:")
    input(ClerkID)
    print(" | ")
    print(" | Clerk - Password:")
    input(ClerkPassword)
    print(" | ")
    Footer(Display_EmployeeOptions)
    if Footer(Display_EmployeeOptions) == 'C':
        # Repeat loop
        FindCurrentEmployee(EmployeeIDtoRemove)
        if FindCurrentEmployee(EmployeeIDtoRemove) == 'False':
            print("ERROR EMPLOYEE NOT FOUND!")
            print("Enter Valid Employee: ")
            input(EmployeeIDtoRemove)
        # Repeat loop condition: Until(FindCurrentEmployee(EmployeeIDtoRemove) != 'False')
        # Second Repeat loop
        FindEmployee(ClerkID, ClerkPassword)
        if FindEmployee(ClerkID, ClerkPassword) == 'No':
            print("ERROR CLERK NOT FOUND!")
            print("Enter Valid Clerk - ID: ")
            input(ClerkID)
            print("Enter Valid Clerk - Password: ")
            input(ClerkPassword)
        # Repeat loop condition: Until(FindEmployee(ClerkID, ClerkPassword) == 'Yes')
        EmployeetoDelete = FindCurrentEmployee(EmployeeIDtoRemove)
        # Delete EmployeetoDelete
        # Delete EmployeeArrayFile(EmployeeID)
        Display_ClerkOptions(EmployeeID)


def Display_EditEmployee(ClerkID):
    EmployeeArray = []
    Header("Interactive: Clerk", "Edit Employee")
    print(" | ")
    print(" | Café - Au - Lait - ID:")
    input(EmployeeID)
    print(" | ")
    print(" | Password:")
    input(EmployeePassword)
    print(" | ")
    print(" | Role: [B]arista / [M]anager / [C]lerk")
    input(EmployeeRole)
    print(" | ")
    print(" | Superannuation: [1]4% / [2]6% / [3]8%")
    input(EmployeeSuperannuation)
    print(" | ")
    print(" | Health Insurance:")
    print(" | [A]ncillery / [SU]perior / [ST]andard(default)")
    print(" | ")
    input(EmployeeHealthInsurance)
    Footer(Display_ClerkEmployeeOptions(ClerkID))
    if Footer(Display_ClerkEmployeeOptions(ClerkID)) == 'C':
        FindCurrentEmployee(EmployeeID)
        # Repeat loop
        if FindCurrentEmployee(EmployeeID) == 'Not found':
            print("ERROR: PLEASE DO NOT EDIT EMPLOYEE ID")
            input(EmployeeID)
        # Repeat loop condition: Until(FindCurrentEmployee(EmployeeID) != 'Not found')
        EmployeeArray = FindCurrentEmployee(EmployeeID)
        EmployeeArray[1] = EmployeePassword
        EmployeeArray[4] = EmployeeRole
        EmployeeArray[6] = EmployeeSuperannuation
        EmployeeArray[7] = EmployeeHealthInsurance


def Display_FinancialOptions(EmployeeID):
    Header("Interactive: Clerk", "Financial Options")
    print(" | ")
    print(" | [T]ax rate / [S]uperannuation / [H]ealth insurance /")
    print(" | [P]ay rates(default)")
    input(ClerkFinancialOption)
    print(" | ")
    Footer(Display_ClerkOptions(EmployeeID))
    if Footer(Display_ClerkOptions(EmployeeID)) == 'C':
        if ClerkFinancialOption == 'T':
            Display_Financial_TaxRates()
        elif ClerkFinancialOption == 'S':
            Display_Financial_Superannuation()
        elif ClerkFinancialOption == 'H':
            Display_Financial_HealthInsurance()
        else:
            Display_Financial_PayRates()


def Display_Financial_TaxRates(TaxRateArray, EmployeeID):
    LoopCalculator = ArrayLengthCalculator(TaxRateArray)
    LoopCounter = 0
    TaxRateprintStringBegin = " | Tax rates: "
    TaxRateprintString = ""
    Header("Interactive: Clerk", "Tax Adjustment")
    # Repeat loop
    TaxRateprintString = "[" + LoopCounter + "]" + TaxRateArray[LoopCounter] + " % "
    LoopCounter = LoopCounter + 1
    # Repeat loop condition: Until(LoopCounter==LoopCalculator)
    print(" | ")
    print(" | " + TaxRateprintStringBegin + TaxRateprintStringEnd)
    print(" | ")
    print(" | Delete tax rate: // using options 1, 2, 3 etc.")
    input(TaxRateToBeDeleted)
    print(" | ")
    print(" | Add tax rate: // using number without percentage tag")
    input(TaxRateToBeAdded)
    print(" | ")
    Footer(Display_FinancialOptions(EmployeeID))
    if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
        # Repeat loop
        if ArrayValidationAndDeletion(TaxRateToBeDeleted, TaxRateArray) == 'InvalidEntry':
            print("ERROR INVALID TAX RATE: NOT ON Array")
            print("Please input a valid tax rate to be deleted:")
            input(TaxRateToBeDeleted)
        # Repeat loop condition: Until(ArrayValidationAndDeletion(TaxRateToBeDeleted, TaxRateArray) == 'Complete')
        # Second Repeat loop
        if ArrayValidationAndAddition(TaxRateToBeAdded, TaxRateArray) == 'InvalidEntry':
            print("ERROR INVALIDTAX RATE: INVALID INTEGER ENTRY")
            print("Please input a valid tax rate, using an integer without a percentage sign:")
            input(TaxRateToBeAdded)
        # Repeat loop condition: Until(ArrayValidationAndAdded(TaxRateToBeAdded, TaxRateArray) == 'Complete')


def Display_Financial_Superannuation(SuperArray, EmployeeID):
    LoopCalculator = ArrayLengthCalculator(SuperArray)
    LoopCounter = 0
    SuperprintStringBegin = " | Superannuation: "
    SuperprintString = ""
    Header("Interactive: Clerk", "Superannuation Adjustment")
    # Repeat loop
    SuperprintString = "[" + LoopCounter + "]" + "$" + SuperArray[LoopCounter]
    LoopCounter = LoopCounter + 1
    # Repeat loop condition: Until(LoopCounter==LoopCalculator)
    print("|")
    print(" | " + SuperprintStringBegin + SuperprintStringEnd)
    print(" | ")
    print(" | Delete Superannuation Rate: // using options 1, 2, 3 etc.")
    input(SuperToBeDeleted)
    print("|")
    print(" | Add Superannuation: // using number without percentage tag")
    input(SuperToBeAdded)
    print("|")
    Footer(Display_FinancialOptions(EmployeeID))
    if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
        # Repeat loop
        if ArrayValidationAndDeletion(SuperToBeDeleted, SuperArray) == 'InvalidEntry':
            print("ERROR INVALID SUPERANNUATION RATE: NOT ON Array")
            print("Please input a valid superannuation rate to be deleted:")
            input(SuperToBeDeleted)
    # Repeat loop condition: Until(ArrayValidationAndDeletion(SuperToBeDeleted, SuperArray) == 'Complete')
    # Second Repeat loop
    if ArrayValidationAndAddition(SuperToBeAdded, SuperArray) == 'InvalidEntry':
        print("ERROR INVALID SUPERANNUATION: INVALID INTEGER ENTRY")
        print("Please input a valid superannuation rate, using an integer without a percentage sign:")
        input(SuperToBeAdded)
    # Second loop condition: Until(ArrayValidationAndAdded(SuperToBeAdded, SuperArray) == 'Complete')


def Display_Financial_HealthInsurance(HealthInsuranceArray, EmployeeID):
    LoopCalculator = ArrayLengthCalculator(HealthInsuranceArray)
    LoopCounter = 0
    HealthInsuranceprintStringBegin = " | Health Insurance Deductions: "
    HealthInsuranceprintString = ""
    Header("Interactive: Clerk", "Health Insurance Adjustment")
    # Repeat loop
    HealthInsuranceprintString = "[" + LoopCounter + "]" + "$" + HealthInsuranceArray[LoopCounter]
    LoopCounter = LoopCounter + 1
    # Repeat loop condition: Until(LoopCounter==LoopCalculator)
    print("|")
    print("|" + HealthInsuranceprintStringBegin + HealthInsuranceprintStringEnd)
    print("|")
    print(" | Delete Health Insurance Plan: // using options 1, 2, etc.")
    input(HealthInsuranceToBeDeleted)
    print("|")
    print(" | Add Health Insurance Plan: // using the price")
    input(HealthInsuranceToBeAdded)
    print("|")
    Footer(Display_FinancialOptions(EmployeeID))
    if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
        # Repeat loop
        if ArrayValidationAndDeletion(HealthInsuranceToBeDeleted, HealthInsuranceArray) == 'InvalidEntry':
            print("ERROR INVALID HEALTH CARE PLAN: NOT ON Array")
            print("Please input a valid health care plan to be deleted:")
            input(HealthInsuranceToBeDeleted)
        # Repeat loop condition: Until(ArrayValidationAndDeletion(HealthInsuranceToBeDeleted, HealthInsuranceArray) == 'Complete')
        # Second Repeat loop
        if ArrayValidationAndAddition(HealthInsuranceToBeAdded, HealthInsuranceArray) == 'InvalidEntry':
            print("ERROR: INVALID HEALTH CARE PLAN: INVALID INTEGER ENTRY")
            print("Please input a valid health care plan, inputting the cost:")
            input(HealthInsuranceToBeAdded)
        # Repeat loop condition: Until(ArrayValidationAndAdded(HealthInsuranceToBeAdded, HealthInsuranceArray) == 'Complete')


def Display_Financial_PayRates(RolePaymentArray, RoleNameArray, EmployeeID):
    LoopCalculator = ArrayLengthCalculator(RolePaymentArray)
    LoopCounter = 0
    RolePaymentprintStringBegin = " | Payrates: "
    HealthInsuranceprintString = ""
    Header("Interactive: Clerk", "Payrates Adjustment")
    # Repeat loop
    PayRateprintString = "[" + LoopCounter + "]" + RoleNameArray[LoopCounter] + "($" + PayRateArray[
        LoopCounter] + " / hour)"
    LoopCounter = LoopCounter + 1
    # Repeat loop condition: Until(LoopCounter==LoopCalculator)
    print("|")
    print("|" + PayRateprintStringBegin + PayRateprintStringEnd)
    print("|")
    print(" | Delete Payrate: // using options 1, 2, etc.")
    input(PayRateToBeDeleted)
    print("|")
    print(" | Add Role: // Enter the name")
    input(RoleToBeAdded)
    print("|")
    print("| Add Pay Rate: // Enter the hourly rate as an integer")
    input(PayRateToBeAdded)
    print("|")
    Footer(Display_FinancialOptions(EmployeeID))
    if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
        # Repeat loop
        if ArrayValidationAndDeletion(PayRateToBeDeleted, PayRateArray) == 'InvalidEntry':
            print("ERROR INVALID PAY RATE: NOT ON Array")
            print("Please input a valid pay rate to be deleted:")
            input(PayRateToBeDeleted)
    # Repeat loop condition: Until(ArrayValidationAndDeletion(PayRateToBeDeleted, PayRateArray) == 'Complete')
    # Second Repeat loop
    if ArrayValidationAndAddition(PayRateToBeAdded, PayRateArray) == 'InvalidEntry':
        print("ERROR: INVALID ROLE PAY: INVALID INTEGER ENTRY")
        print("Please input a valid payment, inputting the hourly rate:")
        input(PayRateToBeAdded)
    # Repeat loop condition: Until(ArrayValidationAndAdded(PayRateToBeAdded, PayRateArray) == 'Complete')
    # Third Repeat loop
    if ArrayValidationAndAddition(RoleToBeAdded, RoleNameArray) == 'InvalidEntry':
        print("ERROR: VALIDATION AND ADDITION OF ROLE ERROR")
    # Repeat loop condition: Until ArrayValidationAndAddition(RoleToBeAdded, RoleNameArray) == 'Complete'


def Display_EmployeePaymentScreen(EmployeeID, EmployeeFileArray, EmployeeArray):
    CorrectEmployeeArray = FindCurrentEmployee(EmployeeID)
    EmployeeName = CorrectEmployeeArray[2]
    EmployeeSurname = CorrectEmployeeArray[3]
    Role = CorrectEmployeeArray[4]
    HourlyPay = CorrectEmployeeArray[5]
    DescriptiveIntroduction = "Employee" + EmployeeName + EmployeeID
    HoursWorked = CalculateHoursWorked(CorrectEmployeeArray[12], CorrectEmployeeArray[13], CorrectEmployeeArray[14],
                                       CorrectEmployeeArray[15], CorrectEmployeeArray[16], CorrectEmployeeArray[17],
                                       CorrectEmployeeArray[18])
    BasePay = CalculateBasePay(CorrectEmployeeArray[12], CorrectEmployeeArray[13], CorrectEmployeeArray[14],
                               CorrectEmployeeArray[15], CorrectEmployeeArray[16], CorrectEmployeeArray[17],
                               CorrectEmployeeArray[18], HourlyPay)
    PublicHolidayOvertimeHours = OvertimeCalculator(CorrectEmployeeArray[12])
    WeekOvertimeHours = WeekOvertimeCalculator(CorrectEmployeeArray[12], CorrectEmployeeArray[13],
                                               CorrectEmployeeArray[14], CorrectEmployeeArray[15],
                                               CorrectEmployeeArray[16], CorrectEmployeeArray[17],
                                               CorrectEmployeeArray[18])
    SaturdayOvertime = OvertimeCalculator(CorrectEmployeeArray[17])
    SundayOvertime = OvertimeCalculator(CorrectEmployeeArray[18])
    OvertimePay = CalculateOvertimePay(CorrectEmployeeArray[12], CorrectEmployeeArray[13], CorrectEmployeeArray[14],
                                       CorrectEmployeeArray[15], CorrectEmployeeArray[16], CorrectEmployeeArray[17],
                                       CorrectEmployeeArray[18], HourlyPay)
    PublicHolidayPay = CalculatePublicHolidayPay(CorrectEmployeeArray[12], HourlyPay)
    GrossPay = CalculateTotalPay(BasePay, OvertimePay, PublicHolidayPay, CorrectEmployeeArray[12])
    Tax = CalculateTax(GrossPay, Role)
    NetPay = CalculateNetPay(GrossPay, Tax)
    Header("Interactive: Clerk", DescriptiveIntroduction)
    print("|")
    print(" | Employee Given name:" + EmployeeName)
    print("|")
    print(" | Employee surname:" + EmployeeSurname)
    print("|")
    print(" | Role: " + Role)
    print(" | Hourly rate: " + Role)
    print("|")
    print(" | Monday: " + CorrectEmployeeArray[12])
    print(" | Tuesday: " + CorrectEmployeeArray[13])
    print(" | Wednesday: " + CorrectEmployeeArray[14])
    print(" | Thursday: " + CorrectEmployeeArray[15])
    print(" | Friday: " + CorrectEmployeeArray[16])
    print(" | Saturday: " + CorrectEmployeeArray[17])
    print(" | Sunday: " + CorrectEmployeeArray[18])
    print(" | Public holiday hours: " + CorrectEmployeeArray[12])
    print(" | Public holiday overtime hours: " + PublicHolidayOvertimeHours)
    print(" | Overtime hours:" + WeekOvertimeCalculator)
    print(" | Saturday overtime hours:" + SaturdayOvertime)
    print(" | Sunday overtime hours:" + SundayOvertime)
    print("|")
    print(" | Total hours worked:" + HoursWorked)
    print("|")
    print(" | Base pay:" + BasePay)
    print(" | Overtime pay:" + OvertimePay)
    print(" | Public holiday pay:" + PublicHolidayPay)
    print("|")
    print(" | Gross pay:" + GrossPay)
    print(" | Superannuation deduction:" + CorrectEmployeeArray[6])
    print(" | Health insurance deduction:" + CorrectEmployeeArray[7])
    print(" | Tax:" + Tax)
    print("|")
    print(" | Net pay:" + NetPay)
    print("|")
    Footer(Display_Navigation())
    if Footer(Display_Navigation()) == 'C':
        Display_Navigation()


def Display_TestMode(FileToBeRead):
    DataArray = []
    ##ReadIn FileToBeRead to DataArray
    SortData(DataArray)
    StoreData(DataArray)
    CalculateAndPrint(DataArray)
    print("|")
    print(" | Thankyou for using the test mode.")
    print("|")


# ======================================================================================================================
# mainline code begins below
# ======================================================================================================================

guesses = 0
confirmation = False

if Display_Navigation() == 't':
    clearconsole()
    print("")
    # Display_TestMode(FileToBeRead)
else:
    while guesses < 3 and confirmation == False:
        clearconsole()
        Display_InteractiveLogin()
    # End loop
# End if

# end mainline code
# ======================================================================================================================
