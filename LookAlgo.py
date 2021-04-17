n = int(input("Enter Total Number of track : "))
position = int(input("Enter current Position of R/W head : "))
total = int(input("Enter total number of request : "))
print("Enter your requests : \n")

highest = 0
lowest = n
requests = [0 for i in range(n+1)]
for i in range(total):
    x = int(input())
    requests[x]+=1
    if x>highest:
        highest = x
    if x< lowrequestsest:
        lowest = x


i = position
while i <= highest+1:
    while requests[i]!=0:
        print(i, end=" ")
        requests[i]-=1
    i += 1
j = position-1
while j >= lowest:
    while requests[j]!=0:
        print(j, end=" ")
        requests[j]-=1
    j -= 1
