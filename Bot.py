import discord
import giphypop
from giphypop import translate

g = giphypop.Giphy()
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    user = await client.fetch_user('User ID')
    img = translate('love')
    await user.send(img.url)
    await user.send("Love you :heart:")


client.run("Token")