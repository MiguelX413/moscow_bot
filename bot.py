#!/usr/bin/env python3
import discord


def bot(token: str) -> None:

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
