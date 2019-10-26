#!/bin/bash -l

#SBATCH --job-name=cpu_info
##SBATCH --reservation=training
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out

srun -n 1 lscpu


