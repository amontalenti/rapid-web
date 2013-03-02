#!/bin/bash
[[ -z "$1" ]] && echo "must specify port" && exit 1
# requires an activation script in directory above
source ../activate
# makes a sandbox folder
mkdir -p $1
# copies notebooks over
cp *.ipynb $1/
# goes into it
cd $1
# runs ipython notebook on a public IP w/ specified port
ipython notebook --ip=* --port=$1 --pprint --browser=/bin/true
