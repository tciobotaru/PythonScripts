#!/usr/bin/env python
import argparse
import platform
import getpass
import socket
import os
import psutil
import distro

def get_distro():
    name, version, codename = distro.linux_distribution(full_distribution_name=False)
    print(f"Distro: {name} {version} ({codename})")

def get_memory():
    mem = psutil.virtual_memory()
    print(f"Memory Total: {mem.total // (1024**2)} MB")
    print(f"Memory Used: {mem.used // (1024**2)} MB")
    print(f"Memory Free: {mem.available // (1024**2)} MB")

def get_cpu():
    print(f"CPU Model: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)} physical / {psutil.cpu_count(logical=True)} logical")
    freq = psutil.cpu_freq()
    if freq:
        print(f"CPU Speed: {freq.current:.2f} MHz")
    else:
        print("CPU Speed: N/A")

def get_user():
    print(f"Current User: {getpass.getuser()}")

def get_load():
    load1, load5, load15 = os.getloadavg()
    print(f"Load Average (1, 5, 15 min): {load1}, {load5}, {load15}")

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Information Script")
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
