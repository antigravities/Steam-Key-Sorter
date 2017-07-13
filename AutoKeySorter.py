#!/usr/bin/python

import re, sys

# Defaults
input_file = "filename.txt";
output_file = "2.txt";

if len(sys.argv) >= 2:
    input_file = sys.argv[1];

if len(sys.argv) >= 3:
    output_file = sys.argv[2];

try:
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            matches = re.finditer(r"(\w{5}-){2}\w{5}", line)
            with open(output_file, 'a') as f:
                for match in (matches):
                    sys.stdout = f
                    print ("{match}".format(match = match.group()))
                f.close();
        f.close();
except IOError:
    print("Could not open " + input_file + ". Does it exist?");
    print("Hint: if you'd like to specify the file to open, specify it as the first argument.");
