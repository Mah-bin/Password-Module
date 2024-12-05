import string
import random
from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_password(password: str, key: bytes) -> str:
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password.decode()


def decrypt_password(encrypted_password: str, key: bytes) -> str:
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password.encode())
    return decrypted_password.decode()

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    if strength < 3:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    return "Strong"


print("*****************************************")
print("     Welcome to the Password Module     ")
print("*****************************************")
print('''  
  [1] Generate Password
  [2] Password Strength Checker
  [3] Encrypt Password
  [4] Decrypt Password
  [5] Exit

  Please select an option:
''')
print("*****************************************")


key = generate_key()


while True:
    choice = int(input("What would you like to do? "))
    
    if choice == 1:
   
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

        def get_valid_input():
            while True:
                user_input = input("How many characters do you want in your password? ")
                try:
                    characters_number = int(user_input)
                    if characters_number < 8:
                        print("Your number should be at least 8.")
                    else:
                        return characters_number
                except ValueError:
                    print("Please enter numbers only.")

        characters_number = get_valid_input()

        part1 = round(characters_number * 0.30)
        part2 = round(characters_number * 0.20)
        part3 = round(characters_number * 0.20)
        part4 = characters_number - (part1 + part2 + part3)

        lowercase = random.choices(s1, k=part1)
        uppercase = random.choices(s2, k=part2)
        digits = random.choices(s3, k=part3)
        punctuation = random.choices(s4, k=part4)

        result = lowercase + uppercase + digits + punctuation
        random.shuffle(result)

        password = "".join(result)
        print("Generated Password:", password)
    
    elif choice == 2:
        
        password = input("Enter a password to check its strength: ")
        print("Password Strength:", check_password_strength(password))
    
    elif choice == 3:
       
        password = input("Enter a password to encrypt: ")
        encrypted_password = encrypt_password(password, key)
        print(f"Encrypted Password: {encrypted_password}")
    
    elif choice == 4:
      
        encrypted_password = input("Enter the encrypted password to decrypt: ")
        try:
            decrypted_password = decrypt_password(encrypted_password, key)
            print(f"Decrypted Password: {decrypted_password}")
        except Exception as e:
            print(f"Error decrypting password: {e}")
    
    elif choice == 5:
      
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please choose again.")




    




