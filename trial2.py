#Front$$$$$$$$$$$$$$$$$$$$$$Rear
from collections import deque
import collections
import numpy as np
print("Enter The input size: ")
n=int(input())
arr=[]
notInQ=0
print("Enter the array Elements: ")
for i in range(n):#gets the elements
    arr.append(int(input()))
arr=np.array(arr)
dQue = collections.deque([arr[0]])
print(arr[0], " Appending in Front of Deque")
print(dQue)

print("..........................................................")
for i in range(1, n):
    if (i % 2 == 0):
        if(arr[i]>dQue[0]):
            # print(dQue[0])
            print(arr[i], " Appending in Front of Deque")
            dQue.appendleft(arr[i])
            print(dQue)
            print("..........................................................")
        elif (arr[i] > dQue[-1]):
            # print(dQue[0])
            print(arr[i], " Appending in Rear of Deque")
            dQue.append(arr[i])
            print(dQue)
            print("..........................................................")
        else:
            print(arr[i]," DOES NOT SATISFY CONDITION... IGNORED!")
            notInQ+=1
            print(dQue)
            print("..........................................................")
            continue
    else:
        if (arr[i] > dQue[-1]):
            print(arr[i], " Appending in Rear of Deque")
            dQue.append(arr[i])
            print(dQue)
            print("..........................................................")
        elif (arr[i] > dQue[0]):
            print(arr[i], " Appending in Front of Deque")
            dQue.appendleft(arr[i])
            print(dQue)
            print("..........................................................")
        else:
            print(arr[i]," DOES NOT SATISFY CONDITION... IGNORED!")
            notInQ+=1
            print(dQue)
            print("..........................................................")
            continue
print(dQue)
print("..........................................................")
print(notInQ," is the difference betwwen array and deque")
