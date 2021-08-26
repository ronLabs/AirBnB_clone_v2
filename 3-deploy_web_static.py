#!/usr/bin/python3
"""This module contains a fabric script that
deploys static content to web servers"""
from fabric.api import env, put, run
from datetime import datetime as dt
from os import path
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['35.243.194.38', '54.91.79.148']
path_releases = '/data/web_static/releases'


def deploy():
    """This function deploys the content to a server"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
