# Jacob Vicsik
# GPATester.py
# Takes name and GPA inputs, printing certain outputs in response to GPA. 
lastname = input("Please enter your surname.")
if lastname != "ZZZ":
  firstname = input("Please enter your first name.")
  gpa = input("Please enter your GPA.")
  gpa = float(gpa)
  if gpa >= 3.25:
    print("You have made the Honor Roll.")
  if gpa >= 3.5:
    print("You have made the Dean's List.")
else:
  print("Records processing terminated.")
  