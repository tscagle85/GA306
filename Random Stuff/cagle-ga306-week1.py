import maya.cmds

sphere = maya.cmds.polySphere()[0]
loc = maya.cmds.spaceLocator()[0]
    
  
maya.cmds.connectAttr(sphere+'.ry', loc+'.ty')



