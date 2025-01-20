## @package test
#
# test for entity manager
#
import pyray as pr
import entity_manager as em
import shapes

## the pixels-per-frame that boxes move
SPEED = 3

red = em.Entity(shapes.Rectangle(100,100,40,40))
blue = em.Entity(shapes.Rectangle(300,250,40,40))
yellow = em.Entity(shapes.Rectangle(400,150,40,40))
## the entity manager instance
entity_manager = em.Entity_manager()
entity_manager.add_entity(red, "red")
entity_manager.add_entity(blue, "blue")
entity_manager.add_entity(yellow, "yellow")

pr.init_window(800,450,"entity-test")
pr.set_target_fps(60)
while not pr.window_should_close():
    if pr.is_key_down(pr.KEY_LEFT):
        red.shape.x -= SPEED
    if pr.is_key_down(pr.KEY_RIGHT):
        red.shape.x += SPEED
    if pr.is_key_down(pr.KEY_UP):
        red.shape.y -= SPEED
    if pr.is_key_down(pr.KEY_DOWN):
        red.shape.y += SPEED

    if pr.is_key_down(pr.KEY_A):
        blue.shape.x -= SPEED
    if pr.is_key_down(pr.KEY_D):
        blue.shape.x += SPEED
    if pr.is_key_down(pr.KEY_W):
        blue.shape.y -= SPEED
    if pr.is_key_down(pr.KEY_S):
        blue.shape.y += SPEED

    entity_manager.check_collisions()

    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.draw_rectangle_rec(red.shape.ctype(), pr.RED)
    pr.draw_rectangle_rec(yellow.shape.ctype(), pr.YELLOW)
    pr.draw_rectangle_rec(blue.shape.ctype(), pr.BLUE)
    pr.draw_text(str(len(entity_manager.overlaps)), 20,20,20, pr.BLACK)
    for x in entity_manager.overlaps:
        pr.draw_rectangle_rec(x.shape.ctype(), pr.DARKPURPLE)
    pr.end_drawing()
pr.close_window()
