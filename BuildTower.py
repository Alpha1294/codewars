def tower_builder(n_floors):
    result = []
    temporal = ""
    spaces = round((n_floors - 1))
    stars = 1
    for i in range(n_floors):
        print(spaces * " " + stars * "*" + spaces*" ")
        temporal = spaces * " " + stars * "*" + spaces*" "
        result.append(temporal)
        spaces -= 1
        stars += 2
    return result


print(tower_builder(5))
