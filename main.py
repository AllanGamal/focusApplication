import time
import appscript

safari = appscript.app("Safari")
list = ["google", "chat", "4chan"]

while True:
    time.sleep(3)
    tabs = safari.windows.first.tabs()  # fetch latest tabs
    for keyword in list:
        for tab in tabs:
            if tab.exists() and keyword in tab.URL():
                tab.close()