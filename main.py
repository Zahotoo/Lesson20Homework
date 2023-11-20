# Homework
# Write a recursive program that calculation factorial for example:
# F(4)=4*3*2*1=24
# F(3)=3*2*1=6
# F(2)=2*1=2
# F(1)=1

# HINT: F(x) = x F(x-1) #This is how the recursion can happen

# THIS IS A HARD EXAMPLE, but the code is VERY SHORT, see if you can figure it out!!
n = int(input("Please give me a positive integer: "))

def factorial(n):
     if n == 1:   # The end condition: When n == 1, it ends.
         return 1
     elif n > 1:
         n = n * factorial(n-1)
         return n
     else:
         print("You type an ERROR number, Goodbye!")
         quit()

result = factorial(n)

print(result)

quit()