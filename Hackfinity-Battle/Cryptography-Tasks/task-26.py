class Encryption:

    def __init__(self):
        pass

    def encrypt_func(self, plaintext):
        encrypted_text = []

        for i, c in enumerate(plaintext):
            if c.isalpha():
                if c.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                
                subtracted = ord(c) - base
                shifted = (subtracted + i) % 26
                modified = shifted + base
                final = chr(modified)
                encrypted_text.append(final)
            else:
                encrypted_text.append(c)

        return "".join(encrypted_text)



class Decryption:

    def __init__(self):
        pass

    def decrypt_func(self, ciphertext):

        decrypted_text = []

        for i, c in enumerate(ciphertext):
            if c.isalpha():
                if c.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                subtracted = ord(c) - base
                shifted = (subtracted - i) % 26
                modified = shifted + base
                final = chr(modified)
                decrypted_text.append(final)
            else:
                decrypted_text.append(c)

        return "".join(decrypted_text)



encrypted_message = 'a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm'

encrypted = Encryption().encrypt_func("Hello")

print(encrypted)

decrypted = Decryption().decrypt_func(encrypted_message)

print(decrypted)