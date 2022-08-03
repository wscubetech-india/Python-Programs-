#Quadratic Equation ax**2 + b*x + c = 0
#a, b and c are real numbers
#a!= 0
import cmath

a = int(input("enter number (a!=0): "))
b = int(input("enter number: "))
c = int(input("enter number: "))

#Find discriminants
d = (b**2)-(4*a*c)

#Find the Solutions(roots)
sol1 = ((-b-cmath.sqrt(d))/(2*a))
sol2 = ((-b+cmath.sqrt(d))/(2*a))

print ("the roots are: ",sol1,sol2)




