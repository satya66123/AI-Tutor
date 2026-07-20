import os

print("Executable:", os.sys.executable)

for key in sorted(os.environ):
    if "OPENAI" in key.upper():
        print(key, "=", os.environ[key])