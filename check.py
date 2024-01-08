email=input("enter the email id")
user=email[:email.index('@')]
domain=email[email.index('@')+1:]
print("your user name is ",user,"and domain is " ,domain)
