# given list   print the list of elemnets and sum of them

# list1= [10,20,30,40,50,60]
# s= 0
# # print(list1)
# for i in list1:
#     s= s+i
# print(s)





n= int(input("Enter the length of list: "))
new_list= []
s= 0
for i in range(n):
    d= int(input("Enter the elements of the list: "))
    new_list.append(d)
    s= s+d
print(f"The sum of list is: {s}")

avg= s/n
print("Avg of given list is: ", avg)