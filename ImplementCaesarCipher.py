def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift character and wrap around the alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift character back and wrap around the alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption/Decryption")
    
    while True:
        choice = input("Choose 'e' to encrypt or 'd' to decrypt (or 'q' to quit): ").lower()
        
        if choice == 'q':
            print("Exiting the program.")
            break
        
        if choice not in ['e', 'd']:
            print("Invalid choice. Please choose 'e', 'd', or 'q'.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (1-25): "))
        
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
