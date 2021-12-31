import subprocess
from pystray import Icon, Menu, MenuItem
from PIL import Image

def create_image():
    image = Image.open('icon.png')

    return image

def get_menu():
    menuItems = []
    menuItems.append(MenuItem('PulseEffects', launch_pulseeffects))
    menuItems.append(Menu.SEPARATOR)
    result = subprocess.run([ 'pulseeffects', '-p'], capture_output=True)
    presets = str(result.stderr).partition('\n')[0].replace("b'Output Presets: ", '').split(',')
    presets.pop()
    for i in presets:
        menuItems.append(MenuItem(i, set_preset))

    return menuItems

def launch_pulseeffects():
    subprocess.run([ 'pulseeffects', '--display', '0' ], capture_output=True)

def set_preset(icon, item):
    subprocess.run([ 'pulseeffects', '-l', item.text ])

if __name__ == "__main__":
    menuItems = get_menu()
    Icon('test', create_image(), menu=Menu(*menuItems)).run()
