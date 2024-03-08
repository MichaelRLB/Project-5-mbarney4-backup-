from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *
from CollideObjectBase import *

# Keybinds in Player class don't work after converting to SphereCollideObject.
# Figure out the correct scales for the collision functions.
class Planet(SphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1.05)  

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1.05)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
class Station(CapsuleCollidableObject):
     def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Station, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)   
class Drone(SphereCollideObject):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.5)        

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
class Missile(SphereCollideObject):
    fireModels = {}
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missileCount = 0
    def __init__(self, loader: Task.Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
        super().__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 3.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)
        Missile.missileCount += 1
        Missile.fireModels[nodeName] = self.modelNode
        Missile.cNodes[nodeName] = self.collisionNode
        # We retrieve the solid for our collisionNode.
        Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        Missile.cNodes[nodeName].show()
        print("Fire torpedo #" + str(Missile.missileCount))
        Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        print("Fire torpedo #" + str(Missile.missileCount))