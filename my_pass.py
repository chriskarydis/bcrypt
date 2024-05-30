import bcrypt
import getpass

def hash_password(password):
    try:
        # Number of rounds (cost factor)
        cost = 12
        # Generate a salt
        salt = bcrypt.gensalt(rounds=cost)
        # Hash the password with the generated salt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        # Return the hashed password as a UTF-8 encoded string
        return hashed_password.decode('utf-8')
    except Exception as e:
        # Print any exception that occurs during the hashing process
        print(f"An error occurred: {e}")
        return None

def main():
    # Prompt the user to enter a password, hiding the input
    password = getpass.getpass("Please enter your password: ")
    # Hash the entered password
    hashed_password = hash_password(password)
    # If hashing was successful, proceed to print and write the hashed password
    if hashed_password is not None:
        # Print the hashed password in Greek
        print("Ο κωδικός σας μετά τον κατακερματισμό είναι:", hashed_password)
        # Write the hashed password to a file
        with open("my_hashed_password.txt", "w") as f:
            f.write(hashed_password)

if __name__ == "__main__":
    main()
