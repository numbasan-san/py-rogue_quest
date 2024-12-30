import random
from data.map_things.map_classes.rectangle import Rect
from items.basic_item import BasicItem
from items.basic_environment_item import BasicEnvironmentItem
from npc.basic_enemy import BasicEnemy

class MapGene:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.rooms = None
        
        # Representación textual del mapa: '#' para paredes
        self.map = [['#' for _ in range(h)] for _ in range(w)]

    def make_map(self, max_rooms, room_min_size, room_max_size, map_w, map_h, player):
        self.rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            # Define las dimensiones y coordenadas de una habitación
            w = random.randint(room_min_size, room_max_size)
            h = random.randint(room_min_size, room_max_size)
            x = random.randint(0, map_w - w - 1)
            y = random.randint(0, map_h - h - 1)

            new_room = Rect(x, y, w, h)
            for other_room in self.rooms:
                if new_room.intersect(other_room):  # Evita que las habitaciones se crucen
                    break
            else:
                # Crea una habitación
                self.create_room(new_room)
                (new_x, new_y) = new_room.center()
                if num_rooms == 0:
                    # Posiciona al jugador en el centro de la primera habitación
                    # input(f"{new_x}, {new_y}")
                    player.x = new_x
                    player.y = new_y
                else:
                    # Conecta las habitaciones con túneles
                    (prev_x, prev_y) = self.rooms[num_rooms - 1].center()
                    if random.randint(0, 1) == 1:
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                self.rooms.append(new_room)
                num_rooms += 1

    def create_room(self, room):
        # Marca la habitación en el mapa con '.'
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.map[x][y] = '.'

    def create_h_tunnel(self, x1, x2, y):
        # Crea túneles horizontales
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[x][y] = '.'

    def create_v_tunnel(self, y1, y2, x):
        # Crea túneles verticales
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[x][y] = '.'

    def place_entities(self, room, entities, max_entities_room, entities_list, dungeon_floor):
        """
        Coloca entidades de manera aleatoria dentro de una habitación específica.
        
        :room: La habitación donde se colocarán las entidades.
        :entities: La lista donde se almacenarán las entidades generados.
        :entities_list: Un listado de entidades a procesar.
        :max_entities_room: El número máximo de entidades que puede contener la habitación.
        :dungeon_floor: El piso en turno de la mazmorra.
        """
        num_entities = random.randint(1, max_entities_room)  # Determinar cuántos entidades generar
        entity = None

        for _ in range(num_entities):
            x = random.randint(room.x1 + 1, room.x2 - 1)
            y = random.randint(room.y1 + 1, room.y2 - 1)
            true = True
            while true:
                entity = (random.choice(entities_list))()
                if (isinstance(entity, BasicEnemy) and entity.range <= dungeon_floor) or isinstance(entity, (BasicItem, BasicEnvironmentItem)):
                    entity.x, entity.y = x, y
                    entities.append(entity)
                    true = False
