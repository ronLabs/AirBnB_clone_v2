#!/usr/bin/python3
"""This module contains a fabric script that
deploys static content to web servers"""
from fabric.api import env, put, local, run
from datetime import datetime as dt
from os import path

env.hosts = ['34.138.88.191', '3.91.150.97']


def do_pack():
    """This function packs the contents of web_static into a tgz archive"""
    td = dt.utcnow()
    tgzname = 'versions/web_static_{}{}{}{}{}{}.tgz'\
        .format(td.year, td.month, td.day, td.hour, td.minute, td.second)

    if local('mkdir -p versions').failed:
        return None
    if local('tar -czvf {} web_static'.format(tgzname)).failed:
        return None
    return tgzname


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


def deploy():
    """This function deploys the content to a server"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
