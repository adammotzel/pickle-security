# Pickle Security
A simple method for securely reading contents of pickle files using an isolated Docker container.

Steps to run this code:

1. Ensure `docker` daemon is running (you can just launch the desktop app)
2. Execute `run.py`

`run.py` builds a Docker image using the `Dockerfile` file, then creates a Docker container using the image and bind mounts `container`.

The container will execute `container/unpack_file.py`, which reads a `pkl` file (using `pickletools`) and unpacks it into a `txt` file in the mounted directory. Both the container and the image are deleted upon successful execution of `run.py`.

After deserializing the pickle file, you can explore its contents in `container/contents.txt`. This may help you identify malicious code in the pickle file that you wouldn't want executed in your host system.

When analyzing, certain opcodes can indicate potentially malicious code or suspicious behavior, especially if the pickled data comes from an untrusted source. Here are some opcodes to watch for:

### 1. GLOBAL
- **Purpose**: References a class or function from a module.
- **Malicious Indicator**: If the global object is from a suspicious or unexpected module, it could lead to execution of harmful code when the module is imported.

### 2. REDUCE
- **Purpose**: Indicates that an object can be constructed using a callable (e.g., a class constructor).
- **Malicious Indicator**: If used with unexpected classes or functions, it may indicate an attempt to execute arbitrary code during unpickling.

### 3. CALL
- **Purpose**: Calls a callable object with specified arguments.
- **Malicious Indicator**: A `CALL` opcode could invoke arbitrary functions, especially if the function being called is not well-known or is from an untrusted source.

### 4. SETITEM / APPEND
- **Purpose**: Used to populate collections (lists, dictionaries).
- **Malicious Indicator**: If these opcodes are used in a way that constructs unexpected or harmful data structures, it may signal malicious intent.

### 5. INST
- **Purpose**: Creates an instance of a class.
- **Malicious Indicator**: Instances of classes that are not expected or are from untrusted modules can lead to malicious behavior.

### 6. EXEC
- **Purpose**: Executes a code object.
- **Malicious Indicator**: If this opcode appears, it can execute arbitrary code, posing a significant security risk.

### 7. PUT
- **Purpose**: Stores a value in a local variable.
- **Malicious Indicator**: Storing unexpected values can indicate manipulation of the local state, potentially leading to harmful consequences.

### 8. BUILD
- **Purpose**: Constructs an object from its attributes after unpacking.
- **Malicious Indicator**: If the construction process involves unexpected classes or attributes, it can indicate attempts to manipulate objects in harmful ways.

### General Cautions
- **Imported Modules**: Pay attention to any imported modules referenced by `GLOBAL` or `INST` opcodes. If they are common libraries but not expected in your context, investigate further.
- **Complexity**: The more complex the pickle (using many of the above opcodes), the more likely it is to be used for malicious purposes. Simple data structures are generally safer.
- **Source Verification**: Always verify the source of the pickle data before unpickling. Consider using safer serialization formats (like JSON) for untrusted data.

Be particularly cautious with any opcode that involves executing code, constructing objects, or referencing external modules. Always treat unpickling from untrusted sources as a security risk, and consider safer alternatives whenever possible. Using an isolated environment, such as a Docker container, is a safe approach to reviewing potentially malicious code. 

It’s important to note that while Docker provides isolation, it doesn’t make unpickling inherently safe. This repository simply demonstrates how using an isolated Docker container can add an extra layer of security when unpacking pickle files.
