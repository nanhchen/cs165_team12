# team13:   $1$UT1CXi18$g65Loe8z1eyhdYsuW5lFs1:16653:0:99999:7:::
# salt = $1$UT1CXi18$

#import crypt
import itertools
import string

chars = string.ascii_lowercase
target_hash = '$1$UT1CXi18$g65Loe8z1eyhdYsuW5lFs1:16653:0:99999:7:::'
salt = '$1$UT1CXi18$'

file1 = 'pwd_123.txt'
file2 = 'pwd_4.txt'
file3 = 'pwd_5.txt'
file4 = 'pwd_6.txt'

# with open(file1, 'w') as file:
#     for length in range(1, 4):
#         for combo in itertools.product(chars, repeat=length):
#             password = ''.join(combo)
#             file.write(password + '\n')

with open(file2, 'w') as file:
    for combo in itertools.product(chars, repeat=4):
        password = ''.join(combo)
        file.write(password + '\n')

# with open(file3, 'w') as file:
#     for combo in itertools.product(chars, repeat=5):
#         password = ''.join(combo)
#         file.write(password + '\n')

# with open(file4, 'w') as file:
#     for combo in itertools.product(chars, repeat=6):
#         password = ''.join(combo)
#         file.write(password + '\n')


# Experimenting =================================================================

# for length in range(1, 7):
#     for combo in itertools.product(chars, repeat=length):
#         password = ''.join(combo)
#         hashed_pwd = crypt.crypt(password, salt)
#         # check if input pwd hash matches with hash stored in etc_shadow
#         if (hashed_pwd == target_hash):
#             print('PASSWORD CRACKED')
#             cracked_pwd = password

# print(f"Cracked Password: {cracked_pwd}")