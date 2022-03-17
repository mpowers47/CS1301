original_total = "5.45"
donation = "0.55"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you're writing code for the cash register of a
#fast casual restaurant. For this restaurant, customers have
#the option to round up their total and donate the extra to
#charity. For example, if a customer's total was $5.45, they
#could round up to $6.00, and donate the extra $0.55 to
#charity.
#
#The variables original_total and donation represent these
#values; you may assume they will always add to a whole integer.
#Due to an error by another programmer, though, they are initially
#given to you as strings rather than floats.
#
#Write some code that will print the customer's total and
#how much they donated. This sentence should read as follows:
#
# Your total is $6 and you donated $0.55
#
#Note that because we always round up to a full dollar,
#the total should be printed as an integer. Make sure the
#dollar signs are in the right place, with no spaces following
#the dollar signs.


new_total = float(original_total)
new_don = float(donation)
rounded = round((new_total)+ (new_don))

print(f"Your total is ${rounded} and you donated ${new_don}")
