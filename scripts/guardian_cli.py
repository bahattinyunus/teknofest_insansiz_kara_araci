#!/usr/bin/env python3
"""
Gökbörü Guardian AI - Terminal Interface
A cinematic terminal script that outputs dramatic loading screens and matrices.
Runs a fake diagnostic to give the project a high-tech "WOW" factor.
"""

import time
import sys
import random
import ctypes
import os

# Terminal colors for dramatic effect
class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# Fallback for Windows terminal colors
if os.name == 'nt':
    os.system('color')

def p(text, color=Colors.CYAN, delay=0.03, newline=True):
    sys.stdout.write(color)
    sys.stdout.flush()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write(Colors.RESET + '\n')
    else:
        sys.stdout.write(Colors.RESET)
    sys.stdout.flush()

def matrix_stream(lines=15, width=80):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"
    for _ in range(lines):
        line = "".join(random.choice(chars) if random.random() > 0.5 else " " for _ in range(width))
        sys.stdout.write(Colors.GREEN + line + Colors.RESET + '\n')
        time.sleep(0.05)

def loading_bar(text, duration=2.0, length=40):
    sys.stdout.write(f"{Colors.CYAN}[*] {text} {Colors.RESET}[")
    sys.stdout.flush()
    steps = int(duration / 0.1)
    bar_step_size = length / steps if steps > 0 else length
    
    current_length = 0
    for i in range(steps):
        while current_length < (i + 1) * bar_step_size and current_length < length:
            sys.stdout.write(f"{Colors.GREEN}={Colors.RESET}")
            sys.stdout.flush()
            current_length += 1
        time.sleep(0.1)
    
    while current_length < length:
         sys.stdout.write(f"{Colors.GREEN}={Colors.RESET}")
         sys.stdout.flush()
         current_length += 1
         
    sys.stdout.write(f"] {Colors.YELLOW}DONE{Colors.RESET}\n")

def run():
    os.system('cls' if os.name == 'nt' else 'clear')
    p("\n" + "="*60, Colors.CYAN, 0.01)
    p("  WAKE UP, GÖKBÖRÜ. / / SYSTEM INITIATION PROTOCOL", Colors.BOLD + Colors.CYAN, 0.05)
    p("="*60 + "\n", Colors.CYAN, 0.01)
    
    time.sleep(1)
    
    p("[!!!] UNAUTHORIZED ACCESS DETECTED", Colors.RED, 0.02)
    time.sleep(0.5)
    p("Bypassing security protocols...", Colors.YELLOW, 0.03)
    time.sleep(0.5)
    
    matrix_stream(10)
    
    p("\n[+] ACCESS GRANTED. WELCOME, COMMANDER.", Colors.GREEN, 0.05)
    time.sleep(1)
    
    print("\n")
    loading_bar("Calibrating Wayfinder DVL Sub-systems", 1.5)
    loading_bar("Loading YoloV8 Nano TensorRT Engine", 2.2)
    loading_bar("Synchronizing SLAM Depth Point Clouds", 1.8)
    loading_bar("Aligning PID Control Loops to Vector [X:Y:Z]", 1.2)
    loading_bar("Establishing Secure Tactical Comm Link", 1.0)
    
    print("\n")
    p(">> NEURAL NETWORK ARCHITECTURE: STABLE", Colors.GREEN, 0.02)
    p(">> SENSOR FUSION ENGINE: ONLINE", Colors.GREEN, 0.02)
    p(">> WEAPONS/RESCUE PAYLOAD: ARMED & READY", Colors.YELLOW, 0.02)
    
    print("\n")
    p("="*60, Colors.CYAN, 0.01)
    p("        GÖKBÖRÜ SOTM IS NOW FULLY AUTONOMOUS", Colors.BOLD + Colors.CYAN, 0.05)
    p("="*60, Colors.CYAN, 0.01)
    print("\n")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] INITIATION ABORTED BY USER.{Colors.RESET}")
