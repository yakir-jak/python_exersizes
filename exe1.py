f_name = "Yakir"
l_name = "Bar Siman Tov"

print('Hello ! My Nme Is' , f_name , l_name)

num1 = float(input('Enter a Number :'))
num2 = float(input('Great ! Now Enter The Seconed One :'))

print('Your Nubers Are :', num1 , num2 ,)

if num1 > num2:
    print(num1 ,"Is Bigger")
elif num1 < num2:
    print(num2 , "Is Bigger")
else:   print(num1 , "And" , num2 , "Are Equal")


print('Now Lets Do Some Math :::::::::::::::')

op = input("Enter Operator +  ,  - ,  / ,  *  :")

if  op == '+':
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)

else:   print("Invalid Operator !")