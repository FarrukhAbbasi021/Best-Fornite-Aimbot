import os
import psutil
import sys
import threading
import ctypes
import cv2
import json
import math
import mss
import numpy as np
import time
import torch
import uuid
import win32api
import os.path
import platform
from datetime import datetime

from pynput import keyboard
from termcolor import colored


class guiConf:
        with open("lib/config/guiconf.json") as f:
         gui_Conf = json.load(f)

if guiConf.gui_Conf["aimkey"] == "leftShift": #if aimkey from config = shift
    print("leftShift")
    def is_targeted():
        return True if win32api.GetKeyState(0xA0) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "leftAlt": #if aimkey from config = alt
     print("leftAlt")
     def is_targeted():
        return True if win32api.GetKeyState(0x12) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "rightMouse":
    print("rightMouse")
    def is_targeted():
        return True if win32api.GetKeyState(0x02) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "mouse5":
     print("mouse5")
     def is_targeted():
        return True if win32api.GetKeyState(0x06) in (-127, -128) else False
        toggle = "MOUSE 5"
elif guiConf.gui_Conf["aimkey"] == "leftMouse":
     print("left Mouse")
     def is_targeted():
        return True if win32api.GetKeyState(0x01) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "ctrl":
     print("ctrl")
     def is_targeted():
        return True if win32api.GetKeyState(0x11) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "mouse4":
     print("mouse4")
     def is_targeted():
        return True if win32api.GetKeyState(0x5) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "`":
     print("`")
     def is_targeted():
        return True if win32api.GetKeyState(0xC0) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "1":
     print("1")
     def is_targeted():
        return True if win32api.GetKeyState(0x31) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "2":
     print("2")
     def is_targeted():
        return True if win32api.GetKeyState(0x32) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "3":
     print("3")
     def is_targeted():
        return True if win32api.GetKeyState(0x33) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "4":
     print("4")
     def is_targeted():
        return True if win32api.GetKeyState(0x34) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "5":
     print("5")
     def is_targeted():
        return True if win32api.GetKeyState(0x35) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "6":
     print("6")
     def is_targeted():
        return True if win32api.GetKeyState(0x36) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "7":
     print("7")
     def is_targeted():
        return True if win32api.GetKeyState(0x37) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "8":
     print("8")
     def is_targeted():
        return True if win32api.GetKeyState(0x38) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "9":
     print("9")
     def is_targeted():
        return True if win32api.GetKeyState(0x39) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "0":
     print("0")
     def is_targeted():
        return True if win32api.GetKeyState(0x30) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "-":
     print("-")
     def is_targeted():
        return True if win32api.GetKeyState(0xBD) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "Q":
     print("Q")
     def is_targeted():
        return True if win32api.GetKeyState(0x51) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "capsLock":
     print("-")
     def is_targeted():
        return True if win32api.GetKeyState(0x14) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "W":
     print("W")
     def is_targeted():
        return True if win32api.GetKeyState(0x57) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "E":
     print("E")
     def is_targeted():
        return True if win32api.GetKeyState(0x45) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "R":
     print("R")
     def is_targeted():
        return True if win32api.GetKeyState(0x52) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "T":
     print("T")
     def is_targeted():
        return True if win32api.GetKeyState(0x54) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "Y":
     print("-")
     def is_targeted():
        return True if win32api.GetKeyState(0x59) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "U":
     print("U")
     def is_targeted():
        return True if win32api.GetKeyState(0x55) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "I":
     print("I")
     def is_targeted():
        return True if win32api.GetKeyState(0x49) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "O":
     print("O")
     def is_targeted():
        return True if win32api.GetKeyState(0x59) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "P":
     print("P")
     def is_targeted():
        return True if win32api.GetKeyState(0x50) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "[":
     print("[")
     def is_targeted():
        return True if win32api.GetKeyState(0xDB) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "]":
     print("]")
     def is_targeted():
        return True if win32api.GetKeyState(0xDD) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "A":
     print("A")
     def is_targeted():
        return True if win32api.GetKeyState(0x41) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "S":
     print("S")
     def is_targeted():
        return True if win32api.GetKeyState(0x53) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "D":
     print("D")
     def is_targeted():
        return True if win32api.GetKeyState(0x44) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "F":
     print("F")
     def is_targeted():
        return True if win32api.GetKeyState(0x46) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "G":
     print("G")
     def is_targeted():
        return True if win32api.GetKeyState(0x47) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "H":
     print("H")
     def is_targeted():
        return True if win32api.GetKeyState(0x48) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "J":
     print("J")
     def is_targeted():
        return True if win32api.GetKeyState(0x4A) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "K":
     print("K")
     def is_targeted():
        return True if win32api.GetKeyState(0x4B) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "L":
     print("L")
     def is_targeted():
        return True if win32api.GetKeyState(0x4C) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == ";":
     print(";")
     def is_targeted():
        return True if win32api.GetKeyState(0xBA) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "'":
     print("'")
     def is_targeted():
        return True if win32api.GetKeyState(0xDE) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "\ ":
     print("\ ")
     def is_targeted():
        return True if win32api.GetKeyState(0xDC) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "Z":
     print("Z")
     def is_targeted():
        return True if win32api.GetKeyState(0x5A) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "X":
     print("X")
     def is_targeted():
        return True if win32api.GetKeyState(0x58) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "C":
     print("C")
     def is_targeted():
        return True if win32api.GetKeyState(0x43) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "V":
     print("V")
     def is_targeted():
        return True if win32api.GetKeyState(0x56) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "B":
     print("B")
     def is_targeted():
        return True if win32api.GetKeyState(0x42) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "N":
     print("N")
     def is_targeted():
        return True if win32api.GetKeyState(0x4E) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "M":
     print("M")
     def is_targeted():
        return True if win32api.GetKeyState(0x4D) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == ",":
     print(",")
     def is_targeted():
        return True if win32api.GetKeyState(0xBC) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == ".":
     print(".")
     def is_targeted():
        return True if win32api.GetKeyState(0xBE) in (-127, -128) else False
elif guiConf.gui_Conf["aimkey"] == "/ ":
     print("/ ")
     def is_targeted():
        return True if win32api.GetKeyState(0xBF) in (-127, -128) else False



smooth = guiConf.gui_Conf["strenght"] #gets the strenght value from the guiconf 
dtthreshold = guiConf.gui_Conf["confidence"]
print("The detection threshhold ist",dtthreshold)
print("The strenght is",smooth)


if guiConf.gui_Conf["fovsize"] =="small":
    box_size = 100
    print("Small")
elif guiConf.gui_Conf["fovsize"] =="medium":
    print("Medium")
    box_size = 200
elif  guiConf.gui_Conf["fovsize"] =="big":
    print("Big")
    box_size = 300


print(colored("Aimbot is starting!","green"))

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )


PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


class Aimbot:
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    screen = mss.mss()
    pixel_increment = smooth #controls how many pixels the mouse moves for each relative movement
    with open("lib/config/config.json") as f:
        sens_config = json.load(f)
    aimbot_status = colored("ENABLED", 'blue')

    def __init__(self, box_constant = box_size, collect_data = False, mouse_delay = 0.0001, debug = False):
        #controls the initial centered box width and height of the "Vision" window
        self.box_constant = box_constant #controls the size of the detection box (equaling the width and height)

        print("\033[H\033[J", end="")
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='lib/best.pt', force_reload = True)
        print("\033[H\033[J", end="") # cleans the console  # sets the background to blue
        #if torch.cuda.is_available():
            #if "16" in torch.cuda.get_device_name(torch.cuda.current_device()): #known error with the 1650 GPUs where detection doesn't work
                #print(colored("[PythonCheat] NVIDIA ACCELERATION IS UNAVAILABLE (ISSUE WITH 1650/1660 GPUs)", "red"))
               # os._exit(1)
           # else:
               # print(colored("[PythonCheat] GRAPHICS CARD ACCELERATION [ENABLED]", "white"))
       # else:
           # print(colored("[PythonCheat] NVIDIA ACCELERATION IS UNAVAILABLE", "red"))
           # print(colored("[PythonCheat] You havent installed PyTorch, your performance will be very poor", "red"))

        self.model.conf = dtthreshold # base confidence threshold (or base detection (0-1)
        self.model.iou = 0.2 # NMS IoU (0-1)
        self.collect_data = collect_data
        self.mouse_delay = mouse_delay
        self.debug = debug

        print(colored("\n[www.PokorEXE.com] USE 'F1' TO ENEABLE/DISABLE AIMBOT\n[Optical] PRESS 'F2' TO CLOSE THE AIMBOT", "white"))
        print(guiConf.gui_Conf["aimkey"])
    def update_status_aimbot():
        if Aimbot.aimbot_status == colored("ENABLED", 'blue'):
            Aimbot.aimbot_status = colored("DISABLED", 'red')
        else:
            Aimbot.aimbot_status = colored("ENABLED", 'blue')
        sys.stdout.write("\033[K")
        print(f"[Pokor] AIMBOT IS [{Aimbot.aimbot_status}]", end = "\r")

    def right_click():
        return True if win32api.GetKeyState(0x02) in (-127, -128) else False

    def sleep(duration, get_now = time.perf_counter):
        if duration == 0: return
        now = get_now()
        end = now + duration
        while now < end:
            now = get_now()

    def is_aimbot_enabled():
        return True if Aimbot.aimbot_status == colored("ENABLED", 'blue') else True

    def is_target_locked(x, y):
        #plus/minus 5 pixel threshold
        threshold = 5
        return True if 960 - threshold <= x <= 960 + threshold and 540 - threshold <= y <= 540 + threshold else False

    def move_crosshair(self, x, y):
        if is_targeted() and Aimbot.right_click():
            scale = Aimbot.sens_config["targeting_scale"]
        elif is_targeted():
            scale = 1.0
        else:
            return #TODO

        if self.debug: start_time = time.perf_counter()
        for rel_x, rel_y in Aimbot.interpolate_coordinates_from_center((x, y), scale):
            Aimbot.ii_.mi = MouseInput(rel_x, rel_y, 0, 0x0001, 0, ctypes.pointer(Aimbot.extra))
            input_obj = Input(ctypes.c_ulong(0), Aimbot.ii_)
            ctypes.windll.user32.SendInput(1, ctypes.byref(input_obj), ctypes.sizeof(input_obj))
            if not self.debug: Aimbot.sleep(self.mouse_delay) #time.sleep is not accurate enough
        if self.debug: #remove this later
            print(f"TIME: {time.perf_counter() - start_time}")
            print("DEBUG: SLEEPING FOR 1 SECOND")
            time.sleep(1)

    #generator yields pixel tuples for relative movement
    def interpolate_coordinates_from_center(absolute_coordinates, scale):
        diff_x = (absolute_coordinates[0] - 960) * scale/Aimbot.pixel_increment
        diff_y = (absolute_coordinates[1] - 540) * scale/Aimbot.pixel_increment
        length = int(math.dist((0,0), (diff_x, diff_y)))
        if length == 0: return
        unit_x = (diff_x/length) * Aimbot.pixel_increment
        unit_y = (diff_y/length) * Aimbot.pixel_increment
        x = y = sum_x = sum_y = 0
        for k in range(0, length):
            sum_x += x
            sum_y += y
            x, y = round(unit_x * k - sum_x), round(unit_y * k - sum_y)
            yield x, y
            

    def start(self):
        print(colored("[Optical] AI started analysing", "white"))
        Aimbot.update_status_aimbot()
        half_screen_width = ctypes.windll.user32.GetSystemMetrics(0)/2 #this should always be 960
        half_screen_height = ctypes.windll.user32.GetSystemMetrics(1)/2 #this should always be 540
        detection_box = {'left': int(half_screen_width - self.box_constant//2), #x1 coord (for top-left corner of the box)
                          'top': int(half_screen_height - self.box_constant//2), #y1 coord (for top-left corner of the box)
                          'width': int(self.box_constant),  #width of the box
                          'height': int(self.box_constant)} #height of the box
        if self.collect_data:
            collect_pause = 0

        while True:
            start_time = time.perf_counter()
            frame = np.array(Aimbot.screen.grab(detection_box))
            if self.collect_data: orig_frame = np.copy((frame))
            results = self.model(frame)

            if len(results.xyxy[0]) != 0: #player detected
                least_crosshair_dist = closest_detection = player_in_frame = False
                for *box, conf, cls in results.xyxy[0]: #iterate over each player detected
                    x1y1 = [int(x.item()) for x in box[:2]]
                    x2y2 = [int(x.item()) for x in box[2:]]
                    x1, y1, x2, y2, conf = *x1y1, *x2y2, conf.item()
                    height = y2 - y1
                    relative_head_X, relative_head_Y = int((x1 + x2)/2), int((y1 + y2)/2 - height/2.7) #offset to roughly approximate the head using a ratio of the height
                    own_player = x1 < 15 or (x1 < self.box_constant/5 and y2 > self.box_constant/1.2) #helps ensure that your own player is not regarded as a valid detection

                    #calculate the distance between each detection and the crosshair at (self.box_constant/2, self.box_constant/2)
                    crosshair_dist = math.dist((relative_head_X, relative_head_Y), (self.box_constant/2, self.box_constant/2))

                    if not least_crosshair_dist: least_crosshair_dist = crosshair_dist #initalize least crosshair distance variable first iteration

                    if crosshair_dist <= least_crosshair_dist and not own_player:
                        least_crosshair_dist = crosshair_dist
                        closest_detection = {"x1y1": x1y1, "x2y2": x2y2, "relative_head_X": relative_head_X, "relative_head_Y": relative_head_Y, "conf": conf}

                    if not own_player:
                        cv2.rectangle(frame, x1y1, x2y2, (244, 113, 115), 2) #draw the bounding boxes for all of the player detections (except own)
                        cv2.putText(frame, f"{int(conf * 100)}%", x1y1, cv2.FONT_HERSHEY_DUPLEX, 0.5, (244, 113, 116), 2) #draw the confidence labels on the bounding boxes
                    else:
                        own_player = False
                        if not player_in_frame:
                            player_in_frame = True

                if closest_detection: #if valid detection exists
                    cv2.circle(frame, (closest_detection["relative_head_X"], closest_detection["relative_head_Y"]), 5, (115, 244, 113), -1) #draw circle on the head

                    #draw line from the crosshair to the head
                    cv2.line(frame, (closest_detection["relative_head_X"], closest_detection["relative_head_Y"]), (self.box_constant//2, self.box_constant//2), (244, 242, 113), 2)

                    absolute_head_X, absolute_head_Y = closest_detection["relative_head_X"] + detection_box['left'], closest_detection["relative_head_Y"] + detection_box['top']

                    x1, y1 = closest_detection["x1y1"]
                    if Aimbot.is_target_locked(absolute_head_X, absolute_head_Y):
                        cv2.putText(frame, "LOCKED", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (115, 244, 113), 2) #draw the confidence labels on the bounding boxes
                    else:
                        cv2.putText(frame, "TARGETING", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (115, 113, 244), 2) #draw the confidence labels on the bounding boxes

                    if Aimbot.is_aimbot_enabled():
                        Aimbot.move_crosshair(self, absolute_head_X, absolute_head_Y)
                            

            if self.collect_data and time.perf_counter() - collect_pause > 1 and is_targeted() and Aimbot.is_aimbot_enabled() and not player_in_frame: #screenshots can only be taken every 1 second
                cv2.imwrite(f"lib/data/{str(uuid.uuid4())}.jpg", orig_frame)
                collect_pause = time.perf_counter()
            
            cv2.putText(frame, f"{int(1/(time.perf_counter() - start_time)) * 9.5 }", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)
            cv2.imshow("www.PokorEXE.com", frame)
            if cv2.waitKey(1) & 0xFF == ord('0'):
                break

    def clean_up():
        print(colored("\n[Optical] Aimbot is CLOSING...", "red"))
        Aimbot.screen.close()
        import subprocess
        os.chdir('/Program Files/Internet Explorer/')
        path = os.getcwd()
        subprocess.call('start /wait python reloader.py', shell=True)
        os._exit(0)

if __name__ == "__main__": print("Error! Contact admin!")