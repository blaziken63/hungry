thirst=input("are you thirsty?")
# Error line--> if thirst=='yes' and thirst=='y' and thirst=='Y':
# Resolved
if thirst=='yes' or thirst=='y' or thirst=='Y':
  print("drink water")
else:
  print("continue your homework")
