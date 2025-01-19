## @package test
#
# test for entity manager
#
import pyray as pr
import entity_manager as em

## the pixels-per-frame that boxes move
SPEED = 3

red = em.Entity(em.Shape_type.RECTANGLE, pr.Rectangle(100,100,40,40))
blue = em.Entity(em.Shape_type.RECTANGLE, pr.Rectangle(300,250,40,40))
yellow = em.Entity(em.Shape_type.RECTANGLE, pr.Rectangle(400,150,40,40))
## the entity manager instance
entity_manager = em.Entity_manager()
entity_manager.add_entity(red, "red")
entity_manager.add_entity(blue, "blue")
entity_manager.add_entity(yellow, "yellow")

pr.init_window(800,450,"entity-test")
pr.set_target_fps(60)
while not pr.window_should_close():
    if pr.is_key_down(pr.KEY_LEFT):
        red.shape.geometry.x -= SPEED
    if pr.is_key_down(pr.KEY_RIGHT):
        red.shape.geometry.x += SPEED
    if pr.is_key_down(pr.KEY_UP):
        red.shape.geometry.y -= SPEED
    if pr.is_key_down(pr.KEY_DOWN):
        red.shape.geometry.y += SPEED

    if pr.is_key_down(pr.KEY_A):
        blue.shape.geometry.x -= SPEED
    if pr.is_key_down(pr.KEY_D):
        blue.shape.geometry.x += SPEED
    if pr.is_key_down(pr.KEY_W):
        blue.shape.geometry.y -= SPEED
    if pr.is_key_down(pr.KEY_S):
        blue.shape.geometry.y += SPEED

    entity_manager.check_collisions()

    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.draw_rectangle_rec(red.shape.geometry, pr.RED)
    pr.draw_rectangle_rec(yellow.shape.geometry, pr.YELLOW)
    pr.draw_rectangle_rec(blue.shape.geometry, pr.BLUE)
    pr.draw_text(str(len(entity_manager.overlaps)), 20,20,20, pr.BLACK)
    for x in entity_manager.overlaps:
        pr.draw_rectangle_rec(x.shape.geometry, pr.DARKPURPLE)
    pr.end_drawing()
pr.close_window()
