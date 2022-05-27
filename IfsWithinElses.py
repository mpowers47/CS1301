balance = 20.0  
salesTax = 1.08 
cardholderName = "David Joyner"
trustedVendors = ["Maria's", "Bob's", "Vrushali's", "Ling's", "Tia's"]

purchasePrice = 19.0
customerName = "David Joyner"
vendor = "Freddy's"
overdraftProtection = True

#This nested conditional checks whether the balance is less than or
#equal to the total price and overdraft protection is not available;
#otherwise, whether the cardholder is not also the customer; and
#otherwise, whether the vendor is not trusted.
if balance <= purchasePrice * salesTax and not overdraftProtection:
    print("Purchase not approved; no funds or overdraft protection.")
else:
    if not cardholderName == customerName:
        print("Purchase not approved; invalid customer.")
    else:
        if not vendor in trustedVendors:
            print("Purchase not approved; untrusted vendor.")
        else:
            print("Purchase approved!")
print("Done!")
