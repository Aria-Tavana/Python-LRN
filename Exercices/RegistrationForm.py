print("Welcome to \"RegistrationForm\" application")

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
phoneNumber = input("Enter your phone number: ")

if (phoneNumber.isdigit() == False):
    print("The phone number is incorrect!")
    phoneNumber = input("Enter your phone number: ")

email = input("Enter your email: ")
print("All right the registration form finished, This is the result. 👇")
print("First name", firstName, sep=": ")
print("Last name", lastName, sep=": ")
print("Phone Number", phoneNumber, sep=": ")
print("Email", email, sep=": ", end="\n\n")
