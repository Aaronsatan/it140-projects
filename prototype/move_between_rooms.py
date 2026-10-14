"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
                "Swedish Rehearsal Dungeon": {"west": "Frozen Record Store"},
                "Frozen Record Store": {"east": "Swedish Rehearsal Dungeon", "north": "Underground Metal Club"},
                "Underground Metal Club": {"south", "Frozen Record Store"}
}
current_room = "Swedish Rehearsal Dungeon"
# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.

# TODO: Run and debug all milestone cases in prototype/README.md.

while True:
                print(f"\nYou are in the {current_room},")
                command = input("Enter north, south, east, west, or exit:").lower().strip()
                if command == "exit":
                                print("Thanks for playing!")
                                break
                elif command in rooms[current_room]:
                                current_room = rooms[current_room][command]
                                print("You moved successfully!")
                else:
                                print("You cannot go that direction.")
                                



                
