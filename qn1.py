#a company decided to give bonus of 1000rs to employe if his/her service is more than 
#5 years ask user their salary and year of service and print the net bonus amount

a = int(input("Enter your salary here:"))
b = int(input("Enter your year of service: "))

if b>5 :
    print("The net bonus amount: ",a+1000)

else:
    print("No bonus recived")
