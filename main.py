import discord
import os.path
import asyncio
from PIL import Image

_list = {'Arevaci': {'Noble Fighters': 0, 'Baleric Slingers': 0, 'Celtiberian Cavalry': 0, 'Painted Warriors': 0},
         'Arverni': {'Chosen Swordsmen': 682, 'Naked Warriors': 437, 'Levy Freemen': 244, 'Oathsworn': 1079}}

client = discord.Client()
TOKEN = 'NzczMDAyMDQ3NzkyMjE4MTMy.X6C4QQ.9ggmuIXQJqgwn-ey1mw--tW7Geg'


def resize_image(file_name, size, all=None):
    image = Image.open(os.path.join('images/units', file_name + str('.png')))
    resized_image = image.resize(size)
    resized_image.save(os.path.join('images/units', file_name + str('.png')))

    return resized_image


@client.event
async def on_ready():
    print('Mansur - we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!unit'):
        _argv = (message.content.split('-'))
        _argv.pop(0)
        _argv = [x.strip(' ') for x in _argv]

        if not _argv:
            await message.channel.send("invalid command")
            return

        found = False
        for i, j in _list.items():
            if i in _argv:
                await message.channel.send(i + '<faction emote goes here>')
                for k in j:
                    image = 'images/units/' + k + str('.png')
                    resize_image(k, (52, 120))
                    msg = '```css\nKILLS: ' + str(_list[i][k]) + '```'
                    await asyncio.wait([message.channel.send(msg, file=discord.File(image))])
                    found = True
        if found is False:
            await message.channel.send('invalid argument')
            return


client.run(TOKEN)
