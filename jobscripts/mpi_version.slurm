#!/bin/bash -l

#SBATCH --job-name=heat_mpi
#SBATCH --reservation=training
#SBATCH --time=00:20:00
#SBATCH --nodes=1
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out

time -p srun -n 4 --hint=nomultithread $PWD/bin/heat_mpi
