from utils import Group, find_targets, load_data, combat_round


def trial_boost(boost):
    immune, infection = load_data(boost=boost)

    prev_units = sum([grp.units for grp in immune + infection])
    while len(immune) > 0 and len(infection) > 0:
        immune, infection = combat_round(immune, infection)

        units = sum([grp.units for grp in immune + infection])
        if prev_units == units:
            break
        prev_units = units

    return immune, infection

def boost_search_value(immune, infection):
    return len(immune) > 0 and len(infection) == 0

def binary_search(low=1, high=None):
    if high is not None:
        mid = (low + high) // 2
    else:
        mid = low * 2

    immune, infection = trial_boost(mid)

    if low == mid:
        return immune
    elif boost_search_value(immune, infection):
        return binary_search(low, mid-1)
    else:
        return binary_search(mid+1, high)

immune = binary_search()

print(sum([grp.units for grp in immune]))
