import subprocess
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEventLoop, QTimer, QRect
import pyttsx3
import speech_recognition as sr
import time
import imaplib
import email
import pyautogui
from email.header import decode_header
from PyQt5.QtCore import Qt, QSize
import sys
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QFont, QPainter, QPen, QBrush, QRadialGradient, QColor, QLinearGradient
import datetime
import requests
from playwright.sync_api import sync_playwright, TimeoutError
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os 

load_dotenv("safe.env")


API_KEY = os.getenv("API_KEY")
mail_password_work = os.getenv("mail_password_work")
insta_id= os.getenv("insta_id")
insta_pwd = os.getenv("insta_pwd")
mail_work =os.getenv("mail_work")

#todo
#image gen
#map insta names to id so that user can just add name
#appointments (timebounds)
#maybe add emojis
#maybe sim youtube,insta , twitter , reddit
#get messages
#copypasting shit from read files
#non flatpak opening
#most of flatpak no opening
#no fall back if voice req fails to og loop
#adding checking things off todo list
#when an input takes time and i try to speak to change setuplayout it wont change like in check mail
#scrolling when email
#play music
#upcoming events google calander type
#Aps to simulate - Discord , Instagram , twitter , Whatsapp(might adb) , amazon , netflix , spotify , attacker tv (prime,disney) , swoggy/ubereats , mmet/zoom
#able to add youtube list maybe some fix for printing
#netflix
#discord

global variable
variable = True
yt_list = ["PewDiePie" , "Patrick Cc:" , "Nicole Rafiee" , "Ludwig" , "HealthyGamerGG", "Cinna", "penguinz0" , "JaidendAnimation" , "Amelia Dimoldenberg" , "theneedledrop"]
d = {
    "Android Studio": "com.google.AndroidStudio",
    "OBS": "com.obsproject.Studio",
    "Spotify": "com.spotify.Client",
    "Whatsapp": "io.github.mimbrero.WhatsAppDesktop",
    "Audacity": "org.audacityteam.Audacity",
    "gimp": "org.gimp.GIMP",
    "Kdenlive": "org.kde.kdenlive"
}
yt_channels = {
    "PewDiePie": "UC-lHJZR3Gqxm24_Vd_AJ5Yw",
    "Patrick Cc:": "UCX0aUB-99m_b958ljpioOhQ",
    "Nicole Rafiee": "UCw8_yg1camlWnYfX_0tfECw",
    "Ludwig": "UCrPseYLGpNygVi34QpGNqpA",
    "HealthyGamerGG": "UClHVl2N3jPEbkNJVx-ItQIQ",
    "penguinz0": "UCq6VFHwMzcMXbuKyG7SQYIg",
    "JaidendAnimation": "UCGwu0nbY2wSkW8N-cghnLpA",
}
path = "/home/shreya/Desktop/notes/"
alarm = QSound("alarm.wav")

imap = imaplib.IMAP4_SSL("imap.gmail.com")
timer = QTimer()
engine = pyttsx3.init()
recognizer = sr.Recognizer()
mic = sr.Microphone()


app = QApplication([])

class HUDPanel(QFrame):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        gradient = QRadialGradient(self.width()/2, self.height()/2, max(self.width(), self.height()))
        gradient.setColorAt(0, QColor(2, 2, 10, 200))
        gradient.setColorAt(0.7, QColor(0, 80, 100, 80))
        gradient.setColorAt(1, QColor(2, 2, 10, 255))
        
        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())
        




class MainWindow(QWidget):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            self.voice_activate()
        if event.key() == Qt.Key_Up :
            changer(variable)
    
    def voice_activate(self):
        listen()

screen = QDesktopWidget().screenGeometry()
window = MainWindow()
window.setWindowTitle("◢ FELLER INTERFACE ◣")
window.setGeometry(50, 0, screen.width() // 2, screen.height() + 100)  


cyber_style = """
QWidget {
    background: qradialgradient(cx:0.5, cy:0.5, radius:1.2,
                               stop:0 rgba(10, 10, 25, 255),
                               stop:0.6 rgba(10, 10, 25, 255),
                               stop:1 rgba(10, 10, , 255));
    color: #557788;
    font-family: 'Orbitron', 'Consolas', monospace;
    font-weight: 500;
}

QLineEdit {
    background: qradialgradient(cx:0.5, cy:0.5, radius:0.9,
                               stop:0 rgba(10, 15, 30, 200),
                               stop:1 rgba(2, 5, 15, 180));
    border: 1px solid rgba(0, 80, 100, 80);
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 12px;
    color: #557788;
    selection-background-color: rgba(0, 80, 100, 30);
}

QLineEdit:focus {
    border: 1px solid #005566;
    background: qradialgradient(cx:0.5, cy:0.5, radius:0.9,
                               stop:0 rgba(15, 20, 35, 200),
                               stop:1 rgba(5, 10, 20, 180));
    box-shadow: 0 0 10px rgba(0, 80, 100, 30);
}

QLabel {
    color: #557788;
    background: transparent;
    font-weight: 600;
}

QScrollArea {
    background: qradialgradient(cx:0.5, cy:0.5, radius:0.9,
                               stop:0 rgba(2, 5, 15, 180),
                               stop:1 rgba(10, 15, 25, 200));
    border: 1px solid rgba(0, 80, 100, 60);
    border-radius: 8px;
}

QScrollBar:vertical {
    background: rgba(2, 5, 15, 150);
    width: 4px;
    border-radius: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                               stop:0 #005566,
                               stop:1 #002244);
    border-radius: 2px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                               stop:0 #007788,
                               stop:1 #003355);
}

QFrame {
    border: none;
    background: transparent;
}
"""

window.setStyleSheet(cyber_style)

main_layout = QVBoxLayout()
main_layout.setContentsMargins(5, 5, 5, 5)
main_layout.setSpacing(3)

top_bar = QHBoxLayout()
top_bar.setSpacing(5)





neural_status = HUDPanel()
neural_status.setFixedHeight(60)
neural_layout = QVBoxLayout()
neural_layout.setContentsMargins(8, 4, 8, 4)
neural_layout.setSpacing(2)

neural_title = QLabel(" FELLER ")
neural_title.setStyleSheet("""
    font-size: 10px;
    color: #557788;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(0, 80, 100, 30);
""")
neural_title.setAlignment(Qt.AlignCenter)

mode = QLabel("◉ COMMAND_MODE")
mode.setStyleSheet("""
    width: 8px;
    font-size: 8px;
    color: #cc3344;
    font-weight: bold;
    padding: 2px 6px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                               stop:0 rgba(200, 50, 70, 35),
                               stop:1 rgba(200, 50, 70, 10));
    border-radius: 4px;
""")
mode.setAlignment(Qt.AlignCenter)

neural_layout.addWidget(neural_title)
neural_layout.addWidget(mode)
neural_status.setLayout(neural_layout)






time_display = QLabel(datetime.datetime.now().strftime("%H:%M:%S │ %Y.%m.%d"))
time_display.setStyleSheet("""
    font-size: 8px;
    color: #557788;
    font-family: 'Courier New', monospace;
""")
time_display.setAlignment(Qt.AlignCenter)

top_bar.addWidget(neural_status)
content_area = QHBoxLayout()
content_area.setSpacing(5)
left_column = QVBoxLayout()
left_column.setSpacing(3)

version_info = QLabel("v2.0 │ NEURAL_LINK: ACTIVE │ STATUS: ONLINE")
version_info.setAlignment(Qt.AlignCenter)
version_info.setStyleSheet("""
    font-size: 8px;
    color: #557788;
    font-family: 'Courier New', monospace;
""")





# ASCII animation panel
ascii_panel = HUDPanel()
ascii_panel.setFixedHeight(120)
ascii_layout = QVBoxLayout()
ascii_layout.setContentsMargins(8, 5, 8, 5)

ascii_header = QLabel("◢ NEURAL CORE PULSE ◣")
ascii_header.setStyleSheet("""
    font-size: 10px;
    color: #557788;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(0, 80, 100, 30);
""")
ascii_header.setAlignment(Qt.AlignCenter)

ascii_frames = [
    """╔════[ CORE ACTIVE ]════╗
║ ▉▉▉▉▉▉▉▉▉▉ 100%    ║
║ ◉ ◎ ◉ ◎ ◉ ◎ ◉      ║
║ FLUX: STABLE        ║
║ PULSE: ████ 80%     ║
╚═══════════════════════╝""",
    """╔════[ CORE ACTIVE ]════╗
║ ▉▉▉▉▉▉▉▉▉▉▉ 120%   ║
║ ◎ ◉ ◎ ◉ ◎ ◉ ◎      ║
║ FLUX: PULSING       ║
║ PULSE: █████ 90%    ║
╚═══════════════════════╝""",
]

ascii_display = QLabel(ascii_frames[0])
ascii_display.setStyleSheet("""
    font-size: 8px;
    color: #557788;
    font-family: 'Courier New', monospace;
    text-shadow: 0 0 3px rgba(0, 80, 100, 25);
""")

ascii_layout.addWidget(ascii_header)
ascii_layout.addWidget(ascii_display)
ascii_panel.setLayout(ascii_layout)


# Task panels
todo_panel = HUDPanel()
todo_panel.setFixedHeight(100)
todo_layout = QVBoxLayout()
todo_layout.setContentsMargins(8, 5, 8, 5)
todo_layout.setSpacing(3)

todo_header = QLabel("◢ NEURAL TASKS ◣")
todo_header.setStyleSheet("""
    font-size: 10px;
    color: #aa5533;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(170, 85, 50, 25);
""")
todo_header.setAlignment(Qt.AlignCenter)

todo_display = QLabel("└─ No active neural tasks\n└─ Task queue empty\n└─ Standby mode")
todo_display.setStyleSheet("""
    font-size: 8px;
    color: #557788;
    font-family: 'Courier New', monospace;
""")

todo_layout.addWidget(todo_header)
todo_layout.addWidget(todo_display)
todo_panel.setLayout(todo_layout)




# Appointments panel
appointment_panel = HUDPanel()
appointment_panel.setFixedHeight(100)
appointment_layout = QVBoxLayout()
appointment_layout.setContentsMargins(8, 5, 8, 5)
appointment_layout.setSpacing(3)

appointment_header = QLabel("◢ TEMPORAL COORDS ◣")
appointment_header.setStyleSheet("""
    font-size: 10px;
    color: #aa4444;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(170, 68, 68, 25);
""")
appointment_header.setAlignment(Qt.AlignCenter)

appointment_display = QLabel("└─ No scheduled events\n└─ Calendar sync: OFF\n└─ Reminder sys: READY")
appointment_display.setStyleSheet("""
    font-size: 8px;
    color: #557788;
    font-family: 'Courier New', monospace;
""")



appointment_layout.addWidget(appointment_header)
appointment_layout.addWidget(appointment_display)
appointment_panel.setLayout(appointment_layout)

left_column.addWidget(ascii_panel)
left_column.addWidget(todo_panel)
left_column.addWidget(appointment_panel)







center_column = QVBoxLayout()
center_column.setSpacing(5)

# Input panel
input_panel = QWidget()
input_panel.setFixedHeight(80)
input_layout = QVBoxLayout()
input_layout.setContentsMargins(10, 8, 10, 8)
input_layout.setSpacing(5)


input_box = QLineEdit()
input_box.setPlaceholderText("Neural command interface - ↓ voice | ↑ chat...")
input_box.setMinimumHeight(35)

input_layout.addWidget(input_box)
input_panel.setLayout(input_layout)

# Main output panel
output_panel = HUDPanel()
output_layout = QVBoxLayout()
output_layout.setContentsMargins(10, 8, 10, 8)
output_layout.setSpacing(5)



status_label = QLabel("hey")
status_label.setWordWrap(True)
status_label.setStyleSheet("""
    font-family: 'Courier New', monospace;
    font-size: 9px;
    color: #557788;
    background: qradialgradient(cx:0.5, cy:0.5, radius:0.9,
                               stop:0 rgba(2, 5, 15, 140),
                               stop:1 rgba(10, 15, 25, 170));
    padding: 8px;
    border-radius: 8px;
    text-shadow: 0 0 3px rgba(0, 80, 100, 25);
""")

scroll = QScrollArea()
scroll.setWidgetResizable(True)
scroll.setWidget(status_label)

output_layout.addWidget(scroll)
output_panel.setLayout(output_layout)

center_column.addWidget(input_panel)
center_column.addWidget(output_panel)




right_column = QVBoxLayout()
right_column.setSpacing(3)

network_panel = HUDPanel()
network_panel.setFixedHeight(120)
network_layout = QVBoxLayout()
network_layout.setContentsMargins(8, 5, 8, 5)

network_header = QLabel("◢ NETWORK STATUS ◣")
network_header.setStyleSheet("""
    font-size: 10px;
    color: #55aa77;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(85, 170, 120, 25);
""")
network_header.setAlignment(Qt.AlignCenter)

network_info = QLabel("""
┌─── CONNECTIONS ───┐
│ WEB: ████████ OK  │
│ MAIL: ███████ OK  │
│ API: ████████ OK  │
│ DNS: ████████ OK  │
└───────────────────┘
LATENCY: 12ms
BANDWIDTH: 100MB/s
""")
network_info.setStyleSheet("""
    font-size: 8px;
    color: #55aa77;
    font-family: 'Courier New', monospace;
    text-shadow: 0 0 3px rgba(85, 170, 120, 20);
""")

network_layout.addWidget(network_header)
network_layout.addWidget(network_info)
network_panel.setLayout(network_layout)

# Protocol status
protocol_panel = HUDPanel()
protocol_panel.setFixedHeight(140)
protocol_layout = QVBoxLayout()
protocol_layout.setContentsMargins(8, 5, 8, 5)

protocol_header = QLabel("◢ PROTOCOL STATUS ◣")
protocol_header.setStyleSheet("""
    font-size: 10px;
    color: #8855aa;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(136, 85, 170, 25);
""")
protocol_header.setAlignment(Qt.AlignCenter)

protocol_info = QLabel("""
┌─── ACTIVE PROTOCOLS ───┐
│ FILE_ACCESS: ████ READY │
│ VOICE_REC: ████ ACTIVE  │
│ MAIL_SCAN: ████ READY   │
│ WEB_SCRAPE: ███ READY   │
│ CHAT_AI: █████ ACTIVE   │
│ SCREENSHOT: ██ READY    │
│ APP_LAUNCH: ███ READY   │
└─────────────────────────┘

NEURAL_PATHWAYS: 7/7 ACTIVE
QUANTUM_SYNC: LOCKED
""")
protocol_info.setStyleSheet("""
    font-size: 7px;
    color: #8855aa;
    font-family: 'Courier New', monospace;
    text-shadow: 0 0 3px rgba(136, 85, 170, 20);
""")

protocol_layout.addWidget(protocol_header)
protocol_layout.addWidget(protocol_info)
protocol_panel.setLayout(protocol_layout)



command_panel = HUDPanel()
command_panel.setFixedHeight(160)
command_layout = QVBoxLayout()
command_layout.setContentsMargins(8, 5, 8, 5)

command_header = QLabel("◢ QUICK REFERENCE ◣")
command_header.setStyleSheet("""
    font-size: 10px;
    color: #cc6644;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(204, 102, 68, 25);
""")
command_header.setAlignment(Qt.AlignCenter)

command_info = QLabel("""
┌─── NEURAL COMMANDS ───┐
│ open app_name         │
│ open website.com      │
│ make note/file/todo   │
│ check mail/youtuber   │
│ send mail/dm          │
│ search query          │
│ read filename         │
│ screenshot name       │
│ show todo/appointments│
│ set reminder          │
└───────────────────────┘

┌─── HOTKEYS ───┐
│ ↓ = VOICE     │
│ ↑ = CHAT      │
└───────────────┘
""")
command_info.setStyleSheet("""
    font-size: 7px;
    color: #cc6644;
    font-family: 'Courier New', monospace;
    text-shadow: 0 0 3px rgba(204, 102, 68, 20);
""")



#odhuhhjgd



command_layout.addWidget(command_header)
command_layout.addWidget(command_info)
command_panel.setLayout(command_layout)

right_column.addWidget(network_panel)
right_column.addWidget(protocol_panel)
right_column.addWidget(command_panel)

left_widget = QWidget()
left_widget.setLayout(left_column)
left_widget.setFixedWidth(200)

center_widget = QWidget()
center_widget.setLayout(center_column)

right_widget = QWidget()
right_widget.setLayout(right_column)
right_widget.setFixedWidth(180)

content_area.addWidget(left_widget)
content_area.addWidget(center_widget)
content_area.addWidget(right_widget)

main_layout.addLayout(top_bar)
main_layout.addLayout(content_area)

window.setLayout(main_layout)
window.show()

# Animation timers
animation_timer = QTimer()
frame_index = 0

def update_animation():
    global frame_index
    frame_index = (frame_index + 1) % len(ascii_frames)
    ascii_display.setText(ascii_frames[frame_index])

animation_timer.timeout.connect(update_animation)
animation_timer.start(800)

core_status_frames = [



    """╔═══════[ SYNAPTIC CORE ]═══════╗
║                               ║
║      ╭──────╮   ◉   ╭──────╮  ║
║      │ ◎ ◎ │  ╱╲  ◉ │ ◎ ◎ │  ║
║      ╰──────╯ ╱╳╲ ╰──────╯  ║
║        ◉     ╲_/     ◉      ║
║   ╔═══╡ THOUGHT RATE: 4.6 ╞═══╗
║   ╚═════════════════════════╝  ║
║                               ║
╚═══════════════════════════════╝""",


    """╔═══════[ SYNAPTIC CORE ]═══════╗
║                               ║
║    ╭────╮     ◉     ╭────╮    ║
║    │ ◎  │   ╱╲╱╲   │  ◎ │    ║
║    ╰────╯  ╲╳╳╳╲  ╰────╯    ║
║      ◉      ╲_/     ◉       ║
║   ╔═══╡ THOUGHT RATE: 9.4 ╞═=══╗
║   ╚═══════════════════════=═╝  ║
║                                ║
╚════════════════════════════=═══╝""",







]
core_frame_index = 0

def update_core_status():
    global core_frame_index
    core_frame_index = (core_frame_index + 1) % len(core_status_frames)
    status_label.setText(core_status_frames[core_frame_index])

core_status_timer = QTimer()
core_status_timer.timeout.connect(update_core_status)
core_status_timer.start(1000)

def pause_status_animation():
    core_status_timer.stop()

def resume_status_animation():
    core_status_timer.start(1000)









def speak(text):
    time.sleep(1)
    formatted_text = f"""
┌─────────────────────────────────────────────────────────┐
│ NEURAL RESPONSE MATRIX                                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ {text}
│                                                         │
└─────────────────────────────────────────────────────────┘
"""
    status_label.setText(formatted_text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)

def get_user_input(yap):
    pause_status_animation()
    speak(yap)

    loop = QEventLoop()
    user_input = {}

    def on_submit():
        user_input['text'] = input_box.text()
        input_box.clear()
        loop.quit()

    input_box.returnPressed.disconnect()
    input_box.returnPressed.connect(on_submit)

    loop.exec_()
    return user_input['text']

def listen():
    
    with mic as source:
        speak("Listening")
        time.sleep(1)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio)
        speak("You said: " + text)
        input_box.setText(text)
    except sr.UnknownValueError:
        speak(" Could not understand audio")
    except sr.RequestError as e:
        speak(f"d API error: {e}")

def show_input():
    text = input_box.text()
    yap = text.lower()
    input_box.clear()
    checker(yap)

def changer (d) :
    global variable
    if d == True :
        mode.setText("◉ CHAT_MODE")
        mode.setStyleSheet("""
            font-size: 8px;
            color: #55aa77;
            font-weight: bold;
            padding: 2px 6px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                       stop:0 rgba(85, 170, 120, 35),
                                       stop:1 rgba(85, 170, 120, 10));
            border-radius: 4px;
        """)
        variable =  False
    else:
        variable = True
        mode.setText("◉ COMMAND_MODE")
        mode.setStyleSheet("""
            font-size: 8px;
            color: #cc3344;
            font-weight: bold;
            padding: 2px 6px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                       stop:0 rgba(200, 50, 70, 35),
                                       stop:1 rgba(200, 50, 70, 10));
            border-radius: 4px;
        """)




# def check() :
#     with open ("safe.py" , "a+") as f:
#         l=[]
#         if len(f.read()) == 0:
#             speak("I will ask u for some information say -no- if u dont wanna give it away and the function that needs it wont work. Okay?")
#             l.append(f"API_KEY = {get_user_input("Your grok api key")}") 
#             l.append(f"YT_API_KEY = {get_user_input("Your api key")}") 
#             l.append(f"insta_id = {get_user_input("Your insta id")}") 
#             l.append(f"insta_pwd = {get_user_input("Your insta pwd")}") 
#             a = get_user_input("what to call your mail id")
#             l.append(f"mail_password_{a} = {get_user_input("enter mail id")}") 
#         # b = get_user_input("what to call mail 2")
#         # l.append(f"mail_password_{b} = {get_user_input("Your grok api key")}") 
#         # c = get_user_input("what to call mail 3")
#         # l.append(f"mail_password_{c} = {get_user_input("Your grok api key")}")
#             for i in l :
#                 if i=="no":
#                     pass
#                 else:
#                     f.write(i) 
#     input_box.returnPressed.disconnect()
#     input_box.returnPressed.connect(show_input)
#     resume_status_animation()










def OpenSoftware(yap):
    parts = yap.split()
    appname = parts[1]
    try:
        subprocess.Popen([appname])
        speak("There you go!")
    except:
        if appname in d:
            subprocess.Popen(["flatpak", "run", d[appname]])
            speak("There you go")
        else:
            speak("Couldn't find flat")
    time.sleep(3)

    resume_status_animation()

def OpenWebsite(yap):
    parts = yap.split()
    if ".com" in yap:
        word = parts[1]
        try:
            webbrowser.open("https://" + word)
            speak("Opening website")
        except:
            speak("Couldn't open")
    else:
        name =get_user_input("what website?" )
        webbrowser.open("https://" + name)
        speak("Opening website")
        input_box.returnPressed.disconnect()
        input_box.returnPressed.connect(show_input)

    time.sleep(3)
    resume_status_animation()

def OpenFile():
    name = get_user_input("What to search ?")
    file_type = get_user_input("What type of file is it image/text/video/else")
    
    if file_type == "text":
        cmd = f'find ~ -iname "*{name}*.txt"'
    elif file_type in ["image", "picture"]:
        # Use raw f-string for Python 3.12+
        cmd = rf'find ~ \( -iname "*{name}*.jpg" -o -iname "*{name}*.png" -o -iname "*{name}*.jpeg" \)'
    elif file_type == "video":
        cmd = f'find ~ -iname "*{name}*.mp4"'
    else:
        cmd = f'find ~ -iname "*{name}*"'
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_list = [f for f in result.stdout.strip().split('\n') if f]
    
    if not file_list:
        speak("No files found.")
        return
    
    message = "1. " + "\n".join(f"{i+1}. {file_list[i]}" for i in range(len(file_list))) + "\n\nWhich one ?"
    number = int(get_user_input(message))
    
    path = file_list[number-1]
    subprocess.run(['xdg-open', path])
    
    speak("done")
    time.sleep(2)
    
    input_box.returnPressed.disconnect()
    input_box.returnPressed.connect(show_input)
    resume_status_animation()


def make_a_note():
    try:
        content = get_user_input("What do u want to note?")
        path = "/home/shreya/Desktop/Notes.txt"
        with open(path, "a+") as f:
            a = f"{datetime.date.today()}  at  {datetime.datetime.now().strftime("%H:%M")}"
            f.write(a + "\n")
            f.write(content + "\n")
            answer = get_user_input("Is that it?")
            if answer == "yes" :
                speak("done gg")
            else:
                content = get_user_input("go on")
                f.write(content+ "\n")
                speak("Note saved")
    except:
        speak("Didnt work")
    finally:
        input_box.returnPressed.disconnect()
        input_box.returnPressed.connect(show_input)
        resume_status_animation()

def make_a_file():
    type= get_user_input("What type ?")
    if "text" == type :
        name= get_user_input("What should I name it ?")
        string = path + name
        content = get_user_input ("What do u want to write ?")
        speak("done")
        time.sleep(2)
        with open(string , "w+") as f :
            f.write(content)
            input_box.returnPressed.disconnect()
            input_box.returnPressed.connect(show_input)
            resume_status_animation()

def set_a_reminder () :
    content = get_user_input("What do u wanna be reminded about ?")
    rtime = get_user_input("When?(type in 24 hour time if you are)")
    splitted =rtime.split(":")

    if int(splitted[0]) <10 :
        rtime = "0" + rtime 
    if "pm"  in rtime:
        rtime = rtime[0:5] + " PM"
        rtime = datetime.datetime.strptime(rtime, "%I:%M %p").strftime("%H:%M")
    else:
        rtime = rtime[0:5]
    with open("reminders.txt" , "a+") as f:
        f.write(rtime +  content + "\n")
    speak("done")
    time.sleep(4)
    input_box.returnPressed.disconnect()
    input_box.returnPressed.connect(show_input)
    resume_status_animation()

def check_reminder ():
    pause_status_animation()
    global rn
    rn = datetime.datetime.now().strftime("%H:%M")
    with open("reminders.txt" , "r") as f :
        lines = f.readlines()
        for i in lines :
            if i[0:5] == rn :
                speak("U have a reminder")
                time.sleep(3)
                reminder = i[5::]
                QSound.play("alarm.wav")
                status_label.setText(f"""
╔══════════════════════════════════════════════════════════════╗
║                    ⚠️ NEURAL ALERT ⚠️                        ║
║                                                              ║
║ {reminder}                                               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
            else:
                pass

def read_file() :
    name = get_user_input("What to search ?")
    cmd = f'find ~ -iname "*{name}*"'
    print(cmd)    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_list = result.stdout.strip().split('\n')
    file_list = [f for f in file_list if f]
    name = "1."
    for i in range(len(file_list)) :
        name =  name + file_list[i] + "\n" +str(i+2)+"."
    message = name +"\n \n \n" + "Which one ?"
    number = int(get_user_input(message))
    path = file_list[(number-1)]
    with open(path , "r") as f :
        a = f.read()
    b = get_user_input(a + "\n press okay when done") 
    if "ok" in b :
        input_box.returnPressed.disconnect()
        input_box.returnPressed.connect(show_input)
    resume_status_animation()

def edit_file():
    name = get_user_input("What to search ?")

    cmd = f'find ~ -iname "*{name}*"'
    print(cmd)    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_list = result.stdout.strip().split('\n')
    file_list = [f for f in file_list if f]
    name = "1."
    for i in range(len(file_list)) :
        name =  name + file_list[i] + "\n" +str(i+2)+"."
    message = name +"\n \n \n" + "Which one ?"
    number = int(get_user_input(message))
    path = file_list[(number-1)]
    with open(path , "a+") as f :
        f.read()
        content = get_user_input("What to add ?")
        f.write(content)
        input_box.returnPressed.disconnect()
        input_box.returnPressed.connect(show_input)
        resume_status_animation()


def mail_picker(mail, pwd):        
    from datetime import datetime, timezone
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(mail, pwd)
    imap.select("inbox")
    status, messages = imap.search(None, 'ALL')
    email_ids = messages[0].split()
    email_ids = email_ids[-50:]  
    emails = []
    today = datetime.now().date() 
    for i in email_ids:
        try:
            res, msg_data = imap.fetch(i, "(RFC822)")
            for response in msg_data:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    date_str = msg.get("Date")

                    try:
                        msg_date = email.utils.parsedate_to_datetime(date_str)
                        msg_date = msg_date.astimezone()  # convert to local timezone
                    except:
                        msg_date = datetime.now(timezone.utc)

                    if msg_date.date() != today:
                        continue  # Skip emails not from today

                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8", errors="ignore")

                    from_ = msg.get("From")

                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                try:
                                    body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                                    break
                                except:
                                    pass
                    else:
                        try:
                            body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
                        except:
                            body = ""

                    emails.append({
                        "from": from_,
                        "subject": subject,
                        "date": msg_date,
                        "body": body.strip()
                    })
        except Exception as e:
            print(f"Error fetching email {i}: {e}")
            continue

    emails.sort(key=lambda x: x["date"], reverse=True)

    format = ""
    for email_data in emails:
        format = format + f"From: {email_data['from']} \n\n Subject: {email_data['subject']}\n\n Content: ({email_data['body'][:500]})...\n\n\n\n\n\n"

    answer = get_user_input(format + "\n" + "say done to move on")
    input_box.returnPressed.disconnect()
    input_box.returnPressed.connect(show_input)
    imap.logout()
    resume_status_animation()

def check_mail():
    which = "work"
    speak("on it")
    global mail1,mail2,mail3,pwd1,pwd2,pwd3
    if which == "work":
        mail1 = mail_work
        pwd1 = mail_password_work
        mail_picker(mail1,pwd1)
    elif which == "extra" :
        mail2 = "shreyadita1611@gmail.com"
        pwd2 = mail_password_extra
        mail_picker(mail2,pwd2)

    elif which == "personal" :
        mail3 = "musicreviewnerdsxo@gmail.com"
        pwd3 = mail_password_personal
        mail_picker(mail3,pwd3)
    else:
        mail_picker("shreyakadian124@gmail.com",mail_password_work)
        mail_picker("shreyadita1611@gmail.com",mail_password_extra)
        mail_picker("musicreviewnerdsxo@gmail.com",mail_password_personal)
    resume_status_animation()

def check_mailll():
        mail_picker(mail_work,mail_password_work)



def send_email():
    send_email = get_user_input("Which mail ?")
    if send_email == "work" :
        send_email = "shreyakadian124@gmail.com"
        pwd = mail_password_work
    elif send_email == "personal" :
        send_email = "musicreviewnerds@gmail.com"
        pwd = mail_password_personal
    elif send_email == "extra" :
        send_email = "shreyadita1611@gmail.com"
        pwd = mail_password_extra

    else:
        pass
    to_email = get_user_input("To who ?")
    subject = get_user_input("Subject ?")
    body = get_user_input("content ?")

        
    try:
        msg = MIMEMultipart()
        msg["From"] = send_email
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  
        server.login(send_email, pwd)
        server.send_message(msg)
        server.quit()

        speak("Email sent successfully.")

    except Exception as e:
        speak("Failed to send email.")
    input_box.returnPressed.disconnect()
    input_box.returnPressed.connect(show_input)
    resume_status_animation()

def make_todo () :
    with open("todo.txt", "w+") as f:
        date = f"{datetime.date.today()}"
        f.write(date + "\n")
        count = 0
        content = []
        while True :
            count = count +1
            list = get_user_input(" Alright keep adding say stop to stop")
            if list !=  "stop" :
                d = f'{count}. {list}"\n"'
                content.append(d)
            else:
                break
        f.writelines(content)
        f.write("\n")
    list =  date + '\n'
    for i in content :
        list = list + i
    list = list + '\n'
    with open ("oldtodos.txt" , "a+") as k:
        k.write(list)  

    input_box.returnPressed.disconnect()
    input_box.returnPressed.connect(show_input)
    formatted_list = f"""
╔══════════════════════════════════════════════════════════════╗
║                    NEURAL TASK PROTOCOL                      ║
║                                                              ║
║ {list}                                                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    status_label.setText(formatted_list)

def show_todo():
    with open("todo.txt" , "r") as f :
        a = f.read()
        f.seek(0)
    speak(a)

def chat(yap) :
    with open("chathistory.txt" , "r") as f:
        a = f.read()
    url = "https://api.groq.com/openai/v1/chat/completions"
    string = f"Bearer {API_KEY}"
    game = a +"CURRENT QUERY--" +yap + "(always keep it sigma)"
    headers = {
    "Authorization": string,
    "Content-Type": "application/json"}
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": game}]}
    response = requests.post(url, headers=headers, json=data)
    answer = response.json()["choices"][0]["message"]["content"]
    speak(answer)
    with open("chathistory.txt" , "a+") as f :
        f.write(str(datetime.datetime.now())+"\n")
        f.write(f"User:{yap}\n")
        f.write(f"AI:{answer}\n\n")
 
def search_yt (yap) :
    yap = yap.replace("on youtube", "")
    yap = yap.replace("search", "")
    yap = yap.replace(" " , "+")
    address =f"https://www.youtube.com/results?search_query={yap}"
    webbrowser.open(address)
    resume_status_animation()

def make_appointments () :
    with open("appointments.txt", "w+") as f:
        date = f"{datetime.date.today()}"
        f.write(date + "\n")
        count = 0
        content = []
        while True :
            count = count +1
            list = get_user_input(" Alright keep adding say stop to stop")
            time = get_user_input(" What time ? ")
            if list !=  "stop" :
                d = f'{count}. {list}"\n" --- {time}'
                content.append(d)
            else:
                break
        f.writelines(content)
        f.write("\n")
    list =  date + '\n'
    for i in content :
        list = list + i
    list = list + '\n'
    with open ("oldappointments.txt" , "a+") as k:
        k.write(list)  

    input_box.returnPressed.disconnect()
    input_box.returnPressed.connect(show_input)
    formatted_list = f"""
╔══════════════════════════════════════════════════════════════╗
║                 NEURAL APPOINTMENT PROTOCOL                  ║
║                                                              ║
║ {list}                                                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    status_label.setText(formatted_list)

def show_appointments():
    with open("appointments.txt" , "r") as f :
        a = f.read()
        f.seek(0)
    speak(a)

def youtube_channel(yap) :
    address= "https://www.youtube.com/@AKAMAI_edits/videos"
    url = "https://api.groq.com/openai/v1/chat/completions"
    string = f"Bearer {API_KEY}"
    yap = yap.replace("search" , "")
    yap = yap.replace("on youtube", "")
    game = f"I want u to search {yap}'s channel on youtube and give me his channel name on you youtube like Vedant Rusty's channel id is @vedantrusty and get the channel type shit and just give me the id with the @ and not one word extra from u i want your out to only be the id?"
    headers = {
    "Authorization": string,
    "Content-Type": "application/json"}
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": game}]}
    response = requests.post(url, headers=headers, json=data)
    answer = response.json()["choices"][0]["message"]["content"]
    answer = answer.partition("@")
    address = f"https://www.youtube.com/@{answer[2]}/videos"
    webbrowser.open(address)
    resume_status_animation()

def screenshot ():
    name = get_user_input("What to name it ?")
    a = f"/home/shreya/pitures/{name}.png"
    pyautogui.screenshot(a)
    resume_status_animation()

from playwright.sync_api import sync_playwright, TimeoutError
import time

def send_dm():
    who = get_user_input("Who to dm ?")
    what = get_user_input("What to say ?")

    p = sync_playwright().start()  # start fresh each time
    browser = p.chromium.launch(
        headless=False,
        executable_path="/usr/bin/brave-browser"
    )
    page = browser.new_page()

    # login
    page.goto("https://www.instagram.com/accounts/login/")
    page.wait_for_selector("input[name='username']")
    page.fill("input[name='username']", insta_id)
    page.fill("input[name='password']", insta_pwd)
    page.click("button[type='submit']")
    page.wait_for_timeout(8000)

    # open inbox
    page.goto("https://www.instagram.com/direct/inbox/")
    page.wait_for_timeout(5000)

    try:
        page.click("button:has-text('Not Now')", timeout=3000)
        print("🔕 'Turn on Notifications' dismissed.")
    except TimeoutError:
        pass

    print("✉️ Composing new message...")
    page.click("svg[aria-label='New message']")
    page.wait_for_selector("input[name='queryBox']")
    page.fill("input[name='queryBox']", who)
    time.sleep(2)

    try:
        page.click("input[name='ContactSearchResultCheckbox']", timeout=10000)
    except TimeoutError:
        browser.close()
        p.stop()
        return
    try:
        page.click("div[role='button']:has-text('Chat')", timeout=10000)
    except TimeoutError:
        browser.close()
        p.stop()
        return

    try:
        chatbox = page.locator("div[aria-label='Message'][contenteditable='true']")
        chatbox.click()
        chatbox.fill(what)
        chatbox.press("Enter")
    except Exception as e:
        print(f"⚠️ Could not send message: {e}")

    time.sleep(3)
    browser.close()
    p.stop()   # <--- explicitly stop Playwright loop

    # reconnect your signals
    input_box.returnPressed.disconnect()
    input_box.returnPressed.connect(show_input)
    resume_status_animation()

def get_latest_video(channel_id):
    from datetime import datetime, timezone
    from dateutil import parser

    url = f"https://www.googleapis.com/youtube/v3/search?key={YT_API_KEY}&channelId={channel_id}&order=date&part=snippet&type=video&maxResults=1"
    response = requests.get(url)
    data = response.json()

    if "items" in data and len(data["items"]) > 0:
        video = data["items"][0]
        title = video["snippet"]["title"]
        published_at = video["snippet"]["publishedAt"]
        published_dt = parser.isoparse(published_at).astimezone(timezone.utc)
        return title, published_dt
    return None, None

def check_if_uploaded_today():
    from datetime import datetime, timezone
    list = {}
    string = ""
    today = datetime.now(timezone.utc).date()

    for name, channel_id in yt_channels.items():
        if not channel_id:
            continue
        title, published_dt = get_latest_video(channel_id)

        if published_dt.date() == today:
            list[name] = [title]
        

    if len(list) != 0:
        joined_string = "\n".join(f"{k} - {v}" for k, v in list.items())
        joined_string = "Here is the folks who dropped \n\n" + joined_string
        speak(joined_string)


def checker(yap):
    if variable :
        if "open" in yap:
            if ".com" in yap or "website" in yap:
                OpenWebsite(yap)
            elif "file" in yap:
                OpenFile()
            else:
                OpenSoftware(yap)
        elif "write" in yap or "note" in yap:
                make_a_note()
        elif "screenshot" in yap :
            screenshot()
        elif "channel" in yap :
            youtube_channel(yap)

        elif "make" in yap:
            if "file" in yap :
                make_a_file()
            elif "todo" in yap :
                make_todo()
            elif "appointment" in yap :
                make_appointments()
            else:
                pass
        elif "set" in yap:
            set_a_reminder()
        elif "read" in yap:
            read_file()
        elif "check" in yap :
            if "mail" in yap :
                try:
                    check_mail()
                except:
                    print("no mail entered")
            # elif "youtuber" in yap :
            #     try :
            #         check_if_uploaded_today()
            #     except:
            #         print("no yt api key")
        elif "send" in yap:
            if "mail" in yap :
                try:
                    send_email()
                except:
                    print("no mail found")

            elif "dm" in yap:
                # try:
                    send_dm()
                # except:
                #     print("no insta id/pwd found")
    
        elif "show" in yap :
            if "todo" in yap :
                show_todo()
            elif "appointment" in yap :
                show_appointments()
            else:
                pass
        elif "search" in yap :
            if "youtube" in yap :
                search_yt(yap)
        else:
            try:
                chat(yap)
            except:
                print("no groq key found")
    else:
        try:
            chat(yap)
        except:
            print("no groq key found")

input_box.returnPressed.connect(show_input)

timer.timeout.connect(check_reminder)
timer.start(10000)

def update_time():
    time_display.setText(datetime.datetime.now().strftime("%H:%M:%S │ %Y.%m.%d"))

time_timer = QTimer()
time_timer.timeout.connect(update_time)
time_timer.start(1000)

app.exec_()

