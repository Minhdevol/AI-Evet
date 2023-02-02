from datetime import date   #Thư viện thời gian
from datetime import timedelta
from datetime import datetime #Thư viện thời gian
import random #Thư viện ngẫu số
import webbrowser #Thư viện cào web
import subprocess #Thư viện mở tệp trong ổ đĩa
import os #Thư viện hệ thống
import pyttsx3 #Thư viện giọng nói
import sys #Thư viện hệ thống
from rich.console import Console#Đặt thuộc tính giá trị màu
from rich import print
from time import sleep#Điếm thời gian cho hiệu ứng
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from rich.markdown import Markdown

# giọng nói trợ lí
evet = pyttsx3.init()
voices = evet.getProperty("voices")
evet.setProperty("voice",voices[1].id)

#Giá trị màu của biến
setimeline = datetime.now().hour
if setimeline >=6 and setimeline<12:
    text_output = Console(style="#A142CB")
    line_style = Console(style="#000AA0")
    special_type = Console(style="")
elif setimeline >=12 and setimeline<14:
    text_output = Console(style="#B4EA17")
    line_style = Console(style="#FFFF00")
    special_type = Console(style="")
elif setimeline >=14 and setimeline<18:
    text_output = Console(style="#00EEF2")
    line_style = Console(style="#FF4500")
    special_type = Console(style="")
elif setimeline >=18 and setimeline<24:
    text_output = Console(style="#F1FF18")
    line_style = Console(style="#FF0000")
    special_type = Console(style="")
#Ngẫu nhiên biến chứa nhiều giá trịtrị
symbol_type = ['⌯', '∷', '▸', '▹']
symtype = random.choice(symbol_type)
showing_type = ["⌥ lệnh một chiều/ ▸", "⌥ lệnh bắt buộc/ ▸"]
showtype = random.choice(showing_type)


# MARKDOWN = """


# """

# d = Console()
# md = Markdown(MARKDOWN)
# d.print(md)


# Các hàm lệnh:
def speak(audio):
    line_style.print(f"-" *72)
    audio = f"◈ " + audio + "\n"
    for i in audio:
        text_output.print(i, end = "")
        sleep(0.0005)
    line_style.print(f"-" *72)
    evet.say(audio)
    evet.runAndWait()

def talk(audio):
    evet.say(audio)
    evet.runAndWait()

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
    styling = Console()
    styling.print(times)
    line_style.print(f"-" *72)
    audio = f"{tr} {hours} giờ {minute} phút"
    talk(audio)

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
    daystyle.add_column("NGÀY", justify="center", style="#2F4037")
    daystyle.add_column("", justify="center", style="#2F4037")
    daystyle.add_column("", justify="center", style="#2F4037")
    daystyle.add_column("", justify="center", style="#2F4037")
    daystyle.add_column("", justify="center", style="#2F4037")
    daystyle.add_row(f"{time_1}",f"{time_2}",f"[#9278CD][bold][u]{time_3}",f"{time_4}",f"{time_5}")
    styling = Console()
    styling.print(daystyle)
    date_re = ['Hôm nay là', 'Nay là']
    dr = random.choice(date_re)
    speak(f"{dr} ngày {time_3}")  

def weekcouns():
    weekdays = datetime.now().strftime("%A")
    date_re = ['Hôm nay là', 'Nay là']
    dr = random.choice(date_re)
    days = Table(title="", box = box.SIMPLE)
    line_style.print(f"-" *72 + "\n❖")
    days.add_column("THỨ", justify="center", style="#1C5635")
    days.add_column("", justify="center", style="#1C5635")
    days.add_column("", justify="center", style="#1C5635")
    days.add_column("", justify="center", style="#1C5635")
    days.add_column("", justify="center", style="#1C5635")
    days.add_column("", justify="center", style="#1C5635")
    days.add_column("", justify="center", style="#1C5635")
    if "Monday" in weekdays:
        days.add_row("[#00FF33][bold][u]Hai", "Ba", "Tư", "Năm", "Sáu", "Bảy", "Chủ Nhật")
        styling = Console()
        styling.print(days)
        speak(f"{dr} thứ hai!")
    elif "Tuesday" in weekdays:
        days.add_row("Hai", "[#0D70FF][bold][u]Ba", "Tư", "Năm", "Sáu", "Bảy", "Chủ Nhật")
        styling = Console()
        styling.print(days)
        speak(f"{dr} thứ ba")
    elif "Wednesday" in weekdays:
        days.add_row("Hai", "Ba", "[#FF26DC][bold][u]Tư", "Năm", "Sáu", "Bảy", "Chủ Nhật")
        styling = Console()
        styling.print(days)
        speak(f"{dr} thứ tư")
    elif "Thursday" in weekdays:
        days.add_row("Hai", "Ba", "Tư", "[#FFBA1A][bold][u]Năm", "Sáu", "Bảy", "Chủ Nhật")
        styling = Console()
        styling.print(days)
        speak(f"{dr} thứ năm")
    elif "Friday" in weekdays:
        days.add_row("Hai", "Ba", "Tư", "Năm", "[#3800FF][bold][u]Sáu", "Bảy", "Chủ Nhật")
        styling = Console()
        styling.print(days)
        speak(f"{dr} thứ sáu")
    elif "Saturday" in weekdays:
        days.add_row("Hai", "Ba", "Tư", "Năm", "Sáu", "[##FD2902][bold][u]Bảy", "Chủ Nhật")
        styling = Console()
        styling.print(days)
        speak(f"{dr} thứ bảy")
    elif "Sunday" in weekdays:
        days.add_row("Hai", "Ba", "Tư", "Năm", "Sáu", "Bảy", "[#00FFEF][bold][u]Chủ Nhật")
        styling = Console()
        styling.print(days)
        speak("Hôm nay là chủ nhật")
    
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
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng một!")
    elif "February" in month:
        months.add_row("Một - 1", "[#0051FF][bold][u]Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng hai")
    elif "March" in month:
        months.add_row("Một - 1", "Hai - 2", "[#0FFF00][bold][u]Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng ba")
    elif "April" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "[#002AB7][bold][u]Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng tư")
    elif "May" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("[#00B76F][bold][u]Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng năm")
    elif "June" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "[#B70040][bold][u]Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng sáu")
    elif "July" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "[#B73200][bold][u]Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng bảy")
    elif "August" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "[#FF3F25][bold][u]Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng tám")
    elif "September" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("[#6025FF][bold][u]Chín - 9", "Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng chín")
    elif "October" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "[#8EE541][bold][u]Mười - 10", "Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng mười")
    elif "November" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "[#F7FE2D][bold][u]Mười Một - 11", "Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng mười một")
    elif "December" in month:
        months.add_row("Một - 1", "Hai - 2", "Ba - 3", "Bốn - 4")
        months.add_row("Năm - 5", "Sáu - 6", "Bảy - 7", "Tám - 8")
        months.add_row("Chín - 9", "Mười - 10", "Mười Một - 11", "[#F82DFE][bold][u]Mười Hai - 12")
        styling = Console()
        styling.print(months)
        speak(f"{dr} tháng mười hai")

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
    styling = Console()
    styling.print(year)
    speak(f"{dr} năm {time_3}")

def shutdownprograms():
    while True:
        option_choising_1 = ['Đây là tác vụ shutdown máy ⍝  bạn thực sự muốn thực hiện nó không?',  'Liệu bạn có muốn shutdown máy ⍝  không?', 'Tác vụ shutdown ⍝  được khởi chạy bạn muốn tắt hay không?']
        oc1 = random.choice(option_choising_1)
        speak(f"{oc1}\n                ⌈ có ⌋ hoặc ⌈ không ⌋")
        me = Prompt.ask(f"⦿ [red]{showtype} ").lower()
        if me == "có":
            os.system("shutdown /s /t 30")
            keeping = ['HÃY TẮT ⌧ CÁC TÁC VỤ CÒN ĐANG CHẠY', 'HÃY TẮT ⌧ CÁC ỨNG DỤNG CÒN ĐANG CHẠY', 'TẮT ⊗ CÁC TÁC VỤ CÒN ĐANG HOẠT ĐỘNG', 'BẠN NÊN TẮT ⊗ CÁC ỨNG DỤNG CÒN HOẠT ĐỘNG']
            kpp = random.choice(keeping)
            speak(f'LƯU Ý: "             {kpp}             \n{symtype}             MÁY TÍNH SẼ TẮT ⤬ TRONG 30 GIÂY             "')
            break
        elif me == "không":
            speak("Bạn muốn làm gì tiếp?")
            break
        else:
            option_choising_2 = ['⊑ LƯU Ý: đây là lệnh mà chỉ có thể trả lời là ', '⊑ Vui lòng trả lời với hai lệnh duy nhất là ', '⊑ Hãy chỉ nhập với hai lệnh đã cho là ']
            oc2 = random.choice(option_choising_2)
            speak(f"{oc2} ⌈ có ⌋ hoặc ⌈ không ⌋")

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

def wellcome():
    intro = "[\]=>>>>>>>>>>>>======================================<<<<<<<<<<<<<<===|\n|==██▓███▒█----██-------██----██▒█▓▓▓█----███░██▓████==================|\n|==▒██----------▓█-----▒▒-----█▒█-------------█▒▒======================|\n|==███▓▒██-------█▒---▒█------█░█▒▒██---------█▓█======================|\n|==▒█▒------------██-█▓-------▒██-------------▒██====AI product========|\n|==█░████▓▓--------██▒--------█▒▒██░▒█--------▓░█=「 by ⌨  MINHDEVOL 」|\n|===>>>>>>>>>>>>=====================================<<<<<<<<<<<<<<<="
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

#Biến lưu
acept_token_1 = ["tắt chương trình", "hủy chương trình", "nghỉ", "ngủ", "dừng", "ngừng", "@sd"]#từ ngữ bổ sung ngừng hoạt động AI
acept_token_2 = ["giờ", "tiếng", "phút", "thời gian"]#từ ngữ bổ sung thời gian [giờ]
acept_token_3 = ["thứ", ]#từ ngữ bổ sung thời gian [thứ]
acept_token_4 = ["ngày", "day", "days"]#từ ngữ bổ sung thời gian [ngày]
acept_token_5 = ["tháng", "month"]#từ ngữ bổ sung thời gian [tháng]
acept_token_6 = ["năm", "year", "years"]#từ ngữ bổ sung thời gian [năm]
acept_token_7 = ["tắt laptop", "shutdown", "shutdown máy tính", "shutdown laptop", "tắt nguồn"]#từ ngữ tắt máy tính
acept_token_8 = []#
acept_token_9 = []#
acept_token_10 = []#






# Nơi gán hàm và các câu lệnh cũng như vòng lặp để khởi động chương trình
if __name__ =="__main__":
    wellcome() #lời chào
    while True:
        you = Prompt.ask("[#B075CB]⦿ ").lower() #Phương thức tương tác
        if you in acept_token_1: #Lời tạm biệt
            bye()
            break
        elif you in acept_token_2: 
            timecouns()
        elif you in acept_token_3:
            weekcouns()
        elif you in acept_token_4:
            daycouns()
        elif you in acept_token_5:
            monthcoun()
        elif you in acept_token_6:
            yearscoun()
        elif you in acept_token_7: #chế độ tắt máy tính
            shutdownprograms()
        else:
            respond_data = ["Dữ liệu", "Từ khóa", "Cụm chữ", "Chức năng", "Nhập liệu"]
            respond_feed_back_1 = ["này không nằm trong khả năng của tôi", "đó không có trong phạm vi mà tôi có thể thực hiện", "này không được chấp nhận", "kia không có trong những dữ liệu mà tôi có thể đọc \n được"]
            respond_feed_back_2 = ['Hãy nhập lại sau khi kiểm tra', 'Hãy thay thế bằng một từ khác và nhập lại lần nữa', 'Hãy kiếm nội dung khác thay vì dùng từ khóa trên']
            rd = random.choice(respond_data)
            rfb1 = random.choice(respond_feed_back_1)
            rfb2 = random.choice(respond_feed_back_2)
            speak(f"{rd} [{you}] {rfb1}\n{symtype} {rfb2}") #Các trả lời khi không có các tương tác liên quan hoặc sai từ
        
        
