import json, Player

def load_level_data(file_path):
    with open(file_path, 'r') as file:
        level_data = json.load(file)
    return level_data


def create_level(level_data):
    tile_map = level_data['tile_map']
    player_start = level_data['player_start']

    player = Player(player_start['x'], player_start['y'])

    return player
