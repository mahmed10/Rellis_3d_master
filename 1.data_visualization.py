import numpy as np
from open3d import *    


cloud = read_point_cloud("./Rellis-3D/00000/os1_cloud_node_color_ply/frame000000-1581624652_770.bin") # Read the point cloud
draw_geometries([cloud]) # Visualize the point cloud 