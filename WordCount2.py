

def word_count(my_string):
    
    try:
        
        word_count = 1
        
        #Notice first that we're using a for loop instead of a
        #for-each loop. That's because we want to know the index
        #of each letter as we look at it. Notice also that we're
        #starting at the second letter -- we'll cover why in a
        #second.
        for i in range(1, len(my_string)):
            
            #Here's the unfamiliar syntax: the brackets let us
            #access the character at index i in the string. So,
            #if my_string is "Hi David!", my_string[0] will be
            #"H", my_string[1] will be "i", and so on.
            if my_string[i] == " ":
                
                #If we've reached here, we know the current
                #character is a space. Now we need to make sure
                #the letter before it wasn't a space. This line
                #checks the previous character, at index i - 1.
                #That's why we started the loop at 1, to avoid
                #checking the -1 character.
                
                if not my_string[i - 1] == " ":
                    
                    #If we've reached here, it means that the
                    #current character is a space, and the
                    #previous character was not a space. So, we
                    #can go ahead and count:
                    
                    word_count += 1
        
        #And now we're done, and can return our word count:
        return word_count
    
    except:
        return "Not a string"
