from random import randint

EmployeeLoginDetails = [['1', 'Billy', 'Bob', 'EmployeePass123'], ['2', 'Timmy', 'Tom', 'EmployeePass456'],
                        ['3', 'Charlie', 'Chaplin', 'ClerkPass432'], ['4', 'Telina', 'Swarez', 'ManagerPass123']]

def ArrayLengthCalculator(array):
    length = 1
    for entities in array:
        length = length + 1
    # end for
# end def

def GenerateEmployeePass(EmployeeLoginArray, Role):
    arrayLength = ArrayLengthCalculator(EmployeeLoginArray)
    validatePass = False
    validationCounter = 0
    employeePass = Role + "pass"
    endingNum = randint(100, 999)
    employeePass = employeePass + str(endingNum)
    while validatePass == False:
        for password in EmployeeLoginArray:
            if password[3] == employeePass:
                endingNum = randint(100, 999)
                employeePass = Role + "pass" + endingNum

            else:
                validationCounter = validationCounter + 1
            # end if
            if validationCounter == validation

    return employeePass
