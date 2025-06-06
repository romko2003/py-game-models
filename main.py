import datetime
from uuid import uuid4

from db.models import Race, Skill, Player, Guild


def main() -> None:
    race, _ = Race.objects.get_or_create(name="Elf")
    guild_data = {"name": "Mages of Light"}  # Приклад даних, можеш замінити

    guild, _ = Guild.objects.get_or_create(
        name=guild_data["name"],
        defaults={"description": guild_data.get("description", "")},
    )

    skill, _ = Skill.objects.get_or_create(name="Fireball", race=race)

    unique_nickname = f"max_elf_{uuid4().hex[:6]}"

    player, created = Player.objects.get_or_create(
        nickname=unique_nickname,
        defaults={
            "email": "max@gmail.com",
            "bio": "Hello, I'm Max, elf mag",
            "race": race,
            "guild": guild,
            "created_at": datetime.datetime.now(),
        },
    )

    if hasattr(player, "skills"):
        player.skills.add(skill)

    print("Player created" if created else "Player already exists:", player)


if __name__ == "__main__":
    main()
