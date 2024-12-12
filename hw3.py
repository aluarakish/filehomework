def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            code = ord(char) + shift
            if char.islower():
                code = (code - ord('a')) % 26 + ord('a')
            elif char.isupper():
                code = (code - ord('A')) % 26 + ord('A')
            result += chr(code)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

text = "hello world"
shift = 3

encrypted = encrypt(text, shift)
decrypted = decrypt(encrypted, shift)

print("Encrypted:", encrypted) 
print("Decrypted:", decrypted) 
