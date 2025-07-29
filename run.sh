#!/bin/bash

## Run the deserialization process.
## Place your pickle files in the `container/` directory, then execute this script.

## Steps:
## 1. Build image + container
## 2. Mount ./container/ into /app
## 3. Disable all network access inside the container
## 4. Make the entire container filesystem read-only
## 5. Limit the number of processes to 50 (can be more or less)
## 6. Drop all Linux capabilities
## 7. revent processes from gaining extra privileges

if ! find ./container -maxdepth 1 -type f -name "*.pkl" | grep -q .; then
    echo "No .pkl files found in './container'. Aborting process."
    return
fi

docker build -t pkl-inspection .
docker container run --name inspect-pkl \
    --mount type=bind,source="$PWD/container",target=/app \
    --network none \
    --read-only \
    --pids-limit 50 \
    --cap-drop ALL \
    --security-opt no-new-privileges \
    pkl-inspection

docker rm inspect-pkl

echo -e "\nProcess complete.\n"
