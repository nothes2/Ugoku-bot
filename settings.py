import discord
import json
from const import Constants
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


async def change_settings(
    guild_id: int,
    setting: str,
    value,
    path: str = Constants.SETTINGS_PATH
) -> None:
    with open(path, 'r') as json_file:
        settings = json.load(json_file)

    # Change value
    settings[setting][str(guild_id)] = value

    # Write new data
    with open(path, 'w') as json_file:
        json.dump(settings, json_file)


def get_setting(
    guild_id: int | str,
    setting: int | str,
    default: int | str,
    path: str = Constants.SETTINGS_PATH,
) -> str | int:
    guild_id = str(guild_id)
    with open(path, 'r') as json_file:
        settings = json.load(json_file)

    try:
        value = settings[setting][guild_id]
        return value

    except Exception as e:
        logging.info(f'Default setting used: {e}')
        print(e)
        settings[setting][guild_id] = default
        with open(path, 'w') as json_file:
            json.dump(settings, json_file)
        return default
