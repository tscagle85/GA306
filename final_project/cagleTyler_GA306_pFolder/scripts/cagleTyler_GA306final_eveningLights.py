import maya.cmds as cmds

#Create directional light with evening color, set outwards for placement
cmds.directionalLight(rotation=(-90, 0, 0), rgb=[0.726, 0.466, 0.557])
cmds.setAttr('directionalLight1.translateZ', 15) 
cmds.setAttr('directionalLight1.translateY', 10)
cmds.directionalLight(e=True, intensity=0.10 )
# Query it
cmds.directionalLight(q=True, intensity=True )
    


#Create fill light with evening color, full intensity
cmds.pointLight(rotation=(0, 0, 0), rgb=[0.787, 0.585, 0.475])
cmds.setAttr('pointLight1.translateZ', 15) 
cmds.setAttr('pointLight1.translateY', 10)
cmds.setAttr('pointLight1.translateX', 10)
cmds.pointLight(e=True, intensity=0.55 )
# Query it
cmds.pointLight(q=True, intensity=True )

#Create another fill light with, but with 75% intensity
cmds.pointLight(rotation=(0, 0, 0), rgb=[0.787, 0.585, 0.475])
cmds.setAttr('pointLight2.translateZ', 15) 
cmds.setAttr('pointLight2.translateY', 10)
cmds.setAttr('pointLight2.translateX', -10)
cmds.pointLight(e=True, intensity=0.50 )
# Query it
cmds.pointLight(q=True, intensity=True )
