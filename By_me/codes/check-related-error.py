import sys
import re

logfile = sys.argv[1]
pids = {} #empty dictionary to count PIDS which is repeated
with open(logfile) as file:
    for line in file:
        if "nautilus" not in line:
            continue #continue the for loop if the word is not found
        pattern = r"\[(\d+)\]"
        result = re.search(pattern, line)
        if result is None:
            continue
        pids[result[1]] = pids.get(result[1], 0) +1 #to count how many times we get the same PID
print(pids) 
