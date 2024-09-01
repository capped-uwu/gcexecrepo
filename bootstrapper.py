import os
import requests
import zipfile
import subprocess
from io import BytesIO
import sys

APPDATA_PATH = os.getenv('APPDATA')
GCEDEXC_DIR = os.path.join(APPDATA_PATH, 'gcexec')
VERSION_FILE = os.path.join(GCEDEXC_DIR, 'version')
VERSION_URL = 'https://raw.githubusercontent.com/capped-uwu/gcexecrepo/main/version'
BASE_DOWNLOAD_URL = 'https://github.com/capped-uwu/gcexecrepo/releases/download'

def get_remote_version():
    try:
        response = requests.get(VERSION_URL)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error fetching remote version: {e}")
        return None

def get_local_version():
    if not os.path.exists(VERSION_FILE):
        return None
    with open(VERSION_FILE, 'r') as file:
        return file.read().strip()

def download_and_extract_zip(url, extract_to):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with zipfile.ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(extract_to)
        print(f"Downloaded and extracted ZIP to {extract_to}")
    except requests.RequestException as e:
        print(f"Error downloading ZIP file: {e}")
    except zipfile.BadZipFile as e:
        print(f"Error extracting ZIP file: {e}")

def update_version_file(version):
    with open(VERSION_FILE, 'w') as file:
        file.write(version)

def run_ui_exe():
    ui_exe_path = os.path.join(GCEDEXC_DIR, 'ui.exe')
    if os.path.exists(ui_exe_path):
        try:
            subprocess.Popen([ui_exe_path], cwd=GCEDEXC_DIR)
            print(f"Executed {ui_exe_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing {ui_exe_path}: {e}")
            sys.exit(1)
    else:
        print(f"{ui_exe_path} not found")
    sys.exit(0)

def main():
    if not os.path.exists(GCEDEXC_DIR):
        os.makedirs(GCEDEXC_DIR)

    local_version = get_local_version()
    remote_version = get_remote_version()

    if remote_version is None:
        print("Failed to get remote version. Exiting.")
        return

    if local_version is None or local_version < remote_version:
        print(f"Updating from version {local_version} to {remote_version}")
        zip_download_url = f"{BASE_DOWNLOAD_URL}/{remote_version}/gcexec.zip"
        download_and_extract_zip(zip_download_url, GCEDEXC_DIR)
        update_version_file(remote_version)
        print(f"Updated to version {remote_version}")
    else:
        print("Already up-to-date.")

    run_ui_exe()

if __name__ == "__main__":
    main()
