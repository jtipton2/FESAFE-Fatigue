# FESAFE-Fatigue
Workflow for FESAFE fatigue analysis and postprocessing using Python and Abaqus

## FESAFE_run.sh
PBS Torque submission script to run FE-SAFE on the cluster

## Abq_Fatigue.macro
FE-SAFE macro to run the analysis in batch mode (as opposed to GUI).  It switches to the active directory.  Most of the wall time is spent in the "prescan" phase where the Abaqus ODB is opened and the results for all timesteps are read and stored in FE-SAFE analysis format.  Then the mesh part is selected and the fatigue analysis is performed.

NOTE: Once the prescan steps are completed, they do not have to be repeated if a rerun of the fatigue analysis is desired.  You can just comment out the prescan steps and resubmit the job.

## Abq_Fatigue.ldf
FE-SAFE load definition file.  This just sequentially follows the steps in the ODB.  The number of data steps should equal the total number of timesteps that was prescanned from the ODB.  As an example, let's say an ODB has 2 steps.  Step-1 is a beam pulse with steps 0 to 7.  Step-2 is the pulse response with steps 0 to 200.  Then the load definition file would go from 1 to 209.

## Abq_Fatigue.stlx
FE-SAFE analysis settings.  It is in XML markup language and can be difficult to read.

## FESAFE_Fatigue_Plots.py
Uses Python to produce a plot of the Goodman failure envelope.  Also plots the worst-case mean stress and stress amplitude for each element of the stress analysis.  This uses a history text file with the Haigh diagram that is requested in the FE-SAFE fatigue analysis.  Must first clean up this file as follows:
  * cat FESAFE.odb-history.txt | grep -n 'El#' > grepout
  * head grepout
  * vi FESAFE.odb-history.txt
  * <line number> <shift+g>
  * <m a>
  * <ctrl+end>
  * <d ' a>
  * <: w q>
  * mv FESAFE.odb-history.txt FESAFE.txt

## abaqusMacros.py
FE-SAFE will copy the ODB file (be careful with large file sizes!). Then it will add a new step to the end of the copied ODB and write requested output (e.g. FOS, Smean, Samp, Smax, etc.).  These can then be plotted using contour plots in Abaqus CAE.  This python file can be loaded as a macro in Abaqus CAE to change plotting options for pretty output.
