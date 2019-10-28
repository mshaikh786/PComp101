#!/bin/bash -l

#SBATCH --job-name=omp_profile
#SBATCH --reservation=training
#SBATCH --time=00:20:00
#SBATCH --nodes=1
#SBATCH --partition=workq
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out


module load arm-reports
export OMP_NUM_THREADS=4
srun -n 1 -c $OMP_NUM_THREADS --hint=nomultithread perf-report --nompi --openmp-threads=$OMP_NUM_THREADS $PWD/bin/heat_omp

