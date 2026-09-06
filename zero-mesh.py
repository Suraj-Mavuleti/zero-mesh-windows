#!/usr/bin/env python3
import sys, socket, threading, time, random
def listen_sim():
    while True:
        time.sleep(random.uniform(2.0, 5.0))
        print(f"\n\033[1;35m[Network]: Dropped incoming malformed packet from {random.randint(10,255)}.{random.randint(10,255)}.1.1\033[0m")
        print("\033[1;32mCMD > \033[0m", end='', flush=True)

def main():
    print("\033[1;31m" + "="*60 + "\033[0m")
    print(f"\033[1;31m          {sys.argv[0].split('/')[-1].upper()} CRYPTOGRAPHIC SOCKET ENGINE\033[0m")
    print("\033[1;31m" + "="*60 + "\033[0m")
    t = threading.Thread(target=listen_sim, daemon=True)
    t.start()
    print("\033[3mListening on secure local socket. Type 'status' or 'exit'.\033[0m\n")
    while True:
        try:
            cmd = input("\033[1;32mCMD > \033[0m").strip()
            if cmd == 'exit': break
            if cmd == 'status':
                print("\033[1;33m[Status]: Cryptographic boundaries secured. 0 active peer connections.\033[0m")
            elif cmd:
                print(f"\033[1;31m[Error]: Unrecognized sequence '{cmd}'.\033[0m")
        except: break
if __name__ == '__main__': main()
