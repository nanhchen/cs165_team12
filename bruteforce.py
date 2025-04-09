import hashlib
import threading

target_hash = "g65Loe8z1eyhdYsuW5lFs1"  # password hash (target)
salt = "UT1CXi18" # salt 
input_file = "pwd_123.txt"
threads = 10 

found = threading.Event()

def md5_hash(password):
    return hashlib.md5((salt + password).encode()).hexdigest()

def worker(start_char):
    for password in passwords: 
        if found.is_set(): 
            return 
        
        if md5_hash(password) == target_hash: 
            print(f"[+] Found: {password}")
            found.set()
            return 

def load_passwords():
    with open(input_file, "r") as f:
        return [line.strip() for line in f if line.strip()]

def split_into_chunks(data, n):
    k, m = divmod(len(data), n)
    return [data[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

def main():
    all_passwords = load_passwords()
    chunks = split_into_chunks(all_passwords, num_threads)

    threads = []
    for chunk in chunks:
        t = threading.Thread(target=worker, args=(chunk,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    if not found.is_set():
        print("[-] Password not found.")

if __name__ == "__main__":
    main()