import datetime
from uuid import uuid4

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Створюємо або отримуємо расу
    race, _ = Race.objects.get_or_create(
        name="Elf",
        defaults={
            "description": "Graceful and wise forest dwellers.",
        },
    )

    # Створюємо або отримуємо гільдію
    guild, _ = Guild.objects.get_or_create(
        name="Mages of Light",
        defaults={
            "description": "An ancient order of elven mages.",
        },
    )

    # Створюємо або отримуємо скіла
    skill, _ = Skill.objects.get_or_create(
        name="Fireball",
        defaults={
            "description": "A powerful fire magic spell.",
            "power": 50,
        },
    )

    # Унікальний nickname через UUID, щоб не було конфліктів
    unique_nickname = f"max_elf_{uuid4().hex[:6]}"

    # Створюємо або отримуємо гравця
    player, created = Player.objects.get_or_create(
        nickname=unique_nickname,
        defaults={
            "email": "max@gmail.com",
            "bio": "Hello, I'm Max, elf mag",
            "race": race,
            "guild": guild,
            "created_at": datetime.datetime.now(),
        }
    )

    if hasattr(player, "skills"):
        player.skills.add(skill)

    print("Player created" if created else "Player already exists:", player)


if __name__ == "__main__":
    main()
