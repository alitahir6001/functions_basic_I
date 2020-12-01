#1 -- output will be 5
def a():
    return 5
print(a())
# Right

#2 -- output will be 10
def a():
    return 5
print(a()+a())
#  Right

#3
def a():
    return 5
    return 10
print(a())
# WRONG -- I forgot when a def executes a return statement, the function stops/exits so it didn't even check for line 16 once line 15 was executed.

#4 -- Output is 5
def a():
    return 5
    print(10)
print(a())
# Right -- 10 doesn't get printed because the function had already stopped running once a return statement was exec.

#5 -- Output is 5
def a():
    print(5)
x = a()
print(x)
# WRONG -- no return statement! Duh

#6 -- no output 
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# Right - there's no return statement to return the result of 8 

#7 -- output is 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Right! we told it to return those ints as strings

#8 -- outputs will be: 100, and 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# Right -- first thing we told the function to do was print val of var b (100), and the next print statement would be 10 because 100 is not less than 10, so the else statement was executed. 7 doesn't get returned because the else return was true and was executed first.

#9
def a(b,c):
    if b<c: 
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # 2 is less than 3, so should return 7
print(a(5,3)) # 5 not less than 3, so should return 14
print(a(2,3) + a(5,3)) # 7 + 14 = 21
# Right! 

#10 -- output should be 8 
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# Right!

#11 - outputs should be 500, 500, 300, 500
b = 500
print(b) # first output
def a():
    b = 300
    print(b) # output here is 300 when the function is called
print(b) # outside the function, so output is 500
a() # output here is 300
print(b) # output should be 500
#Right!  Hell yeah

#12 -- outputs should be: 500, 300, 300,500
b = 500
print(b) # first output
def a():
    b = 300
    print(b) # second output
    return b # third output since there's a return statement here
print(b) #again, outside the function so 500
a() # output 300
print(b) # output 500

#WRONG -- line 94 is a return statement not a print statement. should've been 500, 500, 300, 500

#13 -- outputs should be: 500, 500, 300, 300
b = 500
print(b) #first output
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# Right! since b was set to be the new value of def a(), when line 110 runs, it's gonna print that new value.

#14 -- outputs should be: 1 , 3 
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# WRONG -- I actually dont understand why 2 is being outputted...is b() a nested def inside def a()?

#15 -- outputs should be: 1, 3, 5, 10
def a():
    print(1) # first output
    x = b() # set x to be the value of def b()
    print(x)
    return 10
def b():
    print(3) # second output
    return 5 # third output
y = a() # set y to equal the value of def a
print(y) # return 10, last output
#Right! -- If you follow it line by line, it makes sense why it printed 3 first and not 10.
