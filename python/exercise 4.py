english = int(input("English: "))
if english  > 100 or english< 0:
    print("invalid number")

math = int(input("Math: "))
if math  > 100 or math <0:
    print("invalid number")

history = int(input("History: "))
if history  > 100 or history <0:
    print("invalid number")

geo = int(input("Geo: "))
if  geo >100 or geo < 0:
    print( "invalid number")

computer = int(input("Computer: "))

if computer >100 or computer < 0:
   print( "invalid number")


sum = english+ math + history + geo + computer
print(f"he total marks are{sum}")
average = sum/5
print(f"the average is {average}")

if average <= 39:
    print("E")
elif average >= 40 and average <= 59:
    print("D")
elif average >= 60 and average <= 69:
    print("C")
elif average >= 70 and average <= 79:
    print("B")
if average >= 80 and average <= 100:
    print("A")
else:
    print("invalid")

