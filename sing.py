import random

class AdventureQuest:
    def __init__(self):
        self.player_name = ""
        self.current_room = None
        self.game_over = False
        
    def setup_game(self):
        print("Welcome to Adventure Quest!")
        self.player_name = input("Enter your character's name: ")
        
        # Define rooms
        self.rooms = {
            "start": Room("Start", "You find yourself at the entrance of a dark cave."),
            "cave_entrance": Room("Cave Entrance", "A vast cave opens up before you."),
            "treasure_room": Room("Treasure Room", "You've discovered a room full of treasure!"),
            "dragon_lair": Room("Dragon Lair", "A fierce dragon guards the path forward."),
            "exit": Room("Exit", "Congratulations! You've successfully completed the adventure.")
        }
        
        # Define room connections
        self.rooms["start"].add_connection(self.rooms["cave_entrance"])
        self.rooms["cave_entrance"].add_connection(self.rooms["treasure_room"])
        self.rooms["cave_entrance"].add_connection(self.rooms["dragon_lair"])
        self.rooms["treasure_room"].add_connection(self.rooms["exit"])
        self.rooms["dragon_lair"].add_connection(self.rooms["exit"])
        
        # Set starting room
        self.current_room = self.rooms["start"]
        
    def play(self):
        while not self.game_over:
            self.current_room.describe()
            self.current_room.print_connections()
            
            choice = input("Enter your choice (or 'quit' to exit the game): ").lower()
            
            if choice == "quit":
                self.game_over = True
                print("Thanks for playing!")
                break
            
            if choice in self.current_room.connections:
                self.current_room = self.current_room.connections[choice]
                self.handle_room()
            else:
                print("Invalid choice. Try again.")
    
    def handle_room(self):
        if self.current_room == self.rooms["dragon_lair"]:
            print("The dragon breathes fire at you! You must make a daring escape.")
            escape_chance = random.randint(1, 10)
            if escape_chance <= 6:
                print("You manage to escape the dragon's lair.")
            else:
                print("You've been caught by the dragon. Game over.")
                self.game_over = True
        elif self.current_room == self.rooms["exit"]:
            print(f"Congratulations, {self.player_name}! You've completed the adventure.")
            self.game_over = True

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        
    def add_connection(self, room):
        self.connections[room.name.lower()] = room
    
    def describe(self):
        print(f"You are in {self.name}. {self.description}")
    
    def print_connections(self):
        print("Available paths:")
        for room_name in self.connections:
            print(f"- {room_name.capitalize()}")

if __name__ == "__main__":
    game = AdventureQuest()
    game.setup_game()
    game.play()
