import os
import requests
import zipfile
import subprocess
from io import BytesIO
import sys

os.system('cls')

APPDATA_PATH = os.getenv('APPDATA')
GCEDEXC_DIR = os.path.join(APPDATA_PATH, 'gcexec')
VERSION_FILE = os.path.join(GCEDEXC_DIR, 'version')
VERSION_URL = 'https://raw.githubusercontent.com/capped-uwu/gcexecrepo/main/version'
BASE_DOWNLOAD_URL = 'https://github.com/capped-uwu/gcexecrepo/releases/download'

BOOTSTRAPPER_DIR = os.path.join(APPDATA_PATH, 'gcbootstrapper')
BOOTSTRAPPER_VERSION_FILE = os.path.join(BOOTSTRAPPER_DIR, 'version')
BOOTSTRAPPER_VERSION_URL = 'https://raw.githubusercontent.com/capped-uwu/bootstrpppp/main/version'
BOOTSTRAPPER_DOWNLOAD_URL = 'https://github.com/capped-uwu/bootstrpppp/releases/download'

def get_remote_version(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error fetching remote version from {url}: {e}")
        return None

def get_local_version(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file:
        return file.read().strip()

def download_file(url, destination):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded file to {destination}")
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")

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

def update_version_file(version, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(version)
    except IOError as e:
        print(f"Error updating version file: {e}")

def run_exe(exe_path):
    if os.path.exists(exe_path):
        try:
            process = subprocess.Popen([exe_path], cwd=os.path.dirname(exe_path))
            print(f"Executed {exe_path}")
            sys.exit(0)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {exe_path}: {e}")
            sys.exit(1)
    else:
        print(f"{exe_path} not found")
        sys.exit(1)

def main():
    if not os.path.exists(BOOTSTRAPPER_DIR):
        os.makedirs(BOOTSTRAPPER_DIR)

    bootstrapper_local_version = get_local_version(BOOTSTRAPPER_VERSION_FILE)
    bootstrapper_remote_version = get_remote_version(BOOTSTRAPPER_VERSION_URL)

    if bootstrapper_remote_version is None:
        print("Failed to get remote version for gcbootstrapper. Exiting.")
        return

    current_dir = os.path.dirname(os.path.abspath(__file__))
    bootstrapper_exe_path = os.path.join(current_dir, 'gcbootstrapper.exe')

    if bootstrapper_local_version is None or bootstrapper_local_version < bootstrapper_remote_version:
        print(f"Updating gcbootstrapper from version {bootstrapper_local_version} to {bootstrapper_remote_version}")

        if os.path.exists(bootstrapper_exe_path):
            try:
                os.remove(bootstrapper_exe_path)
                print(f"Deleted old {bootstrapper_exe_path}")
            except OSError as e:
                print(f"Error deleting old {bootstrapper_exe_path}: {e}")

        bootstrapper_download_url = f"{BOOTSTRAPPER_DOWNLOAD_URL}/{bootstrapper_remote_version}/gcbootstrapper.exe"
        download_file(bootstrapper_download_url, bootstrapper_exe_path)
        update_version_file(bootstrapper_remote_version, BOOTSTRAPPER_VERSION_FILE)
        print(f"Updated gcbootstrapper to version {bootstrapper_remote_version}")
        run_exe(bootstrapper_exe_path)
    else:
        print("gcbootstrapper is already up-to-date.")

    if not os.path.exists(GCEDEXC_DIR):
        os.makedirs(GCEDEXC_DIR)

    local_version = get_local_version(VERSION_FILE)
    remote_version = get_remote_version(VERSION_URL)

    if remote_version is None:
        print("Failed to get remote version for gcexec. Exiting.")
        return

    if local_version is None or local_version < remote_version:
        print(f"Updating gcexec from version {local_version} to {remote_version}")
        zip_download_url = f"{BASE_DOWNLOAD_URL}/{remote_version}/gcexec.zip"
        download_and_extract_zip(zip_download_url, GCEDEXC_DIR)
        update_version_file(remote_version, VERSION_FILE)
        print(f"Updated gcexec to version {remote_version}")
    else:
        print("gcexec is already up-to-date.")

    run_exe(os.path.join(GCEDEXC_DIR, 'ui.exe'))

if __name__ == "__main__":
    main()
