#!/bin/bash
mkdir -p $1
cp *.ipynb $1/
cd $1
ipython notebook --ip=* --port=$1 --pprint --browser=/bin/true
