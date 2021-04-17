f= open('input.txt','r')
n,position, total = [int(x) for x in next(f).split()]
requests = [0 for i in range(n+1)]

theInts = []
for val in f.read().split():
    theInts.append(int(val))

for i in range(total):
    requests[theInts[i]]+=1

#n = int(input("Enter Total Number of track : "))
#position = int(input("Enter current Position of R/W head : "))
#total = int(input("Enter total number of request : "))
#print("Enter your requests : \n")

#requests = [0 for i in range(n+1)]
#for i in range(total):
 #   x = int(input())
  #  requests[x]+=1
i = position

while i <= n:
    while requests[i] != 0:
        print(i, end=" ")
        requests[i]-=1
    i+=1
j = 0
while j < position:
    while requests[j] != 0:
        print(j, end=" ")
        requests[j]-=1
    j+=1