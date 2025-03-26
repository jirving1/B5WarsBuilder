#self, faction, name, ship_class, rarity, in_service, hanger_size, cost
from vessels import Ship, Fighter
starship_units = [
    Ship("Earth Alliance", "Artemis Heavy Frigate (Beta Model)", "Heavy Combat Vessel", "Base model", 2190, 0, 625),
    Ship("Earth Alliance", "Artemis Escort Frigate (Zeta Model)", "Heavy Combat Vessel", "Uncommon Artemis variant", 2242, 0, 650),
    Ship("Earth Alliance", "Avenger Heavy Carrier (Gamma Model)", "Capital Ship", "Base Model", 2240, 48, 580),
    Ship("Earth Alliance", "EarthForce One (Delta Model)", "Capital Ship", "Base model", 2251, 12, 350),
    Ship("Earth Alliance", "Explorer Survey Ship (Alpha Model)", "Enormous Unit", "Base model", 2253, 24, 1000),
    Ship("Earth Alliance", "Hermes Priority Transport (Beta Model)", "Heavy Combat Vessel", "Base model", 2168, 6, 420),
    Ship("Earth Alliance", "Hyperion Heavy Cruiser (Theta Model)", "Capital Ship", "Base model", 2246, 6, 705),
    Ship("Earth Alliance", "Hyperion Aegis Cruiser (Lambda Model)", "Capital Ship", "Rare Hyperion variant", 2257, 6, 800),
    Ship("Earth Alliance", "Hyperion Assault Cruiser (Gamma Model)", "Capital Ship", "Common Hyperion variant", 2230, 0, 600),
    Ship("Earth Alliance", "Nova Dreadnought (Beta Model)", "Capital Ship", "Base model", 2242, 24, 1350),
    Ship("Earth Alliance", "Olympus Corvette (Delta Model)", "Heavy Combat Vessel", "Base model", 2241, 0, 600),
    Ship("Earth Alliance", "Omega Destroyer (Alpha Model)", "Capital Ship", "base model", 2250, 24, 925),
    Ship("Earth Alliance", "Oracle Scout Cruiser (Gamma Model)", "Capital Ship", "Base model", 2216, 0, 600),
    Ship("Earth Alliance", "Orestes System Monitor (Epsilon Model)", "Capital Ship", "Base model", 2249, 12, 650),
    Ship("Earth Alliance", "Poseidon Supercarrier (Alpha Model)", "Capital Ship", "Base model", 2255, 96, 950),
    Ship("Earth Alliance", "Sagittarius Missile Cruiser (Beta Model)", "Capital Ship", "Base model", 2230, 0, 700),
    Ship("Earth Alliance", "Tethys Police Cutter (Kappa Model)", "Medium Ship", "Base model", 2246, 0, 375),
]



fighter_units = [
    Fighter("Earth Alliance", "Starfury Heavy Fighter", "Heavy Fighters", 2244, 57),
    Fighter("Earth Alliance", "Badger Long-Range Fighters", "Heavy Fighters", 22, 70),
    Fighter("Earth Alliance", "Thunderbolt Assault Fighters", "Heavy Fighters", 2259, 80),
]
#make a ship variant class that inherits from ship
# skip variant rules for now


#"hyperion_aegis" : ShipVariant("Earth Alliance", "Hyperion Aegis Cruiser (Lambda Model)", "Capital Ship", "Rare Hyperion variant", 2257, 6, 800, "hyperion_ca"),
    #"hyperion_assault" :  ShipVariant("Earth Alliance", "Hyperion Assault Cruiser (Gamma Model)", "Capital Ship", "Common Hyperion variant", 2230, 0, 600, "hyperion_ca"),
    #"artemis_escort" : ShipVariant("Earth Alliance", "Artemis Escort Frigate (Zeta Model)", "Heavy Combat Vessel", "Uncommon Artemis variant", 2242, 0, 650, "artemis_heavy"),