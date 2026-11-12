# Trabalho de Matematica Discreta
Trabalho desenvolvido para a matéria de Logica e Matematica Discreta com o objetivo de aprendizado de limpeza de dados e formação de base de conhecimentos de Prolog.

## Como foi feito?
O projeto utiliza-se do json de informações de Pokémons gerados no modelo Gen 9 Random Battle do site Pokémon Showdown, https://pkmn.github.io/randbats/data/gen9randombattle.json, renomeado para pokemon.json nesse arquivo.

A estruturação da base de fatos a partir do projeto foi feita da seguinte maneira:

Fatos de dois argumentos:
- pokemon - Representa um Pokémon e seu nível.
- role - Representa um Pokémon e uma possível função desempenhada no time.

Fatos de tres argumentos:
- tera - Representa a relação entre um pokémon, sua função, e os possiveis tipos tera (diferente dos tipos reais) que ele pode pode ter quando desempenhando essa função.
- move - Representa a relação entre um pokémon, sua função, e os possiveis ataques/movimentos quando desempenhando tal função.

Fatos com dois ou tres argumentos:
- ability - Representa um Pokémon e suas posiveis habilidades quando tem dois argumentos, e adiciona função quando possui três, relacionando função com habilidade.
- item - Representa um Pokémon e os itens que pode estar segurando quando tem dois argumentos, e adiciona função quando tem três, relacionando função com o item segurado.

## Escolhas tomadas ao longo do projeto
1. Escolha da base de dados
- Eu já tinha o json e utilizava ele para poder jogar o modo. Como todos os Pokémons meus quanto do meu oponente vão ser gerados a partir desta base, decidi utiliza-la para o projeto e no futuro para mais fácilmente referenciar dados enquanto jogo.
2. Por que foram estruturados assim os fatos?
- Principalmente, por que estão assim na base, já uso ela e sei que ela está, em geral, correta com o que esta no jogo.
3. Detalhes no tratamento: Casos especiais
- Existem três casos especiais, um que não foi levado para a base de conheciento, e outro que foi necessario tratar de uma maneira especifica.
- **EVs e IVs**: Estes dois são valores que são usados no calculo dos status do Pokémon. EVs foram excluidos por que normalmente representam mudanças muito pequenas, e menores ainda partindo de Pokémon de nível baixo. Já os IVs são mudanças mais significativas, mas, em geral, não são identificados a menos que um iv ou outro não seja o maxímo, em tal caso costumam estar no mínimo para lidar com situações específicas que é em geral identificavel antes mesmo de ter informações do Pokémon que o oponente tem.
- **Items**: Items foi mantido, porém tradado diferente, enquanto não tem jeito de um Pokémon não ter nível, tipo tera, função e moves, items não são obrigatórios quando fazendo a "ficha" de um Pokémon. E, de fato, existe pelo menos um Pokémon que prefere não usar itens.
Ao invés de usar:
```
pokemon["itens"]
```
e 
```
setup["itens"]
```
foi usado:
```
pokemon.get("items", [])
```
e 
```
setup.get("items", [])
```
4. Correções da base de conhecimento
- Eu acho que não daria muito erro continuar do jeito que tava. Funcionava? Funcionava. Mas procurando na internet, encontrei que utilizar "" (duas aspas) significava lista em prolog. Então decidi por adequar, trocando espaços por "-" e removendo os valores ' de dentro do nome de alguns pokemons e habilidades para poder utilizar '' para estruturção de fatos no prolog. 
5. Criação de funções
- **Formação das Funções**: De primeira, eu ia fazer funções especificas para cada fato (role, abilidade, move, item, tera), e, de fato, cheguei a fazer essas funções, em especifico, a função exclusive_relation era exlusive_ability e só funcionava para habilidades, e as funções relation e count_relation eram role_share e count_share, que funcionavam somente para funções. Porém eu encontrei um certo camarada chamado call que me permitiu encurtar de sei la quantas funções para 3.
- **Função move/2**: Existe PURAMENTE para funcionar com relation.
- **Função moves_by_role**: Essa aqui sobreviveu por que existem pokemons com moves possiveis muito diversos, e isso permite que eles tenham fuções muito diversas. Descobrir um move e comparar com moves_by_role ajuda de um jeito quando eu vou jogar...

## Considerações finais
Pokémon é um jogo complexo e essa base de conhecimento exige conhecimento externo a ela para uso dentro do contexto que eu mencionei ao inicio, muito desse contexto é explicado dentro do jogo, porém existem pontos cegos quando unindo as informações dessa base e do jogo. Como planejo fazer uso pessoal dessa base dentro deste contexto no futuro, existem chances de que eu vá continuar trabalhando nesse projeto, talvez até o tornando em um site ou algo similar.