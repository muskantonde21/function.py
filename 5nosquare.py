# Write a Python program to generate and print a list of 
# first and last 5 elements where 
#the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

# def square():
#     l=[]
#     for i in range(0,31):
#         l.append(i**2)
#     print(l[:5],l[-5:])
# square()


# Write a function For example, if we give 9119 
#  the function should return  811181, as the  square of 9 is 81 
# and square of 1  is 1.

a=1981
b=str(a)
i=0
while i<len(b):
    print(int(b[i])**2,end="")
    i=i+1



    