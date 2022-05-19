import requests as req
import datetime as dt
import json
import time
import os


TOKEN = os.environ['TOKEN'] 

def timeout(**kwargs):
	kwargs = {"userid": "0", "seconds" : 300, "guildid": "0", **kwargs} 
	API_URL = f'https://discord.com/api/v6/guilds/{kwargs["guildid"]}/members/{kwargs["userid"]}'
	timestamp = (dt.datetime.utcnow() + dt.timedelta(seconds=kwargs["seconds"])).isoformat()
	body = {"communication_disabled_until": timestamp}
	patch_content = json.dumps(body)
	header = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}
	try:
		patch_request = req.patch(API_URL, data=patch_content, headers=header)
		patch_request.raise_for_status()
		print(patch_request) # debug
	except req.exceptions.HTTPError as e:
		print(e)
		time.sleep(5) # arbitrary timeout
		print(patch_request) # debug


def main():
	pass


if __name__ == "__main__":
	main()