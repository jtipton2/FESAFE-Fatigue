#!/bin/sh 
#PBS -V 
#PBS -j oe 
#PBS -m abe 
#PBS -l nodes=1:ppn=8 
#PBS -l walltime=24:00:00
#PBS -N FESAFE
#PBS -M tvj@ornl.gov 
#PBS -q all 
# #PBS -W depend=afterany:14721

cd $PBS_O_WORKDIR 


# Define particulars of this run: 
INPUT_FILENAME=/data2/home/tvj/Documents/10_ConceptExploration/v10_Lasagna/1_DoubleRibs/Unirrad/FESAFE_IN718/Abq_Fatigue.macro
JOBNAME=Abq_Fatigue


#executable for fe-safe 
EXEC=/usr/SIMULIA/EstProducts/2020/fe-safe_cl 

 
# 
# To manage fe-safe jobs, you need to catch signals 
# and use "pkill -9" to kill the fe-safe job 
# 

exit_gracefully () { 
pkill -9 fe-safe_cl  
echo fe-safe job $JOBNAME terminated 
exit 
} 


# invoke fe-safe in the background on the compute node: 
trap exit_gracefully SIGUSR2 
$EXEC macro=$INPUT_FILENAME >FESAFE_run.log 
