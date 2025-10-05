import os
import platform
import pprint

def get_system_info():
    info={
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        
    }
    return info

pprint.pprint(get_system_info())