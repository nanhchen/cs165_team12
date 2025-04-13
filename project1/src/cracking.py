import itertools
from passlib.hash import md5_crypt
import time
from multiprocessing import Pool, cpu_count
import string

target_hash = '$1$UT1CXi18$g65Loe8z1eyhdYsuW5lFs1'
mysalt = 'UT1CXi18'

chars = string.ascii_lowercase  
max_length = 6  
output_file = "attempted_pwds_6.txt"  


def trial(password):
    hasher = md5_crypt.using(salt=mysalt)
    hashed_password = hasher.hash(password)
    
    if hashed_password == target_hash:
        return password 
    
    return None

# Function to write a batch of passwords to the output file
def write_to_file(passwords):
    with open(output_file, "a") as file:
        for password in passwords:
            file.write(password + '\n')

# Generate all possible passwords up to max_length
def generate_passwords(chars, max_length):
    for length in range(1, max_length + 1):
        for password in itertools.product(chars, repeat=length):
            yield ''.join(password)

# Function to try passwords and write to file every 1000 attempts
def crack_passwords(passwords):
    password_batch = []  # Buffer to hold passwords before writing to file
    password_count = 0  # Keep track of the number of passwords processed

    for password in passwords:
        result = trial(password)
        if result:
            print(f"SUCCESS: Password found: {result}")
            return result

        # Collect passwords and write to file every 1000 attempts
        password_batch.append(password)
        password_count += 1

        if password_count % 1000 == 0:
            write_to_file(password_batch)
            password_batch.clear()  # Clear the batch after writing

    print("FAIL: Password not found")

# Main function to orchestrate the process
def main():
    # Start measuring time
    start_time = time.time()
    
    passwords = generate_passwords(chars, max_length)
    crack_passwords(passwords)

    # Time elapsed
    end_time = time.time()
    time_elapsed = end_time - start_time
    hours = int(time_elapsed // 3600)
    minutes = int((time_elapsed % 3600) // 60)
    seconds = int((time_elapsed % 60))
    print(f"Time taken: {hours}h {minutes}m {seconds}s")

if __name__ == '__main__':
    main()