# Pickle Security

This repository demonstrates how using an isolated, tightly sandboxed Docker container can add extra security when unpacking pickle files. It does not make unpickling *inherently* safe.

## Requirements

- Python 3+
- **Docker** (must be installed and running)
- A bash-compatible shell

## Running the Code

Steps to run this code:

1. Ensure Docker daemon is running (you can just launch the desktop app)
2. Upload your `pkl` files to the `container/` directory 
3. Execute `scripts/run.sh`

The `run.sh` script builds a Docker image using the `Dockerfile`, then creates a Docker container using the image with strict isolation and security settings.

The container will execute `container/unpack_file.py`, which reads all `pkl` files in the mounted `container/` directory (using `pickletools`) and unpacks them into `txt` files. The container is deleted upon successful execution of `run.sh`.

After deserializing the pickle files, you can explore their contents in the `txt` files. This may help you identify malicious code that you wouldn't want executed in your host system.

You can clean up the remaining artifacts by executing `scripts/cleanup.sh` (`pkl` files, `txt` files, Docker image, etc.).

## Opcodes

See [docs/OPCODES.md](docs/OPCODES.md) for details on opcodes to look out for.
