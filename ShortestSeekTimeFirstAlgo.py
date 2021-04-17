n = int(input("Enter Total Number of track : "))
position = int(input("Enter current Position of R/W head : "))
total = int(input("Enter total number of request : "))
print("Enter your requests : \n")

token = position
requests = []
for i in range(total):
    x = int(input())
    requests.append(x)

temp = n
tempIndex = 0
while requests:

    for i in range(len(requests)):
        if abs(token - requests[i])<temp :
            temp = abs(token - requests[i])
            tempIndex = i

    token = requests[tempIndex]
    print(token, end=" ")
    temp = n
    requests.remove(requests[tempIndex])
