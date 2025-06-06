import json
from db.models import Race, Skill, Player, Guild


def main():
    # Відкриваємо JSON з гравцями
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for p in players_data:
        # Отримуємо або створюємо расу
        race_obj, _ = Race.objects.get_or_create(
            name=p["race"]["name"],
            defaults={"description": p["race"].get("description", "")},
        )

        # Отримуємо або створюємо гільдію (якщо є)
        guild_data = p.get("guild")
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")},
            )
        else:
            guild_obj = None

        # Створимо список об'єктів скіллів
        skill_objs = []
        for skill_data in p.get("skills", []):
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "description": skill_data.get("description", ""),
                    "race": race_obj,
                },
            )
            skill_objs.append(skill_obj)

        # Створюємо або отримуємо гравця
        player_obj, created = Player.objects.get_or_create(
            nickname=p["nickname"],
            defaults={
                "email": p.get("email", ""),
                "bio": p.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj,
            },
        )

        # Оновлюємо скіли гравця (ManyToMany)
        player_obj.skills.set(skill_objs)
        player_obj.save()
