# Name: Emily Yu
# Date: 7/18/22
# Description: Microservice that creates Caesar Cipher
#              Outputs .txt file with encrypted key to be used to encrypt messages
import string
import time
import random
while True:
    time.sleep(10)



    with open('encrypt-key.txt','r') as f:
        line = f.readline()
        f.close()
    if line.upper() == 'RUN':
        with open('encrypt-key.txt', 'w') as f:
            # accounts for all uppercase and lowercase letters
            # if only lowercase letters desired, use string.ascii_lowercase
            # if only uppercase letters desired, use string.ascii_uppercase
            letters = string.ascii_letters
            key = ''.join(random.sample(letters, len(letters)))
            f.write(str(key))
            f.close()
    else:
        pass
