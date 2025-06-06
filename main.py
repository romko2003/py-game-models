from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Раси з описами
    elf_race, _ = Race.objects.get_or_create(
        name="elf",
        defaults={"description": "The magic race"},
    )
    human_race, _ = Race.objects.get_or_create(
        name="human",
        defaults={"description": "Human race"},
    )

    # Гільдії з описами
    archers_guild, _ = Guild.objects.get_or_create(
        name="archers",
        defaults={"description": "Archers guild"},
    )
    mags_guild, _ = Guild.objects.get_or_create(
        name="mags",
        defaults={"description": "Mages guild"},
    )
    blacksmiths_guild, _ = Guild.objects.get_or_create(
        name="blacksmiths",
        defaults={"description": "Blacksmiths guild"},
    )

    # Скіли з правильними описами
    Skill.objects.get_or_create(
        name="Teleportation",
        defaults={
            "description": (
                "The ability to move so fast they look like they're teleporting. "
                "Could be considered to technically be Teleportation."
            ),
            "bonus": "",
            "race": elf_race,
        },
    )
    Skill.objects.get_or_create(
        name="Reality Warping",
        defaults={
            "description": (
                "The ability to Warp Reality. Make the impossible become possible "
                "but can't warp anything containing the structure that holds "
                "everything together (Which are many creatures.)"
            ),
            "bonus": "",
            "race": elf_race,
        },
    )

    # Створення гравців (без змін)
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
