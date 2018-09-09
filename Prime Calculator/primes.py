import time
import csv
import sys
import random
import os
from time import sleep
start = time.time()


Author = "Oliver"
Version = "Version 1.0"
Name = "Zenflex®"
print(Name + " -" + "\nVersion: " + Version + "\nAuthor: " + Author)



def calculator():
    amo = int(input("What number do you want to find primes up to?:\n"))
    primes = []

    for x in range(2, ++amo):
        prime = True
        for y in range(2, int(x ** 0.5) + 1):
            if x % y == 0:
                prime = False
                break

        if prime:
            primes.append(x)

    print(primes)
        
    end = time.time()
    print(end - start, "- Execution time")

calculator()

