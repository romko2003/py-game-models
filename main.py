from db.models import Guild, Player, Race, Skill
import json
from datetime import datetime


def main() -> None:
    with open("players.json", "r") as file:
        player_list = json.load(file)

    for player_data in player_list:
        race_obj, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={
                "description": player_data["race"]["description"],
            },
        )

        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race_obj,
                },
            )

        guild_data = player_data.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data["description"],
                },
            )

        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race_obj,
                "guild": guild_obj,
                "created_at": datetime.fromisoformat(
                    player_data["created_at"]
                ),
            },
        )


if __name__ == "__main__":
    main()
