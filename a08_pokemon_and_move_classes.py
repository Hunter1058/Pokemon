# Hunter Potter, Penina Strong, Eriko Peterson, Eugenie Son
# Create Pokemon Class

class Pokemon:
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points

    def get_info(self):
        return f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"

    def heal(self):
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")

