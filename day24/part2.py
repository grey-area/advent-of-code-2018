from utils import Group, find_targets, load_data, combat_round

boost = 1
while True:
    immune, infection = load_data(boost=boost)

    prev_units = sum([grp.units for grp in immune + infection])
    while len(immune) > 0 and len(infection) > 0:
        immune, infection = combat_round(immune, infection)

        units = sum([grp.units for grp in immune + infection])
        if prev_units == units:
            break
        prev_units = units

    if len(immune) > 0 and len(infection) == 0:
        break

    boost += 1

print(sum([grp.units for grp in immune]))
