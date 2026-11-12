import json

with open("pokemon.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

pokemonfatos = """"""
ability2fatos = """"""
item2fatos = """"""
rolefatos = """"""
ability3fatos = """"""
item3fatos = """"""
terafatos = """"""
movefatos = """"""
for nome, pokemon in dados.items():
    nivel = pokemon["""level"""]
    
    nome = nome.replace(' ', '-').replace("'", '')
    pokemonfatos += f"""pokemon('{nome.lower()}', {nivel}).\n"""

    for ability in pokemon["""abilities"""]:
        ability = ability.replace(' ', '-')
        ability2fatos += f"""ability('{nome.lower()}', '{ability.lower()}').\n"""
    
    for item in pokemon.get("""items""", []):
        item = item.replace(' ', '-')
        item2fatos += f"""item('{nome.lower()}', '{item.lower().replace(' ', '-')}').\n"""
    
    for role, setup in pokemon["""roles"""].items():
        role = role.replace(' ', '-')
        rolefatos += f"""role('{nome.lower()}', '{role.lower().replace(' ', '-')}').\n"""
    
        for ability in setup["""abilities"""]:
            ability = ability.replace(' ', '-')
            ability3fatos += f"""ability('{nome.lower()}', '{role.lower().replace(' ', '-')}', '{ability.lower().replace(' ', '-')}').\n"""
        
        for item in setup.get("""items""", []):
            item = item.replace(' ', '-')
            item3fatos +=  f"""item('{nome.lower()}', '{role.lower().replace(' ', '-')}', '{item.lower().replace(' ', '-')}').\n"""
        
        for tera in setup["""teraTypes"""]:
            tera = tera.replace(' ', '-')
            terafatos += f"""tera('{nome.lower()}', '{role.lower().replace(' ', '-')}', '{tera.lower().replace(' ', '-')}').\n"""
        
        for move in setup["""moves"""]:
            move = move.replace(' ', '-')
            movefatos += f"""move('{nome.lower()}', '{role.lower().replace(' ', '-')}', '{move.lower().replace(' ', '-')}').\n"""
        
with open("pokemon.pl", "w", encoding="utf-8") as arquivo:
    arquivo.write(
        pokemonfatos + ability2fatos + ability3fatos + item2fatos + item3fatos + rolefatos + terafatos + movefatos
    )