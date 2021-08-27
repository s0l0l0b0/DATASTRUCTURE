import time
p = int(input("How many prisoners: "))
k = int(input("Skipped number: "))

myList = []
for i in range(1,p+1,1):
    myList.append(i)

i = k-1
count = 0
count_1 = 0

indexList = []
size = len(myList)
while(1 < size):

    indexList.append(i)

    count += 1
    if((i+k)>=size):
        count_1 += 1
        i = (i+k)%size
        size-=count
        count = 0
        temp = []
        for j in range(len(myList)):
            if j not in indexList:
                temp.append(myList[j])
        myList = temp.copy()
        temp.clear()
        indexList.clear()
    else:
        i = (i+k)%size

print("Last survivor: ",myList[0])
# print(count_1)

# recursion 

# def josephus(n,k):
#     if n == 1:
#         return 0;
#     return (josephus(n-1,k)+k)%n

# print(josephus(10,2)+1)