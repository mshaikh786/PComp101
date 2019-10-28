#!/bin/bash -l

#SBATCH --job-name=serial_profile
#SBATCH --reservation=training
#SBATCH --time=00:20:00
#SBATCH --nodes=1
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out
#SBATCH --hint=nomultithread

module load arm-reports
srun -n 1 --hint=nomultithread perf-report --nompi $PWD/bin/heat_serial
