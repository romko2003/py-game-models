import json
from models import Race, Guild, Skill, Player  # Імпортуй свої моделі

def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_data in players.values():
        # Race
        race_obj, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )

        # Skills
        for skill in player_data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )

        # Guild
        guild_data = player_data.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        # Player
        Player.objects.get_or_create(
            email=player_data["email"],
            defaults={
                "bio": player_data["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )
