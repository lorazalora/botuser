"""Use cmd .LZYT , .armor , .love , .hero and check what happens"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "LZYT":

        await event.edit(input_str)

        animation_chars = [

            "😂",

            "🙃",

            "😄",

            "😂",
            
            "🙃",
            
            "😄",
            
            "😂", 
           
            "🙃",
    "😄", 
        "🤭", 
            "😌", 
                "https://t.me.lorazalora", 
                    "🤭",
                        "😐", 
                            "😏", 
                                "🤨", 
                                    "🤪", 
                                        "https://t.melorazaloraza", 
                                            "😀", 
                                                "😝", 
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "armor":

        await event.edit(input_str)

        animation_chars = [

            "😭",

            "🙃",

            "😏",

            "🗿",
            
            "🚨",
            
            "🎮",
            
            "🔥",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])



"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "love":

        await event.edit(input_str)

        animation_chars = [

            "🌚",

            "🌒",

            "🌘",

            "🌗",
            
            "🌔",
            
            "🌾",
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "hero":

        await event.edit(input_str)

        animation_chars = [

            "🍄",

            "🌲",

            "🐲",

            "🐾",
            
            "🐩",
            
            "🐄",
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
