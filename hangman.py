hangman=["""  
         +---+  
             |
             |
             |
             |
         =========
    """,   """
       +---+
       |   |
           |
           |
           |
           |
       =========
    """,       """
       +---+
       |   |
       O   |
           |
           |
           |
       =========
    """,    """
       +---+
       |   |
       O   |
       |   |
           |
           |
       =========
    """,     r"""
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,      r"""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========
    """,       r"""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     =========
    """,       r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
     =========
    """  ]
import string
import random 
cozy_home=['door','window','sofa','kitchen','home','clock','flower','garden']
computer = random.choice(cozy_home)
spaces=["_"]*len(computer)
print("Hint: The word is about (Home Sweet Home)🏡" )
print(hangman[0])
tries = 6
repeated_Wrong_Answers = []
while "_" in spaces and tries > 0 :
    print(" ".join(spaces))
    print(f"You have {tries} tries")
    user=input("Please guess a letter : ").lower()
    if user not in computer :
        if user not in string.ascii_letters :
            print("\nJust letters please !!⚠️​\n ")
        elif user in repeated_Wrong_Answers :
            print("\nYou already guessed that . Try again\n")
        elif user not in repeated_Wrong_Answers :
            repeated_Wrong_Answers.append(user)
            tries -= 1
            print(hangman[6 - tries])  
    else :
     for x in range(len(computer)) :
        if computer[x] == user :
           spaces[x] = user    
print(" ".join(spaces))  
if "_" not in spaces :
  print("""
           *********
           You win !
           *********      """)
elif tries == 0 :
 print(f"You have {tries} tries")
 print(f""" 
            Game over
            You lose !
           {hangman[7]}
                             """)           