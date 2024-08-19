import json
from subprocess import call 
import threading
from termcolor import colored
import json as jsond  # json
from keyauth import api
import shutil
import subprocess
import time  # sleep before exit
import binascii  # hex encoding
import requests  # https requests

from uuid import uuid4  # gen random guid
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
# aes + padding, sha256

import webbrowser
import platform
import subprocess
import datetime
import sys
import os
from keyauth import api
import json
import time
import hashlib
from time import sleep
from datetime import datetime
from requests_toolbelt.adapters.fingerprint import FingerprintAdapter
from termcolor import colored
w = 300
h = 300

import cv2
import numpy as np
import mss
from inference_sdk import InferenceHTTPClient
import onnxruntime as ort
from ultralytics import YOLO
import yaml
import torch
from PIL import Image

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Function to check CUDA availability
def check_cuda_support():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

# Implementing a Updated model

# Initialize the Inference Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="wwL7uZeqDOFEwPxn9fdm"
)

result = CLIENT.infer(r"bus.jpg", model_id="enemy-finder-vqteo/2")
print(result)

# Implementing Yolvo_v8
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format

def load_onnx_model():
    # Load the ONNX model
    onnx_model_path = "yolov8n.onnx"

    # List of available execution providers
    providers = ['CUDAExecutionProvider', 'CPUExecutionProvider'] if ort.get_device() == 'GPU' else ['CPUExecutionProvider']

    # Add ROCm Execution Provider if available
    if 'ROCmExecutionProvider' in ort.get_available_providers():
        providers.append('ROCmExecutionProvider')

    # Initialize the ONNX session
    ort_session = ort.InferenceSession(onnx_model_path, providers=providers)

# Define the input shape
input_shape = (640, 640)

# Function to preprocess input image
def preprocess(image):
    image = cv2.resize(image, input_shape)
    image = image.transpose(2, 0, 1).astype(np.float32) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to run inference
def run_inference(image):
    inputs = preprocess(image)
    ort_inputs = {ort_session.get_inputs()[0].name: inputs}
    ort_outs = ort_session.run(None, ort_inputs)
    return ort_outs



def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "Premium",
    ownerid = "yOIRY2jtoU",
    secret = "8f05ae58e37d911f123a3ed5dabc086b9ac7debed14e6534eaa32338706103e8",
    version = "1.0",
    hash_to_check = getchecksum()
)
path = "lib/config"

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

key = input('Enter your license: ')
keyauthapp.license(key)

# New ASCII Art with additional lines
POKOR_ART = """
██████╗░██████╗░███████╗███╗░░░███╗██╗██╗░░░██╗███╗░░░███╗
██╔══██╗██╔══██╗██╔════╝████╗░████║██║██║░░░██║████╗░████║
██████╔╝██████╔╝█████╗░░██╔████╔██║██║██║░░░██║██╔████╔██║
██╔═══╝░██╔══██╗██╔══╝░░██║╚██╔╝██║██║██║░░░██║██║╚██╔╝██║
██║░░░░░██║░░██║███████╗██║░╚═╝░██║██║╚██████╔╝██║░╚═╝░██║
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝

Discord.gg/PokorEXE
www.PokorEXE.com
"""

def print_art():
    clear_console()
    print(colored(POKOR_ART, 'green'))
    print(colored("Please make your x and y sens the same", 'green'))

def prompt(str):
    valid_input = False
    while not valid_input:
        print_art()
        try:
            number = float(input(str))
            valid_input = True
        except ValueError:
            print(colored("[!] Invalid Input. Make sure to enter only the number (e.g. 6.9)", 'green'))
    return number

print_art()
xy_sens = prompt("Enter your X and Y sens from Fortnite: ")
targeting_sens = prompt("Enter your targeting sensitivity from Fortnite: ")

print("POKOR Make your targeting sens and scoped sense the same")
sensitivity_settings = {"xy_sens": xy_sens, "targeting_sens": targeting_sens, "xy_scale": 10/xy_sens, "targeting_scale": 1000/(targeting_sens * xy_sens)}

with open('lib/config/config.json', 'w') as outfile:
    json.dump(sensitivity_settings, outfile)
    print_art()
    print(colored("POKOR Sensitivity configuration complete", 'green'))


import dearpygui.dearpygui as dpg
import json
import os
import sys
import threading
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
from termcolor import colored
import subprocess
import keyboard
from subprocess import call 
import psutil
from lib.events import Aimbot
import time
import random
import threading
import cv2

import customtkinter as ctk
import os
import subprocess
import webbrowser
from tkinter import PhotoImage

crosshair_enabled = False
crosshair_size = 20
crosshair_color = (255, 0, 0)  # Default color: Red

def draw_crosshair(img, center):
    if crosshair_enabled:
        x, y = center
        cv2.line(img, (x - crosshair_size, y), (x + crosshair_size, y), crosshair_color, 2)
        cv2.line(img, (x, y - crosshair_size), (x, y + crosshair_size), crosshair_color, 2)

def update_crosshair_enable():
    global crosshair_enabled
    crosshair_enabled = checkbox_crosshair.get()

def update_crosshair_size(val):
    global crosshair_size
    crosshair_size = int(val)

def update_crosshair_color(color):
    global crosshair_color
    crosshair_color = color

def adjust_for_resolution(img, target_resolution):
    current_resolution = img.shape[:2]
    scale_x = target_resolution[0] / current_resolution[0]
    scale_y = target_resolution[1] / current_resolution[1]
    return cv2.resize(img, target_resolution, interpolation=cv2.INTER_LINEAR)

# Configuration
target_switch_delay = 0.5  # delay in seconds
targets = ["Target1", "Target2", "Target3", "Target4"]  # Example targets
always_on = True  # Option to run the aimbot continuously
auto_shoot = True
triggerbot_delay = 0.3  # delay in seconds

# Function to simulate acquiring a new target
def acquire_target():
    return random.randint(0, len(targets) - 1)


# Initialize global variables for delays
auto_shoot = False
triggerbot_enabled = False
always_on = False

target_switch_delay = 0.5  # Default values
triggerbot_delay = 0.3

# Example targets list
targets = ["Target1", "Target2", "Target3", "Target4"]

# Function to switch target
def switch_target(current_target_index):
    next_target_index = (current_target_index + 1) % len(targets)
    next_target = targets[next_target_index]
    print(f"Switched from {targets[current_target_index]} to {next_target}")
    return next_target_index

# Basic aimbot function for demonstration
def aimbot_function():
    print("Aimbot function running...")
    current_target_index = acquire_target()
    print(f"Target acquired: {targets[current_target_index]}")
    time.sleep(target_switch_delay)  # Simulate some processing time
    return current_target_index

# Function to simulate shooting
def shoot_function():
    print("Bang! Triggerbot fired.")

# Triggerbot function
def triggerbot():
    if auto_shoot:
        while True:
            shoot_function()
            time.sleep(triggerbot_delay)

def main():
    try:
        # Start triggerbot thread if auto_shoot is enabled
        if auto_shoot:
            triggerbot_thread = threading.Thread(target=triggerbot)
            triggerbot_thread.daemon = True
            triggerbot_thread.start()
        
        if always_on:
            iteration_count = 0  # Adding a counter to avoid infinite loop during testing
            max_iterations = 10  # Run the loop a fixed number of times for testing
            while iteration_count < max_iterations:
                current_target_index = aimbot_function()
                iteration_count += 1
        else:
            print("Aimbot started. Acquiring initial target...")
            current_target_index = acquire_target()
            print(f"Initial target acquired: {targets[current_target_index]}")

            iteration_count = 0  # Adding a counter to avoid infinite loop during testing
            max_iterations = 10  # Run the loop a fixed number of times for testing
            while iteration_count < max_iterations:
                # Simulate switching targets
                time.sleep(target_switch_delay)
                current_target_index = switch_target(current_target_index)
                iteration_count += 1
    except Exception as e:
        print(f"An error occurred: {e}")

def toggle_auto_shoot():
    global auto_shoot
    auto_shoot = not auto_shoot
    start_aimbot()

def toggle_triggerbot():
    global triggerbot_enabled
    triggerbot_enabled = not triggerbot_enabled
    if triggerbot_enabled:
        start_aimbot()

# Callback functions to update delay values from sliders
def update_autoshoot_delay(value):
    global triggerbot_delay
    triggerbot_delay = float(value)

def update_triggerbot_delay(value):
    global triggerbot_delay
    triggerbot_delay = float(value)

def update_target_switch_delay(value):
    global target_switch_delay
    target_switch_delay = float(value)

def toggle_always_on():
    global always_on
    always_on = not always_on
    start_aimbot()


if __name__ == "__main__":
    main()



dpg.create_context()
dpg.create_viewport(title='AI Premium', width=300, height=300, decorated=True, always_on_top=False, clear_color=(255, 255, 255, 128))
def on_insert():
    print('insert was pressed')
    dpg.set_viewport_always_top(True)
    keyboard.add_hotkey('insert', on_insert)


def on_del():
    print('delete was pressed')
    dpg.set_viewport_always_top(False)
    dpg.minimize_viewport
    keyboard.add_hotkey('delete', on_del)

dpg.show_imgui_demo
dpg.set_viewport_max_height(h)
dpg.set_viewport_max_width(w)
dpg.set_viewport_min_height(h)
dpg.set_viewport_min_width(w)
def print_me(sender):
    keyboard = Controller() 
    keyboard.press(Key.f2)#press f2 to close earlier instance of the nn windows
    keyboard.release(Key.f2)
def aimkey_alt():
    global aimkey
    aimkey = "alt"
    print(aimkey)
def aimkey_shift():
    global aimkey
    aimkey = "shift"
    print(aimkey)
def aimkey_leftMouse():
    global aimkey
    aimkey = "leftMouse"
    print(aimkey)
def aimkey_rightMouse():
    global aimkey
    aimkey = "rightMouse"
    print(aimkey)
def aimkey_ctrl():
    global aimkey
    aimkey = "ctrl"
    print(aimkey)
def aimkey_mouse5():
    global aimkey
    aimkey = "mouse5"
    print(aimkey)
def strenght(Sender):
    global aim_strenght
    print(dpg.get_value(Sender))
    aim_strenght = dpg.get_value(Sender)
def detection_threshhold(Sender):
    global dt_value
    print(dpg.get_value(Sender))
    dt_value = (dpg.get_value(Sender))
def fovcolor(Sender):
    print(dpg.get_value(Sender))
def aimbot_toggle(Sender):
    Aimbot.aimbot_status = colored("DISABLED", 'red')


def getAimkeyString(Sender):
    global aimkey
    dpg.get_value(Sender)
    print(dpg.get_value(Sender))
    confAimkey = dpg.get_value(Sender)
    print("Your Aimkey is",confAimkey)
    if confAimkey == "LEFT ALT":
        print("Your Aimkey is LEFT  ALT")
        aimkey = "leftAlt"
    elif confAimkey == "LEFT SHIFT":
        print("Your Aimkey is really LEFT SHIFT")
        aimkey = "leftShift"
    elif confAimkey == "RIGHT CLICK":
        print("Your Aimkey is really RIGHT MOUSE")
        aimkey = "rightMouse"
    elif confAimkey == "LEFT CLICK":
        print("Your Aimkey is really LEFT MOUSE")
        aimkey = "leftMouse"
    elif confAimkey == "MOUSE 4":
        print("Your Aimkey is really MOUSE4")
        aimkey = "mouse4"
    elif confAimkey == "MOUSE 5":
        print("Your Aimkey is really MOUSE5")
        aimkey = "mouse5"
    elif confAimkey == "CNTRL":
        print("Your Aimkey is really CNTRL")
        aimkey = "cntrl"
    elif confAimkey == "`":
        print("Your Aimkey is really `")
        aimkey = "`"
    elif confAimkey == "1":
        print("Your Aimkey is really 1")
        aimkey = "1"
    elif confAimkey == "2":
        print("Your Aimkey is really 2")
        aimkey = "2"
    elif confAimkey == "3":
        print("Your Aimkey is really 3")
        aimkey = "3"
    elif confAimkey == "4":
        print("Your Aimkey is really 4")
        aimkey = "4"
    elif confAimkey == "5":
        print("Your Aimkey is really 5")
        aimkey = "5"
    elif confAimkey == "6":
        print("Your Aimkey is really 6")
        aimkey = "6"
    elif confAimkey == "7":
        print("Your Aimkey is really 7")
        aimkey = "7"
    elif confAimkey == "8":
        print("Your Aimkey is really 8")
        aimkey = "8"
    elif confAimkey == "9":
        print("Your Aimkey is really 9")
        aimkey = "9"
    elif confAimkey == "0":
        print("Your Aimkey is really 0")
        aimkey = "0"
    elif confAimkey == "-":
        print("Your Aimkey is really -")
        aimkey = "-"
    elif confAimkey == "=":
        print("Your Aimkey is really =")
        aimkey = "="
    elif confAimkey == "Q":
        print("Your Aimkey is really Q")
        aimkey = "Q"
    elif confAimkey == "W":
        print("Your Aimkey is really W")
        aimkey = "W"
    elif confAimkey == "E":
        print("Your Aimkey is really E")
        aimkey = "E"
    elif confAimkey == "R":
        print("Your Aimkey is really R")
        aimkey = "R"
    elif confAimkey == "T":
        print("Your Aimkey is really T")
        aimkey = "T"
    elif confAimkey == "Y":
        print("Your Aimkey is really Y")
        aimkey = "Y"
    elif confAimkey == "U":
        print("Your Aimkey is really U")
        aimkey = "U"
    elif confAimkey == "I":
        print("Your Aimkey is really I")
        aimkey = "I"
    elif confAimkey == "O":
        print("Your Aimkey is really O")
        aimkey = "O"
    elif confAimkey == "P":
        print("Your Aimkey is really P")
        aimkey = "P"
    elif confAimkey == "[":
        print("Your Aimkey is really [")
        aimkey = "["
    elif confAimkey == "]":
        print("Your Aimkey is really ]")
        aimkey = "]"
    elif confAimkey == "A":
        print("Your Aimkey is really A")
        aimkey = "A"
    elif confAimkey == "S":
        print("Your Aimkey is really S")
        aimkey = "S"
    elif confAimkey == "D":
        print("Your Aimkey is really D")
        aimkey = "D"
    elif confAimkey == "F":
        print("Your Aimkey is really F")
        aimkey = "F"
    elif confAimkey == "G":
        print("Your Aimkey is really G")
        aimkey = "G"
    elif confAimkey == "H":
        print("Your Aimkey is really H")
        aimkey = "H"
    elif confAimkey == "J":
        print("Your Aimkey is really J")
        aimkey = "J"
    elif confAimkey == "K":
        print("Your Aimkey is really K")
        aimkey = "K"
    elif confAimkey == "L":
        print("Your Aimkey is really L")
        aimkey = "L"
    elif confAimkey == ";":
        print("Your Aimkey is really ;")
        aimkey = ";"
    elif confAimkey == "@":
        print("Your Aimkey is really @")
        aimkey = "@"
    elif confAimkey == "#":
        print("Your Aimkey is really #")
        aimkey = "#"
    elif confAimkey == "Z":
        print("Your Aimkey is really Z")
        aimkey = "Z"
    elif confAimkey == "'":
        print("Your Aimkey is really '")
        aimkey = "'"
    elif confAimkey == "X":
        print("Your Aimkey is really X")
        aimkey = "X"
    elif confAimkey == "C":
        print("Your Aimkey is really C")
        aimkey = "C"
    elif confAimkey == "V":
        print("Your Aimkey is really V")
        aimkey = "V"
    elif confAimkey == "B":
        print("Your Aimkey is really B")
        aimkey = "B"
    elif confAimkey == "N":
        print("Your Aimkey is really N")
        aimkey = "N"
    elif confAimkey == "M":
        print("Your Aimkey is really M")
        aimkey = "M"
    elif confAimkey == ",":
        print("Your Aimkey is really ,")
        aimkey = ","
    elif confAimkey == ".":
        print("Your Aimkey is really .")
        aimkey = "."
    elif confAimkey == "/":
        print("Your Aimkey is really /")
        aimkey = "/"
    elif confAimkey == "CAPS LOCK":
        print("Your Aimkey is really CAPS LOCK")
        aimkey = "capsLock"
    elif confAimkey == "\\":
        print("Your Aimkey is really \\")
        aimkey = "\\ "

def thread_second():
    call(["python", "extension.py"])
    processThread = threading.Thread(target=thread_second)
    processThread.start()

def close():
    stop_aimbot()
    root.destroy()
        
def setsens():
    os.system('python setSens.py')

def fov_state(Sender): #returns 1 or 0 under fov_dis depending on the state of the checkbox
    global fov_dis
    print(dpg.get_value(Sender))
    if dpg.get_value(Sender) == True:
        print("FOV circle is activated")
        fov_dis = 1
    elif dpg.get_value(Sender) == False:
        print("FOV circle is deactivated")
        fov_dis = 0
def save():
    configuration = {"aimkey": aimkey, "strenght": aim_strenght,"confidence":dt_value}
    with open('lib/config/guiconf.json', 'w') as outfile:
     json.dump(configuration, outfile)

# Define callback functions for each widget
def toggle_target_lock_indicator():
    print("Target Lock Indicator toggled")

# Global variables to manage threads and flags
aimbot_thread = None
running = True

def stop_aimbot():
    global running
    running = False
    if aimbot_thread is not None and aimbot_thread.is_alive():
        aimbot_thread.join()

def start():
    keyboard = Controller() 
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    import json
    import os
    import sys
    import threading
    import time
    from pynput import keyboard
    from termcolor import colored
    import customtkinter as ctk
    import subprocess
    
    def on_release(key):
        try:
            if key == keyboard.Key.f1:
                Aimbot.update_status_aimbot()
            if key == keyboard.Key.f2:
                Aimbot.clean_up()
        except NameError:
            pass   
    
    def lunar():
        global lunar
        lunar = Aimbot(collect_data = "collect_data" in sys.argv)
        lunar.start()
    
    def setup():
        path = "lib/config"
        if not os.path.exists(path):
            os.makedirs(path)
    
        print("[POKOR] In-game X and Y sensitivity have to be the same!")
        def prompt(str):
            valid_input = False
            while not valid_input:
                try:
                    number = float(input(str))
                    valid_input = True
                except ValueError:
                    print("[!] Invalid Input. Make sure to enter only the number (e.g. 6.9)")
            return number
    
        xy_sens = prompt("X-Axis and Y Sensitivity (from in-game settings): ")
        targeting_sens = prompt("Targeting Sensitivity (from in-game settings): ")
    
        print("[POKOR] Your in-game targeting sensitivity must be the same as your scoping sensitivity")
        sensitivity_settings = {"xy_sens": xy_sens, "targeting_sens": targeting_sens, "xy_scale": 10/xy_sens, "targeting_scale": 1000/(targeting_sens * xy_sens)}
    
        with open('lib/config/config.json', 'w') as outfile:
            json.dump(sensitivity_settings, outfile)
        print("[POKOR] Sensitivity configuration complete")
    
    if __name__ == "__main__":
        os.system('cls' if os.name == 'nt' else 'clear')
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
        path_exists = os.path.exists("lib/config/config.json")
        if not path_exists or ("setup" in sys.argv):
            if not path_exists:
                print("[POKOR] Ingame sensitivity hasnt been configurated yet...")
            setup()
        path_exists = os.path.exists("lib/data")
        if "collect_data" in sys.argv and not path_exists:
            os.makedirs("lib/data")
        from lib.events import Aimbot
        listener = keyboard.Listener(on_release=on_release)
        listener.start()
        lunar()

# List of weapons
weapon_list = [
    "Heavy Assault Rifle", "Reaper Sniper Rifle", "Shotgun", "Burst Assault Rifle",
    "Pistol", "Drum Gun", "Infantry Rifle", "Striker Pump Shotgun", "Assault Weapons",
    "Stinger SMG", "Submachine Guns", "Thunder Burst SMG", "Deadpool's Dual Hand Cannons",
    "Rocket launcher", "Thermal Scoped Assault Rifle", "Tactical Shotgun",
    "Bolt-Action Sniper Rifle", "Bows", "Charge Shotgun", "Dual pistols",
    "Hammer Pump Shotgun", "Nemesis AR", "Suppressed Submachine Gun", "Explosives"
]

# Function to update the display of the held weapon
def update_held_weapon_display():
    if checkbox_held_weapon.get():
        selected_weapon = weapon_listbox.get(weapon_listbox.curselection())
        weapon_label.configure(text=f"Held Weapon: {selected_weapon}")
        print(f"Held Weapon display enabled: {selected_weapon}")
    else:
        weapon_label.configure(text="Held Weapon: [Hidden]")
        print("Held Weapon display disabled")

# Function to handle weapon selection
def on_weapon_select(event):
    update_held_weapon_display()
        

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Function to open the hyperlink
def open_link(event):
    webbrowser.open_new("https://pokordot.com/")

# Function to change text color on hover
def on_enter(event):
    link_label.configure(text_color="red")

# Function to reset text color when not hovering
def on_leave(event):
    link_label.configure(text_color="White")

# Define the global variables
aim_strenght = 0.5
dt_value = 0.6

def set_enemy_distance(value):
    label_enemy_distance.configure(text=f"Enemy Distance: {int(value)}")

# Define the functions for the sliders
def strength(value):
    global aim_strenght
    print(value)
    aim_strenght = value

def detection_threshhold(value):
    global dt_value
    print(value)
    dt_value = value

def small():
    os.startfile(path + r"\square\small.exe")
    subprocess.call("TASKKILL /F /IM medium.exe", shell=True)
    subprocess.call("TASKKILL /F /IM large.exe", shell=True)

def medium():
    os.startfile(path + r"\square\medium.exe")
    subprocess.call("TASKKILL /F /IM large.exe", shell=True)
    subprocess.call("TASKKILL /F /IM small.exe", shell=True)

def big():
    os.startfile(path + r"\square\large.exe")
    subprocess.call("TASKKILL /F /IM medium.exe", shell=True)
    subprocess.call("TASKKILL /F /IM small.exe", shell=True)

def closeFov():
    subprocess.call("TASKKILL /F /IM medium.exe", shell=True)
    subprocess.call("TASKKILL /F /IM small.exe", shell=True)
    subprocess.call("TASKKILL /F /IM large.exe", shell=True)

def show_frame(frame):
    frame_general.pack_forget()
    frame_advanced.pack_forget()
    frame_aim.pack_forget()
    frame_crosshair.pack_forget()
    frame.pack(fill="both", expand=True, padx=10, pady=10)


# Create the main window
root = ctk.CTk()
root.geometry("600x400")
root.title("Driverless")

# Create a frame for the bottom section
frame_bottom = ctk.CTkFrame(master=root)
frame_bottom.pack(side="bottom", fill="x", padx=5, pady=5)

# Create a label and bind it to open the link
link_label = ctk.CTkLabel(frame_bottom, text="Pokordot.com - Driverless", text_color="White", cursor="hand2", font=("Helvetica", 12, "normal"))
link_label.pack(pady=2)
link_label.bind("<Button-1>", open_link)
link_label.bind("<Enter>", on_enter)
link_label.bind("<Leave>", on_leave)

path = os.getcwd()

# Create a frame for the left side buttons
frame_left = ctk.CTkFrame(master=root, width=300)
frame_left.pack(side="left", fill="y", padx=20, pady=20)

# Load and add the logo above the buttons
logo_image = ctk.CTkImage(Image.open("logo.jpg"), size=(150, 150))  # Adjust the size as needed
label_logo = ctk.CTkLabel(master=frame_left, image=logo_image, text="")
label_logo.pack(pady=(3, 10))  # Add some padding below the logo

# Add navigation buttons to the left frame
button_general = ctk.CTkButton(master=frame_left, text="General", command=lambda: show_frame(frame_general), fg_color="red")
button_general.pack(pady=5)

button_advanced = ctk.CTkButton(master=frame_left, text="Advanced", command=lambda: show_frame(frame_advanced), fg_color="red")
button_advanced.pack(pady=5)

button_aim = ctk.CTkButton(master=frame_left, text="Aim Settings", command=lambda: show_frame(frame_aim), fg_color="red")
button_aim.pack(pady=5)

button_crosshair = ctk.CTkButton(master=frame_left, text="Custom Crosshair", command=lambda: show_frame(frame_crosshair), fg_color="red")
button_crosshair.pack(pady=5)

# Create frames for each section
frame_general = ctk.CTkFrame(master=root)
frame_advanced = ctk.CTkFrame(master=root)
frame_aim = ctk.CTkFrame(master=root)
frame_crosshair = ctk.CTkFrame(master=root)

# General settings frame
frame_general = ctk.CTkFrame(master=root)
frame_general.pack(pady=20, padx=20, fill="both", expand=True)

# Add extra empty columns to center the content
frame_general.grid_columnconfigure(0, weight=1)  # Empty column on the left
frame_general.grid_columnconfigure(3, weight=1)  # Empty column on the right

# Add widgets to frame_general
label_general = ctk.CTkLabel(master=frame_general, text="General Settings", font=("Helvetica", 20, "bold"))
label_general.grid(row=0, column=1, columnspan=2, pady=5, padx=20, sticky="ew")

# Enable AI checkbox
enable_ai_checkbox = ctk.CTkCheckBox(master=frame_general, text="Enable AI", command=aimbot_toggle, fg_color="red")
enable_ai_checkbox.grid(row=1, column=1, padx=20, pady=3, sticky="w")

# FOV Circle Radius label
label_fov = ctk.CTkLabel(master=frame_general, text="FOV Circle Radius", font=("Helvetica", 14, "bold"))
label_fov.grid(row=2, column=1, padx=20, pady=3, sticky="w")

# Sliders for settings and detection threshold
slider_settings = ctk.CTkSlider(master=frame_general, from_=0.1, to=5.0, number_of_steps=100, command=strength, progress_color="red", button_color="red")
slider_settings.set(0.5)  # Default value
slider_settings.grid(row=3, column=1, padx=20, pady=3, sticky="ew")

slider_detection_threshhold = ctk.CTkSlider(master=frame_general, from_=0.2, to=0.8, number_of_steps=100, command=detection_threshhold, progress_color="red", button_color="red")
slider_detection_threshhold.set(0.6)  # Default value
slider_detection_threshhold.grid(row=4, column=1, padx=20, pady=3, sticky="ew")

# Checkboxes for FOV options
checkbox1 = ctk.CTkCheckBox(master=frame_general, text="Small FOV", command=small, fg_color="red")
checkbox1.grid(row=5, column=1, padx=20, pady=3, sticky="w")

checkbox2 = ctk.CTkCheckBox(master=frame_general, text="Medium FOV", command=medium, fg_color="red")
checkbox2.grid(row=6, column=1, padx=20, pady=3, sticky="w")

checkbox3 = ctk.CTkCheckBox(master=frame_general, text="Large FOV", command=big, fg_color="red")
checkbox3.grid(row=7, column=1, padx=20, pady=3, sticky="w")

checkbox4 = ctk.CTkCheckBox(master=frame_general, text="Disable Fov", command=closeFov, fg_color="red")
checkbox4.grid(row=8, column=1, padx=20, pady=3, sticky="w")

# Advanced settings frame
frame_advanced = ctk.CTkFrame(master=root)
frame_advanced.pack(pady=20, padx=20, fill="both", expand=True)

# Add extra empty columns to center the content
frame_advanced.grid_columnconfigure(0, weight=1)  # Empty column on the left
frame_advanced.grid_columnconfigure(3, weight=1)  # Empty column on the right

# Add widgets to frame_advanced
label_advanced = ctk.CTkLabel(master=frame_advanced, text="Advanced Settings", font=("Helvetica", 20, "bold"))
label_advanced.grid(row=0, column=1, columnspan=2, pady=10, padx=20, sticky="ew")

checkbox1 = ctk.CTkCheckBox(master=frame_advanced, text="Cuda Support", command=check_cuda_support, fg_color="red")
checkbox1.grid(row=1, column=1, padx=20, pady=10, sticky="w")

checkbox2 = ctk.CTkCheckBox(master=frame_advanced, text="Onnx Support", command=load_onnx_model, fg_color="red")
checkbox2.grid(row=2, column=1, padx=20, pady=10, sticky="w")

checkbox3 = ctk.CTkCheckBox(master=frame_advanced, text="Stretch resolution support", command=adjust_for_resolution, fg_color="red")
checkbox3.grid(row=3, column=1, padx=20, pady=10, sticky="w")

# Aim settings frame
frame_aim = ctk.CTkFrame(master=root)
frame_aim.pack(pady=20, padx=20, fill="both", expand=True)

# Add extra empty columns to center the content
frame_aim.grid_columnconfigure(0, weight=1)  # Empty column on the left
frame_aim.grid_columnconfigure(3, weight=1)  # Empty column on the right

# Add widgets to frame_aim
label_general = ctk.CTkLabel(master=frame_aim, text="Aim Settings", font=("Helvetica", 20, "bold"))
label_general.grid(row=0, column=1, columnspan=2, pady=5, padx=20, sticky="ew")

# Ai always on top
radiobutton1 = ctk.CTkRadioButton(master=frame_aim, text="Ai always on top", command=aimbot_toggle, fg_color="red")
radiobutton1.grid(row=1, column=1, pady=5, padx=20, sticky="w")

# AutoShoot with Delay Slider
radiobutton2 = ctk.CTkRadioButton(master=frame_aim, text="AutoShoot", command=toggle_auto_shoot, fg_color="red")
radiobutton2.grid(row=2, column=1, pady=5, padx=20, sticky="w")

autoshoot_delay_slider = ctk.CTkSlider(master=frame_aim, from_=0.0, to=2.0, number_of_steps=100,progress_color="red", button_color="red", command=update_autoshoot_delay)
autoshoot_delay_slider.grid(row=3, column=1, pady=5, padx=20, sticky="w")

# Triggerbot with Delay Slider
radiobutton3 = ctk.CTkRadioButton(master=frame_aim, text="Triggerbot", command=toggle_triggerbot, fg_color="red")
radiobutton3.grid(row=4, column=1, pady=5, padx=20, sticky="w")  

triggerbot_delay_slider = ctk.CTkSlider(master=frame_aim, from_=0.0, to=2.0, number_of_steps=100,progress_color="red", button_color="red", command=update_triggerbot_delay)
triggerbot_delay_slider.grid(row=5, column=1, pady=5, padx=20, sticky="w")

# Switch target delay with Delay Slider
radiobutton4 = ctk.CTkRadioButton(master=frame_aim, text="Switch target delay",command=switch_target, fg_color="red")
radiobutton4.grid(row=6, column=1, pady=5, padx=20, sticky="w") 

switch_target_delay_slider = ctk.CTkSlider(master=frame_aim, from_=0.0, to=2.0, number_of_steps=100,progress_color="red", button_color="red",command=update_target_switch_delay)
switch_target_delay_slider.grid(row=7, column=1, pady=5, padx=20, sticky="w")

# Always on option
radiobutton5 = ctk.CTkRadioButton(master=frame_aim, text="Always on option", command=toggle_always_on, fg_color="red")
radiobutton5.grid(row=8, column=1, pady=5, padx=20, sticky="w")

# Crosshair settings frame
frame_crosshair = ctk.CTkFrame(master=root)
frame_crosshair.pack(pady=20, padx=20, fill="both", expand=True)

# Add extra empty columns to center the content
frame_crosshair.grid_columnconfigure(0, weight=1)  # Empty column on the left
frame_crosshair.grid_columnconfigure(3, weight=1)  # Empty column on the right

# Add widgets to frame_crosshair
label_crosshair = ctk.CTkLabel(master=frame_crosshair, text="Custom Crosshair Settings", font=("Helvetica", 20, "bold"))
label_crosshair.grid(row=0, column=1, columnspan=2, pady=5, padx=20, sticky="ew")

checkbox_crosshair = ctk.CTkCheckBox(master=frame_crosshair, text="Enable Custom Crosshair", command=update_crosshair_enable, fg_color="red")
checkbox_crosshair.grid(row=1, column=1, columnspan=2, pady=5, padx=20, sticky="ew")

slider_crosshair = ctk.CTkSlider(master=frame_crosshair, from_=0, to=100, progress_color="red", button_color="red", command=update_crosshair_size)
slider_crosshair.grid(row=2, column=1, columnspan=2, pady=5, padx=20, sticky="ew")

checkbox_held_weapon = ctk.CTkCheckBox(master=frame_crosshair, text="Held Weapon", fg_color="red",command=update_held_weapon_display)
checkbox_held_weapon.grid(row=3, column=1, padx=20, pady=5, sticky="w")

# Create the dropdown menu for weapon selection
option_menu_weapon = ctk.CTkOptionMenu(master=frame_crosshair, values=weapon_list,fg_color="red",button_color="red")
option_menu_weapon.grid(row=4, column=1, padx=20, pady=10, sticky="w")

label_enemy_distance = ctk.CTkLabel(master=frame_crosshair, text="Enemy Distance", fg_color="red")
label_enemy_distance.grid(row=7, column=1,pady=10, padx=20, sticky="ew")

slider_enemy_distance = ctk.CTkSlider(master=frame_crosshair, from_=0, to=100, progress_color="red", button_color="red",command=set_enemy_distance)
slider_enemy_distance.grid(row=8, column=1, columnspan=2, pady=10, padx=20, sticky="ew")

# Bottom buttons
frame_bottom = ctk.CTkFrame(master=root)
frame_bottom.pack(side="bottom", fill="x", padx=5, pady=5)

button_save1 = ctk.CTkButton(master=frame_bottom, text="Activate", command=start, fg_color="red")
button_save1.pack(side="left", fill="x", expand=True, pady=10, padx=10)

button_save2 = ctk.CTkButton(master=frame_bottom, text="Save", command=save, fg_color="red")
button_save2.pack(side="left", fill="x", expand=True, pady=10, padx=10)

button_exit = ctk.CTkButton(master=frame_bottom, text="Exit", command=close, fg_color="red")
button_exit.pack(side="right", fill="x", expand=True, pady=10, padx=10)

# Initially show the General frame
show_frame(frame_general)

root.mainloop()


