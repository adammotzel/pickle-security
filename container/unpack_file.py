"""
Search current directory recursively for all .pkl files and unpack them. 
Output is written to new text files with '_unpacked' appended to the original 
filename.
"""

import pickletools
from pathlib import Path


# 5 MB limit -- can be changed
MAX_SIZE_BYTES = 5 * 1024 * 1024

current_dir = Path.cwd()

for pkl_file in current_dir.rglob("*.pkl"):

    # skip symbolic links
    if not pkl_file.is_file() or pkl_file.is_symlink():
        continue

    # skip large files
    if pkl_file.stat().st_size > MAX_SIZE_BYTES:
        print(f"Skipped {pkl_file}: file too large")
        continue

    unpacked_filename = pkl_file.with_name(pkl_file.stem + "_unpacked.txt")

    try:
        with pkl_file.open("rb") as in_file, unpacked_filename.open("w") as out_file:
            pickletools.dis(in_file, out_file)
        print(f"Unpacked: {pkl_file} to {unpacked_filename}")
    except Exception as e:
        print(f"Failed to unpack {pkl_file}: {e}")

print("\Process complete.\n")
