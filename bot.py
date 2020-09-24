import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')

client.run('NzU4MTM2MDE4NzkxNTYzMzA0.X2qjMA.G_aptN89UXH_UoCozr237TyUh8Y')