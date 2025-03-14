def xor_decrypt(ciphertext, key=0x41):
    decrypted = bytearray()
    for c in ciphertext:
        decrypted.append(c ^ key)
    return decrypted



with open("Database1337", 'rb') as dmp_file:

    binary_data = dmp_file.read()


xor_decrypted_data = xor_decrypt(binary_data)


with open("Database1337.kdbx", 'wb') as new_dmp_file:

    new_dmp_file.write(xor_decrypted_data)