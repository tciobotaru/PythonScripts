#!/usr/bin/python3.11

import sys
from collections import Counter
import re

def parse_accesss_log(filename) :
    try:
      with open(filename, 'r') as f:
         lines=f.readlines()
    except FileNotFoundError:
       print(f"Error:File {filename} not found")
       return

    user_agents=[]

    pattern=r'\"([^\"]*)\"\s*$'

    for line in lines:
       match=re.search(pattern,line)
       if match:
          user_agent=match.group(1)
          user_agents.append(user_agent)

    counter=Counter(user_agents)
    print(f"Total number of different User Agents: {len(counter)}")
    print("\nRequests per User Agent:")
    for agent, count in counter.items():
        print(f"{agent}: {count}")          
if __name__ == "__main__":
   if len(sys.argv) != 2:
      print("Invalid number of arguments")
   else:
      parse_accesss_log(sys.argv[1])           
