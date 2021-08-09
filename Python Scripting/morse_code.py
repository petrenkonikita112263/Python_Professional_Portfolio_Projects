from morse_code_translator import MorseCodeTranslator


def print_menu():
    """Print the main menu into console"""
    print(" \nGreetings to Morse Code Translator")
    print("1) Make an encrypt code. \n2) Decode a message. \n3) Quit. \n")


def app_logic(morse_code_program, condition: bool) -> None:
    """Main logic of Morse Code encryption and decryption"""
    while not condition:
        user_operation = int(input("Enter your selection (from 1 to 3): "))
        if user_operation == 1:
            human_text = input("Please type your text: ")
            morse_code_program.text = human_text
            print(f"Here is your encrypt text {morse_code_program.encrypt_text()}")
            print_menu()
        elif user_operation == 2:
            encrypt_text = input("Please type the encrypt text: ")
            normal_text = morse_code_program.decrypt_text(encrypt_text)
            print(f"Here's the original text: {normal_text}")
            print_menu()
        elif user_operation == 3:
            condition = True
            print("Thanks for using")
        else:
            print("Incorrect selection")
            user_operation = input("To continue press 'ENTER' ")
            print_menu()


def main():
    """Run all the main functionality"""
    morse_code_translator = MorseCodeTranslator()
    app_is_on = False
    print_menu()
    app_logic(morse_code_program=morse_code_translator, condition=app_is_on)


if __name__ == "__main__":
    main()
