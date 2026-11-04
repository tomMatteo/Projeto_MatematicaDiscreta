import json

with open("pokemon.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

with open("pokemon.pl", "w", encoding="utf-8") as arquivo:

    for nome, pokemon in dados.items():

        nivel = pokemon["level"]
        

        arquivo.write(
            f"pokemon('{nome}', {nivel}).\n"
        )

        for ability in pokemon["abilities"]:
            arquivo.write(
                f"ability('{nome}', '{ability}').\n"
            )
        for item in pokemon.get("items", []):
            arquivo.write(
                f"item('{nome}', '{item}').\n"
            )
        for role, setup in pokemon["roles"].items():
            arquivo.write(
                f"role('{nome}', '{role}').\n"
            )
            for ability in setup["abilities"]:
                arquivo.write(
                    f"ability('{nome}','{role}', '{ability}').\n"
                )
            for item in setup.get("items", []):
                arquivo.write(
                    f"item('{nome}','{role}', '{item}').\n"
                )
            for tera in setup["teraTypes"]:
                arquivo.write(
                    f"tera('{nome}','{role}', '{tera}').\n"
                )
            for move in setup["moves"]:
                arquivo.write(
                    f"move('{nome}','{role}', '{move}').\n"
                )