import json
import os
import time
import subprocess
from typing import Dict, List

def get_watch_files(file_types: List[str], exclude: List[str]) -> List[str]:
    watch_files: List[str] = []
    # get all dirs, files recursively
    for root, _, files in os.walk("."):
        # check if node_modules is not part of the root path
        excludable: bool = False
        for exclude_type in exclude:
            if exclude_type in root:
                excludable = True
                break
        if excludable: continue
        # get full path of each file
        for file in files:
            for file_type in file_types:
                if file.endswith(file_type):
                    path = os.path.join(root, file)
                    watch_files.append(path)
                    break

    return watch_files

def get_mod_time(file_path : str) -> float:
    return os.path.getmtime(file_path)

def run_process(cmd : str) -> subprocess.Popen:
    print("ARD: %s \n" % (cmd))
    process = subprocess.Popen(cmd.split())
    return process

def check_files(file_to_date : Dict, process : subprocess.Popen, run_cmd: str) -> None:
    while True:
        try:
            time.sleep(200 / 1000)
            for file, date in file_to_date.items():
                current_mod = get_mod_time(file)
                if current_mod > date:
                    file_to_date[file] = current_mod
                    print("\nARD: Detected change in %s !" % (file))
                    print("ARD: Reloading!")
                    process.kill()
                    process = run_process(run_cmd)
        except KeyboardInterrupt:
            process.kill()
            print("ARD: AUTO-RELOAD Stopped")
            return

def main():
    config = None
    with open("./auto_reload.config.json", "r") as f:
        config = json.load(f)
    file_endings: List[str] = config["file_endings"]
    run_cmd: str = config["command"]
    exclude: List[str] = config["exclude"]

    watch_files: List[str] = get_watch_files(file_endings, exclude)
    file_to_date: Dict[str, float] = {}
    for file in watch_files:
        file_to_date[file] = get_mod_time(file)
    
    node_process = run_process(run_cmd)
    check_files(file_to_date, node_process, run_cmd)


if __name__ == "__main__":
    main()
