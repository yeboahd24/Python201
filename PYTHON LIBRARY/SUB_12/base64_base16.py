import base64

original_data = b'This is the data, in the clear.'
print('Original:', original_data)
encoded_data = base64.b16encode(original_data)
print('Encoded :', encoded_data)
decoded_data = base64.b16decode(encoded_data)
print('Decoded :', decoded_data)
