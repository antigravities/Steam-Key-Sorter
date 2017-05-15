import re

regex = r"(.{5}-){2}.{5}"

test_str = ("Steam Game - xxxxx-xxxxx-xxxxx")
matches = re.finditer(regex, test_str)
for match in (matches):
    print ("{match}".format(match = match.group()))

input("")


