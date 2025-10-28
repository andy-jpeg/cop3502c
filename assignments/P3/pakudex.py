from pakuri import *

class Pakudex:
    def __init__(self, capacity = 20):
        self.capacity = int(capacity)
        self.size = 0
        self.my_pakudex = []

    def get_size(self):
        return self.size
    
    def get_capacity(self):
        return self.capacity
    
    def get_species_array(self):
        if len(self.my_pakudex) != 0:
            species_list = []

            for pakuri in self.my_pakudex:
                species_list.append(pakuri.get_species())

            return species_list
        else:
            return None
        
    def get_stats(self, species):
        entry = None

        for pakuri in self.my_pakudex:
            if pakuri.species == species:
                entry = pakuri

        if entry:
            return [entry.get_attack(), entry.get_defense(), entry.get_speed()]
        else:
            return None

    def sort_pakuri(self):
        names = []

        for pakuri in self.my_pakudex:
            names.append(pakuri.species)

        names.sort()
        sorted_species = []

        for name in names:
            for pakuri in self.my_pakudex:
                if pakuri.get_species() == name:
                    sorted_species.append(pakuri)

        self.my_pakudex = sorted_species

    def add_pakuri(self, species):
        if self.capacity == self.size:
            return None

        entry = None

        for pakuri in self.my_pakudex:
            if pakuri.get_species() == species:
                entry = pakuri

        if not entry:
            pakuri = Pakuri(species)
            self.my_pakudex.append(pakuri)

            self.size += 1
            return pakuri.species
        else:
            return False

    def evolve_species(self, species):
        entry = None

        for pakuri in self.my_pakudex:
            if pakuri.get_species() == species:
                entry = pakuri

        if entry:
            entry.evolve()
            return f"{entry.get_species()} has evolved!"
        else:
            return False