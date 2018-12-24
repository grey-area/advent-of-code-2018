import re
from collections import defaultdict


def find_targets(attacking_army, defending_army):
    attacking_army = sorted(attacking_army, key=lambda g: (g.effective_power, g.initiative), reverse=True)

    for attack_grp in attacking_army:
        attack_grp.attacking = None
        to_attack = None
        best_damage = 0
        best_effective_power = 0
        best_initiative = 0
        for defend_grp in defending_army:
            if defend_grp.under_attack:
                continue

            damage = attack_grp.do_damage(defend_grp, simulation=True)
            if damage > best_damage:
                best_damage = damage
                to_attack = defend_grp
                best_effective_power = defend_grp.effective_power
                best_initiative = defend_grp.initiative
            elif damage == best_damage:
                if defend_grp.effective_power > best_effective_power:
                    to_attack = defend_grp
                    best_effective_power = defend_grp.effective_power
                    best_initiative = defend_grp.initiative
                elif best_effective_power == defend_grp.effective_power:
                    if defend_grp.initiative > best_initiative:
                        to_attack = defend_grp
                        best_initiative = defend_grp.initiative

        if to_attack is not None and best_damage is not 0:
            attack_grp.attacking = to_attack
            to_attack.under_attack = True


def combat_round(immune, infection):
    find_targets(immune, infection)
    find_targets(infection, immune)
    all_groups = sorted(immune + infection, key=lambda g:g.initiative, reverse=True)
    for grp in all_groups:
        grp.do_damage(grp.attacking, simulation=False)
    for grp in immune:
        grp.attacking = None
        grp.under_attack = False
        grp.compute_effective_power()
    for grp in infection:
        grp.attacking = None
        grp.under_attack = False
        grp.compute_effective_power()
    immune = [grp for grp in immune if grp.units > 0]
    infection = [grp for grp in infection if grp.units > 0]
    return immune, infection


class Group():
    def __init__(self, build_str, boost=0):
        re_str = '(\d+) units each with (\d+) hit points (?:\(([^\)]+)\) )*with an attack that does (\d+) (\S+) damage at initiative (\d+)'
        units, HP, strengths_str, damage, self.dtype, initiative = re.search(re_str, build_str).groups()
        self.units, self.HP, self.damage, self.initiative = int(units), int(HP), int(damage), int(initiative)
        self.modifiers = defaultdict(list)
        self.boost = boost

        if strengths_str is not None:
            strengths_re = '(\S+) to ([^;]+)(?:; (\S+) to ([^;]+))?'
            strength_type1, strengths1, strength_type2, strengths2 = re.search(strengths_re, strengths_str).groups()

            self.modifiers[strength_type1] = strengths1.split(', ')
            if strength_type2 is not None:
                self.modifiers[strength_type2] = strengths2.split(', ')

        self.attacking = None
        self.under_attack = False
        self.compute_effective_power()

    def do_damage(self, other, simulation=True):
        if other is None:
            return 0

        HP_damage = self.effective_power
        if self.dtype in other.modifiers['immune']:
            HP_damage = 0
        elif self.dtype in other.modifiers['weak']:
            HP_damage *= 2

        if not simulation:
            units_to_remove = HP_damage // other.HP
            other.units -= units_to_remove
            if other.units < 0:
                other.units = 0
            other.compute_effective_power()

        return HP_damage

    def compute_effective_power(self):
        self.effective_power = self.units * (self.damage + self.boost)


def load_data(boost=0):
    with open('input') as f:
        immune_str, infection_str = f.read().split('\n\n')

    immune = [Group(line, boost) for line in immune_str.splitlines()[1:]]
    infection = [Group(line) for line in infection_str.splitlines()[1:]]

    return immune, infection
