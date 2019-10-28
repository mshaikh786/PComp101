#!/bin/bash -l

#SBATCH --job-name=mpi_profile
#SBATCH --reservation=training
#SBATCH --time=00:20:00
#SBATCH --nodes=1
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out


module load arm-reports
perf-report srun --hint=nomultithread -n 32 $PWD/bin/heat_mpi

