# GNuker V1 Pro

🔵 **Self Token Discord Nuker Tool**
Advanced Discord Nuking tool using **self-tokens**, built for speed, reliability, and full control over multiple guilds.

---

## ✨ Features

| Feature                       | Description                                                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------- |
| 🚀 Multi Guild Support        | Attack multiple servers at once using multiple Guild IDs.                                |
| 🌐 Proxy Support              | Use proxies to protect your IP (auto-loaded from `proxies.txt`).                         |
| 🔁 Rate Limit Handling        | Automatically handles Discord 429 errors (rate limits) and waits intelligently.          |
| 🛡️ Admin Permissions Checker | Checks if the self-account has Admin permissions before executing actions.               |
| 🗑️ Mass Channel Deletion     | Deletes all channels (text and voice) quickly using threading.                           |
| 🛠️ Mass Channel Creation     | Creates a large number of new channels fast.                                             |
| 📢 Mass Spam in Channels      | Spams all channels with a predefined GhostByte team message.                             |
| 👞 Filtered Mass Kick         | Kick specific users by ID list or kick all members.                                      |
| 🔨 Filtered Mass Ban          | Ban specific users by ID list or ban all members.                                        |
| ✉️ Mass Direct Messaging (DM) | Send mass DM messages to all server members.                                             |
| 📂 Easy Config Files          | Manage settings easily through external files (`proxies.txt`, `members.txt`).            |
| 🖥️ Clean CLI Interface       | Simple, clean command-line interface without complications.                              |
| 🛠️ Highly Customizable       | Designed to be easily extended with more features (Auto Rotation, Webhook Nuking, etc.). |

---

## 📂 Important Files

- `proxies.txt` — List of proxies (one per line).
- `members.txt` — List of user IDs to target for kicks or bans.
- `tokens.txt` *(optional)* — For future support of multiple token rotations.

---

## 📥 Quick Usage

```bash
pip install requests
python gnuker.py
```

- Enter your self-token (NOT bot token).
- Enter target Guild IDs (comma separated).
- Choose your desired action from the menu.

---

## ⚠️ Disclaimer

> This tool is for **educational and testing purposes only**.
> Misuse can lead to permanent account suspension by Discord.
> The developer is **not responsible** for any misuse of this tool.

---

# 📸 Screenshots

![{82ED1176-0239-4FA3-A5A5-118AF7436BE0}](https://github.com/user-attachments/assets/41550da0-82ea-4c94-98ad-fea86dc74e69)

![{0BF0639F-E7B8-44A2-9F59-AE2E57D1000B}](https://github.com/user-attachments/assets/c4033f07-2eea-4c22-92ae-a344e0a5fe00)



---

## 🧠 Notes

- Tested on Python 3.10+
- Highly optimized for speed and mass operations.
- Thread-safe and resistant against basic API rate limiting.

