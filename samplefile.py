# Python Program to find the L.C.M. of two input number

x=15
y=45

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1


print("The L.C.M. is", lcm)
