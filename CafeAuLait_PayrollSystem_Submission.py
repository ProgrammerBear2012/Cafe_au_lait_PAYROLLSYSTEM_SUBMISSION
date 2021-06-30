######################################################################################################################################################
#                                                          TO-BE COMPLETE FUNCTIONS                                                                  #
######################################################################################################################################################

def TimeCalculator(ClockInTime, ClockOutTime)
def TimeChecker(time)
def FindEmployee(EmployeeID, Password)
def FindCurrentEmployee(EmployeeID)
def RandomGenerateEmployeeID()
def RandomGenerateEmployeePass()
def ValidateRole(EmployeeRole)
def RecordLengthCalculator(Record)
def RecordValidationAndDeletion(SpecificValueToBeDeleted, Record)
def RecordValidationAndAddition(Spec ificValueToBeAdded, Record)
def FindPaymentForRole(EmployeeRole)
def CalculateBasePay(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours, SundayHours, HourlyRate)
def OvertimeCalculator(DayHours)
def WeekOvertimeCalculator(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours, SundayHours)
def CalculateOvertimePay(MondayHours, TuesdayHours, WednesdayHours, ThursdayHours, FridayHours, SaturdayHours, SundayHours)
def CalculatePublicHolidayPay(PublicHolidayHours, HourlyPay)
def CalculateTotalPay(BasePay, OvertimePay, PublicHolidayPay, PublicHolidayHours)
def CalculateTax(GrossPay, Role)
def CalculateNetPay(GrossPay, Tax)
def SortData(DataRecord)
def StoreData(DataRecord)
def CalculateAndprint(DataRecord)

######################################################################################################################################################
#                                                                   ARRAYS                                                                           #
######################################################################################################################################################




######################################################################################################################################################
#                                                            ALGORITHMIC FUNCTIONS                                                                   #
######################################################################################################################################################

def isInt(number):
    if number - int(number) == 0:
        return True
    else:
        return False

######################################################################################################################################################
#                                                            DISPLAY FUNCTIONS                                                                       #
######################################################################################################################################################


def Header(SystemHeader, HeaderMessage):
    print("")
    print("Cafe au Lait – Payment System: " + SystemHeader)
    print("----------------------------------------------------------------------------------------") 
    print("| " + HeaderMessage)
    print("----------------------------------------------------------------------------------------") 
   
def Footer(PreviousPageFunction):
    SelectedNavigation = ''
    Confirmation = 0
    print("----------------------------------------------------------------------------------------")
    print("| [R]eturn")
    print("| [C]onfirm") 
    print("----------------------------------------------------------------------------------------")
    input(SelectedNavigation)
    while(Confirmation != 1):
        if SelectedNavigation == 'R':
            Confirmation = 1
            PreviousPageFunction
        elif SelectedNavigation == 'C':
            return 'C'
        elif SelectedNavigation != 'C' and SelectedNavigation != 'R':
            print("Please select a valid option")

def Display_Navigation():
    optionSelected = ''
    Header("Navigation", "") 
    print("|Please select the required mode to be used:") 
    print("|")
    print("|[T]est mode/[I]nteractive mode (default)")
    input(optionSelected)
    if optionSelected.lower() == 't':
        print("Returning test")
        return 't'
    else: 
        print("Returning interactive")
        return 'i' 

def Interactive_Login(Header, Footer):
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
    Footer(Display_Navigation()) 
    if Footer(Display_Navigation()) == C:
        while Guesses < 3 and FindEmployee(EmployeeID, Password) == 'Yes':
            if FindEmployee(EmployeeID, Password) == False:
                Guesses = Guesses + 1
    if Guesses == 3:
        print("ERROR: INVALID EMPLOYEE")
        Display_Navigation()

def Display_InteractiveMode(EmployeeID, EmployeeRecord):
    Confirmation = 0
    HoursWorked = 0
    EmployeeName = EmployeeRecord[1]
    EmployeeWelcome = "Welcome Employee" + EmployeeName
    Header( "Interactive: Employee", EmployeeName)
    print( " | ")
    print( " | Clock - [I]n / [O]ut(default)")
    input(clockSelection)
    print( " | ")
    print( " | // input the day using the designated 3 letter shortened word")
    print( " | ")
    print( " | [MON]day, [TUE]day, [WED]day, [THU]day, [FRI]day, [SAT]day, [SUN]day")
    print( "Day:")
    #Repeat loop here
    input(DaySelection)
    if DaySelection !=  "MON" and DaySelection !=  "TUE" and DaySelection !=  "WED" and DaySelection !=  "THU" and DaySelection !=  "FRI" and DaySelection !=  "SAT" and DaySelection !=  "SUN":
        print( " ")
        print( "ERROR: Please enter a valid day")
    else:
        Confirmation = 1
    #Loop condition: Until(Confirmation = 1)
    Confirmation = 0
    print( " | ")
    print( " | ")
    print( " | // input day using the time code hhmm e.g. 11:00am is 1100")
    print( " | ")
    print( "Time:")
    #Repeat loop here
    input(TimeStamp)
    TimeChecker(TimeStamp)
    if TimeChecker == Y:
        Confirmation = 1
    else:
        print( "")
        print( "ERROR: Please enter valid time")
    #Repeat condition: Until(Confirmation==1)
    Confirmation = 0
    Footer(Display_InteractiveLogin(EmployeeFileRecord))
    if Footer(Display_InteractiveLogin(EmployeeFileRecord)) == 'C':
        if clockSelection == 'I':
            EmployeeRecord[8] =  "CLOCK - IN"
            EmployeeRecord[9] = TimeStamp
            EmployeeRecord[10] =  "Shift in progress"
        else:
            EmployeeRecord[8] =  "CLOCK - OUT"
            EmployeeRecord[9] = TimeStamp
            HoursWorked = TimeCalculator(EmployeeRecord[2], EmployeeRecord[3])
        if DaySelection ==  "MON":
            EmployeeRecord[12] = HoursWorked
            EmployeeRecord[11] =  "MONDAY"
        elif DaySelection ==  "TUE":
            EmployeeRecord[13] = HoursWorked
            EmployeeRecord[11] =  "TUESDAY"
        elif DaySelection ==  "WED":
            EmployeeRecord[14] = HoursWorked
            EmployeeRecord[11] =  "WEDNESDAY"
        elif DaySelection ==  "THU":
            EmployeeRecord[15] = HoursWorked
            EmployeeRecord[11] =  "THURSDAY"
        elif DaySelection ==  "FRI":
            EmployeeRecord[16] = HoursWorked
            EmployeeRecord[11] =  "FRIDAY"
        elif DaySelection ==  "SAT":
            EmployeeRecord[17] = HoursWorked
            EmployeeRecord[11] =  "SATURDAY"
        elif DaySelection ==  "SUN":
            EmployeeRecord[18] = HoursWorked
            EmployeeRecord[19] =  "SUNDAY"

def Display_Clockinprint(EmployeeID, EmployeeFileRecord, EmployeeRecord):
    CurrentEmployee = FindCurrentEmployee(EmployeeID)
    Header( "Interactive: Employee",  "Have a good day employee" + CurrentEmployee[1])
    print( " | ")
    print( " | Status: " + CurrentEmployee[8])
    print( " | ")
    print( "Day:  " + CurrentEmployee[11])
    print( " | ")
    if CurrentEmployee[Status] ==  "CLOCK - IN":
        print( " | Time:  " + CurrentEmployee[9])
        print( " | ")
        print( " | Hours: In - progress")
    else:
        print( " | Time:  " + CurrentEmployee[10])
        print( " | ")
        print( " | Hours:  " + TimeCalculator(CurrentEmployee[9], CurrentEmployee[10]))
        print( " | ")
        print( "-----------------------------------------------------------")

def Display_ClerkOptions(EmployeeID):
    Header( "Interactive: Clerk",  "Welcome Clerk" + EmployeeID)
    print( " | ")
    print( " | [P]ayment / [F]inancial / [E]mployee options(default)")
    input(ClerkSelection)
    print( " | ")
    Footer(Display_InteractiveLogin(EmployeeFileRecord))
    if Footer(Display_InteractiveLogin(EmployeeFileRecord)) == 'C':
        if ClerkSelection == P:
            Display_ClerkPaymentOptions(EmployeeID)
        elif ClerkSelection == F:
            Display_ClerkFinancialOptions(EmployeeID)
        else:
            Display_ClerkEmployeeOptions(EmployeeID)

def Display_ClerkPaymentOptions(EmployeeFileRecord, ClerkID):
    Header( "Interactive: Clerk",  "Payment")
    print( " | ")
    print( " | Enter employee ID")
    print( " | ")
    print( " | Employee - ID:")
    input(EmployeeID)
    print( " | ")
    Footer(Display_ClerkOptions(ClerkID))
    if Footer(Display_ClerkOptions(ClerkID)) == 'C':
        #Repeat loop
        FindCurrentEmployee(EmployeeID)
        if FindCurrentEmployee(EmployeeID) == 'Not found':
            print( "ERROR! Invalid employee")
            print( "Please input a valid employee ID")
            input(EmployeeID)
        # Repeat loop condition: Until(FindCurrentEmployee(EmployeeID) != 'Not found')

def Display_ClerkEmployeeOptions(ClerkID):
    Header( "Interactive: Clerk",  "Employee Options")
    print( " | ")
    print( " | [A]dd / [R]emove / [E]dit Employee(default)")
    input(ClerkSelection)
    print( " | ")
    Footer(Display_ClerkOptions(EmployeeID))
    if Display_ClerkOptions(EmployeeID) == 'C':
        if ClerkSelection == 'A':
            Display_AddEmployee(ClerkID)
        elif ClerkSelection == 'R':
            Display_RemoveEmployee()
        else:
            Display_EditEmployee()

def Display_AddEmployee(RolePaymentRecord, ClerkID, EmployeeFileRecord):
    NewEmployeeHourlyRate = 0
    Header( "Interactive: Clerk",  "Add Employee")
    print( " | ")
    print( " | Enter employee's details")
    print( " | ")
    print( "Given Name: ")
    input(EmployeeGivenName)
    print( " | ")
    print( "Surname: ")
    input(EmployeeSurname)
    print( " | ")
    print( "Role: [B]arista / [M]anager / [C]lerk")
    input(EmployeeRole)
    print( " | ")
    print( "Superannuation: [1]4 % / [2]6 % / [3]8 % (default)")
    input(EmployeeSuperannuation)
    print( " | ")
    print( "HealthInsurance:")
    print( "[A]ncillery / [SU]perior / [ST]andard(default)")
    input(EmployeeHealthInsurance)
    print( " | ")
    Footer(Display_EmployeeOptions)
    if Footer(Display_EmployeeOptions) == 'C':
        #Repeat loop
        ValidateRole(EmployeeRole)
        if ValidateRole == False:
            print( "ERROR INVALID ROLE")
            print( "Please input valid role: ")
            input(EmployeeRole)
        #Repeat loop condition: Until(ValidateRole== 'Barista' OR 'Manager' OR 'Clerk')
        NewEmployeeHourlyRate = FindPaymentForRole(EmployeeRole)
        NewEmployeeID = RandomGenerateEmployeeID()
        NewEmployeePass = RandomGenerateEmployeePass()
        EmployeeFileRecord.append(NewEmployeeID)
        NewEmployeeRecord = [NewEmployeeID, NewEmployeePass, EmployeeGivenName,
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

def Display_RemoveEmployee(EmployeeRecordFile):
    EmployeetoDelete =  ""
    Header("Interactive: Clerk",  "Remove Employee")
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
        #Repeat loop
        FindCurrentEmployee(EmployeeIDtoRemove)
        if FindCurrentEmployee(EmployeeIDtoRemove) == 'False':
            print( "ERROR EMPLOYEE NOT FOUND!")
            print( "Enter Valid Employee: ")
            input(EmployeeIDtoRemove)
        #Repeat loop condition: Until(FindCurrentEmployee(EmployeeIDtoRemove) != 'False')
        # Second Repeat loop
        FindEmployee(ClerkID, ClerkPassword)
        if FindEmployee(ClerkID, ClerkPassword) == 'No':
            print( "ERROR CLERK NOT FOUND!")
            print( "Enter Valid Clerk - ID: ")
            input(ClerkID)
            print( "Enter Valid Clerk - Password: ")
            input(ClerkPassword)
        #Repeat loop condition: Until(FindEmployee(ClerkID, ClerkPassword) == 'Yes')
        EmployeetoDelete = FindCurrentEmployee(EmployeeIDtoRemove)
        #Delete EmployeetoDelete
        #Delete EmployeeRecordFile(EmployeeID)
        Display_ClerkOptions(EmployeeID)

def Display_EditEmployee(ClerkID):
    EmployeeRecord = []
    Header("Interactive: Clerk",  "Edit Employee")
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
    print( " | [A]ncillery / [SU]perior / [ST]andard(default)")
    print( " | ")
    input(EmployeeHealthInsurance)
    Footer(Display_ClerkEmployeeOptions(ClerkID))
    if Footer(Display_ClerkEmployeeOptions(ClerkID)) == 'C':
        FindCurrentEmployee(EmployeeID)
        #Repeat loop
        if FindCurrentEmployee(EmployeeID) == 'Not found':
            print( "ERROR: PLEASE DO NOT EDIT EMPLOYEE ID")
            input(EmployeeID)
        #Repeat loop condition: Until(FindCurrentEmployee(EmployeeID) != 'Not found')
        EmployeeRecord = FindCurrentEmployee(EmployeeID)
        EmployeeRecord[1] = EmployeePassword
        EmployeeRecord[4] = EmployeeRole
        EmployeeRecord[6] = EmployeeSuperannuation
        EmployeeRecord[7] = EmployeeHealthInsurance

def Display_FinancialOptions(EmployeeID):
    Header("Interactive: Clerk",  "Financial Options")
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

def Display_Financial_TaxRates(TaxRateRecord, EmployeeID):
    LoopCalculator = RecordLengthCalculator(TaxRateRecord)
    LoopCounter = 0
    TaxRateprintStringBegin =  " | Tax rates: "
    TaxRateprintString =  ""
    Header( "Interactive: Clerk",  "Tax Adjustment")
    #Repeat loop
    TaxRateprintString =  "[" + LoopCounter +  "]" + TaxRateRecord[LoopCounter] +  " % "
    LoopCounter = LoopCounter + 1
    #Repeat loop condition: Until(LoopCounter==LoopCalculator)
    print(" | ")
    print(" | " + TaxRateprintStringBegin + TaxRateprintStringEnd)
    print(" | ")
    print(" | Delete tax rate: // using options 1, 2, 3 etc.")
    input(TaxRateToBeDeleted)
    print(" | ")
    print(" | Add tax rate: // using number without percentage tag")
    input(TaxRateToBeAdded)
    print( " | ")
    Footer(Display_FinancialOptions(EmployeeID))
    if Footer(Display_FinancialOptions(EmployeeID)) == 'C':
        #Repeat loop
        if RecordValidationAndDeletion(TaxRateToBeDeleted, TaxRateRecord== 'InvalidEntry':
            print( "ERROR INVALID TAX RATE: NOT ON RECORD")
            print( "Please input a valid tax rate to be deleted:")
            input(TaxRateToBeDeleted)
        #Repeat loop condition: Until(RecordValidationAndDeletion(TaxRateToBeDeleted, TaxRateRecord) == 'Complete')
        #Second Repeat loop
        if RecordValidationAndAddition(TaxRateToBeAdded, TaxRateRecord== 'InvalidEntry'
print( "ERROR
INVALID
TAX
RATE: INVALID
INTEGER
ENTRY")
print( "Please
input
a
valid
tax
rate, using
an
integer
without
a
percentage
sign:")
input(TaxRateToBeAdded)

Until(RecordValidationAndAdded(TaxRateToBeAdded, TaxRateRecord) == 'Complete')

End
Module
 
Module: Display_Financial_Superannuation(SuperRecord, EmployeeID)
LoopCalculator = RecordLengthCalculator(SuperRecord)
LoopCounter = 0
SuperprintStringBegin =  " | Superannuation
Rates: "
SuperprintString =  ""
Header( "Interactive: Clerk",  "Superannuation
Adjustment")
Repeat
SuperprintString =  "[" + LoopCounter +  "]" +  "$" + SuperRecord[LoopCounter]
LoopCounter = LoopCounter + 1
Until(LoopCounter==LoopCalculator)
print( " | ")
print( " | " + SuperprintStringBegin + SuperprintStringEnd)
print( " | ")
print( " | Delete
Superannuation
Rate: // using
options
1, 2, 3
etc.")
input(SuperToBeDeleted)
print( " | ")
print( " | Add
Superannuation: // using
number
without
percentage
tag")
input(SuperToBeAdded)
print( " | ")
Footer(Display_FinancialOptions(EmployeeID))
 if
Footer(Display_FinancialOptions(EmployeeID)) == 'C'
Repeat
 if
RecordValidationAndDeletion(SuperToBeDeleted, SuperRecord== 'InvalidEntry'
print( "ERROR
INVALID
SUPERANNUATION
RATE: NOT
ON
RECORD")
print( "Please
input
a
valid
superannuation
rate
to
be
deleted:")
input(SuperToBeDeleted)

Until(RecordValidationAndDeletion(SuperToBeDeleted, SuperRecord) == 'Complete')
Repeat
 if
RecordValidationAndAddition(SuperToBeAdded, SuperRecord== 'InvalidEntry'
print( "ERROR
INVALID
SUPERANNUATION: INVALID
INTEGER
ENTRY")
print( "Please
input
a
valid
superannuation
rate, using
an
integer
without
a
percentage
sign:")
input(SuperToBeAdded)

Until(RecordValidationAndAdded(SuperToBeAdded, SuperRecord) == 'Complete')

End
Module
 
Module: Display_Financial_HealthInsurance(HealthInsuranceRecord, EmployeeID)
LoopCalculator = RecordLengthCalculator(HealthInsuranceRecord)
LoopCounter = 0
HealthInsuranceprintStringBegin =  " | Health
Insurance
Deductions: "
HealthInsuranceprintString =  ""
Header( "Interactive: Clerk",  "Health
Insurance
Adjustment")
Repeat
HealthInsuranceprintString =  "[" + LoopCounter +  "]" +  "$" HealthInsuranceRecord[LoopCounter]
LoopCounter = LoopCounter + 1
Until(LoopCounter==LoopCalculator)
print( " | ")
print( " | " + HealthInsuranceprintStringBegin + HealthInsuranceprintStringEnd)
print( " | ")
print( " | Delete
Health
Insurance
Plan: // using
options
1, 2, etc.")
input(HealthInsuranceToBeDeleted)
print( " | ")
print( " | Add
Health
Insurance
Plan: // using
the
price")
input(HealthInsuranceToBeAdded)
print( " | ")
Footer(Display_FinancialOptions(EmployeeID))
 if
Footer(Display_FinancialOptions(EmployeeID)) == 'C'
Repeat
 if
RecordValidationAndDeletion(HealthInsuranceToBeDeleted, HealthInsuranceRecord== 'InvalidEntry'
print( "ERROR
INVALID
HEALTH
CARE
PLAN: NOT
ON
RECORD")
print( "Please
input
a
valid
health
care
plan
to
be
deleted:")
input(HealthInsuranceToBeDeleted)

Until(RecordValidationAndDeletion(HealthInsuranceToBeDeleted, HealthInsuranceRecord) == 'Complete')
Repeat
 if
RecordValidationAndAddition(HealthInsuranceToBeAdded, HealthInsuranceRecord== 'InvalidEntry'
print( "ERROR: INVALID
HEALTH
CARE
PLAN: INVALID
INTEGER
ENTRY")
print( "Please
input
a
valid
health
care
plan, inputting
the
cost:")
input(HealthInsuranceToBeAdded)

Until(RecordValidationAndAdded(HealthInsuranceToBeAdded, HealthInsuranceRecord) == 'Complete')

End
Module
 
Module: Display_Financial_PayRates(RolePaymentRecord, RoleNameRecord, EmployeeID)
LoopCalculator = RecordLengthCalculator(RolePaymentRecord)
LoopCounter = 0
RolePaymentprintStringBegin =  " | Pay
rates: "
HealthInsuranceprintString =  ""
Header( "Interactive: Clerk",  "Pay
Rates
Adjustment")
Repeat
PayRateprintString =  "[" + LoopCounter +  "]" + RoleNameRecord[LoopCounter] +  "(
    $" + PayRateRecord[LoopCounter] +  " / hour)"
LoopCounter = LoopCounter + 1
Until(LoopCounter==LoopCalculator)
print( " | ")
print( " | " + PayRateprintStringBegin + PayRateprintStringEnd)
print( " | ")
print( " | Delete
Pay
Rate: // using
options
1, 2, etc.")
input(PayRateToBeDeleted)
print( " | ")
print( " | Add
Role: // Enter
the
name")
input(RoleToBeAdded)
print( " | ")
print( " | Add
Pay
Rate: // Enter
the
hourly
rate as an
integer")
input(PayRateToBeAdded)
print( " | ")
Footer(Display_FinancialOptions(EmployeeID))
 if
Footer(Display_FinancialOptions(EmployeeID)) == 'C'
Repeat
 if
RecordValidationAndDeletion(PayRateToBeDeleted, PayRateRecord== 'InvalidEntry'
print( "ERROR
INVALID
PAY
RATE: NOT
ON
RECORD")
print( "Please
input
a
valid
pay
rate
to
be
deleted:")
input(PayRateToBeDeleted)

Until(RecordValidationAndDeletion(PayRateToBeDeleted, PayRateRecord) == 'Complete')
Repeat
 if
RecordValidationAndAddition(PayRateToBeAdded, PayRateRecord== 'InvalidEntry'
print( "ERROR: INVALID
ROLE
PAY: INVALID
INTEGER
ENTRY")
print( "Please
input
a
valid
payment, inputting
the
hourly
rate:")
input(PayRateToBeAdded)

Until(RecordValidationAndAdded(PayRateToBeAdded, PayRateRecord) == 'Complete')
Repeat
 if
RecordValidationAndAddition(RoleToBeAdded, RoleNameRecord== 'InvalidEntry'
print(ERROR: VALIDATION
AND
ADDITION
OF
PAY
ERROR)
Until
RecordValidationAndAddition(RoleToBeAdded, RoleNameRecord== 'Complete'

End

 
 : Display_EmployeePaymentScreen(EmployeeID, EmployeeFileArray, EmployeeRecord)
CorrectEmployeeRecord = FindCurrentEmployee(EmployeeID)
EmployeeName = CorrectEmployeeRecord[2]
EmployeeSurname = CorrectEmployeeRecord[3]
Role = CorrectEmployeeRecord[4]
HourlyPay = CorrectEmployeeRecord[5]
DescriptiveIntroduction =  "Employee" + EmployeeName + EmployeeID
HoursWorked = CalculateHoursWorked(CorrectEmployeeRecord[12], CorrectEmployeeRecord[13], CorrectEmployeeRecord[14],
                                   CorrectEmployee
Record[15], CorrectEmployeeRecord[16], CorrectEmployeeRecord[17], CorrectEmployeeRecord[18])
BasePay = CalculateBasePay(CorrectEmployeeRecord[12], CorrectEmployeeRecord[13], CorrectEmployeeRecord[14],
                           CorrectEmployee
Record[15], CorrectEmployeeRecord[16], CorrectEmployeeRecord[17], CorrectEmployeeRecord[18], HourlyPay)
PublicHolidayOvertimeHours =   OvertimeCalculator(CorrectEmployeeRecord[12])
WeekOvertimeHours = WeekOvertimeCalculator(CorrectEmployeeRecord[12], CorrectEmployeeRecord[13],
                                           CorrectEmployeeRecord[14], CorrectEmployee
Record[15], CorrectEmployeeRecord[16], CorrectEmployeeRecord[17], CorrectEmployeeRecord[18])
SaturdayOvertime = OvertimeCalculator(CorrectEmployeeRecord[17])
SundayOvertime = OvertimeCalculator(CorrectEmployeeRecord[18])
OvertimePay = CalculateOvertimePay(CorrectEmployeeRecord[12], CorrectEmployeeRecord[13], CorrectEmployeeRecord[14],
                                   CorrectEmployee
Record[15], CorrectEmployeeRecord[16], CorrectEmployeeRecord[17], CorrectEmployeeRecord[18], HourlyPay)
PublicHolidayPay = CalculatePublicHolidayPay(CorrectEmployeeRecord[12], HourlyPay)
GrossPay = CalculateTotalPay(BasePay, OvertimePay, PublicHolidayPay, CorrectEmployeeRecord[12])
Tax = CalculateTax(GrossPay, Role)
NetPay = CalculateNetPay(GrossPay, Tax)
Header( "Interactive: Clerk", DescriptiveIntroduction)
print(" | ")
print(" | Employee Given name:" + EmployeeName)
print(" | ")
print(" | Employee surname:" + EmployeeSurname)
print(" | ")
print(" | Role: " + Role)
print(" | Hourly rate: " + Role)
print(" | ")
print(" | Monday: " + CorrectEmployeeRecord[12])
print(" | Tuesday: " + CorrectEmployeeRecord[13])
print(" | Wednesday: " + CorrectEmployeeRecord[14])
print(" | Thursday: " + CorrectEmployeeRecord[15])
print(" | Friday: " + CorrectEmployeeRecord[16])
print(" | Saturday: " + CorrectEmployeeRecord[17])
print(" | Sunday: " + CorrectEmployeeRecord[18])
print(" | Public holiday hours: " + CorrectEmployeeRecord[12])
print(" | Public holiday overtime hours: " + PublicHolidayOvertimeHours)
print(" | Overtime hours:" + WeekOvertimeCalculator)
print(" | Saturday overtime hours:" + SaturdayOvertime)
print(" | Sunday overtime hours:" + SundayOvertime)
print(" | ")
print(" | Total hours worked:" + HoursWorked)
print(" | ")
print(" | Base pay:" + BasePay)
print(" | Overtime pay:" + OvertimePay)
print(" | Public holiday pay:" + PublicHolidayPay)
print(" | ")
print(" | Gross pay:" + GrossPay)
print(" | Superannuation deduction:" + CorrectEmployeeRecord[6])
print(" | Health insurance deduction:" + CorrectEmployeeRecord[7])
print(" | Tax:" + Tax)
print(" | ")
print(" | Net pay:" + NetPay)
print(" | ")
Footer(Display_Navigation())
 if Footer(Display_Navigation()) == 'C'
Display_Navigation()

End

 
 : Display_TestMode(FileToBeRead)
DataRecord = []
ReadIn
FileToBeRead
to
DataRecord
SortData(DataRecord)
StoreData(DataRecord)
CalculateAndprint(DataRecord)
print(" | ")
print(" | Thankyou for using the test mode.")
print(" | ")



######################################################################################################################################################
#                                                                       BODY                                                                         #
######################################################################################################################################################

Display_Navigation()

