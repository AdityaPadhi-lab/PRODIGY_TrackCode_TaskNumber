def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
    else:
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")
