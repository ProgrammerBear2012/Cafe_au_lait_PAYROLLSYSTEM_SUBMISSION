from random import randint

EmployeeLoginDetails = [['1', 'Billy', 'Bob', 'EmployeePass123'], ['2', 'Timmy', 'Tom', 'EmployeePass456'],
                        ['3', 'Charlie', 'Chaplin', 'ClerkPass432'], ['4', 'Telina', 'Swarez', 'ManagerPass123']]

def ArrayLengthCalculator(array):
    length = 0
    for entities in array:
        length = length + 1
    return length
    # end for
# end def

def GenerateEmployeePass(EmployeeLoginArray, Role):
    arrayLength = ArrayLengthCalculator(EmployeeLoginArray)
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
#
# role = 'Clerk'
# print("Works")
# EmployeePass = GenerateEmployeePass(EmployeeLoginDetails, role)
# print(EmployeePass)
# print("YIKES")
#
# num = 8.1
# numInt = int(num)
# print(num)
# print(numInt)

taxArray = [30, 40, 20]


# print(CalculateTax(23462.32, 40, taxArray))

def DoesItReTurnFalse():
    string = "HelloTHEREE"
    if string.isnumeric() == False:
        return False
    else:
        return True

DoesItReTurnFalse()


loopCounter = 1
HealthInsuranceprintString = ''

for taxes in taxArray:
    HealthInsuranceprintString = HealthInsuranceprintString + "[" + str(loopCounter) + "]" + "$" + str(taxArray[loopCounter-1]) + ", "
    loopCounter = loopCounter + 1

print(HealthInsuranceprintString)