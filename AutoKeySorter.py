import re, sys
filename = "test.txt"
with open(filename) as f:
    for line in f:
        line = line.strip()
        matches = re.finditer(r"(\w{5}-){2}\w{5}", line) 
        with open('2.txt', 'a') as f:
            for match in (matches):
                sys.stdout = f
                print ("{match}".format(match = match.group()))

   
