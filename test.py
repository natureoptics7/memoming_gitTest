

import matplotlib.pyplot as plt

a = 3
b = 1
a+b
print(" ========== start start start start start ========== ")

# str1 = "\n\n\n Hello world \n\n\n"
# myList= [1,2,3,4,5,6,0,0,0]
# print(str1)
# print(str1.strip())

# str()  : from number to str
# int()  : from str to number
# float()
# len    : length of str or number

# A = "1"
# B = int(A) + 1
# print(B)

# open - > close

# C = len(myList)
# print(C)

# print(type(contents))             # checking the type of the object

# # reading txt file using the "open"     ----------------------------------------
# fileStream = open("lab002.txt")     # open the fileStream
# contents = fileStream.read()
# print(contents)
# fileStream.close()                  # close the fileStream

# print(type(contents))
# --------------------------------------------------------------------------------


# # reading string by string
# fileStream = open("lab002.txt")     # open the fileStream
# contents = fileStream.readline()    # one string
# print(contents)

# c2 = fileStream.readline()
# print(c2)

# fileStream.close()                  # close the fileStream


# # reading several strings
# fileStream = open("lab002.txt")     # open the fileStream
# c1 = fileStream.readlines()         # make list with reading string by string
# print(c1[3].strip())

# print(len(c1)

# fileStream.close()                  # close the fileStream
# --------------------------------------------------------------------------------

# A = [1,2,3,4,5,6,7,8,9,10]
# B = "We are going to stury for rougth"
# for i in B :
#     print(i)

# --------------------------------------------------------------------------------

# # Let's study range(a,b,c)
# A = range(1,11,2)
# for i in A :
#     print(i)

# # example 1
# example_file = open('lab001.txt')
# text = example_file.readline()
# test = text.strip()
# print(int(text)+1)
# example_file.close()

# # example 2
# example_file = open('lab003.txt')
# rlt = 0
# numList = example_file.readlines()

# for str_number in numList:
#     rlt = rlt + int(str_number)
# print(rlt)

# --------------------------------------------------------------------------------

# value = 4
# if (value == 1) :
#     print("one")
# elif (value == 2) :
#     print("two")
# else :
#     print("three")


# # Let's study while
# i = 1
# while(True) :
#     print(i)
#     i = i+2
#     if (i==11) :
#         break


# myDict = {
#   "id" : "memoming",
#   "no" : 4
# }

# print(myDict["id"])
# print(myDict["no"])
# print(type(myDict["id"]))


############### set #################
# myList = [1,2,2,3,3,10, 10, 3,5,8,8,5,5,5,5]
# mySet = set(myList)
# print(mySet)


############### list #################
# test_list = ["a","b","c"]
# print(test_list[-1])
# print(test_list[-2])
# print(test_list[-3])


# ############### makeing and elediting the list #################
# A = [1,2,3,4,5,2,5]
# print(A[-1])

# B = list()
# B.append("one")
# B.append("2")
# print(B)

# A.append(5)

# A[4]=-1
# print(A)

# A.remove(5)       # Remove from the beginning of list
# print(A)

# print (A.index(1))

# A.sort()
# print(A)


# # list index error
# A = [1,5,7,6,10]
# input_numb = 4
# if (input_numb in A):
#     print(A.index(input_numb))
# else :
#     print("there is no requested number")

# A.insert(5,"d")
# print(A)
# print(A.count(5))

# A = [7,7,2,6,3,2,7]
# print(A.count(7))     # count how many "5" is in the list

# ######### Using the list sliding
# A = [1,2,3,4,5,6,7,8]
# B = A[0:5:2]
# print(B)

print(" ========== end end end end end ========== ")


# A = [1,2,3,4,5,6,7,8,9,10]
# B = "We are going to stury for rougth"
# for i in B :
#     print(i)

# example 3
T_list = open("poketmon_data.txt")
T_index = open("poketmon_index.txt")

Tlist = T_list.readlines()
Tindex = T_index.readlines()
print(Tindex[2])

print(len(Tlist))
print(len(Tindex))
# for i in Tindex:
#     print(i)

sum=[0]
for i in range(0,len(Tindex)-1):
    sum.append(0)
 
print(sum)

for j in range(0,len(Tindex)):
    for i in range(0,len(Tlist)):
        if Tindex[j] == Tlist[i]:
            sum[j]=sum[j]+1

print(sum)

for i in range(0,len(sum)):
    print(Tlist[i],":",sum[i])


# # with teacher
# T_list = open("poketmon_data.txt")
# T_index = open("poketmon_index.txt")

# Tlist = T_list.readlines()
# Tindex = T_index.readlines()
# name_list=list()
# for i in Tindex:
#     name_list.append(i.strip())
# print(name_list)



# # for str_number in numList:
# #     rlt = rlt + int(str_number)
# # print(rlt)

# # T_list.close()
# T_index.close()

# # print(type(contents))