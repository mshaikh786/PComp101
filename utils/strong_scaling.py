#!/usr/bin/env python3
import subprocess as sb
import os
import math
from matplotlib import pyplot as plt
import matplotlib


def submit_job(mpi_tasks):
    
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
       if "real" in line:
            t_time = float(line.split()[1])
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
        fname = "strong_scaling.%s.out" %(jobids[i])        
        results.update( {mpi_tasks[i]:get_compute_time(fname)} )
    return results

def plot(results):
    matplotlib.use('Agg')
    procs=list(results.keys())
    T=list(results.values())
    S=[T[0]/T[i] for i in range(len(T))]
    T_ideal=[T[0]/i for i in procs]
    S_ideal=[T_ideal[0]/T_ideal[i] for i in range(len(T_ideal))]
    E=[ 100.0*S[i]/procs[i] for i in range(len(procs))]
    
    x_axis=['2^%d'%math.log(p,2) for p in procs]
    
    figure=plt.figure(1)
    ax=figure.gca()
    ax.plot(procs,T,'b-', label='real')
    ax.plot(procs,T_ideal,'r--', label='ideal')
    ax.legend(loc='upper left')
    ax.set_xscale('log', basex=2)
    plt.xticks(procs,x_axis)
    plt.xlabel('MPI Processes (log2)')
    plt.ylabel('Time(s)')
    plt.title('Runtime')
    plt.savefig('Runtime.png')
    plt.close()
    
    figure=plt.figure(2)
    ax=figure.gca()
    ax.plot(procs,S,'b-',label='real')
    ax.plot(procs,S_ideal,'r--',label='ideal')
    ax.legend(loc='upper left')
    ax.set_xscale('log', basex=2)
    plt.xticks(procs,x_axis)
    plt.xlabel('MPI Processes (log2)')
    plt.ylabel('Speedup')
    plt.title('Speedup')
    plt.savefig('Speedup.png')
    plt.close()
    
    
    figure=plt.figure(3)
    ax=figure.gca()
    ax.plot(procs,E)
    ax.set_xscale('log', basex=2)
    plt.xticks(procs,x_axis)
    plt.xlabel('MPI Processes (log2)')
    plt.ylabel('% Efficiency')
    plt.title('Parallle Efficiency')
    plt.ylim(0.0,100.0)
    plt.savefig('Efficiency.png')
    plt.close()    

if __name__ == '__main__':
    mpi_tasks=[2**x for x in range(0,8)]
    jobids=execute_tests(mpi_tasks)
    results = get_scaling(mpi_tasks,jobids)
    plot(results)