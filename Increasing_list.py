'''Write a function expanding(l) that takes as input a list of integer l and
returns True if the absolute difference between each adjacent pair of
elements strictly increases.'''

def expanding(l):
   diff = abs(l[1] - l[0])
   for i in range (1,lenstr - 1):
       if diff > abs(l[i] - l[i+1]):
           return(False)
           break
   else:
       return(True)

lst = []
lenstr = int(input("Enter the number of elements in the list:"))
for i in range(lenstr):
    lst.append(int(input("Enter the number:")))

print(expanding(lst))