import hashlib
import time
import os


def calculate_file_hash(file_path, hash_algorithm='sha256'):
    try:
        hasher = hashlib.new(hash_algorithm)
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(4096)  # Read file in 4KB chunks
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
        return None


def store_initial_hashes(file_list):
    initial_hashes = {}
    if not file_list:
        print("Warning: No files provided for monitoring.")
        return initial_hashes

    print("Calculating initial hashes...")
    for file_path in file_list:
        file_hash = calculate_file_hash(file_path)
        if file_hash:
            initial_hashes[file_path] = file_hash
            print(f"Initial hash calculated for: {file_path}")
    print("Initial hash calculation complete.")
    return initial_hashes


def monitor_files(file_list, initial_hashes, check_interval=5):
    print("\nStarting file monitoring...")
    while True:
        for file_path in file_list:
            current_hash = calculate_file_hash(file_path)
            if current_hash:
                print(f"Checking {file_path}:")
                print(f"  Current Hash: {current_hash}")
                if file_path in initial_hashes:
                    print(f"  Initial Hash: {initial_hashes[file_path]}")
                    if current_hash != initial_hashes[file_path]:
                        print(f"  *** Change detected in: {file_path} ***")
                        print(f"    Old Hash: {initial_hashes[file_path]}")
                        print(f"    New Hash: {current_hash}")
                        initial_hashes[file_path] = current_hash
                    else:
                        print("  No change detected.")
                else:
                    print(f"  Warning: {file_path} was not in the initial list. Calculating and storing its hash.")
                    initial_hashes[file_path] = current_hash
            else:
                print(f"Could not calculate hash for {file_path}.")

        time.sleep(check_interval)


if __name__ == "__main__":
    files_to_monitor = [
        r'C:\Users\gogul\OneDrive\New folder\OneDrive\Documents\document.txt',
        r'C:\Users\gogul\OneDrive\New folder\OneDrive\Documents\document2.txt'
    ]
    # Replace with your actual file paths

    # Create some dummy files for testing if they don't exist
    os.makedirs('folder', exist_ok=True)
    for f in files_to_monitor:
        if not os.path.exists(f):
            with open(f, 'w') as temp_file:
                temp_file.write(f"This is a dummy file: {f}")

    initial_hash_values = store_initial_hashes(files_to_monitor)

    if initial_hash_values:
        monitor_files(files_to_monitor, initial_hash_values, check_interval=7)  # Set check interval to 3 seconds for testing
    else:
        print("No initial hashes were calculated. Monitoring cannot start.")
