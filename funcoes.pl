exclusive_relation(Relation, Pokemon, Value) :-
    call(Relation, Pokemon, Value),
    \+ (
        call(Relation, OutroPokemon, Value),
        OutroPokemon \= Pokemon
    ).

moves_by_role(Pokemon, Result) :-
    setof(Role-Moves,
          (setof(Move, move(Pokemon, Role, Move), Moves)),
          Result).

move(Pokemon, Move) :-
    distinct([Pokemon, Move], move(Pokemon, _, Move)).

tera(Pokemon, Tera) :-
    distinct([Pokemon, Tera], tera(Pokemon, _, Tera)).

relation(Relation, Value, Result) :-
    findall(Pokemon,
            call(Relation, Pokemon, Value),
            Pokemons),
    sort(Pokemons, Result).

count_relation(Relation, Value, Count) :-
    relation(Relation, Value, Result),
    length(Result, Count).