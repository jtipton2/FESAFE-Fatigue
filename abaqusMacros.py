# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def PostProcessSetViews():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.graphicsOptions.setValues(backgroundStyle=SOLID, 
        backgroundColor='#FFFFFF')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendDecimalPlaces=0, legendNumberFormat=FIXED)
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        triadFont='-*-verdana-medium-r-normal-*-*-100-*-*-p-*-*-*', 
        legendFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*', 
        titleFont='-*-verdana-medium-r-normal-*-*-100-*-*-p-*-*-*', 
        stateFont='-*-verdana-medium-r-normal-*-*-100-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.463519, 
        farPlane=0.819019, width=0.222319, height=0.299255, cameraPosition=(
        -0.261619, 0.364145, 0.43473), cameraUpVector=(0.474799, 0.57735, 
        -0.664254))
    session.viewports['Viewport: 1'].view.fitView()
    session.View(name='User-1', nearPlane=0.32171, farPlane=0.96512, width=0.15969, 
        height=0.10865, projection=PERSPECTIVE, cameraPosition=(-0.27296, 
        0.36073, 0.43283), cameraUpVector=(0.4748, 0.57735, -0.66425), 
        cameraTarget=(0.032534, -0.010748, 0.0054344), viewOffsetX=0, 
        viewOffsetY=0, autoFit=ON)
    session.View(name='User-2', nearPlane=0.14092, farPlane=0.27004, width=0.13098, 
        height=0.12774, projection=PARALLEL, cameraPosition=(-0.18565, 
        0.097138, 0.11023), cameraUpVector=(0.4748, 0.57735, -0.66425), 
        cameraTarget=(-0.078182, -0.0056914, -0.031536), viewOffsetX=0, 
        viewOffsetY=0, autoFit=OFF)
    session.View(name='User-3', nearPlane=0.11374, farPlane=0.23935, width=0.13099, 
        height=0.12774, projection=PARALLEL, cameraPosition=(0.03338, 0.043907, 
        -0.16733), cameraUpVector=(-0.39879, 0.72054, 0.56726), cameraTarget=(
        -0.079075, -0.023707, -0.0092094), viewOffsetX=0, viewOffsetY=0, 
        autoFit=OFF)
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendBox=OFF)
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        visibleEdges=FEATURE)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        deformationScaling=UNIFORM, uniformScaleFactor=5000)
#    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
#        legendDecimalPlaces=1, legendNumberFormat=ENGINEERING)
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendDecimalPlaces=1, legendNumberFormat=FIXED)
    session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
        averageElementOutput=False)

