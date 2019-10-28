#!/bin/bash -l

#SBATCH --job-name=serial_profile
#SBATCH --time=00:20:00
#SBATCH --nodes=1
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out
#SBATCH --hint=nomultithread
module load openmpi

srun -n 1 --hint=nomultithread $PWD/bin/heat_serial
