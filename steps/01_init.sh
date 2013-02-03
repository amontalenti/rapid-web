echo "installing pip"
sudo easy_install pip
echo "installing virtualenv"
sudo pip install virtualenv
echo "creating virtualenv"
virtualenv rapid-env
echo "now, activate with: source rapid-env/bin/activate"
