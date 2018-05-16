import requests, time, discord, asyncio, sys, os, pyautogui

CLIENT_ID="446146247741538304"
myid="<@434753259958173697>"

TOKEN = 'NDQ2MTQ2MjQ3NzQxNTM4MzA0.Dd0yVw.Vp5dbvUXEU5_WqdrXTzna4lXOhs'

client = discord.Client()

def semis():
	url = "https://www.usabo-trc.org/src/exam-scores"
	html = requests.get(url)
	htm = html.text
	if "<h3>Semi" in htm:
		return True
	else: return False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def semis():
    await client.wait_until_ready()
    channel = discord.Object(id='446146122528849943')
    while not client.is_closed:
        if semis():
            msg = '%s USABO Semifinals scores are' % myid
            await client.send_message(channel, msg)
            return 0
        await asyncio.sleep(120)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

loop=asyncio.get_event_loop()
task = asyncio.Task(semis())
client.run(TOKEN)