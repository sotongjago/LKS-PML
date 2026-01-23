import base64

flag = "LKSPML{berlapis_lapis_gini_udah_aman_kan}"

def encode_base64_100x(input_string):
    encoded = input_string
    for _ in range(50):
        encoded = base64.b64encode(encoded.encode('utf-8')).decode('utf-8')
    return encoded

encoded_flag = encode_base64_100x(flag)

with open("secret.txt", "w") as file:
    file.write(encoded_flag)

print("Encoding selesai dan hasil disimpan dalam file secret.txt")