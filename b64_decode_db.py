import base64

with open("Database1337", 'r') as b64encoded_dmpfile:

    binary_data = b64encoded_dmpfile.read()

decode_binary_data = base64.b64decode(binary_data)

with open('Database1337', 'wb') as binary_file:

    binary_file.write(decode_binary_data)