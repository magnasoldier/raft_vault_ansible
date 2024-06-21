import subprocess


def read_keys(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    keys = []
    for line in lines:
        if line.startswith("Unseal Key"):
            keys.append(line.split(": ")[1].strip())
    
    return keys


def unseal_vault(key):
    result = subprocess.run(['vault', 'operator', 'unseal', key], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully unsealed with key: {key}")
    else:
        print(f"Failed to unseal with key: {key}. Error: {result.stderr}")


if __name__ == "__main__":
    file_path = '/tmp/keys.txt' 
    keys = read_keys(file_path)
    
    if len(keys) < 3:
        print("Error: Not enough keys found in the file.")
    else:
        for i in range(3):
            unseal_vault(keys[i])
