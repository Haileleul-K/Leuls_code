
import cmath
#1
x=float(input ("Enter the radius of a circle to calculate the area: "))
print ('Area = ', cmath.pi*x**2)

#2
x=float(input('Enter temperature in Fahrenheit: '))
print ('the temperature of the city in Centigrade degrees is ', 5/9 *(32-x))
#3 unfinished
x=float(input ("Enter a salary of mr.abebe "))

#4

x=input('Enter the first name: ')
y=input('Enter the second name: ')
print ("The reversed name is: ")
print (y+' '+x)

#5
r=6
v = 4/3*cmath.pi*r**3
print ('The volume of sphare with radius 6 is', v)

#6
n=int(input ("Enetr a number with 5 digits"))

if (n>=10000 and n<=99999):

    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n//10
    print ("The sum  of the digits is: ",sum)
else:
    print("Please enter a number with 5 digit")

#7
print("Enter two numbers!")
x=float (input())
y=float (input())

print ("press"
       " +  for addition"
       " -  for subtracton"
       " x  for multiplication"
       " /  for division  : ")
z=(input())
if (z=='+'):
    sum=x+y;
    print ("Sum= ",sum)

elif (z=='-'):
    sub=x-y;
    print ("Difference = ",sub)

elif (z== 'x' or 'X'):
    mul=x*y;
    print ("Product = ",mul)

elif(z=='/'):
    dif=x/y;
    print ("Quotient= ",dif)
else :
    print("You have put undefined symbol please check again")

#8


a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b ** 2) - (4 * a * c)



# find two results
root1 = (-b - cmath.sqrt(d)) / (2 * a)
root2 = (-b + cmath.sqrt(d)) / (2 * a)

# printing the results
print("The roots are: ")
print(root1)
print(root2)


#9
a=('Haileleul Kindie Alemayehu',23,'Injibara')
print ("My name  :", a[0])
print ("My age   :", a[1])
print ("My adress:", a[2])

#10

x=int (input('Enter a decimal number'))

binary=bin(x)
octal=oct(x)
hexa=hex(x)

print(binary, "in binary.")
print(octal, "in octal.")
print(hexa, "in hexadecimal.")


#11

n=1
sum=0
while (n<=25):
    sum += 1/n
    n+=3

print ('The sum is ',sum)

#12

n=2
sum=0

while(n<=20):
    sum+=n**3
    n+=2

print (sum)
''' 3.	Abebe’s basic salary is input through the keyboard. His dearness allowance is 40% of
basic salary, and house rent
allowance is 20% of basic salary.
Write a program to calculate his gross salary. 




bsal=float(input("Enter abebe's basic salary"))
dall=bsal*0.4
hrent=bsal*0.2
gsal=bsal+dall+hrent
print ("Gross salary for abebe is :",gsal)

def abe(x,y):
     print(x+y)'''
sum=0;

while(n!=0):
    sum=sum+(n%10);
    n=n//10;
