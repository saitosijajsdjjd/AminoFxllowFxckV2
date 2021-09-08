import AminoLab
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_SKY_BLUE_3B + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("Aminofxllowfxckv2", font="stampatello"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
ndc_Id = clients.ndc_Id[int(input("Select the community >> "))-1];
while True:
	with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
		users = client.get_online_members(ndc_Id=ndc_Id)
		for user_Id, nickname in zip(users.user_Id, users.nickname):
			try:
				_ = [executor.submit(client.follow_user, ndc_Id, user_Id)]
				print(f"Followed {nickname}")
			except Exception as e:	print(e)
