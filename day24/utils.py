import re
from collections import defaultdict


def find_targets(attacking_army, defending_army):
    attacking_army = sorted(attacking_army, key=lambda g: (g.effective_power, g.initiative), reverse=True)

    for attack_grp in attacking_army:
        candidate_to_attack = sorted(defending_army, key=lambda g: (g.under_attack,
                                                                    -attack_grp.do_damage(g, simulation=True),
                                                                    -g.effective_power,
                                                                    -g.initiative))[0]


        damage = attack_grp.do_damage(candidate_to_attack, simulation=True)
        if damage > 0 and not candidate_to_attack.under_attack:
            attack_grp.attacking = candidate_to_attack
            candidate_to_attack.under_attack = True


def combat_round(immune, infection):
    find_targets(immune, infection)
    find_targets(infection, immune)
    all_groups = sorted(immune + infection, key=lambda g:g.initiative, reverse=True)
    for grp in all_groups:
        grp.do_damage(grp.attacking)
    for grp in all_groups:
        grp.post_combat_reset()
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

    def do_damage(self, other, simulation=False):
        if other is None:
            return 0

        HP_damage = self.effective_power
        if self.dtype in other.modifiers['immune']:
            HP_damage = 0
        elif self.dtype in other.modifiers['weak']:
            HP_damage *= 2

        if not simulation:
            units_to_remove = HP_damage // other.HP
            other.units = max(0, other.units - units_to_remove)
            other.compute_effective_power()

        return HP_damage

    def compute_effective_power(self):
        self.effective_power = self.units * (self.damage + self.boost)

    def post_combat_reset(self):
        self.attacking = None
        self.under_attack = False
        self.compute_effective_power()


def load_data(boost=0):
    with open('input') as f:
        immune_str, infection_str = f.read().split('\n\n')

    immune = [Group(line, boost) for line in immune_str.splitlines()[1:]]
    infection = [Group(line) for line in infection_str.splitlines()[1:]]

    return immune, infection
