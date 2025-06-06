from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Створюємо раси
    elf_race, _ = Race.objects.get_or_create(name="elf", defaults={"description": ""})
    human_race, _ = Race.objects.get_or_create(name="human", defaults={"description": ""})

    # Створюємо гільдії
    archers_guild, _ = Guild.objects.get_or_create(name="archers", defaults={"description": ""})
    mags_guild, _ = Guild.objects.get_or_create(name="mags", defaults={"description": ""})
    blacksmiths_guild, _ = Guild.objects.get_or_create(name="blacksmiths", defaults={"description": ""})

    # Створюємо скіли (якщо потрібно, можна додати більше)
    Skill.objects.get_or_create(name="Fireball", defaults={"bonus": "", "race": elf_race})

    # Створюємо гравців згідно з тестом
    Player.objects.get_or_create(
        nickname="john",
        defaults={
            "email": "john@gmail.com",
            "bio": "Hello, I'm John, elf ranger",
            "race": elf_race,
            "guild": archers_guild,
        },
    )
    Player.objects.get_or_create(
        nickname="max",
        defaults={
            "email": "max@gmail.com",
            "bio": "Hello, I'm Max, elf mag",
            "race": elf_race,
            "guild": mags_guild,
        },
    )
    Player.objects.get_or_create(
        nickname="arthur",
        defaults={
            "email": "arthur@gmail.com",
            "bio": "Arthur, elf mag",
            "race": elf_race,
            "guild": mags_guild,
        },
    )
    Player.objects.get_or_create(
        nickname="andrew",
        defaults={
            "email": "andrew@gmail.com",
            "bio": "Hello, I'm Andrew",
            "race": human_race,
            "guild": blacksmiths_guild,
        },
    )
    Player.objects.get_or_create(
        nickname="nick",
        defaults={
            "email": "nick@gmail.com",
            "bio": "Hello, I'm Nick",
            "race": human_race,
            "guild": None,
        },
    )


if __name__ == "__main__":
    main()
