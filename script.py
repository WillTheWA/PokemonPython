# Classes:

class Pokemon:
    super_effective = {"fire": "grass", "grass": "water", "water": "fire"}

    def max_hp_calc(self):
        """Calculates maximum HP on .__init__() or .level_up()"""
        self.max_hp = round(self.base_hp * (1 + ((self.level - 1) * 0.05)))

    def current_hp_fraction_calc(self):
        """Calculates fraction of max HP, which is used in .level_up() and .revive()"""
        self.current_hp_fraction = round(self.current_hp / self.max_hp)

    def current_hp_calc(self):
        """Sets HP to specific level defined by current_hp_fraction"""
        self.current_hp = round(self.max_hp * self.current_hp_fraction)

    def __init__(self, name, level, ptypes, base_hp=50, fainted=False, current_hp_fraction=1):
        self.name = name.title()
        self.level = min(level, 100) # max level is 100
        self.ptypes = [ptype.title() for ptype in ptypes] # ptype/ptypes to avoid confusion with type() function
        # The Pokemon's maximum health scales with its level and is dependent on its base health at level 1
        self.base_hp = base_hp
        self.current_hp_fraction = current_hp_fraction
        self.max_hp_calc()
        # Current hp might be < max when catching a hurt Pokemon (not implemented yet)
        self.current_hp_calc()
        if fainted:
            self.current_hp = 0
        self.fainted = fainted

    def __repr__(self):
        """Returns basic information on the Pokemon"""
        ptypes_list = [ptype for ptype in self.ptypes]
        ptypes = "-".join(ptypes_list)
        return f"{self.name} is a level {self.level} {ptypes} type Pokémon. It currently has {self.current_hp} HP."

    def level_up(self):
        """Adds a level and calculates new max HP and current HP"""
        self.level += 1
        self.current_hp_fraction_calc()
        # Full recalculation of max HP to avoid rounding to 0
        self.max_hp_calc()
        self.current_hp = round(self.max_hp * self.current_hp_fraction)
        return f"Your {self.name} is now level {self.level}!"

    def lose_health(self, amount):
        """Reduces the current HP by the specified amount (calculated sparately via .attack(), etc.)"""
        self.current_hp -= amount
        self.current_hp_fraction_calc()
        if self.current_hp <= 0:
            return self.knock_out()
        else:
            return f"{self.name.title()} has taken {amount} damage and is now at {self.current_hp} HP."

    def gain_health(self, amount):
        """Heals a Pokemon by amount"""
        self.current_hp += amount
        self.current_hp_fraction_calc()
        if self.current_hp <= 0:
            return self.knock_out()
        else:
            return f"{self.name.title()} has restored {amount} HP and is now at {self.current_hp} HP."

    def knock_out(self):
        self.fainted = True
        self.current_hp_fraction = 0
        self.current_hp = 0
        # This string is not printed immediately to allow for different messages in special circumstances
        return f"{self.name.title()} has been knocked out."

    def revive(self, full=False):
        """Revives the Pokemon to either half HP, or full HP if full=True"""
        if self.fainted == False:
            return f"{self.name} is not fainted and cannot be revived."
        self.fainted = False

        if full:
            self.current_hp_fraction = 1
        else:
            self.current_hp_fraction = .5

        self.current_hp_calc()
        return f"{self.name} has been revived to {self.current_hp} HP."
            

    def attack(self, other):
        """Calculates the damage dealt by an attacking Pokemon"""
        damage = 0

        return damage



# Pokemon Defining:
# NAME = Pokemon("POKEMON NAME", LEVEL#, ["TYPE"])

# Test actions:
# print(POKEMON.revive())
# print(POKEMON.level_up())
# print(POKEMON.lose_health(AMOUNT))
# print(POKEMON.gain_health(AMOUNT))

charmander = Pokemon("charmander", 5, ["fire"])
print(charmander)
