try : 
    number = int(input("Enter a number : "))
    variable = 10/0 
except ZeroDivisionError as e: 
    print("You got an error ->",e)
except ValueError as error_message : 
    print("Invalid form of input",error_message)
except : 
    print("Invalid syntax")