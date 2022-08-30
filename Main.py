import discord

class MyClient(discord.Client):

    async def on_ready(self):

        print(f'Logged on as {self.user}!')

    async def on_message(self, message):

        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()

intents.message_content = True

client = MyClient(intents=intents)

client.run('OTc4NDYyNDE1MzE2NDgwMDgw.GFzv__.8Gi2fTS6XWo2Tl253MpF3MRnd1zMpGyAogRCFY')

