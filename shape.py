#!/usr/bin/env python3

## @package shape
#
# definition for shape class and type enums

## imports
import pyray as pr
from enum import Enum, auto


## enum of allowed geometries for an entity
#
# detailed description
class Shape_type(Enum):
    ## indicates no geometry
    NONE = 0
    ## not supported
    #
    # pr.Vector2
    POINT = auto()
    ## not supported, priority
    #
    # tuple(pr.Vecotr2, pr.Vector2)
    LINE = auto()
    ## supported
    #
    # pr.Rectangle
    RECTANGLE = auto()
    ## not supported
    CIRCLE = auto()
    ## not supported
    POLYGON = auto()
    ## not supported
    TRIANGLEFAN = auto()
    ## not supported
    TRIANGLESTRIP = auto()
    ## not supported


## an arbitrary geometric shape with its type and data
class Shape:
    def __init__(self, type, geometry):
        ## the type of the shape
        self.type = type
        ## the geometric data
        #
        # processed acotrding to self.type
        self.geometry = geometry
