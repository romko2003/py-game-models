import datetime
from uuid import uuid4

from db.models import Guild, Race, Player


def main():
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

    # Унікальний nickname через UUID
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

    print("Player created" if created else "Player already exists:", player)
