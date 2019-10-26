#!/bin/bash -l

#SBATCH --job-name=strong_scaling
#SBATCH --reservation=training
#SBATCH -n 4
#SBATCH --time=00:20:00
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out


module load arm-reports
perf-report  -o mpi_strong_scaling_${SLURM_NTASKS}p_$SLURM_JOBID.txt  srun -n ${SLURM_NTASKS} ${PWD}/bin/heat_mpi -m 10
