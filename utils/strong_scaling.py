#!/usr/bin/env python3
import subprocess as sb
import os
from matplotlib import pyplot as plt
import matplotlib


def submit_job(mpi_tasks):
    
    out = sb.run(['srun','--hint=nomultithread', 'perf-report', '-n', '%s' %mpi_tasks, '-o',
                  'mpi_strong_scaling_%s_tasks_%s.txt' %(mpi_tasks,os.getenv('SLURM_JOBID')),
                  '%s/bin/heat_mpi'%os.getenv('PWD'),'-m','%s'%10],stdout=sb.PIPE,stderr=sb.PIPE)
    print(str(out.stdout.decode('utf8')))
    print(str(out.stderr.decode('utf8')))
    #if str(out.stderr.decode('utf8')) != "":
     #   print(str(out.stderr.decode('utf8')))
    #else:
    return "mpi_strong_scaling_%s_tasks_%s.txt" %(mpi_tasks,os.getenv('SLURM_JOBID'))

def get_time(fname):
    f = open(fname,'r+')
    buf = f.readlines()
    f.close()
    t_time=0.0
    for line in buf:
       if "Total time" in line:
            t_time = float(line.split()[2])
    return t_time
        
def execute_tests(mpi_tasks):
    results=dict()
    for i in mpi_tasks:
        print("Profiling heat_mpi to run on %d MPI processes" % i )
        #results.update( {i:get_time(submit_job(i))} )
        print("Finshed profiling heat_mpi on %d MPI processes" % i )
    return results

def plot(results):
    matplotlib.use('Agg')
    plt.plot(list(results.keys()),list(results.values()))
    plt.savefig('Strong_scaling.png')

if __name__ == '__main__':
    mpi_tasks=[2**x for x in range(0,2)]
    results = execute_tests(mpi_tasks)
    #plot(results)
            