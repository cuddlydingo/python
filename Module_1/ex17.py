from sys import argv
from os.path import exists

from_file = "test.txt"
to_file = "new_test.txt"

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist?  {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input("> ")

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
