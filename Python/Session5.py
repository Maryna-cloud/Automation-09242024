print("Hello Team!")

name = "Anna"
age = 18
print (f"Hello, {name}!")
print(f"My name is {name} and I am {age} years old.")

#----- Variable types
#integer
x = 10
#float
pi = 3.14
#string
name = "Anna"
name_of_the_restaurant = "McDonalds"
print(x,pi,name)

print(f"My favorite restaurant is '{name_of_the_restaurant}'!")

counter = 0
print ("counter right now is ", counter)
counter += 1
print ("counter right now is ", counter)
counter = counter +1
print ("counter right now is ", counter)
print (type(counter))
print(type(x),type(pi),type(name))

#calculating with different variables
price_of_item =10.56
quantity_of_item = 9
total_cost = price_of_item * quantity_of_item
print (f"The cost of the purchase is ${total_cost}")
name_of_customer = "Anna"
result_of_purchase = name_of_customer +" paid "+ str(total_cost) +" apples "
print(result_of_purchase)
#Annapaid95.04apples
#Anna paid 95.04 apples

print(f"The cost of the purchase is ${total_cost}")
name_of_customer = "Gleb"
result_of_purchase = name_of_customer + " paid "+ str(total_cost) + " apples "
print(result_of_purchase)

boolean variable
number = +10
is_positive = number >0
less_than_hundred = number < 100
print(is_positive)
if is_positive:
    print ("this number is positive")
else:
    print ("this number is negative")

if number >0:
    print ("this number is positive")
else:
    print ("this number is negative")

if is_positive and less_than_hundred:
    print ("this number is positive and less than 100")
else:
    print ("this number is either negative or more than 100")

if is_positive or less_than_hundred:
    print ("this number is in range 1-99")
else:
    print ("this number is not in range 1-99")

print ("# test results : A -100%, B 90-99, c 80-89, D less then 80")

# test results : A -100%, B 90-99, c 80-89, D less then 80
score = 100
if score == 100:
    print("Your grade is A")
elif score >=90 and score <=99:
    print("Your grade is B")
elif score >=80 and score <=89:
    print("Your grade is C")
else:
    print("Your grade is D")

#input
print ("# INPUT: test results : A -100%, B 90-99, c 80-89, D less then 80")
score = int(input("What is your score?"))
print (f"Your grade is {score}")
if score == 100:
    print("Your grade is A")
elif score >=90 and score <=99:
    print("Your grade is B")
elif score >=80 and score <=89:
    print("Your grade is C")
else:
    print("Your grade is D")
word = "Hurray "
print (word*3 + "!")

#length of the string that we verify as a long/short(less then 10 char) word for password
print ("#length of the string that we verify as a long/short(less then 10 char) word for password")
new_string = input("Enter a string: ")
length_of_new_string = len(new_string)
print("the length of the string is "+ str(length_of_new_string))
if length_of_new_string >= 10:
    print ("this string is good enough for long password")
elif length_of_new_string < 10 and length_of_new_string >0:
    print ("this password is short")
else:
    print ("this is not a password format")


#MAC command / -    comment out
#MAC command / +    remove comment
#MAC control /     comment out
#MAC control /     remove comment















