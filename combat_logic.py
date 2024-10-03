
from utilities import *


# the name explains it self
def combat_logic(attacker, victim, game_map):
    from start_world_elements import start_player
    start_player_instance = start_player()  # Crear una instancia de la clase
    player = start_player_instance.get_player()
    # Calcular el daño en función del ataque y la defensa del oponente
    damage = max(1, int(attacker.damage / (2 ** (victim.defense / attacker.damage))))
    victim.hp -= damage

    # Determinar nombres adecuados para el atacante y la víctima (considerando si es el jugador)
    attacker_name = 'player' if isinstance(attacker, type(player)) else attacker.name
    victim_name = 'player' if isinstance(victim, type(player)) else victim.name

    # Mostrar el resultado del ataque
    utilities.print_effect(f'\nEl/La [{attacker_name}] atacó a [{victim_name}]. {str(damage)} de daño.')

    # Lógica específica si el atacante es el jugador
    if isinstance(attacker, type(player)):
        # Procesar los efectos de equipo (espada y escudo)
        for equip in ['sword', 'shield']:
            item = attacker.equipment.get(equip)
            if item and item.battle_effect and not victim.alter_status:
                item.battle_effect(victim)

    # Aplicar efectos de estado alterado si los tiene
    if victim.alter_status:
        victim.alter_status[0](victim)  # Aplicar efecto
        victim.alter_status[1] -= 1     # Reducir la duración del efecto
        if victim.alter_status[1] <= 0: # Si el efecto ha terminado
            victim.alter_status = None

    # Verificar si la víctima ha muerto
    if victim.hp <= 0 and victim.state:
        # Cambiar el estado y sprite del mapa para representar la muerte
        game_map[victim.x][victim.y].state = False
        game_map[victim.x][victim.y].sprite = '%'
        utilities.print_effect(f'\n[{victim_name}] murió.\n')

        if not isinstance(victim, type(player)): # Si el enemigo muere
            attacker.exp += victim.exp  # El atacante recibe la experiencia del enemigo
