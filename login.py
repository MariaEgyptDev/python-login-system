print("=" * 30)
print("Login System")
print("=" * 30)

username = input("Enter your Username: ")
password = input("Enter your Password: ")

if username == "Maria" and password == "12345":
    print("\n✅ Login Successful!")
    print("Welcome Maria!")
    
elif username == "Maria" or password == "12345":
    print("\n⚠️ One of the details is wrong")
    print("Please try again")
    
else:
    print("\n❌ SORRY")
    print("Both username and password are incorrect")

print("\n" + "=" * 30)

input("Press Enter to exit...")