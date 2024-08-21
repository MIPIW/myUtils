#!/bin/bash

ssh -fNTR $JPORT:$(hostname):$JPORT -p7777 nlplab;jupyter-notebook --ip=$(hostname) --port=$JPORT
