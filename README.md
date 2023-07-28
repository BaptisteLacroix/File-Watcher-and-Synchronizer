# File Watcher and Synchronizer

### Overview

The "File Watcher and Synchronizer" is a Python script designed to monitor changes in a specific file in a directory and synchronize it with a corresponding file located in a Windows Subsystem for Linux (WSL) directory. This script is useful when working with shared files between a Windows host and a WSL environment, allowing seamless synchronization of the designated file.

### Use Case

Suppose you have a file named "export.json" that needs to be synchronized between the current working directory (download directory) on the Windows host and a specific directory in the WSL environment. Instead of manually copying the file back and forth whenever changes are made, this script automates the synchronization process, ensuring that the file is always up-to-date in both locations.

### How It Works

1. The script listens for modifications in the current working directory (download directory) on the Windows host.

2. When the "export.json" file is modified in the download directory, the script detects the change using the `watchdog` library.

3. Upon detecting the modification, the script automatically copies the updated "export.json" file to the specified WSL directory.

### Configuration

- `directory_to_listen`: The path of the directory to be monitored for changes. By default, it is set to the current working directory (".").

- `wsl_directory`: The path of the specific directory in the WSL environment where the "export.json" file will be synchronized. Modify this path to match your WSL environment.

- `filename_to_listen`: The name of the file to be monitored for changes. By default, it is set to "export.json".

### Prerequisites

- Python 3.x should be installed on your system.

- Install the `watchdog` library using the following command:

  ```
  pip install watchdog
  ```

### How to Use

1. Save the script to a Python file (e.g., "file_watcher.py") in the same directory as the "export.json" file you want to synchronize.

2. Open a terminal or command prompt and navigate to the directory where the script and "export.json" are located.

3. Run the script using the following command:

   ```
   python file_watcher.py
   ```

4. The script will start watching for changes in the current directory. Whenever "export.json" is modified, it will automatically synchronize the updated file with the corresponding file in the specified WSL directory.

5. To stop the script, press `Ctrl + C`.

### Note

- The script will display a message whenever a change is detected and synchronized.

- Make sure to update the `wsl_directory` variable with the correct path to your desired directory in the WSL environment.

- Avoid renaming the script file while it is running, as it may affect the file synchronization process.

### Disclaimer

This script assumes that the specified file ("export.json") and directories exist in their respective locations. Additionally, it is designed for the specific use case of synchronizing a single file between a Windows host and a WSL environment. Modifying the script to handle multiple files or different synchronization scenarios may require additional customization.

---

Developed by Lacroix Baptiste
