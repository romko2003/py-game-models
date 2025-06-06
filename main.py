from db.models import Guild, Player, Race, Skill
import json
from datetime import datetime


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for p in players:
        race_obj, _ = Race.objects.get_or_create(
            name=p["race"]["name"],
            defaults={"description": p["race"]["description"]},
        )

        for skill in p["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race_obj,
                },
            )

        guild_data = p.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )

        Player.objects.get_or_create(
            nickname=p["nickname"],
            defaults={
                "email": p["email"],
                "bio": p["bio"],
                "race": race_obj,
                "guild": guild_obj,
                "created_at": datetime.fromisoformat(p["created_at"]),
            },
        )


if __name__ == "__main__":
    main()
