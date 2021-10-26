# DataMan - CTS-285
# Taylor J. Brown
# 11OCT21

"""
_______________________________________________________________________________
______Sprint 1______ 
-New Content-
   
Main Menu:
-----------
    Placeholder functions and a menu displayed with working paths.

Basic Calculator:
------------------
    The calculator works with the operands"+, -, /, *" and passes the entered 
    equation through an if-elif-else structure then displays the answer to 
    the entered equation using the choosen operand entered.
_______________________________________________________________________________
______Sprint 2______
Basic Calculator
-----------------
    refactored this function, the processing component to a new function named 
    calculator_core. Now sends the string to the function and recives a tuple 
    to unpack and display.

-New Content-
Answer Checker
----------------
    "User made questions" where the user inputs ten equations and 
     then is asked to solve them. At the end the user is prompted with how many
     correct and incorrect answers out of ten.
_______________________________________________________________________________
______Sprint 3______
Answer Checker
----------------
    refactored this function to be utilized by memory bank function and to 
    shorten the overall length of the program.

    - Now asks the user how many equations they would like to enter before 
      asking them to enter equations.

-New Content-
Memory Bank
----------------
    -"Ten random questions" where the user will be prompted with ten random 
     question and they will have 3 chances to get it right before the answer 
     is given, at the end of the ten questions the user will get his/her score
     out of ten.

    - Only uses addition, subtraction, and multiplication. The reasoon for that 
      is that divition problems have decimal places and arent easily verified 
      by the program.

    - Asks the user how many questions they would like to be asked for this 
      specific game mode.
_______________________________________________________________________________
______Sprint 4______
-New Content-
Number Guesser
---------------
    The user is asked to guess a number between 1-100 and each time the user 
    enters a number it will check against the secret number and tell them 
    higher or lower. When they get the correct answer they will be 
    congradulated and then sent back to the main menu.
_______________________________________________________________________________
"""

import random

def main():
    """ Basic menu to send the user to other functions. """
    keep_going = True
    
    while keep_going == True:
        print("\n","_"*7,"MENU","_"*7,"\n1. Normal Calculator\n2. Answer Checker\
              \n3. Memory Bank\n4. Number Guesser\n5. Exit", sep='')
        usr_inp = input("Please Enter choice: ")
        
        if usr_inp == "1":
            regular_calculator()
        elif usr_inp == "2":
            answer_checker()
        elif usr_inp == "3":
            memory_bank()
        elif usr_inp == "4":
            number_guesser()
        elif usr_inp == "5":
            print("Goodbye")
            keep_going = False
        else:
            print("Please choose a valid option")
            
def regular_calculator():
    """
    - Gathers equation information and sends it to the calculator_core function.
    - Gets decoded answer back and splits the list apart.
    - If the list length is not greater than 0 the function aborts.
    - Prints out the solved equation.
    """
    print("\nNormal Calculator-")
    keep_going = True
    
    while keep_going == True:
        equate = input("Enter an equation or enter exit: ")
        val_print = calculator_core(equate)
        if len(val_print) > 0:
            x,y,z = val_print[0],val_print[1],val_print[2]
            operator = val_print[3]
            print(x, operator, y, "=", z)
        else:
            break

def answer_checker():
    """ 
    - Asks the user how many equations they would like to enter
    - Iterates through a for loop to take user equations and sends them to the calculator_core
      function and send them back
    - Returned equations are seperated and appended to lists(equation_list and answer_list)
    - Sends both new lists to memory_answer_core function and asks the user to asnwer the questions.
    """
    print("Answer Checker")
    equation_list, answer_list = [],[]

    c = int(input("How many questions would you like to input?"))
    print("Format Example: Number1+Number2")
    for _ in range(c):
        x = input("Enter equation/s here > ")
        equation_list.append(x)
        answer = calculator_core(x)
        answer_list.append(answer[2])

    memory_answer_core(equation_list,answer_list,c)    
    
def memory_bank():
    """
    - Asks the user how many questions they want to be asked 
    - The program will automatically generate the first and second number and choose between 
      multiplication, subtraction or addition.
    - Then the program sends the generated equations to the memory_answer_core function and 
      asks the user to asnwer the questions.
    """
    print("Memory Bank")
    int_range = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    equation_list, answer_list, x, y, o = [],[],[],[],[]
    c = int(input("How many questions would you like to be asked?"))
    
    for count in range(c):
        # First variable
        i = random.randint(0,12)
        k = int_range[i]
        x.append(k)
        
        # Operator
        operators = ['+','-','*']
        i = random.randint(0,2)
        k = operators[i]
        o.append(k)                
        
        # Second variable
        i = random.randint(0,12)
        k = int_range[i]
        y.append(k)                    

        # Setting up equations & Getting an answer list to check against
        i = ''.join([x[count],o[count],y[count]])
        answer = calculator_core(i)
        answer_list.append(answer[2])
        equation_list.append(i)
    
    memory_answer_core(equation_list,answer_list,c)

def number_guesser():
    """
    - Ask the user to guess a number between 1-100
    - If the user guesses the correct number congradulate them and send back to menu
    - If the user guesses a number lower than the secret number tell them and let them guess again
    - If the user guesses a number higher than the secret number tell them and let them guess again 
    """
    keep_going = True
    print("Number Guesser")
    SECRET_NUMBER = random.randint(1,100)
    print("Please guess a number between 1-100")

    while keep_going == True:
        usr_inp = input("> ")
        try:
            usr_inp = int(usr_inp)
            if usr_inp == SECRET_NUMBER:
                print("That is the correct guess! Good Job!")
                keep_going = False
            elif usr_inp > SECRET_NUMBER:
                print("That guess is too high. Please try again")
            elif usr_inp < SECRET_NUMBER:
                print("That guess is too low. Please try again")
        except:
            print("Please enter a vaild integer")

def memory_answer_core(equation_list,answer_list,c):
    """
    - Takes in three arguments and iterates through them and calculates the correct and incorrect 
      counts then displays them.
    """
    equation_list = equation_list
    answer_list = answer_list
    index, count, correct, incorrect = 0,0,0,0

    while len(answer_list) > 0:            
        while len(answer_list) > 0:
            print(equation_list[index],"= ?")
            i = int(input("Answer: "))
                
            if i == answer_list[0]:
                print("That is correct!")
                correct += 1
                index += 1
                del answer_list[0]
                break
            elif count == 2:
                print("Sorry but the answer was:", answer_list[0],"\n")
                incorrect += 1
                count = 0
                index += 1
                del answer_list[0]
            elif i != answer_list[0]:
                print("Sorry that was incorrect")
                count += 1
                
    print("\nYou got", correct, "correct and", incorrect, "incorrect out of", c)
    return
    
def calculator_core(equate):
    """
     - Determines the type of equation entered by the operand seperating
         the two numbers entered.
     - Delete the operator from the string.
     - Split the equation into a list.
     - Preform appropriate process to equation and then return the results 
         in a tuple.
    """
    split_equate, return_L = [],[]
    
# Addition
    if "+" in equate:
      split_equate = equate.split("+")
      x = int(split_equate[0])
      y = int(split_equate[1])
      z = x + y
      return_L.extend((x,y,z))
      return_L.append("+")
      return return_L
      
# Subtraction
    elif "-" in equate:
      split_equate = equate.split("-")
      x = int(split_equate[0])
      y = int(split_equate[1])
      z = x - y
      return_L.extend((x,y,z))
      return_L.append("-")
      return return_L
        
# Division  
    elif "/" in equate:
      split_equate = equate.split("/")
      x = int(split_equate[0])
      y = int(split_equate[1])
      try:
          z = x / y
          return_L.extend((x,y,z))
          return_L.append("/")
          return return_L
      except ZeroDivisionError:
          print("You cannot divide by zero!")
      return
    
# Multiplication
    elif "*" in equate:
      split_equate = equate.split("*")
      x = int(split_equate[0])
      y = int(split_equate[1])
      z = x * y
      return_L.extend((x,y,z))
      return_L.append("*")
      return return_L
      
    elif equate == "exit" or "quit":
       return return_L
    else:
        print("That is not a valid equation.")

if __name__ == "__main__":
    main()