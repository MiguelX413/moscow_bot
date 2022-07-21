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

    @bot.slash_command(description="Invite link for this bot")
    async def invite(ctx: discord.ApplicationContext, useless: str = "") -> None:
        await ctx.respond(
            f"https://discord.com/api/oauth2/authorize?client_id={bot.application_id}&permissions=2147551232&scope=applications.commands%20bot"
        )

    bot.run(token)


def main() -> None:
    import os

    bot(os.environ["BOT_TOKEN"])


if __name__ == "__main__":
    main()
