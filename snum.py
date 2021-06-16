#python program to find smallest number among three numbers

#taking input from user
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: ")) 
num3 = int(input("Enter 3rd number: "))

if(num1 <= num2) and (num1 <= num3):
    snum = num1
elif(num2 <=num1) and (num2 <=num3):
    snum = num2
else:
    snum = num3

print("The smallest number among ", num1,",", num2,",", num3 ,"is :", snum)