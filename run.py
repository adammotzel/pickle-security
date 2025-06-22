"""
Run the deserialization process.

Place your pickle files in the `container/` directory, then execute 
this script.
"""

import subprocess
import os


root = os.getcwd()

commands = [
    "docker build -t pkl-inspection .",
    f"docker container run --name inspect-pkl --mount type=bind,source={root}/container,target=/app --network none pkl-inspection",
    "docker rm inspect-pkl",
    "docker rmi pkl-inspection"
]

for command in commands:
    subprocess.run(command, check=True)

print("\nProcess complete.\n")
