from fabric.api import *
from fabric.contrib.project import rsync_project

env.use_ssh_config = True
env.hosts = ["shared@hacknode"]

def unique_id():
    def sh(cmd):
        return local(cmd, capture=True)
    return "{}__{}".format(sh("whoami"), sh("hostname"))

@task
def print_my_id():
    """Print your unique identifier."""
    puts("UNIQUE ID: " + unique_id())

@task
def list_home():
    """List files in home directory."""
    run("ls -lha")

@task
def list_deploys():
    """List deployment directories."""
    run("ls deploys")

def virtualenv_run(cmd):
    run("source rapid-env/bin/activate && {}".format(cmd))

@task
def setup_virtualenv():
    """Set up virtualenv on remote machine."""
    with cd("deploys/" + unique_id()):
        run("virtualenv rapid-env")
        virtualenv_run("pip install -r requirements.txt")

@task
def run_devserver():
    """Run the dev Flask server on remote machine."""
    with cd("deploys/" + unique_id()):
        virtualenv_run("cd app && python app.py runserver --host=0.0.0.0 --port=8000")

@task
def deploy():
    """Deploy project remotely."""
    run("mkdir -p deploys")
    rsync_project(remote_dir="deploys/" + unique_id(),
                  local_dir="./",
                  exclude=("*.pyc", ".git", "rapid-env", "steps", "activate"))

