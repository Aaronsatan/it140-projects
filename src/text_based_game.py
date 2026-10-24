# Name: Aaron Bouma
# Course IT-140
# Project Two: Text-Based Adventure Game
# Game Title: Death Metal vs Rap
# Description: Collect six metal artifacts



def show_instructions():
    print("DEATH METAL VS RAP")
    print("Collect all six metal artifacts to defeat the Rap King!")
    print("Move: go north, go south, go east, go west")
    print("Collect items: get item name")
    print("Type exit to quit the game.")


def show_status(current_room, inventory, rooms):
    print("Current room:", current_room)
    print("Inventory:",inventory)
    if 'item' in rooms [current_room] :
        print("You see:", rooms[current_room] ['item'])

def main():
    rooms = {
        'Swedish Rehearsal Dungeon':{
            'West': 'Frozen Record Store',
            'North': "Rap King's Arena"
        },
        'Frozen Record Store': {
            'East': 'Swedish Rehearsal Dungeon',
            'North': 'Underground Metal Club',
            'item': 'Ancient Vinyl'
        },
        'Underground Metal Club': {
            'South': 'Frozen Record Store',
            'North': 'Haunted Recording Studio',
            'item': 'Spiked Microphone'
        },
        'Haunted Recording Studio': {
            'South': 'Underground Metal Club',
            'East': 'Festival Backstage',
            'item': 'Drumsticks of Doom'
        },
        'Festival Backstage': {
            'West': 'Haunted Recording Studio',
            'East': 'Abandoned Guitar Factory',
            'item': 'Battle Vest'
        },
        'Abandoned Guitar Factory': {
            'West': 'Festival Backstage',
            'South': 'Hall of Metal Legends',
            'item': 'ESP Guitar'
        },
        'Hall of Metal Legends': {
            'North': 'Abandoned Guitar Factory',
            'West': "Rap King's Arena",
            'item': 'Skull Amplifier'
        },
        "Rap King's Arena": {
            'South': 'Swedish Rehearsal Dungeaon',
            'East': 'Hall of Metal Legends'
        }
    }
    current_room = 'Swedish Rehearsal Dungeon'
    inventory = []
    show_instructions()

    while True:
        show_status(current_room,inventory, rooms)
        command = input("Enter your move: ").lower().strip())
        if command == 'exit':
            print("Thanks for playing Death Metal vs Rap!")
            break
        elif command.startswith('go '):
            direction = command[3:].capitalize()
            if direction in rooms [current_room]:
                current_room = rooms [current_room][direction]
                print("You entered", current_room)
            else:
            print("You cannot go that way!")
            continue
        elif command.startswith('get '):
            item_name = command[4:]
            room_item = rooms [current_room].get('item')
            if room_item and item_name == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]['item']
                print("You picked up", room_item)
            else:
                print("That item is not here!")
        else:
            print("Invalid command!")
    if current_room == "Rap King's Arena":
        if len(inventory) == 6:
        print("You defeated the Rap King! You win!")
            break
        else:
            print("The Rap King defeated you! Game over!")
            break
                
if __name__ == "__main__":
    main()

