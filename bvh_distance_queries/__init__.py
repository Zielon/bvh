# -*- coding: utf-8 -*-

# Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG) is
# holder of all proprietary rights on this computer program.
# You can only use this computer program if you have closed
# a license agreement with MPG or you get the right to use the computer
# program from someone who is authorized to grant you that right.
# Any use of the computer program without a valid license is prohibited and
# liable to prosecution.
#
# Copyright©2019 Max-Planck-Gesellschaft zur Förderung
# der Wissenschaften e.V. (MPG). acting on behalf of its Max Planck Institute
# for Intelligent Systems. All rights reserved.
#
# @author Vasileios Choutas
# Contact: vassilis.choutas@tuebingen.mpg.de
# Contact: ps-license@tuebingen.mpg.de

import torch
from .bvh_search_tree import BVH, BVHRayIntersection
from .tetra_sampler import Sampler
from .mesh_distance import PointToMeshResidual