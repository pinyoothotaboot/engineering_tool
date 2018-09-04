import sys
sys.path.append("..")

from engineering_tool.volumes import *


def Volume_All():

    radius = 15.5
    radius2 = 16.7
    radius3 = 19.5
    base   = 20
    wide   = 30
    height = 40
    area = 4

    sphere = Volume.sphere(radius)
    cube   = Volume.cube(base)
    rectangular = Volume.rectangular(wide,base,height)
    cylinder = Volume.cylinder(radius,height)
    pyramid = Volume.pyramid(base,height)
    cone = Volume.cone(radius,height)
    triangular = Volume.triangular(base,height,wide)
    ellipsoid = Volume.ellipsoid(radius,radius2,radius3)
    irregular = Volume.irregular(area,height)

    print("Volume.....")
    print("Sphere       : %.3f"%sphere)
    print("Cube         : %.3f"%cube)
    print("Rectangular  : %.3f"%rectangular)
    print("Cylinder     : %.3f"%cylinder)
    print("Pyramid      : %.3f"%pyramid)
    print("Cone         : %.3f"%cone)
    print("Trianglar    : %.3f"%triangular)
    print("Ellipsoid    : %.3f"%ellipsoid)
    print("Irregular    : %.3f"%irregular)

Volume_All()


