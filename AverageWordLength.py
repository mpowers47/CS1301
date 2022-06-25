#In this problem, you should write three functions:
#word_count, letter_count, and average_word_length.
#
#word_count should take as input a string. It should return
#the number of words in the string. You may assume that the
#number of words in the string will be one more than the
#number of spaces in the string.
#
#letter_count should take as input a string. It should return
#the number of letters in the string. You may assume that
#the string is only letters and spaces: no punctuation or
#numbers.
#
#average_word_length should take as input a string. It should
#return the average length of the words in the string. You
#can find the average length by dividing the number of letters
#by the number of words.
#
#Your implementation for average_word_length *must* call
#word_count and letter_count.


#Add your code here!
def letter_count(a_string):
    letters = 0
    for character in a_string:
        if not character == " ":
            letters += 1
    return letters

def word_count(a_string):
    words = 1
    for character in a_string:
        if character == " ":
            words += 1
    return words
###start word count with 1 because the first space marks the start of word count 2
def average_word_length(a_string):
    return letter_count(a_string) / word_count(a_string)


a_string = "Up with the white and gold"

print(average_word_length(a_string))

