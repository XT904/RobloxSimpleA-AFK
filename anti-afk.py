import time
import psutil
import keyboard

def is_roblox_running():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'RobloxPlayerBeta.exe' in proc.info['name']:
            return True
    return False

def press_space():
    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')

def anti_afk_roblox():
    while True:
        if is_roblox_running():
            press_space()
        time.sleep(30)

if __name__ == "__main__":
    anti_afk_roblox()
