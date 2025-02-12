#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean:
"""

from fabric.api import env, local, run, cd, lcd

env.hosts = ['54.208.227.111', '34.201.174.167']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Deletes all unnecessary archives in the versions and releases folders
    """
    number = int(number)
    if number < 1:
        number = 1
    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -f".format(number + 1))
    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
