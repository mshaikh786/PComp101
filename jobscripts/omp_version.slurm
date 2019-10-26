#!/bin/bash -l

#SBATCH --job-name=heat_omp
##SBATCH --reservation=training
#SBATCH --time=00:20:00
#SBATCH --nodes=1
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out

export OMP_NUM_THREADS=4
time -p srun -n 1 -c $OMP_NUM_THREADS --hint=nomultithread $PWD/bin/heat_omp
