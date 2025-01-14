#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the do_pack function.
"""

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    Creates a compressed archive of web_static directory
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_" + date + ".tgz"
        source_path = "./web_static"
        dest_path = "./versions/" + file_name
        local("tar -cvzf " + dest_path + " " + source_path)
        return dest_path
    except Exception:
        return None
