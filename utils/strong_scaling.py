#!/usr/bin/env python3
import subprocess as sb
import os
from matplotlib import pyplot as plt
import matplotlib


def submit_job(mpi_tasks):
    
    #out = sb.run(['srun','--hint=nomultithread', 'perf-report', '-n', '%s' %mpi_tasks, '-o',
    #              'mpi_strong_scaling_%s_tasks_%s.txt' %(mpi_tasks,os.getenv('SLURM_JOBID')),
    #              '%s/bin/heat_mpi'%os.getenv('PWD')],stdout=sb.PIPE,stderr=sb.PIPE)
    out = sb.run(['sbatch', '-n', '%s' %mpi_tasks, 'jobscripts/strong_scaling.slurm'],stdout=sb.PIPE,stderr=sb.PIPE)
    text=str()
    for word in out.args:
        text = text + word + ' '
    print(text)
    jobid = out.stdout.decode('utf8').split()[3]
    
    if str(out.stderr.decode('utf8')) != " ":
        print(str(out.stderr.decode('utf8')))
    
    return jobid

def execute_tests(mpi_tasks):
    jobids=list()
    for i in mpi_tasks:
        jobids.append(submit_job(i))
    return(jobids)


def get_compute_time(fname):
    f = open(fname,'r+')
    buf = f.readlines()
    f.close()
    t_time=0.0
    for line in buf:
       if "Total time" in line:
            t_time = float(line.split()[2])
    return t_time

def wait_for_all_jobs(jobids):
    out = sb.run(['squeue','-h','-u','%s' %os.getenv('USER'),'-n','strong_scaling','-o','%t'],stdout=sb.PIPE)
    jobid_list=out.stdout.decode('utf8').split()
    
    while len(jobid_list) > 0 :
        os.system('sleep 5')
        out = sb.run(['squeue','-h','-u','%s' %os.getenv('USER'),'-n','strong_scaling','-o','%t'],stdout=sb.PIPE)
        jobid_list=out.stdout.decode('utf8').split()



def get_scaling(mpi_tasks,jobids):
    wait_for_all_jobs(jobids)
    results=dict()
    for i in range(len(mpi_tasks)):
        fname = "mpi_strong_scaling_%sp_%s.txt" %(mpi_tasks[i],jobids[i])        
        results.update( {i:get_compute_time(fname)} )
    return results

def plot(results):
    matplotlib.use('Agg')
    plt.plot(list(results.keys()),list(results.values()))
    plt.savefig('Strong_scaling.png')

if __name__ == '__main__':
    mpi_tasks=[2**x for x in range(0,8)]
    jobids=execute_tests(mpi_tasks)
    print(jobids)
    results = get_scaling(mpi_tasks,jobids)
    plot(results)