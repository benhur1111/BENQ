class MCPAdapter:
    def build_context(self, game_state):
        return {
            "role": "Game Master",
            "rules": [
                "Never act for the player",
                "Only update world via tools",
                "Respect game difficulty"
            ],
            "state": game_state
        }

    def allowed_tools(self):
        return [
            "retrieve_lore",
            "update_world",
            "store_memory"
        ]
