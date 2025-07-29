#!/bin/bash

# delete container, if it exists
docker rm -f inspect-pkl 2>/dev/null

# delete image, if it exists
docker image rm pkl-inspection 2>/dev/null

# delete all pickle files from /container
rm -f container/*.pkl container/*_unpacked.txt

echo "Cleanup complete."
