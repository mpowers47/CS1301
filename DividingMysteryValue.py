mystery_value = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a program that divides mystery_value by mystery_value
#and prints the result. If that operation results in an
#error, divide mystery_value by (mystery_value + 5) and then
#print the result. If that still fails, multiply mystery_value
#by 5 and print the result. You may assume one of those three
#things will work.
#
#You may not use any conditionals.
#
#Hint: You're going to want to test one try/except structure
#inside another! Think carefully about whether the second
#one should go inside the try block or the except block.


#Add your code here!
try:
    div= mystery_value / mystery_value
    print(div)
except ZeroDivisionError:
    div_5= mystery_value / (mystery_value + 5)
    print(div_5)
except Exception:
    multiple= mystery_value * 5
    print(multiple)
##########################
---OR---
mystery_value = 5

#This can be kind of a big problem, so let's break it down
#into chunks.
#
#What do we want to try first? Well, our first step is to
#try to divide mystery_value by itself. So, we'll try
#(literally) that:

try:
    print(mystery_value / mystery_value)
    
#We know that might not work, both logically (what if
#mystery_value is 0?) and because the directions told us it
#might not. So, if it doesn't work, we want to catch that
#error. So, we jump straight to having ane except block:
except:
    
    #Now at this point, we can forget how we got here. We
    #don't need to worry about the earlier error. All we
    #need to know is that if we get here, we should try
    #to divide mystery_value by itself plus 5. So, we
    #try that:
    try:
        print(mystery_value / (mystery_value + 5))
        
    #Like before, the directions tipped us off that this
    #might not work, and we know this won't work if
    #mystery_value isn't a number. So, we need to handle
    #another error:
    except:
        print(mystery_value * 5)
    
    #Notice that this except is at the same level of
    #indentation as the second try. It only reacts if the
    #second try hits an error. If we were able to perform
    #our original mystery_value / mystery_value operation,
    #then we never need to even look here!
