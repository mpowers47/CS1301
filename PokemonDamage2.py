def calculate_modifier(STAB, Type, Critical, Other, Random):
    return STAB*Type*Critical*Other*Random

def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    
    initial_damage = ((2 * Level + 10) / 250) * (Attack / Defense) * Base + 2
    
    modifier = calculate_modifier(STAB, Type, Critical, Other, Random)
    
    return initial_damage * modifier
    
      
    
STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))
