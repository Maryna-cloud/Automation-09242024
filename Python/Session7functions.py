def greeting():
    print("Hello World")

def greeting_to_someone(name,number):
    #print out the string
    print("Hello " + name + str(number))


def greeting_to_someone_w_return(name):
    #function create a string
    return f"Good evening "+ name + "!"

#function that calculate taxes from salaries :
#if salary <= 100000 then tax = 10%
#if salary > 100000 then tax = 20%
def calculate_tax(salary):
    if salary <= 100000:
        return salary * 0.1 #if salary <= 100000 then tax = 10%
    else:
        return salary *0.2 #if salary > 100000 then tax = 20%
