import arcade

# screen size constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

ocean_level = 0

def sandbags():
    

def ocean_rise(self):
    
    # access global var
    global ocean_level
    # redraw island & updated sea level
    island()
    
    # flood island
    for i in range (0, ocean_level):
        arcade.draw_arc_outline(300, 260 + i, 225, 55, arcade.color.TEAL, 180, 360, 2, 0, 20)
    
    # increase sea level
    ocean_level += 1
    

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
    
    
def island():
    
    # ocean
    arcade.draw_rectangle_filled(SCREEN_WIDTH/2, 150, SCREEN_WIDTH, 300 + (ocean_level * 2), arcade.color.TEAL)
    
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
    # atop mountain 3
    tree(335, 365)
    tree(320, 355)
    
    
    # HOUSES 

    # bottom right of mountain 1
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

    
def main():
    
    # open window, set dimensions and title
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'island')
    # set background color to white
    arcade.set_background_color(arcade.color.WHITE)
    # start render process
    arcade.start_render()
    
    # draw island
    island()
    arcade.schedule(ocean_rise, .01)

    # finish drawing and display result
    arcade.finish_render();
    # keep window open until closed by user
    arcade.run();
    
if __name__ == "__main__": 
    main()
