from numpy import *


#numpy
    #array

arr = array([1,2,4,5,34.9],float)
print(arr.dtype)

i=0
for i in range(len(arr)):
    print(arr[i], end=" ")
print()

#linespace ( here upper value is also included and the third value is step
arr2 = linspace(1,10,10)
print("linespace : ",arr2)

#in range , the upper value is not included and the third value difines the gap between two value
x= range(1,10,8)
for n in x:
    print(n)

#arrange(similar to range , both exclude the upper value)
s = arange(1,11,2)
print("arange : ",s)

#logspace

arr3 = logspace(1,20,5)
print("logspace : ", arr3)

#zeros and ones (to create an array with default value zero)
arr4 = zeros(5)
print(arr4)
arr5 = ones(5, int) #can also specify int or float
print(arr5)


arr6 = array([1,2,3,4,5])
arr6 = arr6 + 5
arr7 = array([10, 11, 12, 13, 14])
arr8 = arr7+arr6
print(arr8, end="\n\n")

arr9= array([4,81,25,100])
print("sin value : ",sin(arr9))
print("sqrt value : ", sqrt(arr9))
print("log value : ", log(arr9))
print("min value : ", min(arr9 ))
print("concatanate : ", concatenate([arr6, arr7]))

arr10 = arr9    # it just aliases the array, address remains same
arr11 = arr9.view() # it does the shallow copy which is litte deep
arr12 = arr9.copy() #it does the deep copy, where after changing value of previous array, doesnt affect on new ones
print(arr9)
print(arr10)
print(arr11)
print(arr12)
print(id(arr9))
print(id(arr10))
print(id(arr11))
print(id(arr12))

arr9[2]=121
print(arr9)
print(arr10)
print(arr11)
print(arr12, end="\n\n")

#matrix in numpy

arr13 = array([ [[3,2,1,],[6,5,4]],
                [[10,9,8], [11,13,12]],
                [[100,200,300],[101,301,201]]

])

print("arr113 : \n",arr13)
print("datatype of arr13 : ",arr13.dtype)
print("shape of arr13 : ",arr13.shape)
print("arr13 size : ",arr13.size)

arr14 = arr13.flatten() #this function will make the array to one dimension
print("arr14 : ",arr14)
arr15 = arr14.reshape(3,6)  #tis function will make one dimentional array to multi dimentional array
print("arr15 : \n", arr15)

m= matrix('3,2,1;4,6,5;9,8,7')
print("m : \n",m)
print("max vaue of m : ",m.max())
print("diagonal of m1 : ",m.diagonal())
m2 = matrix('4,2,3;8,6,5;9,8,5')
print("m2 : \n",m2)

m3 = m+m2
print("m+m2 : \n", m3)
m3 = m*m2
print("m*m2 : \n", m3)

