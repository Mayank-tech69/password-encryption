import rsa

(public_key, private_key) = rsa.newkeys(2048)

with open("public_key.pem", "wb") as f:
    f.write(public_key.save_pkcs1())

with open("private_key.pem", "wb") as f:
    f.write(private_key.save_pkcs1())

with open("public_key.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

file_path = input("Enter the path to the text file: ")

try:
    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = rsa.encrypt(data, public_key)

    with open("encrypted_data.txt", "wb") as f:
        f.write(encrypted_data)

    print("Data encrypted successfully!")

    private_key_path = input("Enter the path to the private key file: ")

    try:
        with open(private_key_path, "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())

        decrypted_data = rsa.decrypt(encrypted_data, private_key)

        with open("decrypted_data.txt", "wb") as f:
            f.write(decrypted_data)

        print("Data decrypted successfully!")

    except FileNotFoundError:
        print("Private key file not found!")

except FileNotFoundError:
    print("File not found!")