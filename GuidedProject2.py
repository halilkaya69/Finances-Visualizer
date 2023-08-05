#Step 1 - Getting Inputs
print("--------------------------------")
print("----- FINANCIAL VISUALIZER -----")
print("--------------------------------")
salary=input("Annual Salary:\n")
housing=input("Monthly Housing:\n")
bills=input("Monthly Bills:\n")
food=input("Weekly Food:\n")
travel=input("Annual Travel:\n")

#Step 2 - Validating Inputs
valids=["1","2","3","4","5","6","7","8","9","0","."]
for i in salary:
    if i in valids:
        bool1= True
    else:
        bool1=False

for i in housing:
    if i in valids:
        bool2= True
    else:
        bool2=False

for i in bills:
    if i in valids:
        bool3= True
    else:
        bool3=False

for i in food:
    if i in valids:
        bool4= True
    else:
        bool4=False

for i in travel:
    if i in valids:
        bool5= True
    else:
        bool5=False


if bool1 and bool2 and bool3 and bool4 and bool5:
    salary=float(salary)
    housing=float(housing)
    bills=float(bills)
    food=float(food)
    travel=float(travel)
    print("All inputs confirmed valid.")
else:
    print("Invalid input, please try again.")

#Step 3 - Taxes

if salary>=0 and salary<=10000:
    tax=salary*0.05
    tax=round(tax,2)
elif salary>=10001 and salary<=40000:
    tax=salary*0.1
    tax=round(tax,2)
elif salary>=40001 and salary<=80000:
    tax=salary*0.15
    tax=round(tax,2)
else:
    tax=salary*0.2
    tax=round(tax,2)
    
print("Annual tax is ",tax)

#Step 4 - Calculations
annualHousing = housing * 12
annualBills = bills * 12
annualFood = food * 52
annualExtra = salary - annualHousing - annualBills - annualFood - travel - tax
percentageTax = (tax / salary) * 100
percentageHousing = (annualHousing / salary) * 100
percentageBills = (annualBills / salary) * 100
percentageFood = (annualFood / salary) * 100
percentageTravel = (travel / salary) * 100
percentageExtra = (annualExtra / salary) * 100

#Step 5 - Bar Chart
print("----------------------------------------------------------")
print(f'housing | ${round(annualHousing, 2)} | '+f'{round(percentageHousing, 1)}% | ' + "#" * int(percentageHousing))
print(f'bills   | ${round(annualBills, 2)} | '+f'{round(percentageBills, 1)}% | ' + "#" * int(percentageBills))
print(f'food    | ${round(annualFood, 2)} | '+f'{round(percentageFood, 1)}% | ' + "#" * int(percentageFood))
print(f'travel  | ${round(travel, 2)} | '+f'{round(percentageTravel, 1)}% | ' + "#" * int(percentageTravel))
print(f'tax     | ${round(tax, 2)} | '+f'{round(percentageTax, 1)}% | ' + "#" * int(percentageTax))
print(f'extra   | ${round(annualExtra, 2)} | '+f'{round(percentageExtra, 1)}% | ' + "#" * int(percentageExtra))
print("----------------------------------------------------------")
