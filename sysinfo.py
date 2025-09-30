#!/usr/bin/env python3
import argparse
import subprocess
import getpass


def run_cmd(cmd):
    """Run a shell command and return its output."""
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return result.stdout.strip() if result.returncode == 0 else f"Error running {cmd}"

def get_distro():
    print("Distro:", run_cmd("lsb_release -d | cut -f2"))

def get_memory():
    print(run_cmd("free -m"))

def get_cpu():
    print("CPU Info:")
    print(run_cmd("lscpu | egrep 'Model name|CPU(s)|Core|MHz'"))

def get_user():
    print(f"Current User: {getpass.getuser()}")

def get_load():
    print("Load Average:", run_cmd("uptime | awk -F'load average:' '{print $2}'"))

def get_ip():
    ip = run_cmd("hostname -I | awk '{print $1}'")
    print(f"IP Address: {ip}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Information Script (Linux commands version)")
    parser.add_argument("-d", action="store_true", help="Show distro info")
    parser.add_argument("-m", action="store_true", help="Show memory info")
    parser.add_argument("-c", action="store_true", help="Show CPU info")
    parser.add_argument("-u", action="store_true", help="Show current user")
    parser.add_argument("-l", action="store_true", help="Show load average")
    parser.add_argument("-i", action="store_true", help="Show IP address")
    args = parser.parse_args()

    if args.d: get_distro()
    if args.m: get_memory()
    if args.c: get_cpu()
    if args.u: get_user()
    if args.l: get_load()
    if args.i: get_ip()

    if not any(vars(args).values()):
        parser.print_help()
