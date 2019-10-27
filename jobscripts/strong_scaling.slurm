#!/bin/bash -l

#SBATCH --job-name=strong_scaling
##SBATCH --reservation=training
#SBATCH --time=00:20:00
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out
#SBATCH --hint=nomultithread


time -p srun --hint=nomultithread -n ${SLURM_NTASKS} ${PWD}/bin/heat_mpi -r 8090 -c 8090 
