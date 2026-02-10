from openclaw.games.dungeon_master import DungeonMaster

# Temporary placeholders
llm = None
vector_store = None

game = DungeonMaster(llm, vector_store)

print("🗡️ Welcome to OpenCLaW Dungeon")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("> ")
    if user_input.lower() in ("exit", "quit"):
        print("👋 Goodbye, adventurer.")
        break

    response = game.turn(user_input)
    print("\n" + str(response) + "\n")
