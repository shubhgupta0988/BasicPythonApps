''' Write a function accordian(l) that takes as input a list of integer l and
returns True if the absolute difference between each adjacent pair of
elements alternates between increasing strictly and decreasing strictly.'''

def accordian(l):
   x = abs(l[0] - l[1])
   y = abs(l[1] - l[2])
   if x>y :
       for i in range (2, len(l) - 1):
           if i % 2 == 0 :
               if abs(l[i] - l[i+1]) < y:
                   print("False")
                   return (False)
               y = abs(l[i] - l[i+1])
           else :
               if abs(l[i] - l[i+1]) > y:
                   print("False")
                   return (False)
               y = abs(l[i] - l[i + 1])
       else :
           print("True")
           return (True)

   if x<y :
       for i in range(2, len(l) - 1):
           if i % 2 == 0:
               if abs(l[i] - l[i + 1]) > y:
                   print("False")
                   return (False)
               y = abs(l[i] - l[i + 1])
           else:
               if abs(l[i] - l[i + 1]) < y:
                   print("False")
                   return (False)
               y = abs(l[i] - l[i + 1])
       else :
           print("True")
           return (True)
   if x == y :
        print("False")
        return (False)

lst_len = int(input("Enter the number of elements in your list:"))
lst = []
for i in range (lst_len):
    n = int(input("Enter the number:"))
    lst.append(n)

accordian(lst)




