year=int(input("enter the year :"))
if (year%4==0):
   print("the given year is leap year ")
elif (year%4==0 and year%100!=0):
   print("the given year is leap year")
else:
   print("the given year is not a leap year")
