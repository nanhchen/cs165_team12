# cs165_team13
cs165 - computer security

password: msthve 

Number of threads/processes used 
- 8 parallel processes used (one for each file for part_01.txt and so forth)
- each process uses all CPU cores (8 in total) due to Pool(cpu_count())
- 8 * 8 = 64 threads

CPU Model Info
- ARM M3 Chip
- total 8 cores 

Throughput 
- each file has 38,600,000 passwords in each part_01.txt
- 308,915,776 passwords (all 8 files combined)
- total time: 10 hrs aprox = 10 * 60 * 60 = 36,000 sec
- Throughput = Total Passwords / Total Time
             = 308,915,776 / 36,000
             ≈ 8,581 passwords/second

