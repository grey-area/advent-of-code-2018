from utils import Group, find_targets, load_data, combat_round

immune, infection = load_data()

while len(immune) > 0 and len(infection) > 0:
    immune, infection = combat_round(immune, infection)

print(sum([grp.units for grp in infection]))
