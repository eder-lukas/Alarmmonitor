import os
import subprocess
import platform

def _ping(host) -> bool:
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', param, '1', host]

    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # return true for success
    return response.returncode == 0

def connected_to_internet() -> bool:
    """
    returns true, if google.com can be pinged
    """
    return _ping("google.com")