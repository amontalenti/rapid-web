from fabric.api import *

env.use_ssh_config = True
env.hosts = ["shared@hacknode"]

@task
def list_home():
    """List files in home directory."""
    run("ls -lha")
