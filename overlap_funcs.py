#!/usr/bin/env python3
## @package collision_funcs
#
# functions for collisions of specific shapes
# not yet included in implementation

## for geometry structs
import pyray as pr
import shapes

## get the overlap between two line segments
#
# done, not checked\n
# takes two tuples and returns a tuple\n
# called twice in two dimentions for overlap_rec_rec\n
def overlap_line_segments(tup1, tup2):
    if tup1[0] <= tup2[0]:
        left_of_right = tup2[0]
    else:
        left_of_right = tup1[0]
    if tup1[1] <= tup2[1]:
        right_of_left = tup1[1]
    else:
        right_of_left = tup2[1]
    overlap = ( left_of_right, right_of_left )
    return overlap

## return shape of overlap between two rectangles
##
# in progress\n
# takes two pr.rectangles\n
# return Shape_type.NONE for no overlap\n
# return Shape_type.POINT for touching corners\n
# return Shape_type.LINE for touching edge\n
# return Shape_type.RECTANGLE for overlaping area\n
def overlap_rec_rec(rect1, rect2):
    shape_overlap = None
    overlapX = overlap_line_segments((rect1.x, rect1.x + rect1.width), (rect2.x, rect2.x + rect2.width))
    overlapY = overlap_line_segments((rect1.y, rect1.y + rect1.height), (rect2.y, rect2.y + rect2.height))
    lenX = overlapX[1] - overlapX[0]
    lenY = overlapY[1] - overlapY[0] 
    if lenX < 0 or lenY < 0:
        pass
    elif lenX == 0 and lenY == 0:
        shape_overlap = shapes.Point(overlapX[0], overlapY[0])
    elif lenX == 0 or lenY == 0:
        shape_overlap = shapes.Line(shapes.Point(overlapX[0], overlapY[0]), shapes.Point(overlapX[1], overlapY[1]))
    else:
        shape_overlap = shapes.Rectangle(overlapX[0], overlapY[0], lenX, lenY)
    return shape_overlap
