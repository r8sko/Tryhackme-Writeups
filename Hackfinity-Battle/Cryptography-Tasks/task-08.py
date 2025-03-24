


decrypted_data = bytearray()

repeating = 0x4f524445523a # "ORDER:"

text = 0x1c1c01041963 # "First 6 bytes of the given xor encrypted data"

key = repeating ^ text # This step produces an integer which is the actual xor key in int

full_encrypted_data = '1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60'

encrypted_data = bytes.fromhex(full_encrypted_data)

key_bytes = key.to_bytes((key.bit_length() + 7) // 8, byteorder='big')  # Convert key to bytes

for i in range(len(encrypted_data)):
    decrypted_data.append(encrypted_data[i] ^ key_bytes[i % len(key_bytes)])

decrypted_text = decrypted_data.decode('utf-8', errors='ignore')

print(decrypted_data)