from utils import Group, find_targets, load_data, combat_round

boost = 1
while True:
    print(boost)

    immune, infection = load_data(boost=boost)

    prev_immune_units = sum([grp.units for grp in immune])
    prev_infection_units = sum([grp.units for grp in infection])

    while len(immune) > 0 and len(infection) > 0:
        immune, infection = combat_round(immune, infection)

        immune_units = sum([grp.units for grp in immune])
        infection_units = sum([grp.units for grp in infection])
        if prev_immune_units == immune_units and prev_infection_units == infection_units:
            break
        prev_immune_units = immune_units
        prev_infection_units = infection_units

    if len(immune) > 0 and len(infection) == 0:
        print(sum([grp.units for grp in immune]))
        break

    boost += 1
