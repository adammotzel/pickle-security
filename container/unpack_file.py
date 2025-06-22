"""
Search current directory recursively for all .pkl files and unpack them. 
Output is written to new text files with '_unpacked' appended to the original 
filename.
"""

import pickletools
from pathlib import Path


current_dir = Path.cwd()

for pkl_file in current_dir.rglob("*.pkl"):

    unpacked_filename = pkl_file.with_name(pkl_file.stem + "_unpacked.txt")

    with pkl_file.open("rb") as in_file, unpacked_filename.open("w") as out_file:
        pickletools.dis(in_file, out_file)

    print(f"Unpacked: {pkl_file} to {unpacked_filename}")

print("\nAll pickle files unpacked.\n")
