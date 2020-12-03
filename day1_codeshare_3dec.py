#Code sharing
#stay tuned

#----------------------------------
# List - pg 33
'''
my_list = [1,5,15]
my_list.append(20)
print(my_list)
my_list.remove(5)
print(my_list)
'''

# pg 35
'''
name = input("Enter patient's name: ")
temp = input("Enter patient's temperature: ")
delta = 36.9 - float(temp)
print("%s's temperature is %.2f degree celsius from 36.9 degree celsius"%(name, delta))
'''

#if.. else
'''
marks = int(input("Enter the marks: "))
if marks < 50:
    print("Fail")
elif marks < 80:
    print("Pass")
else:
    print("Excellent")
'''

#pg 43 BMI Calculator
'''
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight/(height*height)
print(bmi)

if (bmi < 18):
    print("UnderWeight")
elif (bmi<25):
    print("Ideal")
elif (bmi<30):
    print("Overweight")
else:
    print("Obese")
'''

#pg 49 For loop
'''
numbers = range(10)
for i in numbers:
    print(i)
'''
'''
numbers = range(1,11,2)
for i in numbers:
  print(i, end=",")
'''

# Odd/even numbers
'''
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_count = 0
even_count = 0

for i in numbers:
    remainder = i%2
    if remainder == 0:
        odd_count = odd_count + 1
    else:
        even_count = even_count + 1
print("There are : "+ str(even_count) + " odd number")
print("Odd #: "+ str(odd_count))
'''

# Calculate area of rectangle
'''
def cal_area(width, height):
    return width * height

area = cal_area(3, 4)
print(area)
'''
'''
def cal_area1(width, height):
    print(width * height)
    
cal_area1(3,4)
'''

#pg 56
'''
def add(a, b):
    return a+b

def add(a, b, c):
    return a+b+c

answer = add(5, 6)
print(answer)
'''

#pg 57
'''
def getBiggerNumber(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
answer = getBiggerNumber(a, b)
print("The bigger number is :"+str(answer))
'''

#pg 58
'''
#Write a function that takes in a number as argument, and returns that number
def func1(num):
    return num
answer = func1(6)
print("Function 1: %d" % (answer)) 
#%d: integer/whole number %f: float/decimal point number %s: string/text

print("Function 1: " + str(answer))

#Write a function that takes in a number as argument, and returns that number incremented by 1
def func2(num):
    return num+1

answer = func2(6)
print("Function 2: "+ str(answer))

#Write a function that calculates and returns the double of the number given as argument
def func3(num):
    return num * 2
answer = func3(6)
print("Function 3: "+str(answer))
'''

'''
#pg 59 : Simple get discount
def get_discount(price, percent):
    discounted_amt = percent/100 * price
    discounted_price = price - discounted_amt
    return discounted_price

answer = get_discount(100, 10)
print("Discounted price: $"+str(answer))
'''

'''
#pg 59 Get discount based on user input values
def get_discount(price, percent):
    discounted_amt = percent/100 * price
    discounted_price = price - discounted_amt
    return discounted_price

original = float(input("Enter original price: "))
percent = float(input("Enter % of discount: "))
answer = get_discount(original, percent)
print("Discounted price: $"+str(answer))
'''

'''
#pg 59
def get_sum(aList): #[5,2,7,4]
    total = 0
    for i in aList:
        #print(i)
        total = total + i
    return total

answer = get_sum([5,2,7,4, 8, 9, 10])
print("Answer: "+str(answer))
'''


'''
# Illustrate concept on default parametsr pg 60
def introduce(name, school="RP"):
    print("I am %s from %s" % (name, school))
    
introduce("Mei Lan")
introduce("Mary", "Somewhere else")
'''

'''
score = 85
if score > 80:
    print("A")
if score > 70:
    print("B")
'''
'''
score = 65
if score > 80:
    print("A")
elif score > 70: # <=80  (elif => else if)
    print("B")
elif score > 60:
    print("C")
    print("BBBBB")
else:
    print("D")

print("End of program")
'''

'''
#Error handling (try.. except)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    print(num1/num2)
except Exception as e:
    print("An error has occured, please contact Helpdesk and provide error %s"%(e.args))
finally: # will always run
    print("Thank you for using the program. ")

'''
'''
#String operations
word = "HElLO"
word = word.lower()
print(word)
'''
'''
a = "python or java"
aList = a.split(" ") #split by space
print(aList)
print(aList[0])  #[0] means first position
'''
'''
data = "Tay Mei Lan,20,RP" #useful if using csv file
aList = data.split(",")  # split by ,
print(aList)
print("Name : "+aList[0])
print("Age: "+aList[1])
print("School: "+aList[2])
'''
'''
a = ["Mary", "John", "Betty"] #list
b = ", ".join(a)
print(b + " are good friends") #str: "Mary John Betty"
'''
'''
s = "freedom"
print(s[0:4]) #free -> index 0(f), 1(r), 2(e), 3(e)
print(s[:4]) #starting of string

print(s[4:7]) #dom -> index 4(d), 5(o), 6(m)
print(s[4:]) #extract till end of string
print(s[-3:]) #start from third last letter

print(s[-1]) #last letter
print(s[-2]) # second last letter
print(s[0])  # first letter
'''
# Also available in day1.zip (longest-word.py)
'''
sentence = "Python is an interpreted, high-level, general-purpose programming language."
words = sentence.split()

print(words)

longest = words[0] #default to first word in list

for word in words:
    if len(word) > len(longest): #len -> find out how many characters in a word
        longest = word

print("Longest word: " + longest)
'''
'''
import math

print("Pi is " + str(math.pi))
print("Pi is approx %.2f I can add" % (math.pi))

print("Pos or Neg: %d %d"%(-5,3))
print("Pos or Neg: %+d %+d"%(-5,3))

b = 5
print("%d"%(b)) #5
print("%03d"%(b)) #005
#Student ID 20200001, 20200002,... 20209999
'''

'''
aList = ["python", "programming"]
for word in aList:
    print("%15s"%(word))

for word in aList:
    print("%-15s*"%(word))
'''

'''
import random
for i in range(10):  #4 times
    num = random.randint(1, 9999)
    print("Lucky 4D num: %4d"%(num))
    #print("Lucky 4D num: %04d"%(num))
'''

'''
# Guessing game - last exeecise
import random
luckynum = random.randint(1,20)
print(luckynum)

for i in range(6):
    guess = int(input("Enter a number: "))
    if guess > luckynum:
        print("Your guess is too high")
    elif guess < luckynum:
        print("Your guess is too low")
    else:
        print("Good job! Correct answer")
        break;
'''

#Pg 73: Receipt Printing
#receipt.py
'''

print (items[0] + "     " + "$" + str(prices[0]) )
print (items[1] + "         " + "$" + str(prices[1]) )
print (items[2] + "         " + "$" + str(prices[2]) )
print (items[3] + "          " + "$" + str(prices[3]) )
'''
'''
items = ["Watermelon", "Apples", "Mangos", "Pizza"]
prices = [5.00, 14.00, 140.33, 20.50]

for i in range( len(items)):
    line = "%-25s $ %.2f" % (items[i], prices[i])
    print (line)

print ("-" * 35)
print ("%-25s $ %.2f" % ("Total : ", sum(prices)) )
'''