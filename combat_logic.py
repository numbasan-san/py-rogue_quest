
from utilities import *

def combat_logic(attacker, victim, game_map, player):

    # Calcular el daño en función del ataque y la defensa del oponente
    damage = max(1, int(attacker.damage / (2 ** (victim.defense / attacker.damage))))
    victim.hp -= damage

    # Determinar nombres adecuados para el atacante y la víctima
    attacker_name = 'player' if attacker is player else attacker.name
    victim_name = 'player' if victim is player else victim.name

    # Mostrar el resultado del ataque
    utilities.print_effect(f'\nEl/La [{attacker_name}] atacó a [{victim_name}]. {damage} de daño.')

    # Lógica específica si el atacante es el jugador
    if attacker is player:
        for equip in ['sword', 'shield']:
            item = attacker.equipment.get(equip)
            if item and item.battle_effect and not victim.alter_status:
                item.battle_effect(victim)

    # Aplicar efectos de estado alterado si los tiene
    if victim.alter_status:
        victim.alter_status[0](victim)  # Aplicar efecto
        victim.alter_status[1] -= 1       # Reducir la duración del efecto
        if victim.alter_status[1] <= 0:   # Si el efecto ha terminado
            victim.alter_status = None

    # Verificar si la víctima ha muerto
    if victim.hp <= 0:
        # Cambiar el estado y sprite del mapa para representar la muerte
        game_map[victim.x][victim.y].state = False
        game_map[victim.x][victim.y].sprite = '%'
        
        if not victim is player:
            utilities.print_effect(f'\n[{victim_name}] murió.')

        if victim is not player:  # Si el enemigo muere
            attacker.exp += victim.exp  # El atacante recibe la experiencia del enemigo
