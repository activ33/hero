from pyrogram import Client


hero = Client(
	"hero",
	api_id = 24541704,
	api_hash = "7b1b63a5c5a2e53233a0e78727c068d3",
	bot_token = "6591055925:AAH4G-nS1DwVXSrvin-bbYrCDlNzxdNWOVA",
	plugins=dict(root="hero"),
)


print("I'm Alive.")
hero.run()
