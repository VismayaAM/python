email=input("enter the email id ").strip()
user=email[:email.index('@')]
domain=email[email.index('@')+1:]
print(f"your user name is {user} and domain is {domain}")
