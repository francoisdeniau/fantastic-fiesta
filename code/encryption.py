from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open('key.key', 'wb')
file.write(key)
file.close()


dataset = 'dataset.csv'
dataset_crypted = 'dataset.crypt'

with open(dataset, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(dataset_crypted, 'wb') as f:
    f.write(encrypted)
