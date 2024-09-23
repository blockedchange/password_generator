import random
import string
import base64
import json


def generate_password(length):
    """Set allowed character set for password"""
    characters = string.ascii_letters + string.digits + string.punctuation

    #Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    """Get user's input, generate password, encrpyt password in b64, save info in json file"""
    service_name = input("Enter the service you're creating an account for (ie facebook, gmail, x): ")
    username= input("Enter the username: ")
    password_length = int(input("Enter the desired password length: "))

    #Generate password
    password = generate_password(password_length)

    #Encrypt the password in base64
    encrypted_password = base64.b64encode(password.encode()).decode()

    #Create a dictionary with user details
    user_details = {
        "service": service_name,
        "username": username,
        "encrypted_password": encrypted_password
    }

    #Save details to an appendable JSON file
    filename = "passwords.json"
    with open(filename, "a") as f:
        json.dump(user_details, f, indent=4)


    print(f"User details saved in {filename}")
    print(f"Password is {password}")
    print(f"Encryped password is {encrypted_password}")


if __name__ == "__main__":
    main()