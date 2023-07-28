import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the paths for the download directory and the specific directory in WSL
directory_to_listen = "."
wsl_directory = "//wsl.localhost/Ubuntu/home/user/JSON_schema/"
filename_to_listen = "export.json"

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Check if the event is for a file and not a directory
        if event.is_directory:
            return
        
        # Get the absolute path of the changed file
        source_file = os.path.abspath(event.src_path)
        
        # Check if the changed file is the one we are interested in
        if os.path.basename(source_file) == filename_to_listen:
            # Construct the destination path in the WSL directory
            destination_file = os.path.join(wsl_directory, os.path.basename(source_file))
            
            # Copy the file from the download directory to the WSL directory
            try:
                shutil.copy2(source_file, destination_file)
                print(f"File copied from {source_file} to {destination_file}")
            except Exception as e:
                print(f"Failed to copy the file: {e}")

def main():
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, directory_to_listen, recursive=True)
    observer.start()

    try:
        print(f"Watching {directory_to_listen} for changes...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
