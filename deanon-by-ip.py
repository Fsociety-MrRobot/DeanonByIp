from colorama import Fore, Back, Style
import requests
import time
import sys

def get_info(ip):
	global data, r

	r = requests.get(url=f'http://ip-api.com/json/{ip}').json()
	data = {
	'[IP]': r.get('query'),
	'[Int prov]': r.get('isp'),
	'[Org]': r.get('org'),
	'[Country]': r.get('country'),
	'[Region Name]': r.get('regionName'),
	'[City]': r.get('city'),
	'[ZIP]': r.get('zip'),
	'[Lat]': r.get('lat'),
	'[Lon]': r.get('lon'),	
	}


def print_info():
	global data

	for k, v in data.items():
		print(Fore.MAGENTA + f'{k}: {v}')


def collecting_data(arg):

	for i in range(10):
		sys.stdout.write(Back.LIGHTMAGENTA_EX + Fore.BLACK + '\rCollecting data |')
		time.sleep(0.2)
		sys.stdout.write(Back.LIGHTMAGENTA_EX + Fore.BLACK + '\rCollecting data /')
		time.sleep(0.2)
		sys.stdout.write(Back.LIGHTMAGENTA_EX + Fore.BLACK + '\rCollecting data -')
		time.sleep(0.2)
		sys.stdout.write(Back.LIGHTMAGENTA_EX + Fore.BLACK + '\rCollecting data \\')
		time.sleep(0.2)
		
	print(Style.RESET_ALL + '')

	get_info(ip = arg)	
	print(Style.RESET_ALL + '')
	print(Back.LIGHTGREEN_EX + Fore.BLACK + f'[+] Data collected successfully!')
	print(Style.RESET_ALL + '')
	print_info()


def check_network_conection(ip_addr):

	print(Style.RESET_ALL + '')

	r = requests.get(url=f'http://ip-api.com/json/{ip_addr}').json()
	stat = r.get('status')

	for i in range(5):
		sys.stdout.write(Back.LIGHTCYAN_EX + Fore.BLACK + '\rSetting up the connection |')
		time.sleep(0.2)
		sys.stdout.write(Back.LIGHTCYAN_EX + Fore.BLACK + '\rSetting up the connection /')
		time.sleep(0.2)
		sys.stdout.write(Back.LIGHTCYAN_EX + Fore.BLACK + '\rSetting up the connection -')
		time.sleep(0.2)
		sys.stdout.write(Back.LIGHTCYAN_EX + Fore.BLACK + '\rSetting up the connection \\')
		time.sleep(0.2)

	print(Style.RESET_ALL + '')	
		
	if stat == 'success':
		print(Style.RESET_ALL + '')
		sys.stdout.write(Back.LIGHTGREEN_EX + Fore.BLACK + f'\rStatus: {stat}.')
		print(Style.RESET_ALL + '')
		print(Back.LIGHTGREEN_EX + Fore.BLACK + f'[+] Connection {stat}!')
		print(Style.RESET_ALL + '')
		collecting_data(arg = ip_addr)


	else:
		print(Style.RESET_ALL + '')
		sys.stdout.write(Back.LIGHTRED_EX + Fore.BLACK + f'\rStatus: {stat}.')
		print(Style.RESET_ALL + '')
		print(Back.LIGHTRED_EX + Fore.BLACK + f'[-] Connection {stat}! Check your network connection.')
		print(Style.RESET_ALL + '                                                                                                                                                                      ')
		sys.exit()


def start():
	ip_addr_in = input("\nEnter IP-Address you want to scan: ")
	check_network_conection(ip_addr = ip_addr_in) 

def main():
	start()

if __name__ == '__main__':
	main()
