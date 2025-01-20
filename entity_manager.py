## @package entity_manager
#
# an entity manager:
# handles collisions between arbitrary geometries that are registered with the manager

import pyray as pr
from . import shapes
from . import overlap_funcs

## an overlap between 2 arbitrary entities
class Overlap:	
    def __init__(self, entity1, entity2, shape):
        self.entity1 = entity1
        self.entity2 = entity2
        self.shape = shape


## a Shape which can be tested for collisions
class Entity:
    def __init__(self, shape):
        ## the shape of the entity
        self.shape = shape
        ## a list of overlaps with this entity
        self.overlaps = []

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
        overlap = Overlap(entity1, entity2, None)
        if isinstance(entity1.shape, shapes.Rectangle) and isinstance(entity2.shape, shapes.Rectangle):
            overlap.shape = overlap_funcs.overlap_rec_rec(entity1.shape, entity2.shape)
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
                if isinstance(overlap.shape, shapes.Rectangle):
                    self.overlaps.append(overlap)
                    entity1.overlaps.append(overlap)
                    entity2.overlaps.append(overlap)
