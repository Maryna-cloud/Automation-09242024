# #Loops, lists,strings
# #loops
# # 0+1+2+3+4+5+6+7+8+9+10
# total = 0
# for i in range(0,10):
#     total = total + i
#     print(f"total for each step is {total}")
#    # total += i
# print(f"the total is : {total}")
#
# #same with while loop
# total = 0
# i = 0
# while i<10 :
#     total = total + i
#     i += 1
#     print(f"total for each step is {total}")
# print(f"the total is : {total}")
#
# #for loop with increment = 2 in each iteration
# total = 0
# for i in range(0,11,2):
#     total = total + i
#     print(f"total for each step is {total}")
#    # total += i
# print(f"the total is : {total}")

#lists
# fruits = ["apple", "banana", "cherry"]
# mixed_list = ["apples", 2,"cherry", 4]
# print(fruits)
# print(fruits[0])
# fruits.append("potato")
# print(fruits)
# print(type(fruits))
#
# print (mixed_list)
# mixed_list.append("potato")
# print (mixed_list)
# mixed_list.remove("potato")
# print (mixed_list)
# mixed_list.remove("cherry")
# print (mixed_list)
#
# print ("*"*50)
# many_items = ["apple", "banana", "cherry",1,4,"top", 5,6,"bottom"]
# print(f"the length of the many_items list is {len(many_items)} ")
# print(many_items[len(many_items)-1])
# many_items.remove(many_items[len(many_items)-5])
# print(many_items )

# prices = [10,50,30,1,100,4]
# print(f"Max price is {max(prices)}")
# print(f"Min price is {min(prices)}")

print ("*"*50)
for i in range (1,6):
    if i == 3:
        print ("stop and break when i=3")
        break
    print (i)

print ("*"*50)
#There is the list of prices. We want to create another list with only even prices from original one
prices = [10,50,31,1,100,99,4,8,9,123,785]
even_prices =[]
odd_prices =[]

for item in prices:
    # if item ==99:
    #     break
    if item % 2 ==0:  # 101 %2 =1   100%2 =0
        even_prices.append(item)
    else:
        odd_prices.append(item)
    if item ==99:
        break
print(prices)
print(even_prices)
print(odd_prices)

# Reverse a string
print ("*"*50)

word = "Tomorrow is the Christmas eve"
rev_word = ""
for letter in word:
    rev_word = letter+ rev_word
    print(rev_word)

print(word)
print(rev_word)

len_word = len(word)
len_rev_word = len(rev_word)

if len_word == len_rev_word:
    print("We are on the right way!")
    print("we are on the right way!".lower())
    print("we are on the right way!".upper())

print("Christmas" in word )
print("Christmas" in rev_word)

each_word = word.split()
print (each_word)

print ("*"*50)
# *
# **
# ***
# ****
# *****
rows = 5
for i in range (1,rows+1):
    print("*"*i)

#       *
#      ***
#     *****
#    *******

rows = 10
for i in range (1,rows+1):
    print("." * (rows - i) + "*" *(2 * i - 1))

    #       *
    #      ***
    #     *****
    #    *******
    #       |

#       @
#      @*@
#     @***@
#    @*****@
#       |