#This program is menu driven and preforms different expressions.
# Taylor J. Brown
# 16AUG21
# M1HW


def main():
    keep_going = 0
    
    while keep_going == 0:
        print("Welcome to the calculator program.")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Mulitiply")
        print("5. Exit")
        usr_choice = int(input("Enter a number: "))

        if usr_choice == 1:
            add()
        elif usr_choice == 2:
            sub()
        elif usr_choice == 3:
            div()
        elif usr_choice == 4:
            multi()
        elif usr_choice == 5:
            print("Goodbye.")
            keep_going += 1
        else:
            print("Please choose a valid option!\n")

def add():
    keep_going = 0
    
    while keep_going == 0:
        validation = 0
        print("\nAdd")
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        z = x + y  
        print(x, '+', y, '=', z)
            
        keep_going = rep(validation)
          
def sub():
    keep_going = 0
    
    while keep_going == 0:
        validation = 0
        print("\nSubtract")
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        z = x - y
        print(x, '-', y, '=', z)
        
        keep_going = rep(validation)
            
def div():
    keep_going = 0
    
    while keep_going == 0:
        validation = 0
        print("\nDivide")
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        z = x / y
        print(x, '/', y, '=', z)
        
        keep_going = rep(validation)
            
def multi():
    keep_going = 0
    
    while keep_going == 0:
        validation = 0
        print("\nMultiply")
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        z = x * y
        print(x, '*', y, '=', z)
        
        keep_going = rep(validation)
                
def rep(validation):
    while validation == 0:
        print("1. Repeat")
        print("2. Main Menu")
        usr_choice = int(input("Enter a number: "))
        
        if usr_choice == 1:
            validation += 1
            return (0)
        elif usr_choice == 2:
            validation += 1
            return (1)
        else:
            print('Please choose a valid option!\n')
         
main()