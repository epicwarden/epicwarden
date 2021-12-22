bill = input("what is the total of your bill? ")
tip = input("how much would you like to type 10% 12% 15% 18% ")
percent = ((float(tip)/100+1))
total_bill =(float(bill) * (float(percent)))
print(round(total_bill))
people = input("how many people to slipt he bill? ")
slipt =float(total_bill)/float(people)
to_pay = slipt
print(f"you will need to pay per person is £{round (to_pay,2)} ")