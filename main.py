from questionbank import pythonquestionbank as questionbank
from options import pythonoptions as options
from explaination import pythonexplaination as explaination
from time import sleep
from os import system

score=0

for i in range(9,-2,-1):
  #print("*****************************************")
  #print("Welcome to the Quiz")
  print("\n\n")

  print("                   Your quiz starts in",i+1,"s",end="")
  sleep(1)
  system("clear")

print("\n************************************************************")
print("                     Welcome to the Quiz")

print("\n\n")

for question in range(len(questionbank)):
  print("************************************************************")
  print(questionbank[question]["text"])
  
  for option in range(4):
    print(options[question][option])
  
  user_guess=input("\nYour Answer: ").upper()
  print()

  if user_guess==questionbank[question]["answer"]:
    print("Correct Answer")
    print(explaination[question])
    score+=1

  else:
    print("Incorrect Answer")
    print("Correct Answer is",questionbank[question]["answer"])
    print(explaination[question])

  print(f"\nYour current score is {score}/{len(questionbank)}")
  print()

print()
print(f"Your Final Score is {(score/len(questionbank))*100}%")