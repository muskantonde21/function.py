# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].

# def even():
#     a=[1,2,3,4,5,6,7,8,9]
#     k=[]
#     for i in a:
#         if i%2==0:
#             k.append(i)
#     print(k)
# even()



# Q45. Draw a flowchart to Take 10 numbers as input and 
# create a list of the numbers from the user and update 
# each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
# Sample Input:23,42 ,41 , 1
# Sample Output: -23 , 4200 ,-41 ,-1


def  mul():
    a=[12,23,25,67,33]
    even=[]
    odd=[]
    i=0
    while i<len(a):
        if i%2==0:
            even.append(a[i]*100)
        else:
            odd.append(a[i]*-1)
        i+=1
    # print(even)
    # print(odd)
    even.extend(odd)
    print(even)
mul()

# def mul():
#     a=[23,42,41,1]
#     k=[]
#     for i in a:
#         if i%2==0:
#             k.append(i*100)
#         else:
#             k.append(i*-1)
#     print(k)
# mul()
