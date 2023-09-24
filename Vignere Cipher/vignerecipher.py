def vigenere_cipher(text, key, encrypt=True):
    result = []
    key_len = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = key[i % key_len]
            shift = ord(key_char) - ord('A')
            base = ord('A')
            
            if encrypt:
                encrypted_char = chr((ord(char) - base + shift) % 26 + base)
                result.append(encrypted_char)
            else:
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                result.append(decrypted_char)
        else:
            result.append(char)
    
    return ''.join(result)

def main():
    text = input("Masukkan teks: ")
    key = input("Masukkan kunci (hanya huruf): ")
    
    # Mengubah teks dan kunci menjadi huruf besar
    text = text.upper()
    key = key.upper()
    
    # Mengulang kunci agar sesuai dengan panjang teks
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    
    encrypted_text = vigenere_cipher(text, key, encrypt=True)
    decrypted_text = vigenere_cipher(encrypted_text, key, encrypt=False)
    
    print("\nTeks yang telah dienkripsi:", encrypted_text)
    print("Teks yang telah didekripsi:", decrypted_text)

if __name__ == "__main__":
    main()
