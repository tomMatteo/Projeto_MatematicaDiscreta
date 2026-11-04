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
    
    
    pokemonfatos += f"""pokemon("{nome.lower()}", {nivel}).\n"""

    for ability in pokemon["""abilities"""]:
        
        ability2fatos += f"""ability("{nome.lower()}", "{ability.lower()}").\n"""
    
    for item in pokemon.get("""items""", []):
        
        item2fatos += f"""item("{nome.lower()}", "{item.lower()}").\n"""
    
    for role, setup in pokemon["""roles"""].items():
        
        rolefatos += f"""role("{nome.lower()}", "{role.lower()}").\n"""
    
        for ability in setup["""abilities"""]:
            
            ability3fatos += f"""ability("{nome.lower()}","{role.lower()}", "{ability.lower()}").\n"""
        
        for item in setup.get("""items""", []):
            
            item3fatos +=  f"""item("{nome.lower()}","{role.lower()}", "{item.lower()}").\n"""
        
        for tera in setup["""teraTypes"""]:
            
            terafatos += f"""tera("{nome.lower()}","{role.lower()}", "{tera.lower()}").\n"""
        
        for move in setup["""moves"""]:
            
            movefatos += f"""move("{nome.lower()}","{role.lower()}", "{move.lower()}").\n"""
        
with open("pokemon.pl", "w", encoding="utf-8") as arquivo:
    arquivo.write(
        pokemonfatos + ability2fatos + ability3fatos + item2fatos + item3fatos + rolefatos + terafatos + movefatos
    )