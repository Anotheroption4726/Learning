#
# Constantes de terrain
#
tile_grass = "."
tile_obs = "O"
tile_slow = "_"


#
# Constantes de mouvement
#
player_display = "X"
can_move = "#"
cant_move = "."


#
# Classe Grille
#
class Grid:

    def __init__(self, grid_width, grid_heigth):
        self.terrain_grid = []
        self.movement_grid = []
        self.width = grid_width
        self.heigth = grid_heigth


#
# Classe pion
#
class Pawn:

    def __init__(self, pawn_pos_x, pawn_pos_y, speed):
        self.display = player_display
        self.pos_x = pawn_pos_x
        self.pos_y = pawn_pos_y
        self.speed = speed


#
# Liste d'Obstacles
#
list_obs = []


#
# Classe obstacle
#
class Obstacle:

    def __init__(self, obs_pos_x, obs_pos_y):
        self.display = tile_obs
        self.pos_x = obs_pos_x
        self.pos_y = obs_pos_y

        list_obs.append(self)


#
# Liste Ralentisseurs
#
list_slow = []


#
# Classe Ralentisseur
#
class Slow:

    def __init__(self, slow_pos_x, slow_pos_y):
        self.display = tile_slow
        self.pos_x = slow_pos_x
        self.pos_y = slow_pos_y

        list_slow.append(self)


#
# Grid example test
#
grid_example = [
        [".", ".", ".", ".", "."],
        ["O", "O", "O", "O", "O"],
        [".", ".", ".", ".", "."],
    ]


#
# Création de la grille de terrain
#
def terrain_grid_setup(grid):

    i = 0
    while i < grid.width:
        grid.terrain_grid.append([])

        j = 0
        while j < grid.heigth:
            grid.terrain_grid[i].append(tile_grass)
            j += 1

        i += 1

    return


#
# Création de la grille de mouvement
#
def movement_grid_setup(grid):

    i = 0
    while i < grid.width:
        grid.movement_grid.append([])

        j = 0
        while j < grid.heigth:
            grid.movement_grid[i].append(cant_move)
            j += 1

        i += 1

    return


#
# Affichage de grille de terrain
#
def terrain_grid_display(grid_input):

    for obs in list_obs:
        grid_input[obs.pos_y - 1][obs.pos_x - 1] = obs.display

    for slw in list_slow:
        grid_input[slw.pos_y - 1][slw.pos_x - 1] = slw.display

    i = 0
    while i < len(grid_input):
        j = 0
        while j < len(grid_input[i]):
            print(grid_input[i][j] + "  ", end='')
            j += 1

        print()
        i += 1

    return


#
# Affichage de grille de mouvement
#
def movement_grid_display(grid_input):

    for obs in list_obs:
        grid_input[obs.pos_y - 1][obs.pos_x - 1] = obs.display

    i = 0
    while i < len(grid_input):
        j = 0
        while j < len(grid_input[i]):
            print(grid_input[i][j] + "  ", end='')
            j += 1

        print()
        i += 1

    return


#
# Affichage d'une frame de jeu
#
def game_frame_display(grid, pawn):

    grid.terrain_grid[pawn.pos_y - 1][pawn.pos_x - 1] = pawn.display
    grid.movement_grid[pawn.pos_y - 1][pawn.pos_x - 1] = pawn.display

    print("Terrain Grid")
    terrain_grid_display(grid.terrain_grid)
    print()
    print("Movement Grid")
    movement_grid_display(grid.movement_grid)
    print()
    print("________________________________________")
    print()

    return


def can_move_display(grid, pawn_pos_x, pawn_pos_y, pawn_speed):

    real_pos_x = pawn_pos_x - 1
    real_pos_y = pawn_pos_y - 1

    if pawn_speed > 0 and grid.heigth > real_pos_y + 1 and grid.terrain_grid[real_pos_y + 1][real_pos_x] is not tile_obs:
        if grid.terrain_grid[real_pos_y + 1][real_pos_x] is tile_slow:
            grid.movement_grid[real_pos_y + 1][real_pos_x] = can_move
            can_move_display(grid, pawn_pos_x, pawn_pos_y + 1, pawn_speed - 2)
        else:
            grid.movement_grid[real_pos_y + 1][real_pos_x] = can_move
            can_move_display(grid, pawn_pos_x, pawn_pos_y + 1, pawn_speed - 1)

    if pawn_speed > 0 and real_pos_y > 0 and grid.terrain_grid[real_pos_y - 1][real_pos_x] is not tile_obs:
        if grid.terrain_grid[real_pos_y - 1][real_pos_x] is tile_slow:
            grid.movement_grid[real_pos_y - 1][real_pos_x] = can_move
            can_move_display(grid, pawn_pos_x, pawn_pos_y - 1, pawn_speed - 2)
        else:
            grid.movement_grid[real_pos_y - 1][real_pos_x] = can_move
            can_move_display(grid, pawn_pos_x, pawn_pos_y - 1, pawn_speed - 1)

    if pawn_speed > 0 and grid.width > real_pos_x + 1 and grid.terrain_grid[real_pos_y][real_pos_x + 1] is not tile_obs:
        if grid.terrain_grid[real_pos_y][real_pos_x + 1] is tile_slow:
            grid.movement_grid[real_pos_y][real_pos_x + 1] = can_move
            can_move_display(grid, pawn_pos_x + 1, pawn_pos_y, pawn_speed - 2)
        else:
            grid.movement_grid[real_pos_y][real_pos_x + 1] = can_move
            can_move_display(grid, pawn_pos_x + 1, pawn_pos_y, pawn_speed - 1)

    if pawn_speed > 0 and real_pos_x > 0 and grid.terrain_grid[real_pos_y][real_pos_x - 1] is not tile_obs:
        if grid.terrain_grid[real_pos_y][real_pos_x - 1] is tile_slow:
            grid.movement_grid[real_pos_y][real_pos_x - 1] = can_move
            can_move_display(grid, pawn_pos_x - 1, pawn_pos_y, pawn_speed - 2)
        else:
            grid.movement_grid[real_pos_y][real_pos_x - 1] = can_move
            can_move_display(grid, pawn_pos_x - 1, pawn_pos_y, pawn_speed - 1)

    return


#
# main
#
def main():
    # Grid setup
    game_grid = Grid(10, 10)

    # Player setup
    player1 = Pawn(5, 5, 3)

    # Obstacles setup
    obstacle1 = Obstacle(6, 4)
    obstacle2 = Obstacle(7, 5)
    obstacle3 = Obstacle(8, 5)

    # Ralentisseurs setup
    ralentisseur1 = Slow(5, 4)
    ralentisseur2 = Slow(4, 4)
    ralentisseur2 = Slow(3, 4)
    ralentisseur4 = Slow(5, 7)

    # Terrain Grid Setup
    terrain_grid_setup(game_grid)

    # Movement Grid Setup
    movement_grid_setup(game_grid)

    # Frame
    game_frame_display(game_grid, player1)

    # Display pawn movement
    can_move_display(game_grid, player1.pos_x, player1.pos_y, player1.speed)

    # Frame
    game_frame_display(game_grid, player1)


if __name__ == "__main__":
    main()
