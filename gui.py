import pygame as pg

class Tile():
    _white_tile_width = 100
    _white_tile_height = 200
    _black_tile_width = 70
    _black_tile_height = int(0.7*_white_tile_height)
    _white_shift = 0
    _black_shift = _white_tile_width-_black_tile_width//2

    def __init__(self, type: str, name: str):
        self.name = name
        self.type = type.lower()
        self.surface = None
        self._set_surface()

        if type.lower() == "white":
            self.pos = Tile._white_shift
        elif type.lower() == "black":
            self.pos = Tile._black_shift

    def activate(self) -> None:
        self.surface.fill((255, 0, 0))

    def _deactivate(self) -> None:
        self.type=="white" and self.surface.fill((255, 255, 255))
        self.type=="black" and self.surface.fill((0, 0, 0))

    def _set_surface(self) -> None:
        if self.type == "white":
            self.surface = pg.surface.Surface((Tile._white_tile_width-2, Tile._white_tile_height))
            self.surface.fill((255, 255, 255))
        elif self.type == "black":
            self.surface = pg.surface.Surface((Tile._black_tile_width, Tile._black_tile_height))
            self.surface.fill((0, 0, 0))
    
    def get_surface(self) -> pg.Surface:
        return self.surface
    def get_pos(self) -> int:
        return self.pos
    def get_name(self) -> str:
        return self.name

_width, _height = 7*Tile._white_tile_width, Tile._white_tile_height
WIN = pg.display.set_mode((_width, _height))
pg.display.set_caption("Piano chord")

white_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
black_notes = ['C#', 'D#', 'F#', 'G#', 'A#']
white_tiles: dict[str, Tile] = {}
black_tiles: dict[str, Tile] = {}

def generate_tile_list() -> None:
    for note in white_notes:
        white_tiles[note] = Tile("white", note)
        Tile._white_shift += Tile._white_tile_width
    for note in black_notes:
        black_tiles[note] = Tile("black", note)
        Tile._black_shift += Tile._white_tile_width
        if len(black_tiles)==2: Tile._black_shift += Tile._white_tile_width
generate_tile_list()

def blit_piano() -> None:
    for tile in white_tiles.values():
        WIN.blit(tile.get_surface(), (tile.get_pos(), 0))
    for tile in black_tiles.values():
        WIN.blit(tile.get_surface(), (tile.get_pos(), 0))

def activate_tiles(notes: list[str]) -> None:
    merged_tiles_dict = white_tiles | black_tiles
    for note in notes:
        merged_tiles_dict[note[:-1]].activate()

def run_gui() -> None:
    run = True
    while run:
        WIN.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        blit_piano()
        pg.display.update()