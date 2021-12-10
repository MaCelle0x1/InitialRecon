import os
import subprocess

print('Enter the IP address you would like to scan:') 
trgt = input()

scan = subprocess.run(["nmap", "-sC", "-sV", trgt], stdout=subprocess.PIPE, text=True, input=trgt)

gobust = subprocess.run(["gobuster", "dir", "-u", "http://" + trgt, "-w", "/home/kali/Desktop/wordlists/dirbuster/directory-list-2.3-medium.txt", "-t", "150"], stdout=subprocess.PIPE, text=True, input=trgt)

print(scan.stdout)
print(gobust.stdout)