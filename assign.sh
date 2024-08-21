#!/bin/bash

export JPORT=$(shuf -i 30000-32000 -n 1);srun -p $1 --cpus-per-task=$3 --gres=gpu:A100:$2 --pty /bin/bash

