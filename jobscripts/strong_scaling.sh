#!/bin/bash -l

#SBATCH --job-name=strong_scaling
##SBATCH --reservation=training
#SBATCH --time=00:20:00
#SBATCH --nodes=1
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out


module load arm-reports
module load python/3.6.4
./utils/strong_scaling.py
