## @package entity_manager
#
# an entity manager:
# handles collisions between arbitrary geometries that are registered with the manager

import pyray as pr
from shape import Shape_type, Shape
import overlap_funcs

## an overlap between 2 arbitrary entities
class Overlap:	
    def __init__(self, entity1, entity2, shape):
        self.entity1 = entity1
        self.entity2 = entity2
        self.shape = shape


## a Shape which can be tested for collisions
class Entity:
    def __init__(self, shape_type, geometry):
        ## the shape of the entity
        self.shape = Shape(shape_type, geometry)
        ## the smallest possible rectangle containing the geometry
        self.rectangle = Entity.shape_to_rectangle(self.shape)
        ## a list of overlaps with this entity
        self.overlaps = []
        ## boolean indicating wheather this entities collisions should be checked
        #
        # support for this feature not yet implemented
        self.recalculate = True
    ## return the smallest possible rectangle containing the shape
    #
    ##only rectangles for now, so just return geometry
    def shape_to_rectangle(shape):
        if shape.type == Shape_type.RECTANGLE:
            return shape.geometry
        else:
            return False


## manages entity collisions
class Entity_manager:
        #starts with empty entity dict and overlaps list
    def __init__(self):
        self.entities = {}
        self.overlaps = []
        #adds entity to entitiy dict under name
    def add_entity(self, entity, name):
        self.entities[name] = entity
        #pops name
    def remove_entity(self, name):
        return self.pop(name)
    ##returns the overlap given two arbitrary entities
    #
    #- decide type of both entities
    #- call appropriate collision function
    def get_entity_overlap(entity1, entity2):
        overlap = Overlap(entity1, entity2, Shape(Shape_type.NONE, Shape_type.NONE))
        if entity1.shape.type == entity2.shape.type == Shape_type.RECTANGLE:
            overlap.shape = overlap_funcs.overlap_rec_rec(entity1.shape.geometry, entity2.shape.geometry)
        return overlap
    ## check all necesary collisions
    #
    #- clear overlaps
    #    - for each entity:
    #    -   for each other entity:
    #    -     if there is an overlap:
    #    -       add overlap to manager's and each entity's overlap list"""
    def check_collisions(self):
        self.overlaps.clear()
        length = len(self.entities)
        keys = list(self.entities.keys())
        for i in range(length):
            for j in range(i+1, length):
                entity1 = self.entities[keys[i]]
                entity2 = self.entities[keys[j]]
                overlap = Entity_manager.get_entity_overlap(entity1, entity2)
                if overlap.shape.type == Shape_type.RECTANGLE:
                    self.overlaps.append(overlap)
                    entity1.overlaps.append(overlap)
                    entity2.overlaps.append(overlap)
