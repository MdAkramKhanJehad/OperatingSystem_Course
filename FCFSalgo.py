n = int(input("Enter Total Number of track : "))
position = int(input("Enter current Position of R/W head : "))
total = int(input("Enter total number of request : "))
print("Enter your requests : \n")



requests = []

for i in range(total):
    x = int(input())
    requests.append(x)
for i in range(total):
    print(requests[i], end=" ")
print()
