'''
Made by: Fabrizio Alvarado Barquero.
Problem title: Hours format translation.
'''

#Global variables.
HOUR = 0
MINUTES = 0
PERIOD = ""
NUMBERS_LIST = [
    ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"],
    ["diez", "once", "doce", "trece", "catorce", "", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte"],
    ["veinte", "veintiuno", "veintidos", "veintitres", "veinticuatro", "veinticinco", "veintiseis", "veintisiete", "veintiocho", "veintinueve"],
    ["treinta", "treinta y uno", "treinta y dos", "treinta y tres", "treinta y cuatro", "treinta y cinco", "treinta y seis", "treinta y siete", "treinta y ocho", "treinta y nueve"],
    ["cuarenta", "cuarenta y uno", "cuarenta y dos", "cuarenta y tres", "cuarenta y cuatro", "cuarenta y cinco", "cuarenta y seis", "cuarenta y siete", "cuarenta y ocho", "cuarenta y nueve"],
    ["cincuenta", "cincuenta y uno", "cincuenta y dos", "cincuenta y tres", "cincuenta y cuatro", "cincuenta y cinco", "cincuenta y seis", "cincuenta y siete", "cincuenta y ocho", "cincuenta y nueve"],
    ]

#Functions section.
'''
Description: Checks if the given time is a valid one.
Parameters: The raw input.
'''
def checkInputFormat(rawInput):
    
    newInput = rawInput.replace(" ", "") #Delete all blank spaces.
    if(len(newInput) not in range(6, 8)): #Checks the lenght of the input string.
        return False
    
    try: #Use a try/except structure to avoid unexpected errors.
        
        global HOUR
        global MINUTES
        global PERIOD
        if(len(newInput) == 7): #Checks if the hour is 2 digits long.
            HOUR = int(newInput[:2])
            newInput = newInput[2:]
        else:
            HOUR = int(newInput[:1])
            newInput = newInput[1:]
        if(HOUR == 0): #Checks if the hour is a valid one.
            return False;
        if(newInput[0] != ":"): #Checks if the element is the correct one.
            return False
        newInput = newInput[1:]
        if(HOUR > 12 and hour < 1): #Checks if the hour is a valid number.
            return False
        MINUTES = int(newInput[:2])
        if(MINUTES > 59 and MINUTES < 0): #Checks if the minutes are a valid number.
            return False
        newInput = newInput[2:]
        PERIOD = newInput.lower()
        if(PERIOD != "am" and PERIOD != "pm"): #Checks if the period is valid.
            return False
    except:
        return False
    
    return True
    
'''
Description: Main function of the exercise, it translate a given time in numbers to words. 
Parameters: None.
'''
def numbersToWords():
    
    print("Hi :)")
    print("Please write the hour you want to translate and press ENTER.")
    print("NOTE: Please use this hour format -> [1-12]:[00-59][am/pm]")
    rawInput = input()
    
    if(not checkInputFormat(rawInput)): #Checks if the input has a good format.
        print("Hour format is not correct, please read the note above.")
        print("If you want to try again, just rerun the script.")
        exit(1)
    
    elif(rawInput == "12:00pm"): #Checks if it's noon.
        print("Es medio día.")
        exit(0)
        
    elif(rawInput == "12:00am"): #Checks if it's midnight.
        print("Es media noche.")
        exit(0)
    
    resultString = ""
    
    # Assign hour.
    if(HOUR == 1):
        resultString = "Son la 1"
    elif(HOUR >= 10):
        secondDigit = int((str(HOUR))[1])
        resultString = "Son las " + NUMBERS_LIST[1][secondDigit]
    else:
        resultString = "Son las " + NUMBERS_LIST[0][HOUR]
    
    # Assign minutes.
    if(MINUTES == 0):
        resultString += " en punto"
    elif(MINUTES == 15):
        resultString += " y cuarto"
    elif(MINUTES == 30):
        resultString += " y media"
    else:
        firstDigit = int((str(MINUTES))[0])
        secondDigit = int((str(MINUTES))[1])
        resultString += " y " + NUMBERS_LIST[firstDigit][secondDigit]
    
    # Assign period.
    if(PERIOD == "am" and HOUR in range(1, 13)):
        resultString += " de la mañana."
    elif(PERIOD == "pm" and (HOUR == 12 or HOUR in range(1, 6))):
        resultString += " de la tarde."    
    else:
        resultString += " de la noche."
    
    # Give the answer.
    print(resultString)
    exit(0)
    
numbersToWords()