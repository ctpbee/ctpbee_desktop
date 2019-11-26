import os
from pathlib import Path


def _get_trader_dir(temp_name: str):
    """
    Get path where trader is running in.
    """
    cwd = Path.cwd()
    temp_path = cwd.joinpath(temp_name)
    if temp_path.exists():
        return cwd, temp_path
    # Otherwise use home path of system.
    home_path = Path.home()

    temp_path = home_path.joinpath(temp_name)
    if not temp_path.exists():
        temp_path.mkdir()
    return home_path, temp_path


def get_folder_path(folder_name: str):
    """
    Get path for temp folder with folder name.
    """
    TRADER_DIR, TEMP_DIR = _get_trader_dir(".ctpbee")
    folder_path = TEMP_DIR.joinpath(folder_name)
    if not folder_path.exists():
        os.makedirs(folder_path)
    return folder_path


desktop_path = str(get_folder_path('ctpbee_desktop'))
path = os.path.join(desktop_path, 'ticks')
if not os.path.exists(path):
    os.mkdir(path)
user_account_path = os.path.join(desktop_path, 'user_account.json')


def init_file():
    for i in [user_account_path]:
        if not os.path.exists(i):
            with open(i, 'w'):
                pass
