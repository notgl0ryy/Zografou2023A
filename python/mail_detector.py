email=input("Dwse email: ")
if '@' in email and email[-3]=='.gr':
    print(f"{email}: ACCEPTED")
else:
   print(f"{email}: DENIED")