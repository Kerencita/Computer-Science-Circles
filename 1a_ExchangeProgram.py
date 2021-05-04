#Problem: Write a program to swap the values of two variables. The grader will automatically define variables x and y for you, with numerical values.


xa = x   #making temporary values
ya = y
x =  ya  #re-assigning the values 
y = xa

# the easiest solution which I later found out about would be this one

x , y = y, x 
