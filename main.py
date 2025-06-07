import json

from db.models import Race, Guild, Skill, Player


def main():
    with open("db/data.json", encoding="utf-8") as file:
        data = json.load(file)

    # Створення рас
    for race_name, race_data in data["races"].items():
        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_data["description"]}
        )

        for skill_name, bonus in race_data["skills"].items():
            skill_obj, _ = Skill.objects.get_or_create(name=skill_name)
            race_obj.skills.add(skill_obj, through_defaults={"bonus": bonus})

    # Створення гільдій
    for guild_name, guild_data in data["guilds"].items():
        guild_obj, _ = Guild.objects.get_or_create(
            name=guild_name,
            defaults={"description": guild_data["description"]}
        )

        for skill_name, bonus in guild_data["skills"].items():
            skill_obj, _ = Skill.objects.get_or_create(name=skill_name)
            guild_obj.skills.add(skill_obj, through_defaults={"bonus": bonus})

    # Створення гравців
    for nickname_key, player_data in data["players"].items():
        race_obj = Race.objects.get(name=player_data["race"])
        guild_name = player_data.get("guild")
        guild_obj = Guild.objects.get(name=guild_name) if guild_name else None

        Player.objects.get_or_create(
            nickname=player_data["nickname"],  # це збігається з ключем
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj,
            }
        )
