import json
from db.models import Race, Guild, Skill, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for player_data in players_data:
        # Отримуємо або створюємо расу
        race_obj, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description":player_data["race"].get(
                "description", ""
            )},
        )

        # Отримуємо або створюємо гільдію (може бути None)
        guild_data = player_data.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")},
            )

        # Створюємо/знаходимо скіли і зв'язуємо їх з расою
        skill_objs = []
        for skill_data in player_data.get("skills", []):
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race_obj,
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "description": skill_data.get("description", ""),
                },
            )
            skill_objs.append(skill_obj)

        # Створюємо гравця
        player_obj, created = Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj,
            },
        )

        # Якщо гравець уже існує, оновлюємо поля
        if not created:
            player_obj.email = player_data["email"]
            player_obj.bio = player_data.get("bio", "")
            player_obj.race = race_obj
            player_obj.guild = guild_obj
            player_obj.save()

        # Оновлюємо скіли через many-to-many
        player_obj.skills.set(skill_objs)

    print("Дані успішно додані або оновлені.")
