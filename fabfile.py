from fabric.api import *
from fabric.contrib.project import rsync_project

env.use_ssh_config = True
env.hosts = ["shared@hacknode"]

TEAM_NAME = "hacknode1"

@task
def list_home():
    """List files in home directory."""
    run("ls -lha")

@task
def list_servers():
    """List deployment servers."""
    run("ls servers")

def virtualenv_run(cmd):
    run("source rapid-env/bin/activate && {}".format(cmd))

@task
def setup_virtualenv():
    """Set up virtualenv on remote machine."""
    with cd("servers/" + TEAM_NAME):
        run("virtualenv rapid-env")
        virtualenv_run("pip install -r requirements.txt")

@task
def run_devserver():
    """Run the dev Flask server on remote machine."""
    with cd("servers/" + TEAM_NAME):
        virtualenv_run("cd app && python app.py runserver --host=0.0.0.0 --port=8000")

@task
def deploy():
    """Deploy project remotely."""
    run("mkdir -p servers")
    rsync_project(remote_dir="servers/" + TEAM_NAME,
                  local_dir="./",
                  exclude=("*.pyc", ".git", "rapid-env", "steps", "activate"))

def supervisor_run(cmd):
    sudo("supervisorctl {}".format(cmd), shell=False)

@task
def restart():
    """Restart supervisor service."""
    supervisor_run("restart {}".format(TEAM_NAME))
    run("sleep 1")
    supervisor_run("tail -800 {}".format(TEAM_NAME))

