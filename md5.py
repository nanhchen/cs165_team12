import hashlib
import itertools
import string

target_hash = "900150983cd24fb0d6963f7d28e17f72"  # MD5 of "abc"
salt = ""

def md5_hash(password: str) -> str:
    return hashlib.md5((salt + password).encode()).hexdigest()

def main():
    for length in range(1, 4):  # Try passwords of length 1 to 3
        for chars in itertools.product(string.ascii_lowercase, repeat=length):
            guess = ''.join(chars)
            print(f"Trying: {guess}")
            if md5_hash(guess) == target_hash:
                print(f"[+] Found: {guess}")
                return

    print("[-] Not found")

if __name__ == "__main__":
    main()
