# DataMan - CTS-285
# Taylor J. Brown
# 11OCT21

"""
Sprint 1 -     
Main Menu:
-----------
    Placeholder functions and a menu displayed with working paths.
    
Basic Calculator:
------------------
    The calculator works with the operands"+, -, /, *" and passes the entered 
    equation through an if-elif-else structure then displays the answer to 
    the entered equation using the choosen operand entered.
"""

def main():
    keep_going = True
    
    while keep_going == True:
        print("\n","_"*7,"MENU","_"*7,"\n1. Normal Calculator\n2. Answer Checker\
              \n3. Memory Bank\n4. Number Guesser\n5. Exit", sep='')
        usr_inp = input("Please Enter choice: ")
        
        if usr_inp == "1":
            reg_cal() 
        elif usr_inp == "2":
            ans_chker()
        elif usr_inp == "3":
            mem_bank()
        elif usr_inp == "4":
            num_gesr()
        elif usr_inp == "5":
            print("Goodbye")
            keep_going = False
        else:
            print("Please choose a valid option")
            
def reg_cal():
    """
    - Determines the type of equation entered by the operand seperating
        the two numbers entered.
    - Delete the operator from the string.
    - Split the equation into a list.
    - Preform appropriate process to equation and then display results.
    """
    
    print("\nNormal Calculator-")
    keep_going = True
    
    while keep_going == True:
        split_equate = []
        equate = input("Enter an equation or enter exit: ")
    
    #Addition
        if "+" in equate:
          split_equate = equate.split("+")
          x = int(split_equate[0])
          y = int(split_equate[1])
          z = x + y
          print(x,"+",y,"=",z)
        
    #Subtraction
        elif "-" in equate:
          split_equate = equate.split("-")
          x = int(split_equate[0])
          y = int(split_equate[1])
          z = x - y
          print(x,"-",y,"=",z)
         
    #Division  
        elif "/" in equate:
          split_equate = equate.split("/")
          x = int(split_equate[0])
          y = int(split_equate[1])
          try:
              z = x / y
              print(x,"/",y,"=",z)
          except ZeroDivisionError:
              print("You cannot divide by zero!")
              
    #Multiplication
        elif "*" in equate:
          split_equate = equate.split("*")
          x = int(split_equate[0])
          y = int(split_equate[1])
          z = x * y
          print(x,"*",y,"=",z)
          
        elif equate == "exit" or "quit":
            keep_going = False
        else:
            print("That is not a valid equation.")

def ans_chker():
    print("Answer Checker")

def mem_bank():
    print("Memory Bank")

def num_gesr():
    print("Number Guesser")

if __name__ == "__main__":
    main()