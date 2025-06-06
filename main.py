import json
from db.models import Race, Skill, Guild, Player


def main():
    with open('players.json', 'r') as file:
        data = json.load(file)

    for player_data in data:
        race_name = player_data['race']['name']
        race_description = player_data['race'].get('description', '')

        race, created = Race.objects.get_or_create(name=race_name, defaults={'description': race_description})

        for skill_data in player_data['race'].get('skills', []):
            Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={'bonus': skill_data['bonus'], 'race': race}
            )

        guild_data = player_data.get('guild')
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data['name'],
                defaults={'description': guild_data.get('description')}
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_data['nickname'],
            defaults={
                'email': player_data['email'],
                'bio': player_data['bio'],
                'race': race,
                'guild': guild,
            }
        )

    return Player.objects.all()
