import arcade
import random

class MittSpel(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Pedros jakt!")
        arcade.set_background_color(arcade.color.GUPPIE_GREEN)

        self.player = arcade.Sprite("pedro.png")
        self.player.center_x = 300
        self.player.center_y = 500

        self.mouse_list = arcade.SpriteList()

        self.set_mouse_visible(False)
        self.score = 0
        

    def update(self, dt):
        if random.random() > 0.97: 
            mouse = arcade.Sprite("mouse.png", 0.5)
            mouse.center_x = random.random()*800
            mouse.center_y = random.random()*600
            self.mouse_list.append(mouse)

        hit_list = arcade.check_for_collision_with_list(self.player, self.mouse_list)

        for mouse in hit_list: 
            mouse.kill()
            self.score += 1



    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.mouse_list.draw()
        arcade.draw_text("Dödade: " + str(self.score), 30, 550, arcade.color.AUBURN, 30)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x
        self.player.center_y = y


MittSpel()
arcade.run()


