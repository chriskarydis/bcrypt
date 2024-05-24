import bcrypt
import getpass

def hash_password(password):
    try:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    password = getpass.getpass("Please enter your password: ")
    hashed_password = hash_password(password)
    if hashed_password is not None:
        print("Ο κωδικός σας μετά τον κατακερματισμό είναι:", hashed_password)
        with open("my_hashed_password.txt", "w") as f:
            f.write(hashed_password)

if __name__ == "__main__":
    main()