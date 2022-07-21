#!/usr/bin/env python3
import logging
from typing import List

import discord


def bot(token: str, debug: bool = False) -> None:
    logging_handlers: List[logging.Handler] = []
    try:
        from rich.logging import RichHandler
    except ImportError:
        logging_handlers.append(logging.StreamHandler())
    else:
        logging_handlers.append(RichHandler(rich_tracebacks=True))

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=logging_handlers,
    )

    bot = discord.Bot()

    @bot.slash_command()
    async def hello(ctx, name: str = None):
        name = name or ctx.author.name
        await ctx.respond(f"Hello {name}!")

    @bot.user_command(name="Say Hello")
    async def hi(ctx, user):
        await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

    bot.run(token)


def main() -> None:
    import os

    bot(os.environ["BOT_TOKEN"])


if __name__ == "__main__":
    main()
