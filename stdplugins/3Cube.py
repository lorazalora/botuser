"""Emoji
Available Commands:
.LZ"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 31)

    input_str = event.pattern_match.group(1)

    if input_str == "LZ":

        await event.edit(input_str)

        animation_chars = [

            "👑LZ👑👑👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "◼️👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "◼️◼️👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "◼️◼️◼️️👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "◼️◼️◼️◼️👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "‎◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑👑LZ👑",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑LZ👑👑LZ👑👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑LZ👑👑LZ👑◼️◼️\n◼️👑LZ👑👑LZ👑👑LZ👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑LZ👑👑LZ👑◼️◼️\n◼️👑LZ👑👑LZ👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑LZ👑👑LZ👑◼️◼️\n◼️👑LZ👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑LZ👑👑LZ👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑LZ👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            
            "👑 LZ 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
