import json

with open("pokemon.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

with open("pokemon.pl", "w", encoding="utf-8") as arquivo:

    for nome, pokemon in dados.items():

        nivel = pokemon["level"]
        

        arquivo.write(
            f"pokemon('{nome.lower()}', {nivel}).\n"
        )

        for ability in pokemon["abilities"]:
            arquivo.write(
                f"ability('{nome.lower()}', '{ability.lower()}').\n"
            )
        for item in pokemon.get("items", []):
            arquivo.write(
                f"item('{nome.lower()}', '{item.lower()}').\n"
            )
        for role, setup in pokemon["roles"].items():
            arquivo.write(
                f"role('{nome.lower()}', '{role.lower()}').\n"
            )
            for ability in setup["abilities"]:
                arquivo.write(
                    f"ability('{nome.lower()}','{role.lower()}', '{ability.lower()}').\n"
                )
            for item in setup.get("items", []):
                arquivo.write(
                    f"item('{nome.lower()}','{role.lower()}', '{item.lower()}').\n"
                )
            for tera in setup["teraTypes"]:
                arquivo.write(
                    f"tera('{nome.lower()}','{role.lower()}', '{tera.lower()}').\n"
                )
            for move in setup["moves"]:
                arquivo.write(
                    f"move('{nome.lower()}','{role.lower()}', '{move.lower()}').\n"
                )