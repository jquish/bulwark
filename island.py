"""
Buttons with text on them

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.gui_text_button
"""
import arcade
import random
import os

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Bullwark"

def house(x, y, color):

    # draws a lil house
    house = [[x, y], [x, y+10], [x+6, y+15], [x+12, y+10], [x+12, y]]
    arcade.draw_polygon_filled(house, color)
    # and windows
    arcade.draw_rectangle_filled(x+3, y+5, 2, 4, arcade.color.CORNSILK, 0)
    arcade.draw_rectangle_filled(x+9, y+5, 2, 4, arcade.color.CORNSILK, 0)

def tree(x, y):

    # draws a lil tree
    tree = [[x, y], [x+6, y+10], [x+3, y+10], [x+10, y+20], [x+17, y+10], [x+14, y+10], [x+20, y]]

    arcade.draw_polygon_filled(tree, (18, 77, 18))

def easier_writing(lowX, lowY, string):
    arcade.draw_text(string, lowX, lowY, arcade.color.BLACK, 20)

def island():

    # ocean
    arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.AERO_BLUE)
    arcade.draw_rectangle_filled(SCREEN_WIDTH/2, 150, SCREEN_WIDTH, 300, arcade.color.TEAL)

    # island base
    arcade.draw_ellipse_filled(300, 260, 450, 110, arcade.color.FOREST_GREEN, 0, 20)

    # MOUNTAINS

    # front
    mountain_1 = [[140,280], [200,330], [220,340], [240,340], [320,280], [350,270], [250,260]]
    # middle
    mountain_2 = [[250,280], [320,320], [360,340], [400,360], [440,340], [500,280]]
    # back
    mountain_3 = [[210,300], [290,380], [330,400], [360,380], [380,370], [420,300]]

    arcade.draw_polygon_filled(mountain_3, (23, 97, 23))
    arcade.draw_polygon_filled(mountain_2, arcade.color.FOREST_GREEN)
    arcade.draw_polygon_filled(mountain_1, (78, 162, 78))


    # TREES

    # below mountain 1
    tree(115, 280)
    tree(160, 270)
    tree(140, 265)
    tree(190, 250)
    tree(210, 260)
    tree(230, 250)
    # across mountain 2 (left to right)
    tree(305, 305)
    tree(320, 300)
    tree(340, 280)
    tree(350, 290)
    tree(370, 275)
    tree(390, 285)
    tree(410, 270)
    tree(450, 280)
    tree(465, 265)
    tree(335, 365)
    tree(320, 355)
    house(310, 260, (170, 143, 168))
    house(270, 255, (107, 76, 105))
    house(290, 245, (134, 95, 132))
    # bottom left of mountain 1
    house(210, 260, (134, 95, 132))
    house(180, 265, (107, 76, 105))
    house(150, 260, (107, 76, 105))
    house(170, 245, (170, 143, 168))
    # bottom right of mountain 2
    house(400, 280, (107, 76, 105))
    house(430, 290, (134, 95, 132))
    house(450, 270, (170, 143, 168))
    # left of mountain 2
    house(300, 300, (107, 76, 105))
    house(330, 290, (170, 143, 168))
    # top of mountain 3
    house(350, 360, (134, 95, 132))

def draw_menu():
    # finish drawing and display result
    easier_writing(800, 800, "Bullwark")

    #Menu range - buffer 100ppx in right half
    arcade.draw_rectangle_outline(1200, 450, 600, 700, arcade.color.TROLLEY_GREY)

    #buttons for buying things


class TextButton:
    """ Text-based button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False

def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()

def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()

class DeploySandbagsButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 200, 40, "Deploy Sandbags", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class SellSandbagsButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 200, 40, "Sell Sandbags", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class BuyPanelsButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 200, 40, "Install Solar Power", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class BuyForestsButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 200, 40, "Plant Forests", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class BuyEfficientHousesButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 200, 40, "Renovate Houses", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.pause = False
        self.button_list = None

    def setup(self):
        # Create the Island scene

        # Create our on-screen GUI buttons
        self.button_list = []

        sell_sandbags_button = SellSandbagsButton(1025, 570, self.resume_program)
        self.button_list.append(sell_sandbags_button)

        deploy_sandbags_button = DeploySandbagsButton(1025, 515, self.pause_program)
        self.button_list.append(deploy_sandbags_button)

        buy_panels_button = BuyPanelsButton(1025, 460, self.pause_program)
        self.button_list.append(buy_panels_button)

        buy_forests_button = BuyForestsButton(1025, 405, self.pause_program)
        self.button_list.append(buy_forests_button)

        buy_houses_button = BuyEfficientHousesButton(1025, 350, self.pause_program)
        self.button_list.append(buy_houses_button)



    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        island()
        draw_menu()


        # Draw the buttons
        for button in self.button_list:
            button.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        if self.pause:
            return


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

    def pause_program(self):
        self.pause = True

    def resume_program(self):
        self.pause = False

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
