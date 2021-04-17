from array import *
from math import *
from random import randint


num1 = 10
num2 = 25
num3 = 30


print("ternary: ", num1 if num1>num2 else num2)

'''
print("-------topic 1-----")

fnum = input("enter first num : ")
snum = input("enter second num : ")

print("fnum+snum = ", int(fnum)*int(snum))
'''
print("\n-------topic 2-----")
if num1 > num2 & num1 > num3:
    print(num1, end=" ")

elif num2>num1 & num2 > num3:
    print(num2, end=" ")
else:
    print(num3, end=" ")

print("\npower of num1 ", num1**3)

print("\n-------topic 3-----")

print("maximum between 12 and 13 : ", max(12, 13))
print("minimum between 12 and 13 : ", min(12, 13))
print("abs val of -10 : ", abs(-10))
print("power of : ", pow(3,3))
print("sqrt of 29: ", sqrt(29))

print("\n-------topic 4-----")

print("floor of 10.89 : ", floor(10.89))
print("ceil of 10.89 : ", ceil(10.89))


#Array
val = array('i',[2,-90,23,321, 456])
print(val)

newArr = array(val.typecode,(a for a in val))
for x in newArr:
    print(x)
newArr.reverse()
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1

'''
take array value from user input

value = array('i', [])

n= int(input("enter array size"))
for i in range(n):
    x= int (input("enter array value "))
    value.append(x)
print(value)

'''
print("\n-------topic 5-----")

i=0
while i<=10:
    print(i)
    i=i+1
print("end of whileloop")

print("\n-------topic 6-----")

lists = ["d","a","x","b","e"]
print("prints all : ",lists)
print(lists[2:])
print(lists[:0])
print(lists[:-1])

print("A" in lists)

lists = lists+["x"]
print(lists)
#will print list 2 times
print(lists*2)


lists.append("C")
print(lists)
lists.insert(2,"lol")
print(lists)
lists.remove("lol")
print(lists)

lists.sort()
print(lists)

lists.reverse()
print(lists)

lists.pop()
print(lists)

print(lists.index("e"))

lists2= lists.copy()
print("list2 : ", lists2)
print("total num of x : ",lists.count("x"))

print("\n-------topic 7-----")

temp= list(range(5,11))
print(temp)

temp2= list(range(2,10))
print(temp2)

temp3= list(range(1,11,2)) # here 2 is the difference between numbers
print(temp3)

for x in temp:
    print(x)

#pattern printing
n=5
for x in range(n+1):
    print(x*"*")


i=1
for x in range(n+1):
    print((5-x)*" ",end="")
    print(x*"*")

#guesing game
myNum = 4

for x in range(5):
    random = randint(1,5)
    if myNum == random :
        print("Win")
    else:
        print("lost")

print("\n-------topic 8-----")

n= "10 20   30  40"

array = n.split()
sum=0
for x in array:
    sum = sum + int(x)

print(sum)

print("\n-------topic 9-----")

matrix = [[1,2,3],
          [7,8,9]
        ]

for row in matrix:
    for col in row:
        print(col,end=" ")
    print()


print("\n-------topic 10-----")
#dictionary

idNo = {

    1: "irfan",
    2: "kamal",
    3: "rahman",
}

print(idNo[2])
print(idNo.get(3))
print(idNo.get(5, "NOT A VALID KEY"))

print("\n-------topic 11-----")
#touples where value reassignemnt is not possible

name =(
    "haha",
    "kaka",
    "lala"
)
#name[0]= "ooo" is not valid
print(name[2])

print("\n-------topic 12-----")
#functions

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Bangladesh")
my_function("BD")
my_function()
my_function("BD/Bangladesh")

def calc(x):
    return x*10

print(calc(5))

#use parameters like touple
def calculation(*all):
    sum = 0
    for x in all:
        sum = sum+int(x)
    print(all)
    print("sum = ", sum)

calculation(10,20)
calculation(59,41,100)

#use parameters like dictionary
def calcu(**allInfo):
    print(allInfo)
    print(allInfo["id"])

calcu(id = 100, name = "kuddus")

print("\n-------topic 13-----")
#File

file = open("hello","r")
#print(file.writable())
text = file.read()
#text= file.readlines()
#for line in file:
 #   print(line)
print(text)
print("Total characters: ",len(text))
file.close()

tempFile = open("hello","a")
tempFile.write("\nYasin: A good boy")
tempFile.close()
