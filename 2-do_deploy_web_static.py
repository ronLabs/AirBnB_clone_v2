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
    try:
        file_ext = archive_path.split("/")[-1]
        file_no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_ext, path, file_no_ext))
        run('rm /tmp/{}'.format(file_ext))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_no_ext))
        run('rm -rf {}{}/web_static'.format(path, file_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_no_ext))
        return True
    except:
        return False
