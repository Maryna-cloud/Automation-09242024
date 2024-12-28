from Python.Session7functions import greeting, greeting_to_someone, greeting_to_someone_w_return, calculate_tax

#Tuples
test_result = ("test_login", "passed", "failed")
print(test_result)
print(test_result[0])
# print(test_result[10])  #IndexError: tuple index out of range
print(f"Test : {test_result[0]} has result {test_result[2]}")

#Set
data = ["123","1234", "123", "-123","12"]
print(data)
data1 = {"123","1234", "123", "-123","12"}
print(data1)
numeric_data = {123,1234,123,-123,12,12,12,1,1234}
print(numeric_data)
numeric_data_as_tuple = (123,1234,123,-123,12,12,12,1,1234)
print(numeric_data_as_tuple)
numeric_data.add(12345)
print(f"add an element to set {numeric_data}")
data.append("12345")
print(f"New list with added element {data}")
print ("*"*50)
raw_data= {"123","1234", "123", "-123","12", None}
valid_data = set(filter(None, raw_data))
print(valid_data)

print ("*"*50)
#Create a tuple to store monthly salaries of employees for a year ,
# (1000,1000,5000,4000,2000,4567,12345,4564678,123,4567,12345,4564678)
#printout all year, salary of 5th month, summary of the whole year
salaries = (1000,1000,5000,4000,2000,4567,12345,4564678,123,4567,12345,4564678)
print("Salaries for the whole year:", salaries)
print("Salary for 5th month:", salaries[4])
print("Total salary (summary) for the whole year:",sum(salaries) )
print("the highest salary of the year", max(salaries))
print("the lowest salary of the year", min(salaries))
print("the average salary of the year", sum(salaries)/len(salaries) )

print ("*"*50)
# #Set operations
set1 = {'A','B','C','D'}
set2 = {'A','B','W','Z'}
print ("Union of set1 and set2", set1 | set2)
print ("Difference from set1 and set2", set1 - set2)
print ("Difference from set2 and set1", set2 - set1)
print ("Intersection btw set1 and set2", set1 & set2)

print ("*"*50)
greeting()
greeting_to_someone("Anna",1)
print(greeting_to_someone_w_return("STUDENTS"))

greeting_to_someone(greeting_to_someone_w_return("STUDENTS"),1)

print(greeting_to_someone_w_return("STUDENTS") + greeting_to_someone_w_return("STUDENTS"))

#calculate a tax function
print ("*"*50)
total_salary = sum(salaries)
tax = calculate_tax(total_salary)
print ("tax is ", tax)