import maya.cmds as cmds

#Create directional light with overcast color, set outwards for placement
cmds.directionalLight(rotation=(-90, 0, 0), rgb=[0.231, 0.231, 0.231])
cmds.setAttr('directionalLight1.translateZ', 15) 
cmds.setAttr('directionalLight1.translateY', 10)
cmds.directionalLight(e=True, intensity=0.25 )
# Query it
cmds.directionalLight(q=True, intensity=True )
    


#Create fill light with overcast color, full intensity
cmds.pointLight(rotation=(0, 0, 0), rgb=[0.451, 0.451, 0.451], decayRate=2)
cmds.setAttr('pointLight1.translateZ', 15) 
cmds.setAttr('pointLight1.translateY', 10)
cmds.setAttr('pointLight1.translateX', 10)
cmds.pointLight(e=True, intensity=0.55 )
# Query it
cmds.pointLight(q=True, intensity=True )

#Create another fill light with, but with 75% intensity
cmds.pointLight(rotation=(0, 0, 0), rgb=[0.671, 0.671, 0.671], decayRate=2)
cmds.setAttr('pointLight2.translateZ', 15) 
cmds.setAttr('pointLight2.translateY', 10)
cmds.setAttr('pointLight2.translateX', -10)
cmds.pointLight(e=True, intensity=0.50 )
# Query it
cmds.pointLight(q=True, intensity=True )