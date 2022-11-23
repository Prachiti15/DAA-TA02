# DAA-TA02
In this problem statement it was asked to do insertion operation in Deque such that it follows the pattern of Front-Rear-Front-Rear... 
Along with this, conditions need to be checked and insertion should happen accordingly.

The conditions are: 

Condition 1: If the element present at front is less than the new element, then new element
will be inserted in front. [Otherwise]

Condition 2: If element present at rear is less than the new element, then new element will
be inserted at rear.

Condition 3: If both condition 1 and condition 2 not satisfied, ignore the element and
consider new element.

### For the solution of this problem statement I have taken input the size of array and the array from the user and inserting elements of the array in Front-Rear fashion such that every even i position of the array will check the conditions for front position and for every odd i of the array will check the conditions for rear position.. an alternative solution for this is by maintaining the flag and then checking the condition.

### If the the element is 1st checking the condition for front location then if it is greater than present front of the deque then it will get inserted in the front location... if not then it will check in rear end if the element is greater than current rear then it will get inserted in the rear end... if both the conditions doesnot hold true then that element will be ignored and next element from the array will be checked, Similarly it will happen if the array element is 1st checking the element for the rear end.

### The elements which could not make place in deque will be the difference between the array and the deque.

### The shape of the deque is first decreasing and then increasing (this change happens across the 1st element of the array in deque).


CODE:
```
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
```

## For Ascending input:Testcase01: 
![image](https://user-images.githubusercontent.com/91412980/203615400-fe50b507-de54-4d7d-b442-6fd6395d924b.png)
### Here we can see that all elements from the array are inserted in the deque. None of the element gets ignored as every next element is greater than the previous element which ultimately satisfies the conditions.

## For Descending input:Testcase02: 
![image](https://user-images.githubusercontent.com/91412980/203620852-ed2655b7-c25a-466e-9118-7845c78ae0f0.png)
### Here we can see that only 1st element of the array is inserted and rest all are ignored as the input is descending, thus all the other elements are less than the 1st element and they are getting ignored.

## For Random input:Testcase03: 
![image](https://user-images.githubusercontent.com/91412980/203621372-7b73910a-82e4-4d4c-a1d6-6ef8e42237d4.png)
### Here we can see that in random input array the deque formed did not have number of elements equal to number of elements in the array and the deque was firstly decreasing and then is increasing(changed across the 1st element of the array).

### To modify it such that all the elements of the array can be the part of the deque can be simply inserting them in Front-Rear-Front-Rear.. trend 
```
Example: array=[5,6,4,8,3]
so 5 will get inserted in front ==> F-> 5 <-R
then 6 will be inserted at the rear end ==> F-> 5 ,6 <-R
then 4 will be inserted at the front end ==> F-> 4, 5 ,6 <-R
then 8 will be inserted at the rear end ==> F-> 4, 5 ,6 ,8 <-R
then 3 will be inserted at the front end ==> F-> 3, 4, 5 ,6 ,8 <-R
```

