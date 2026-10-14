"""
QR Code Generator (with Password Tool)
 
"""

import random     
import string     
import qrcode      
import os          
from datetime import datetime    


def make_password(length, use_symbols=True):
    characters=string.ascii_letters + string.digits
    if use_symbols:
        characters+=string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def make_qr_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    return f"qr_output_{timestamp}.png"


def save_qr(text, filename):
    script_folder = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_folder, filename)

    qr_image = qrcode.make(text)   # create the QR code
    qr_image.save(full_path)       # save it as a .png file
    print(f"QR Code saved at: {full_path}")


def ask_length():
    while True:
        user_input = input("Password length (min 4): ")

        if not user_input.isdigit():
            print("Please enter a whole number.")
            continue

        length = int(user_input)

        if length < 4:
            print("Length must be at least 4.")
            continue

        return length  
def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ("y", "n"):
            return answer
        print("Invalid input! Please enter only 'y' or 'n'.")
 

def ask_menu_choice(question, valid_options):
    """Keep asking a menu question until the user picks one of the valid options."""
    while True:
        answer = input(question).strip()
        if answer in valid_options:
            return answer
        print(f"Invalid input! Please enter {' or '.join(valid_options)}.")


def main():
    print(">>> QR Code Generator and Password Tool <<<")

    while True:
        print("\nWhat you want to turn into a QR code?")
        print("1. A  link or any text")
        print("2. A password")
        choice = ask_menu_choice("Enter 1 or 2: ", ["1", "2"])

        if choice == "2":
            own_choice = ask_yes_no("Do you want to use your own password? (y/n): ")

            if own_choice == "y":
                content = input("Enter the password: ")
            else:
                length = ask_length()
                symbols_choice = ask_yes_no("Include symbols? (y/n): ")
                use_symbols = (symbols_choice != "n")   # anything except 'n' counts as yes
                content = make_password(length, use_symbols)
                print(f"\nGenerated Password: {content}")
        else:
            content = input("Enter the text or  link: ")

        save_choice = ask_yes_no("Save this as a QR code? (y/n): ")
        if save_choice == "y":
           
            save_qr(content, make_qr_filename())

        again = ask_yes_no("\nDo this again? (y/n): ")
        if again != "y":
            print("Done!")
            break   
if __name__ == "__main__":
    main()