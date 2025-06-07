import json
from db.models import Player, Race, Skill, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for player_data in players_data.values():
        # Отримуємо або створюємо расу
        race_data = player_data["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        # Додаємо скіли для раси
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race_obj,
            )

        # Отримуємо або створюємо гільдію (може бути None)
        guild_obj = None
        guild_data = player_data.get("guild")
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        # Створюємо гравця
        Player.objects.get_or_create(
            email=player_data["email"],
            defaults={
                "bio": player_data.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj,
            },
        )
