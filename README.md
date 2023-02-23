# FESAFE-Fatigue
Workflow for FESAFE fatigue analysis and postprocessing using Python and Abaqus

## Abq_Fatigue.macro

## Abq_Fatigue.ldf

## Abq_Fatigue.stlx

## FESAFE_run.sh

## FESAFE_Fatigue_Plots.py

FE-SAFE can produce a history text file with the Haigh diagram.  Must first
clean up this file as follows:
  * cat FESAFE.odb-history.txt | grep -n 'El#' > grepout
  * head grepout
  * vi FESAFE.odb-history.txt
  * <line number> <shift+g>
  * <ma>
  * <ctrl+end>
  * <d'a>
  * <:wq>
  * mv FESAFE.odb-history.txt FESAFE.txt

## abaqusMacros.py
