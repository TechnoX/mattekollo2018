import arcade
import random

class MittSpel(arcade.Window):

    def __init__(self):
        super().__init__(800,600,"Pedros jakt")
        arcade.set_background_color(arcade.color.AMAZON)
        
        self.player_sprite = arcade.Sprite("pedro.png")
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.mouse_list = arcade.SpriteList()
        self.score = 0
        self.set_mouse_visible(False)
        
    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        self.mouse_list.draw()
        arcade.draw_text("Dödade: " + str(self.score), 30, 550, arcade.color.AUBURN, 30)
        
    def update(self, delta_time):
        if random.random() > 0.96:
            # Create mus
            mouse = arcade.Sprite("mouse.png", 0.5)
            mouse.center_x = random.randrange(800)
            mouse.center_y = random.randrange(600)

            self.mouse_list.append(mouse)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.mouse_list)

        for mouse in hit_list:
            mouse.kill()
            self.score += 1
            self.player_sprite.scale *= 2
                    
    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        
        
game = MittSpel()
arcade.run()
