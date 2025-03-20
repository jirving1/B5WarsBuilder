import tkinter as tk
import CompositionRules as rules

LARGEFONT = ("Verdana", 35)

class Window:
    def __init__(self, width=800, height=600):
        self.root = tk.Tk()
        self.root.title("B5Builder")
        self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
          # Changed from self to self.root

    def close(self):
        self.root.destroy()

class StartScreen(Window):
    def __init__(self):
        super().__init__()
        
        self.label = tk.Label(self.root, text="B5Builder")
        self.label.pack(padx=10, pady=10)

        self.fleet_name_label = tk.Label(self.root, text="Enter Fleet Name")
        self.fleet_name_label.pack(padx=10, pady=5)
        self.fleet_name = tk.Entry(self.root)  # Removed text parameter, it doesn't work with Entry
        self.fleet_name.insert(0, "Fleet Name")  # Set default text this way
        self.fleet_name.pack(padx=10, pady=5)

        self.selected_faction_label = tk.Label(self.root, text="Select Faction")
        self.selected_faction_label.pack(padx=10, pady=5)
        self.selected_faction_var = tk.StringVar(self.root)
        self.factions = ("Earth Alliance", "Minbari", "Centauri", "Narn")
        self.selected_faction = tk.OptionMenu(self.root, self.selected_faction_var, self.factions[0], *self.factions)
        self.selected_faction.pack(padx=10, pady=5)

        self.fleet_value_label = tk.Label(self.root, text="Enter Point Value")
        self.fleet_value_label.pack(padx=10, pady=5)
        self.fleet_value = tk.Entry(self.root)
        self.fleet_value.insert(0, "Point Value")
        self.fleet_value.pack(padx=10, pady=5)

        self.create_fleet_button = tk.Button(self.root, text="Create Fleet", command=self.create_fleet)
        self.create_fleet_button.pack(padx=10, pady=10)

    def create_fleet(self):
        fleet_name = self.fleet_name.get()
        faction = self.selected_faction_var.get()  # Changed from selected_faction.get() to option_var.get()
        value = self.fleet_value.get()
        new_fleet = rules.Fleet(fleet_name, faction, value)
        FleetScreen(new_fleet)
        # You can add code here to do something with new_fleet, like:
        # print(f"Created fleet: {fleet_name}, {faction}, {value}")

class FleetScreen(Window):
    def __init__(self, fleet_object):
        super().__init__()
        self.fleet = fleet_object
        
        self.label = tk.Label(self.root, text=f"{self.fleet.name} | {self.fleet.faction}")
        self.label.pack(padx=10, pady=5)

        list_items = tk.Variable()
        unit_list = tk.Listbox(self.root,) #make a loop to check for faction, then fetch the locations for that faction's units
    #three listboxes for ships, fighters and structures
        

        
        
       

        
if __name__ == "__main__":
    app = StartScreen()
    app.root.mainloop()