print("Medical Claim Program")

nameList = []
IdList = []
dateList = []
daysList = []
expenseList = []

while True:
    name = input("Please input your name: ")
    Id = input("Please input your student ID: ")
    date = input("Enter the date of MC: ")
    days = input("Enter the no. of MC days: ")
    expense = input("Enter the medical expenses amount: $")
   
    nameList.append(name)
    IdList.append(Id)
    dateList.append(date)
    daysList.append(days)
    expenseList.append(float(expense))  

    entry = input("Do you want to enter another entry (y/n): ")

    if ( entry == "n" ):
        break

Total = sum(expenseList)

print(f"Student name: {name}")
print(f"Student ID: {Id}")
print(f"Total medical expenses amount: ${Total:.2f}") 

