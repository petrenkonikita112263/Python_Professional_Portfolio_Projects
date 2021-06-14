from morse_code_translator import MorseCodeTranslator

print("Greetings to Morse Code Translator")
morse_code_translator = MorseCodeTranslator()
app_is_on = False

while not app_is_on:
    user_operation = input("To encrypt message(type 'e') to decrypt (type 'd')? ").lower()
    if user_operation == "e":
        human_text = input("Please type your text: ")
        morse_code_translator.text = human_text
        print(f"Here is your encrypt text {morse_code_translator.encrypt_text()}")
    elif user_operation == "d":
        encrypt_text = input("Please type the encrypt text: ")
        normal_text = morse_code_translator.decrypt_text(encrypt_text)
        print(f"Here's the original text: {normal_text}")
    user_operation = input("To continue press 'ENTER', to exit (type 'q') ").lower()
    if user_operation == "q":
        app_is_on = True
