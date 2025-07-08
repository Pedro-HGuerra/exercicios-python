def pokedex(pokemon):
    """
    This function takes a Pokémon name as input and returns its Pokédex number.
    """
    pokedex = {
        "Bulbasaur": 1,
        "Charmander": 4,
        "Squirtle": 7,
        "Pidgey": 16,
        "Rattata": 19,
        "Jigglypuff": 39,
        "Psyduck": 54,
        "Machop": 66,
        "Magnemite": 81,
        "Poliwag": 60
    }
    
    return pokedex.get(pokemon, None)