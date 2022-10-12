from utils import *


def __main__():
    print("Enter the ciphertext:\n")
    ciphertext = input()

    print("Guessing key length...\n")
    t = guess_key_length(ciphertext, 24)[0][0]
    print(f"Key length is most likely: {t}")

    print("Guessing key...\n")
    k = translate_key(guess_key(ciphertext, t))
    print(f"Key is most likely: {k}")

    print("Decrypting ciphertext with the key...\n")
    plaintext = decrypt(ciphertext, k)
    print(f"My plaintext guess is: {plaintext}")


__main__()
