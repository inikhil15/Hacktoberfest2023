#Program to find min,max value of List using Function
def maxminList(l):
    maxVal=l[0]
    minVal=l[0]
    for i in range(0,len(l)):
        if(l[i]>maxVal):
            maxVal=l[i]
        if(l[i]<minVal):
            minVal=l[i]
    return minVal,maxVal

print("Enter no. of elements for list : ",end=" ")
n=int(input())
l=[]
for i in range(0,n):
    print("Enter elements no. ",i+1,end=" ")
    l.append(int(input()))
print(l)
print("Smallest,Largest Value in list : ",maxminList(l))
