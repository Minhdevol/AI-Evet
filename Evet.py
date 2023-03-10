import time                                                              #thư viện thời gian - 1
import keyboard                                                          #thư viện nhập liệu bàn phím - 2
import random                                                            #Thư viện ngẫu số - 3
import webbrowser                                                        #Thư viện cào web - 4
import subprocess                                                        #Thư viện mở tệp trong ổ đĩa - 5
import os                                                                #Thư viện hệ thống - 6
import pyttsx3                                                           #Thư viện giọng nói -7
import sys                                                               #Thư viện hệ thống - 8
from datetime import datetime                                            #Thư viện thời gian - 9
from datetime import date                                                #Thư viện thời gian - 10
from time import sleep                                                   #Thư viện thời gian - 11
from rich.console import Console                                         #thư viện giao diện - 12
from rich import print                                                   #thư viện giao diện - 13
from rich.prompt import Prompt                                           #thư viện giao diện - 14
from rich.table import Table                                             #thư viện giao diện - 15
from rich import box                                                     #thư viện giao diện - 16
from rich.progress import track                                          #thư viện giao diện - 17
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn #thư viện giao diện - 18
from rich.tree import Tree                                               #thư viện giao diện - 19
from googletrans import Translator                                       #thư viện dịch ngữ  - 20
 
# giọng nói trợ lí
evet = pyttsx3.init()
evet_rate = 220
evet_volume = 0.55
voices = evet.getProperty("voices")
rate = evet.getProperty('rate')
volume = evet.getProperty('volume')
evet.setProperty("voice",voices[1].id)
evet.setProperty("volume", evet_volume)
evet.setProperty("rate", evet_rate)

#Giá trị màu của biến cho chung theo buổi
setimeline = datetime.now().hour
if setimeline >=6 and setimeline<12:#BUỔI SÁNG
    text_output = Console(style="#A142CB")
    line_style = Console(style="#000AA0")
    special_type = Console(style="")
elif setimeline >=12 and setimeline<14:#BUỔI TRƯA
    text_output = Console(style="#B4EA17")
    line_style = Console(style="#FFFF00")
    special_type = Console(style="")
elif setimeline >=14 and setimeline<18:#BUỔI CHIỀU
    text_output = Console(style="#00EEF2")
    line_style = Console(style="#FF4500")
    special_type = Console(style="")
elif setimeline >=18 and setimeline<24:#BUỔI TỐI
    text_output = Console(style="#F1FF18")
    line_style = Console(style="#FF0000")
    special_type = Console(style="")
elif setimeline >=24 and setimeline<6:#BUỔI TỐI
    text_output = Console(style="#A142CB")
    line_style = Console(style="#000AA0")
    special_type = Console(style="")
#Ngẫu nhiên biến chứa nhiều giá trị
symbol_type = ['⌯', '∷', '▸', '▹']#kí tự tin nhắn caption
symtype = random.choice(symbol_type)#ngẫu nhiên kí tự
showing_type = ["⌥ lệnh một chiều/ ▸", "⌥ lệnh bắt buộc/ ▸"]#đa thức tin nhắn
showtype = random.choice(showing_type)#ngẫu nhiên đa thức tin nhắn
respond_while_loop = ['Bạn muốn làm gì tiếp?', 'Hãy thực thi mệnh lệnh tiếp theo!', 'Tôi vẫn còn ở đây, bạn muốn hỏi về điều gì nữa không?', 'Liệu bạn còn có thắc mắc nào nữa không?', 'Hãy tiếp tục hoặc bạn có thể tắt chương trình này!', 'Hãy đưa ra mệnh lệnh tiếp theo!', 'Hãy hỏi hoặc yêu cầu thêm nếu bạn cần, Evet tôi luôn ở đây']
# rwl = random.choice(respond_while_loop)
# speak(f'{rwl}')
sstyle = Console()

#hàm nói in từ từ các biến
def speak(audio):
    line_style.print(f"-" *72)
    audio = f"◈ " + audio + "\n"
    for i in audio:
        text_output.print(i, end = "")
        sleep(0.0005)
    line_style.print(f"-" *72)
    evet.say(audio)
    evet.runAndWait()

#hàm riêng cho tác vụ nói 
def talk(audio):
    evet.say(audio)
    evet.runAndWait()

#hàm dịch ngôn ngữ
def translate():
    option_feed_back_1 = ['Hãy chọn', 'Xin hãy chọn', 'Vui lòng chọn']
    option_feed_back_2 = ['phương thức', 'cách thức', 'loại thức']
    option_feed_back_3 = ['phiên ngữ', 'dịch ngữ']
    opf1 = random.choice(option_feed_back_1)
    opf2 = random.choice(option_feed_back_2)
    opf3 = random.choice(option_feed_back_3)
    trans = Translator()
    speak(f'{opf1} {opf2} {opf3}:')
    sstyle.print(f'[#814BFF bold]Dịch ngôn ngữ khác sang [#E81D0D]tiế[#E8530D]ng V[#E8B60D]iệt[white]「 [#5AC72E]1[/] 」[/]\n[#814BFF bold]Dịch [#E81D0D]tiế[#E8530D]ng V[#E8B60D]iệt [#814BFF bold]sang ngôn ngữ khác[white]「 [#5AC72E]2[/] 」[/]')
    line_style.print("-" * 72)
    option_chosing = Prompt.ask(f"[#B075CB]⦿ ")
    if "1" in option_chosing:
        speak(f"Hãy viết ngôn ngữ bất kì để dịch sang tiếng Việt")
        while True:
            option_translate = Prompt.ask(f"[#F7210B]▩⨽[/] ")
            result = trans.translate(f'{option_translate}', dest='vi')
            if "@-exit" in option_translate:
                rwl = random.choice(respond_while_loop)
                speak(f'{rwl}')
                break
            with Progress("{task.description}",
                            TextColumn(f"\r[#B075CB] Đang dịch.."),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.8)
                    time.sleep(0.00006)
            text_output.print(f" ↳ [#5AC72E]" + result.text)
            line_style.print("-" * 72)
    elif "2" in option_chosing:
        speak(f"{opf1} {opf3} từ tiếng Việt sang ngôn ngữ khác")
        option_languge = Prompt.ask(f"[#B075CB]⦿[/] ")
        line_style.print("-" * 72)
        result = trans.translate(f'{option_languge}', dest='vi')
        if "@en" in option_languge:
            translate_region = "en"
            region_chosing = "tiếng Anh"
            evet.setProperty("voice",voices[2].id)
            evet.setProperty("volume", evet_volume)
            evet.setProperty("rate", evet_rate)
        elif "@ja" in option_languge:
            translate_region = "ja"
            region_chosing = "tiếng Nhật"
            evet.setProperty("voice",voices[3].id)
            evet.setProperty("volume", evet_volume)
            evet.setProperty("rate", evet_rate)
        elif "@ko" in option_languge:
            translate_region = "ko"
            region_chosing = "tiếng Hàn"
            evet.setProperty("voice",voices[4].id)
            evet.setProperty("volume", evet_volume)
            evet.setProperty("rate", evet_rate)
        while True:
            option_translate = Prompt.ask(f"[#F7210B]▩⨽[#B075CB]([#5AC72E]{region_chosing}[/])[/] ")
            result = trans.translate(f'{option_translate}', dest=f'{translate_region}')
            if "@-exit" in option_translate:
                rwl = random.choice(respond_while_loop)
                speak(f'{rwl}')
                break
            with Progress("{task.description}",
                            TextColumn(f"\r[#B075CB] Đang dịch.."),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.8)
                    time.sleep(0.00006)
            text_output.print(" " * 12 + f" ↳ [#5AC72E]" + result.text)
            evet.say(result.text)
            evet.runAndWait()
            line_style.print("-" * 72)
            evet.setProperty("voice",voices[1].id)
    else:
        option_choising = ['⊑ LƯU Ý: đây là lệnh mà chỉ có thể trả lời', '⊑ Vui lòng trả lời với vài lệnh duy nhất', '⊑ Hãy chỉ nhập với các lệnh']
        oc = random.choice(option_choising)
        speak(f'{oc} theo lệnh được cho!')         

#hàm chạy tác vụ của trên hệ thống (chỉ với window):
def systemW():
    option_feed_back_1 = ['Vui lòng', 'Hãy nhập', 'Hãy']
    option_feed_back_2 = ['nhấn các tổ hợp lệnh', 'các phím tắt', 'các nút', 'các phím']
    option_feed_back_3 = ['để chạy tác vụ hệ thống', 'để chạy tác vụ', 'để tinh chỉnh']
    option_feed_back_4 = ['Đây có', 'Đây là', 'Các']
    option_feed_back_5 = ['các tác vụ', 'tác vụ', 'chức năng']
    option_feed_back_6 = ['','','hiện tại', 'đang có lúc này']
    opf1 = random.choice(option_feed_back_1)
    opf2 = random.choice(option_feed_back_2)
    opf3 = random.choice(option_feed_back_3)
    opf4 = random.choice(option_feed_back_4)
    opf5 = random.choice(option_feed_back_5)
    opf6 = random.choice(option_feed_back_6)
    speak(f"{opf1} {opf2} {opf3}!")
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('1'):#CTRL + 1 =>Thông tin tài khoản hệ thống
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:yourinfo")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('2'):#CTRL + 2 =>Thông tin máy hệ thống
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:about")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('3'):#CTRL + 3 =>Cài đặt
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:controlcenter")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('4'):#CTRL + 4 =>Ứng dụng và gói đã tải
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:appsfeatures")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('5'):#CTRL + 5 =>Tắt - khởi chạy ứng dụng ngầm sau khi khởi động máy
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:startupappsrun")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('6'):#CTRL + 6 =>Kết nối bluetooth
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:bluetooth")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('7'):#CTRL + 7 =>Hiệu chỉnh touchpad
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:devices-touchpad")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('8'):#CTRL + 8 =>Bật tắt kính lúp
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:easeofaccess-magnifier")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('9'):#CTRL + 9 =>Cá nhân hóa giao diện
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:personalization")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('m'):#CTRL + m =>Kết nối điện thoại
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings:mobile-devices-addphone-direct")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('w'):#CTRL + w =>Wifi
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-availablenetworks:")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('d'):#CTRL + d =>Kết nối màn hình ngoài
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-settings-displays-topology:projection")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('p'):#CTRL + p =>Window defencer
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("windowsdefender:")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):#CTRL + c =>Chụp cắt màn hình
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-screenclip:")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):#CTRL + q =>Bảng trung tâm hành động
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("ms-actioncenter:")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('o'):#CTRL + o =>Tinh chỉnh ánh sáng, âm thanh, ...
            with Progress("{task.description}",
                            TextColumn(f""),
                            SpinnerColumn()) as progress:
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.5)
                    time.sleep(0.00006)
            line_style.print("-" * 72)
            os.startfile("mblctr")
        # elif keyboard.is_pressed('ctrl') and keyboard.is_pressed(''):#CTRL +
        #     with Progress("{task.description}",
        #                     TextColumn(f""),
        #                     SpinnerColumn()) as progress:
        #         loading_application = progress.add_task("", total=100)
        #         while not progress.finished:
        #             progress.update(loading_application, advance=1.5)
        #             time.sleep(0.00006)
        #     line_style.print("-" * 72)
        #     os.startfile("")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('capslock'):
            speak(f'{opf4} {opf5} {opf6} là:')
            sstyle.print(f'「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/]thông tin tài khoản      | 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/]Thông tin máy tính')
            sstyle.print(f'「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/]Cài đặt                  | 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]4[/] 」[#F48E2D]⌥►[/]Ứng dụng và gói đã tải')
            sstyle.print(f'「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]5[/] 」[#F48E2D]⌥►[/]ứng dụng chạy ngầm       | 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]6[/] 」[#F48E2D]⌥►[/]Kết nối Bluetooth')
            sstyle.print(f'「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]7[/] 」[#F48E2D]⌥►[/]Hiệu chỉnh touchpad      | 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]8[/] 」[#F48E2D]⌥►[/]Bật tắt kính lúp')
            sstyle.print(f'「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]9[/] 」[#F48E2D]⌥►[/]Cá nhân hóa giao diện    | 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]M[/] 」[#F48E2D]⌥►[/]Kết nối điện thoại')
            sstyle.print(f'「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]W[/] 」[#F48E2D]⌥►[/]Wifi                     | 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]D[/] 」[#F48E2D]⌥►[/]Kết nối màn hình ngoài')
            sstyle.print(f'「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]P[/] 」[#F48E2D]⌥►[/]Window Defencer          | 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]C[/] 」[#F48E2D]⌥►[/]Chụp cắt màn hình')
            sstyle.print(f'「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]Q[/] 」[#F48E2D]⌥►[/]Bảng trung tâm hành động | 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]O[/] 」[#F48E2D]⌥►[/]Tinh chỉnh chung')
            line_style.print("-" * 72)
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('esc'):
            rwl = random.choice(respond_while_loop)
            speak(f'{rwl}')
            break

#hàm chạy chương trình trên máy tính
def OASTEP():
    option_feed_back_1 = ["Hãy nhập", "Hãy", "Nhập", "Vui lòng"]
    option_feed_back_2 = ["phím tắt", "cụm phím", "tổ hợp nút", "tổ hợp phím", "các phím tắt"]
    option_feed_back_3 = ["để mở chương trình", "để chạy chương trình", "để chạy file"]
    option_feed_back_4 = ['đang mở', 'đang chạy', 'đang khởi chạy', 'đang bật']
    option_feed_back_5 = ['Lệnh hiện có', 'Các tác vụ hiện có', 'Các chương trình và tác vụ hiện có']
    opfb1 = random.choice(option_feed_back_1)
    opfb2 = random.choice(option_feed_back_2)
    opfb3 = random.choice(option_feed_back_3)
    opfb4 = random.choice(option_feed_back_4)
    opfb5 = random.choice(option_feed_back_5)
    speak(f"{opfb1} {opfb2} {opfb3}!")
    while True:
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#APPLICATION FOR OFFICER
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('1'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#E15311 bold]PowerPoint[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("POWERPNT.EXE")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('2'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#2D7E27 bold]Excel[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("Excel.exe")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('3'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#2E55AB bold]Word[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("Word.exe")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#APPLICATION FOR EDITOR
        elif keyboard.is_pressed('alt') and keyboard.is_pressed('1'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#41BCEF bold]Photoshopp[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("Photoshop.exe")
        elif keyboard.is_pressed('alt') and keyboard.is_pressed('2'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#ED5699 bold]Premiere Pro[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("Adobe-Premiere-Pro.exe")
        elif keyboard.is_pressed('alt') and keyboard.is_pressed('3'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#4D5ECF bold]After Effect[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("AfterFX.exe")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#APPLICATION MULTIPLE WORKOUT
        elif keyboard.is_pressed('space') and keyboard.is_pressed('1'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#3772F9]G[/][#DC1A1A]o[/][#E2B21C]o[/][#3772F9]g[/][#28D00E]l[/][#DC1A1A]e[/] [#3576F0]Chrome[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("chrome.exe")
        elif keyboard.is_pressed('space') and keyboard.is_pressed('2'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#0FB4E6 bold]Edge[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("msedge.exe")
        elif keyboard.is_pressed('space') and keyboard.is_pressed('3'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#8986E2 bold]Discord[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("Update.exe")
        elif keyboard.is_pressed('space') and keyboard.is_pressed('4'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#178AF6 bold]Zalo[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("Zalo.exe")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#APPLICATION FOR ANOTHER JOB WITH WINDOW APP
        elif keyboard.is_pressed('-') and keyboard.is_pressed('1'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#1D6DA8 bold]Outlook[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("outlookmail://home/")
        elif keyboard.is_pressed('-') and keyboard.is_pressed('2'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#7332EA i]Microsoft Store[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("ms-windows-store://home/")
        elif keyboard.is_pressed('-') and keyboard.is_pressed('3'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#A9A5B2 bold]Máy tính[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("calculator://home/")
        elif keyboard.is_pressed('-') and keyboard.is_pressed('4'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#005DCA bold]Lịch[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("outlookcal://home/")
        elif keyboard.is_pressed('-') and keyboard.is_pressed('5'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#E33804 bold]Đồng hồ[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("ms-clock://home/")
        elif keyboard.is_pressed('-') and keyboard.is_pressed('6'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#814BFF bold]Photos[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("ms-photos://home/")
        elif keyboard.is_pressed('-') and keyboard.is_pressed('7'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#E35604]Snipp[/][#E3B104]ing Tool IMG[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("ms-ScreenSketch://home/")
        elif keyboard.is_pressed('-') and keyboard.is_pressed('8'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#E35604]Snipp[/][#76E304]ing Tool VID[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("ms-screenclip://home/")
        elif keyboard.is_pressed('-') and keyboard.is_pressed('9'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#C5CAC1]Thời[/][#82FFFF]tiết[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("bingweather://home/")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#APPLICATION FOR GAME
        #Bổ sung sau "3"
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#APPLICATION FOR CODING STUFF
        elif keyboard.is_pressed('tab') and keyboard.is_pressed('1'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#157CDC bold bold]Visual Studio Code[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("Code.exe")
        elif keyboard.is_pressed('tab') and keyboard.is_pressed('2'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#70BC3F bold]Android Studio[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("studio64.exe")
        elif keyboard.is_pressed('tab') and keyboard.is_pressed('3'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#9331A0 bold]Github Desktop[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("GitHubDesktop.exe")
        elif keyboard.is_pressed('tab') and keyboard.is_pressed('4'):
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[#FF22B3]Co[/][#ED5FEB]din[#D5775B]g SPA[/][#FDF040]CE[/] [#7641F7]{opfb4}[/]')
                loading_application = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_application, advance=1.3)
                    time.sleep(0.0006)
            line_style.print("-" * 72)
            os.startfile("CODING PROJECT")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TÁC VỤ CHO HỆ THỐNG, TẮT CHƯƠNG TRÌNH, HƯỚNG DẪN
        elif keyboard.is_pressed('esc') and keyboard.is_pressed('tab'):
            sstyle.print(f'{symtype} [#24DE73 bold]{opfb5}:[/]')
            sstyle.print(f'[#979F9A]↳[/] [#E0643C i]Văn phòng:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]1[/] 」     │    [#979F9A]↳[/] [#E0643C i]Thiết ảnh video:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]2[/] 」')
            sstyle.print(f' 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/] [#E15311 bold]PowerPoint[/]    │     「[#814BFF bold]ALT[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/] [#41BCEF bold]Photoshopp[/]')
            sstyle.print(f' 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/] [#2D7E27 bold]Excel[/]         │     「[#814BFF bold]ALT[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/] [#ED5699 bold]Premiere Pro[/]')
            sstyle.print(f' 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/] [#2E55AB bold]Word[/]          │     「[#814BFF bold]ALT[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/] [#4D5ECF bold]After Effect[/]')
            sstyle.print(f' 「 ... 」                     │     「 ... 」')
            sstyle.print(f'[#979F9A]↳[/] [#E0643C i]Đa công cụ:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]3[/] 」    │    [#979F9A]↳[/] [#E0643C i]Lập trình:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]4[/] 」')
            sstyle.print(f' 「[#814BFF bold]SPACE[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/] [#3772F9]G[/][#DC1A1A]o[/][#E2B21C]o[/][#3772F9]g[/][#28D00E]l[/][#DC1A1A]e[/]       │     「[#814BFF bold]TAB[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/] [#157CDC bold bold]Visual Studio Code[/]')
            sstyle.print(f' 「[#814BFF bold]SPACE[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/] [#0FB4E6 bold]Edge[/]         │     「[#814BFF bold]TAB[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/] [#70BC3F bold]Android Studio[/]')
            sstyle.print(f' 「[#814BFF bold]SPACE[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/] [#8986E2 bold]Discord[/]      │     「[#814BFF bold]TAB[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/] [#9331A0 bold]Github Desktop[/]')
            sstyle.print(f' 「[#814BFF bold]SPACE[/] [#5AC72E bold]+[/] [#814BFF bold]4[/] 」[#F48E2D]⌥►[/] [#178AF6 bold]Zalo[/]         │     「[#814BFF bold]TAB[/] [#5AC72E bold]+[/] [#814BFF bold]4[/] 」[#F48E2D]⌥►[/] [#FF22B3]CO[/][#ED5FEB]DIN[#D5775B]G SPA[/][#FDF040]CE[/]')
            sstyle.print(f' 「 ... 」                     │     「 ... 」')
            sstyle.print(f'[#979F9A]↳[/] [#E0643C i]Microsoft:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]5[/] 」')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]1[/]」[#F48E2D]⌥►[/] [#1D6DA8 bold]Outlook[/]           ╎     「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]6[/]」[#F48E2D]⌥►[/] [#814BFF bold]Photos[/]')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]2[/]」[#F48E2D]⌥►[/] [#7332EA i]Microsoft Store[/]   ╎     「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]7[/]」[#F48E2D]⌥►[/] [bold][#E35604]Snippi[/][#E3B104]ng Tool IMG[/]')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]3[/]」[#F48E2D]⌥►[/] [#A9A5B2 bold]Máy tính[/]          ╎     「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]8[/]」[#F48E2D]⌥►[/] [bold][#E35604]Snipp[/][#76E304]ing Tool VID[/]')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]4[/]」[#F48E2D]⌥►[/] [#005DCA bold]Lịch[/]              ╎     「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]9[/]」[#F48E2D]⌥►[/] [#C5CAC1]Weat[/][#82FFFF]her[/]')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]5[/]」[#F48E2D]⌥►[/] [#E33804 bold]Đồng hồ[/]           ╎     「 ... 」')
            line_style.print("-" * 72)
        elif keyboard.is_pressed('esc') and keyboard.is_pressed('1'):
            sstyle.print(f'[#979F9A]↳[/] [#E0643C i]Văn phòng:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]1[/] 」')
            sstyle.print(f' 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/] [#E15311 bold]PowerPoint[/]')
            sstyle.print(f' 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/] [#2D7E27 bold]Excel[/]')
            sstyle.print(f' 「[#814BFF bold]CRTL[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/] [#2E55AB bold]Word[/]')
            sstyle.print(f' 「 ... 」')
            line_style.print("-" * 72)
        elif keyboard.is_pressed('esc') and keyboard.is_pressed('2'):
            sstyle.print(f'[#979F9A]↳[/] [#E0643C i]Thiết ảnh video:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]2[/] 」')
            sstyle.print(f' 「[#814BFF bold]ALT[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/] [#41BCEF bold]Photoshopp[/]')
            sstyle.print(f' 「[#814BFF bold]ALT[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/] [#ED5699 bold]Premiere Pro[/]')
            sstyle.print(f' 「[#814BFF bold]ALT[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/] [#4D5ECF bold]After Effect[/]')
            sstyle.print(f' 「 ... 」')
            line_style.print("-" * 72)
        elif keyboard.is_pressed('esc') and keyboard.is_pressed('3'):
            sstyle.print(f'[#979F9A]↳[/] [#E0643C i]Đa công cụ:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]3[/] 」')
            sstyle.print(f' 「[#814BFF bold]SPACE[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/] [#2041BC]G[/][#DC1A1A]o[/][#E2B21C]o[/][#2041BC]g[/][#28D00E]l[/][#DC1A1A]e[/]')
            sstyle.print(f' 「[#814BFF bold]SPACE[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/] [#0FB4E6 bold]Edge[/]')
            sstyle.print(f' 「[#814BFF bold]SPACE[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/] [#8986E2 bold]Discord[/]')
            sstyle.print(f' 「[#814BFF bold]SPACE[/] [#5AC72E bold]+[/] [#814BFF bold]4[/] 」[#F48E2D]⌥►[/] [#178AF6 bold]Zalo[/]')
            sstyle.print(f' 「 ... 」')
            line_style.print("-" * 72)
        elif keyboard.is_pressed('esc') and keyboard.is_pressed('4'):
            sstyle.print(f'[#979F9A]↳[/] [#E0643C i]Lập trình:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]4[/] 」')
            sstyle.print(f' 「[#814BFF bold]TAB[/] [#5AC72E bold]+[/] [#814BFF bold]1[/] 」[#F48E2D]⌥►[/] [#157CDC bold bold]Visual Studio Code[/]')
            sstyle.print(f' 「[#814BFF bold]TAB[/] [#5AC72E bold]+[/] [#814BFF bold]2[/] 」[#F48E2D]⌥►[/] [#70BC3F bold]Android Studio[/]')
            sstyle.print(f' 「[#814BFF bold]TAB[/] [#5AC72E bold]+[/] [#814BFF bold]3[/] 」[#F48E2D]⌥►[/] [#9331A0 bold]Github Desktop[/]')
            sstyle.print(f' 「[#814BFF bold]TAB[/] [#5AC72E bold]+[/] [#814BFF bold]4[/] 」[#F48E2D]⌥►[/] [#FF22B3]Co[/][#ED5FEB]din[#D5775B]g SPA[/][#FDF040]CE[/]')
            sstyle.print(f' 「 ... 」')
            line_style.print("-" * 72)
        elif keyboard.is_pressed('esc') and keyboard.is_pressed('5'):
            sstyle.print(f'[#979F9A]↳[/] [#E0643C i]Microsoft:[/] 「 [#4568DF bold]ESC[/] + [#4568DF bold]5[/] 」')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]1[/]」[#F48E2D]⌥►[/] [#1D6DA8 bold]Outlook[/]         ╎     「 [#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]6[/]」[#F48E2D]⌥►[/] [#814BFF bold]Photos[/]')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]2[/]」[#F48E2D]⌥►[/] [#7332EA i]Microsoft Store[/] ╎     「 [#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]7[/]」[#F48E2D]⌥►[/] [bold][#E35604]Snipp[/][#E3B104]ing Tool IMG[/]')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]3[/]」[#F48E2D]⌥►[/] [#A9A5B2 bold]Máy tính[/]        ╎     「 [#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]8[/]」[#F48E2D]⌥►[/] [bold][#E35604]Snipp[/][#76E304]ing Tool VID[/]')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]4[/]」[#F48E2D]⌥►[/] [#005DCA bold]Lịch[/]            ╎     「 [#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]9[/]」[#F48E2D]⌥►[/] [#C5CAC1]Weat[/][#82FFFF]her[/]')
            sstyle.print(f' 「[#814BFF bold]-[/] [#5AC72E bold]+[/] [#814BFF bold]5[/]」[#F48E2D]⌥►[/] [#E33804 bold]Đồng hồ[/]         ╎     「 ... 」')
            line_style.print("-" * 72)
        elif keyboard.is_pressed('esc') and keyboard.is_pressed('o'):
            rwl = random.choice(respond_while_loop)
            speak(f'{rwl}')
            return
            
#Tìm kiếm dữ liệu
def searching_data():
    otp1 = ['Hãy nhập', 'Nhập', 'Gõ']
    otp2 = ['từ khóa', 'dữ liệu', 'cụm chữ']
    otp3 = ['để truy xuất website', 'để tìm kiếm', 'để truy cập']
    otp4 = ['Đang truy xuất', 'Đang tìm dữ liệu', 'Đang tìm kiếm']
    otp5 = ['lựa chọn', 'muốn', 'chọn']
    otp6 = ['cách', 'phương thức', 'cách thức', 'kiểu']
    opf1 = random.choice(otp1)
    opf2 = random.choice(otp2)
    opf3 = random.choice(otp3)
    opf4 = random.choice(otp4)
    opf5 = random.choice(otp5)
    opf6 = random.choice(otp6)
    speak(f"{opf1} {opf2} {opf3}")
    typing_data = "[..]"
    while True:
        link_prompt = Prompt.ask(f"[red]{typing_data}").lower()
        line_style.print(f"━" *72)
        srch = "Tìm kiếm"
        list_option = Tree(f'[#FFF997]{symtype} Bạn {opf5} [u bold #FF44E0]{opf6}[/] nào dưới đây:[/]')
        google_list = Tree("[bold][#2041BC]G[/][#DC1A1A]o[/][#E2B21C]o[/][#2041BC]g[/][#28D00E]l[/][#DC1A1A]e[/]")
        youtube_list = Tree("[bold]You[#D52B3A]tube[/]")
        list_option.add(f'[yellow]Hủy {srch} [/][red]⌥ @c[/]') 
        google_list.add(f"[purple]{srch} [u]tất cả[/]     [green]⌥ @all[/]    │   [purple]{srch} [u]video[/]        [green]⌥ @vid[/]\n[purple]{srch} [u]hình ảnh[/]   [green]⌥ @img[/]    │   [purple]{srch} [u]báo chí[/]      [green]⌥ @news[/]\n[purple]{srch} [u]sách[/]       [green]⌥ @bk[/]     │   [purple]{srch} [u]mua sắm[/]      [green]⌥ @sp[/]\n[purple]{srch} [u]chuyến bay[/] [green]⌥ @pl[/]     │   ▫ ▫ ▫")
        youtube_list.add(f"[purple]{srch} [u]youtube[/]    [green]⌥ @yt[/]")  
        sstyle.print(list_option)
        sstyle.print(google_list)
        sstyle.print(youtube_list)
        line_style.print(f"-" *72)
        talk(f'Bạn {opf5} {opf6} nào dưới đây:')
        option_prompt = Prompt.ask(f"[#B075CB]⦿[/] [red]{showtype}").lower()
        line_style.print(f"━" *72)
        if "@all" in option_prompt:
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[red]{opf4}[/] từ [cyan bold]"{link_prompt}"[/]')
                loading_searching = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_searching, advance=1.1)
                    time.sleep(0.0006)
            webbrowser.open(f"https://www.google.com/search?q={link_prompt}")
            line_style.print(f"-" *72)
        elif "@vid" in option_prompt:
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[red]{opf4}[/] từ [cyan bold]"{link_prompt}"[/]')
                loading_searching = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_searching, advance=1.1)
                    time.sleep(0.0006)
            webbrowser.open(f"https://www.google.com/search?q={link_prompt}&source=lnms&tbm=vid")
            line_style.print(f"-" *72)
        elif "@img" in option_prompt:
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[red]{opf4}[/] từ [cyan bold]"{link_prompt}"[/]')
                loading_searching = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_searching, advance=1.1)
                    time.sleep(0.0006)
            webbrowser.open(f"https://www.google.com/search?q={link_prompt}&source=lnms&tbm=isch")
            line_style.print(f"-" *72)
        elif "@news" in option_prompt:
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[red]{opf4}[/] từ [cyan bold]"{link_prompt}"[/]')
                loading_searching = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_searching, advance=1.1)
                    time.sleep(0.0006)
            webbrowser.open(f"https://www.google.com/search?q={link_prompt}&source=lmns&tbm=nws")
            line_style.print(f"-" *72)
        elif "@bk" in option_prompt:
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[red]{opf4}[/] từ [cyan bold]"{link_prompt}"[/]')
                loading_searching = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_searching, advance=1.1)
                    time.sleep(0.0006)
            webbrowser.open(f"https://www.google.com/search?q={link_prompt}&source=lmns&tbm=bks")
            line_style.print(f"-" *72)
        elif "@sp" in option_prompt:
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[red]{opf4}[/] từ [cyan bold]"{link_prompt}"[/]')
                loading_searching = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_searching, advance=1.1)
                    time.sleep(0.0006)
            webbrowser.open(f"https://www.google.com/search?q={link_prompt}&source=lmns&tbm=shop")
            line_style.print(f"-" *72)
        elif "@pl" in option_prompt:
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[red]{opf4}[/] [cyan bold]"{link_prompt}"[/]')
                loading_searching = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_searching, advance=1.1)
                    time.sleep(0.0006)
            webbrowser.open(f"https://www.google.com/search?q={link_prompt}&source=lmns&tbm=flm")
            line_style.print(f"-" *72)
        elif "@yt" in option_prompt:
            with Progress("{task.description}",
                            SpinnerColumn(),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),) as progress:
                sstyle.print(f'[red]{opf4}[/] từ [cyan bold]"{link_prompt}"[/]')
                loading_searching = progress.add_task("", total=100)
                while not progress.finished:
                    progress.update(loading_searching, advance=1.1)
                    time.sleep(0.0006)
            webbrowser.open(f"https://www.youtube.com/results?search_query={link_prompt}")
            line_style.print(f"-" *72)
        elif "@c" in option_prompt:
            rwl = random.choice(respond_while_loop)
            speak(f'{rwl}')
            break
        else:
            option_choising = ['⊑ LƯU Ý: đây là lệnh mà chỉ có thể trả lời', '⊑ Vui lòng trả lời với vài lệnh duy nhất', '⊑ Hãy chỉ nhập với các lệnh']
            oc = random.choice(option_choising)
            speak(f'{oc} theo lệnh được cho!')

#hàm khai báo thời gian trong ngày
def timecouns():
    line_style.print(f"-" *72 + "\n❖")
    hours = datetime.now().strftime("%I")
    minute = datetime.now().strftime("%M")
    time_re = ['Ngay bây giờ là', 'Bây giờ là', 'Hiện giờ là']
    tr = random.choice(time_re)
    times = Table(title="", box = box.MARKDOWN)
    times.add_column("Giờ", justify="center", width=10)
    times.add_column("Phút", justify="center", width=10)
    times.add_row(f"[#E9E619][i]{hours}", f"[#E9E619][i]{minute}")
    sstyle.print(times)
    line_style.print(f"-" *72)
    audio = f"{tr} {hours} giờ {minute} phút"
    talk(audio)

#hàm khai báo ngày
def daycouns():
    line_style.print(f"-" *72 + "\n❖")
    days = datetime.now()
    day = int(days.strftime("%d"))
    time_1 = day - 2
    time_2 = day - 1
    time_3 = day - 0
    time_4 = day + 1
    time_5 = day + 2
    daystyle = Table(title="", box = box.SIMPLE_HEAD)
    daystyle.add_column("NGÀY", justify="center", style="#2F4037", width=5)
    daystyle.add_column("", justify="center", style="#2F4037", width=5)
    daystyle.add_column("", justify="center", style="#2F4037", width=5)
    daystyle.add_column("", justify="center", style="#2F4037", width=5)
    daystyle.add_column("", justify="center", style="#2F4037", width=5)
    daystyle.add_row(f"{time_1}",f"{time_2}",f"[#9278CD][bold][u]{time_3}",f"{time_4}",f"{time_5}")
    sstyle.print(daystyle)
    date_re = ['Hôm nay là', 'Nay là']
    dr = random.choice(date_re)
    speak(f"{dr} ngày {time_3}")  

#hàm khai báo thứ
def weekcouns():
    weekdays = datetime.now().strftime("%A")
    date_re = ['Hôm nay là', 'Nay là']
    dr = random.choice(date_re)
    days = Table(title="", box = box.SIMPLE)
    line_style.print(f"-" *72 + "\n❖")
    days.add_column("THỨ", justify="center", style="#1C5635 dim")
    days.add_column("", justify="center", style="#1C5635 dim")
    days.add_column("", justify="center", style="#1C5635 dim")
    days.add_column("", justify="center", style="#1C5635 dim")
    days.add_column("", justify="center", style="#1C5635 dim")
    days.add_column("", justify="center", style="#1C5635 dim")
    days.add_column("", justify="center", style="#1C5635 dim")
    if "Monday" in weekdays:
        days.add_row("[#00FF33][bold][u]Hai", "Ba", "Tư", "Năm", "Sáu", "Bảy", "Chủ Nhật")
        sstyle.print(days)
        speak(f"{dr} thứ hai!")
    elif "Tuesday" in weekdays:
        days.add_row("Hai", "[#0D70FF][bold][u]Ba", "Tư", "Năm", "Sáu", "Bảy", "Chủ Nhật")
        sstyle.print(days)
        speak(f"{dr} thứ ba")
    elif "Wednesday" in weekdays:
        days.add_row("Hai", "Ba", "[#FF26DC][bold][u]Tư", "Năm", "Sáu", "Bảy", "Chủ Nhật")
        sstyle.print(days)
        speak(f"{dr} thứ tư")
    elif "Thursday" in weekdays:
        days.add_row("Hai", "Ba", "Tư", "[#FFBA1A][bold][u]Năm", "Sáu", "Bảy", "Chủ Nhật")
        sstyle.print(days)
        speak(f"{dr} thứ năm")
    elif "Friday" in weekdays:
        days.add_row("Hai", "Ba", "Tư", "Năm", "[#3800FF][bold][u]Sáu", "Bảy", "Chủ Nhật")
        sstyle.print(days)
        speak(f"{dr} thứ sáu")
    elif "Saturday" in weekdays:
        days.add_row("Hai", "Ba", "Tư", "Năm", "Sáu", "[##FD2902][bold][u]Bảy", "Chủ Nhật")
        sstyle.print(days)
        speak(f"{dr} thứ bảy")
    elif "Sunday" in weekdays:
        days.add_row("Hai", "Ba", "Tư", "Năm", "Sáu", "Bảy", "[#00FFEF][bold][u]Chủ Nhật")
        sstyle.print(days)
        speak("Hôm nay là chủ nhật")

#hàm khai báo tháng  
def monthcoun():
    month = datetime.now().strftime("%B")
    date_re = ['Hôm nay là', 'Nay là']
    dr = random.choice(date_re)
    months = Table(title="", box = box.HORIZONTALS, show_lines=True)
    line_style.print(f"-" *72 + "\n❖")
    months.add_column("", justify="center", style="dim #1C5635")
    months.add_column("", justify="center", style="dim #1C5635")
    months.add_column("", justify="center", style="dim #1C5635")
    months.add_column("THÁNG", justify="center", style="dim #1C5635")
    if "January" in month:
        months.add_row("[#FFD800][bold][u]Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng một!")
    elif "February" in month:
        months.add_row("Một - 1", "[#0051FF][bold][u]Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng hai")
    elif "March" in month:
        months.add_row("Một - 1", "Hai - 2", "[#0FFF00][bold][u]Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng ba")
    elif "April" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "[#002AB7][bold][u]Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng tư")
    elif "May" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("[#00B76F][bold][u]Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng năm")
    elif "June" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "[#B70040][bold][u]Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng sáu")
    elif "July" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "[#B73200][bold][u]Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng bảy")
    elif "August" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "[#FF3F25][bold][u]Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng tám")
    elif "September" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("[#6025FF][bold][u]Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng chín")
    elif "October" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "[#8EE541][bold][u]Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng mười")
    elif "November" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "[#F7FE2D][bold][u]Mười Một - 11", "Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng mười một")
    elif "December" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "[#F82DFE][bold][u]Mười Hai - 12")
        sstyle.print(months)
        speak(f"{dr} tháng mười hai")
        
#hàm khai báo năm
def yearscoun():
    line_style.print(f"-" *72 + "\n❖")
    year = datetime.now()
    years = int(year.strftime("%Y"))
    time_1 = years - 2
    time_2 = years - 1
    time_3 = years - 0
    time_4 = years + 1
    time_5 = years + 2
    date_re = ['Hôm nay là', 'Nay là']
    dr = random.choice(date_re)
    year = Table(title="", box = box.SIMPLE_HEAD)
    year.add_column("Năm", justify="center", style="#2F4037")
    year.add_column("", justify="center", style="#2F4037")
    year.add_column("", justify="center", style="#2F4037")
    year.add_column("", justify="center", style="#2F4037")
    year.add_column("", justify="center", style="#2F4037")
    year.add_row(f"{time_1}",f"{time_2}",f"[#9278CD][bold][u]{time_3}",f"{time_4}",f"{time_5}")
    sstyle.print(year)
    speak(f"{dr} năm {time_3}")

#hàm tắt máy tính
def shutdownprograms():
    while True:
        option_choising_1 = ['Đây là tác vụ shutdown máy ⍝  bạn thực sự muốn thực hiện nó không?',  'Liệu bạn có muốn shutdown máy ⍝  không?', 'Tác vụ shutdown ⍝  được khởi chạy bạn muốn tắt hay không?']
        oc1 = random.choice(option_choising_1)
        speak(f"{oc1}\n                ⌈ có ⌋ hoặc ⌈ không ⌋")
        me = Prompt.ask(f"[#B075CB]⦿ [red]{showtype} ").lower()
        if me == "có":
            os.system("shutdown /s /t 15")
            keeping = ['HÃY TẮT ⌧ CÁC TÁC VỤ CÒN ĐANG CHẠY', 'HÃY TẮT ⌧ CÁC ỨNG DỤNG CÒN ĐANG CHẠY', 'TẮT ⊗ CÁC TÁC VỤ CÒN ĐANG HOẠT ĐỘNG', 'BẠN NÊN TẮT ⊗ CÁC ỨNG DỤNG CÒN HOẠT ĐỘNG']
            kpp = random.choice(keeping)
            speak(f'LƯU Ý: "             {kpp}             \n{symtype}                           MÁY TÍNH SẼ TẮT ⤬ TRONG 15 GIÂY  "')
            break
        elif me == "không":
            rwl = random.choice(respond_while_loop)
            speak(f'{rwl}')
            break
        else:
            option_choising_2 = ['⊑ LƯU Ý: đây là lệnh mà chỉ có thể trả lời là ', '⊑ Vui lòng trả lời với hai lệnh duy nhất là ', '⊑ Hãy chỉ nhập với hai lệnh đã cho là ']
            oc2 = random.choice(option_choising_2)
            speak(f"{oc2} ⌈ có ⌋ hoặc ⌈ không ⌋")

#hàm tín hiệu kết thúc
def bye():
    hour = datetime.now().hour
    goobye = ['Tạm biệt', 'Goodbye', 'Chào', 'Bye bye']
    gb = random.choice(goobye)
    if hour >=6 and hour<12:
        speak("Chúc bạn buổi sáng tốt lành ☼")
        print(f"{gb}")
    elif hour >=12 and hour<14:
        speak("Chúc bạn buổi trưa tốt lành ☼")
        print(f"{gb}")
    elif hour >=14 and hour<18:
        speak("Chúc bạn buổi chiều tốt lành ☼")
        print(f"{gb}")
    elif hour >=18 and hour<24:
        speak("Chúc bạn buổi tối tốt lành ☾")
        print(f"{gb}")

#hàm mở đầu giới thiệu
def wellcome():
    intro = "[\]=>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|\n|  ██▓███▒█    ██       ██    ██▒█▓▓▓█    ███░██▓████                   |\n|  ▒██          ▓█     ▒▒     █▒█             █▒▒                       |\n|  ███▓▒██       █▒   ▒█      █░█▒▒██         █▓█                       |\n|  ▒█▒            ██ █▓       ▒██             ▒██ AI product            |\n|  █░████▓▓        ██▒        █▒▒██░▒█        ▓░█  「 by ⌨  MINHDEVOL 」|\n|<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<="
    hii = ['Evet đây, bạn cần hỗ trợ gì?', 'Tôi là Evet, bạn cần giúp gì?', 'AI EVET đây, bạn cần gì?', 'Có vẻ bạn cần giúp đỡ, tôi là Evet hãy hỏi tôi về vấn đề của bạn?', 'Tôi là Evet, tôi sẽ giúp bạn bằng khả năng của mình.']
    hi = random.choice(hii)
    hour = datetime.now().hour
    if hour >=6 and hour<12:
        print(f"[#228B22]{intro}[\]")
        speak(f"Chào buổi sáng ☼\n{symtype} {hi}")
    elif hour >=12 and hour<14:
        print(f"[#2F3BCF]{intro}[\]")
        speak(f"Chào buổi trưa ☼\n{symtype} {hi}")
    elif hour >=14 and hour<18:
        print(f"[#E56100]{intro}[\]")
        speak(f"Chào buổi chiều ☼\n{symtype} {hi}")
    elif hour >=18 and hour<24:
        print(f"[#EE2727]{intro}[\]")
        speak(f"Chào buổi tối ⬤\n{symtype} {hi}")
    elif hour >=24 and hour<6:
        print(f"[#CE65EC]{intro}[\]")
        speak(f"Chào buổi sáng ⬤\n{symtype} {hi}")

#----------------------------------------------------------------------------------------------------------------------------------------------#

# Nơi gán hàm và các câu lệnh cũng như vòng lặp để khởi động chương trình
if __name__ =="__main__":
    wellcome() #lời chào
    while True:
        you = Prompt.ask("[#B075CB]⦿ ").lower() #Phương thức tương tác
        if "@sd" in you:#kết thúc chương trình
            bye()
            break
        elif "giờ" in you:#trình báo thời gian trong ngày
            timecouns()
        elif "thứ" in you:#trình thứ
            weekcouns()
        elif "ngày" in you:#trình báo ngày
            daycouns()
        elif "tháng" in you:#trình bấo tháng
            monthcoun()
        elif "năm" in you:#trình báo năm
            yearscoun()
        elif "tắt laptop" in you: #chế độ tắt máy tính
            shutdownprograms()
        elif "@oa" in you:
            OASTEP()
        elif "@tran" in you:
            translate()
        elif "@srch" in you:
            searching_data()
        elif "@sys" in you:
            systemW()
        else:#xử lí dữ liệu không có chức năng hoặc từ khóa {vô nghĩa}
            respond_data = ["Dữ liệu", "Từ khóa", "Cụm chữ", "Chức năng", "Nhập liệu"]
            respond_feed_back_1 = ["này không nằm trong khả năng của tôi", "đó không có trong phạm vi mà tôi có thể thực hiện", "này không được chấp nhận", "kia không có trong những dữ liệu mà tôi có thể đọc \n được"]
            respond_feed_back_2 = ['Hãy nhập lại sau khi kiểm tra', 'Hãy thay thế bằng một từ khác và nhập lại lần nữa', 'Hãy kiếm nội dung khác thay vì dùng từ khóa trên']
            rd = random.choice(respond_data)
            rfb1 = random.choice(respond_feed_back_1)
            rfb2 = random.choice(respond_feed_back_2)
            speak(f"{rd} [{you}] {rfb1}\n{symtype} {rfb2}") #Các trả lời khi không có các tương tác liên quan hoặc sai từ
        
       
