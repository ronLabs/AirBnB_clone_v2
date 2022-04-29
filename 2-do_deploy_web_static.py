#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.138.88.191', '3.91.150.97']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False

    file_ext = archive_path.split("/")[-1]
    file_no_ext = file_ext.split(".")[0]
    path = "/data/web_static/releases/"
    if put(archive_path, '/tmp/{}'.format(file_ext)).failed:
        return False
    if run('mkdir -p {}{}/'.format(path, file_no_ext)).failed:
        return False
    if run('tar -xzf /tmp/{} -C {}{}/'
            .format(file_ext, path, file_no_ext)).failed:
        return False
    if run('rm /tmp/{}'.format(file_ext)).failed:
        return False
    if run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_no_ext)).failed:
        return False
    if run('rm -rf {}{}/web_static'.format(path, file_no_ext)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s {}{}/ /data/web_static/current'
           .format(path, file_no_ext)).failed:
        return False
    return True
