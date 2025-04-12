#md5_crypt hashing function from passlib 
from passlib.hash import md5_crypt
#multiprocessing utilities to parallelize work across multiple CPU cores and processes
from multiprocessing import Pool, cpu_count, Manager, Process

target_hash = '$1$UT1CXi18$g65Loe8z1eyhdYsuW5lFs1'
#number of passwords to process in one batch
batch_size = 20000
log_interval = 100000

def check_password(args):
    password, target_hash, shared_flag = args
    
    #if password was already found by another process then stop checking
    if shared_flag.value:
        return None

    #compare current password with target hash using passlib's md5_crypt
    if md5_crypt.verify(password, target_hash):
        #if match found then set the shared flag to 1
        shared_flag.value = 1
        return password

    return None

def crack_file(filename, shared_flag):
    print(f"[>] Cracking started: {filename}")
    total_checked = 0

    #creates a process pool to utilize all CPU cores
    with Pool(cpu_count()) as pool:
        with open(filename, 'r') as f:
            batch = []

            #reads each password from the file
            for line in f:
                if shared_flag.value:
                    #stops when the password is found
                    return  

                password = line.strip()
                if not password:
                    continue

                #append to the current batch
                batch.append((password, target_hash, shared_flag))

                #if the batch is full then process it
                if len(batch) == batch_size:
                    for result in pool.imap_unordered(check_password, batch, chunksize=1000):
                        if result:
                            print(f"[+] Password cracked in {filename}: {result}")
                            shared_flag.value = 1
                            return

                    total_checked += batch_size
                    if total_checked % log_interval == 0:
                        print(f"[{filename}] Checked {total_checked} passwords...")
                    #clears batch for next iteration 
                    batch = [] 

            #process any remaining passwords after the last full batch
            if batch and not shared_flag.value:
                for result in pool.imap_unordered(check_password, batch, chunksize=1000):
                    if result:
                        print(f"[+] Password cracked in {filename}: {result}")
                        shared_flag.value = 1
                        return
                        
    if not shared_flag.value:
        print(f"[-] Password not found in {filename}")

def main():
    #creates a list of filenames 
    files = [f"part_0{i}.txt" for i in range(8)]

    #shared memory object to indicate when a password has been cracked
    manager = Manager()
    shared_flag = manager.Value('i', 0)

    processes = []

    #launch a separate process for each file
    for file in files:
        p = Process(target=crack_file, args=(file, shared_flag))
        p.start()
        processes.append(p)

    #waits for all processes to complete
    for p in processes:
        p.join()

    #final message telling whether password was found or not
    if shared_flag.value == 0:
        print("[-] Password not found in any file.")
    else:
        print("[+] Cracking complete. Terminating all processes.")


if __name__ == "__main__":
    main()
