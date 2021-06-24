import discord
import os
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, typing = False, presences = False, members = True)
nuk = commands.Bot(
  command_prefix='.',
  case_insensitive=True,
  intents = intents
  )
print('Logging in...')


@nuk.event
async def on_ready():
  print('Logged in as {0.user}'.format(nuk))

@nuk.command()
async def mn(ctx, *, wrd):
  await ctx.send(wrd)


@nuk.event
async def on_message(message):
  if message.author == nuk.user:
    return

  if message.content.startswith('Hi'):
    await message.channel.send('Hello {0.author}'.format(message))

nuk.run(os.environ['TOKEN'])