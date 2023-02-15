import time
import appscript
import select
import sys

safari = appscript.app("Safari")
keywords = []
print("Enter 'append', 'remove', 'list' or 'exit': ")
def printy():
    print("Enter 'append', 'remove', 'list' or 'exit': ")

def selectBrowser():
    browser = None
    browserInput = input("Which browser do you want to use? (Safari/Chrome/Firefox): ").lower()
    if browserInput == "safari": 
        browser = appscript.app("Safari")
    elif browserInput == "chrome":
        browser = appscript.app("Google Chrome")
    elif browserInput == "firefox":
        browser = appscript.app("Firefox")
    else:
        print("Invalid browser")
    return browser

command = ''  

browser = selectBrowser()
commandPromptPrinted = False
prevWindowCount = 0

while True:
    # check if browser is available
    if not browser:
        print("Browser not available, exiting...")
        break
    
    lastMessageTime = 0  # initialize last message time to 0

    # check if browser is running
    while not browser.isrunning():
        currentTime = time.time()
        if currentTime - lastMessageTime >= 15:
            print("Browser is not running, please start it")
            lastMessageTime = currentTime
        time.sleep(3)

    # check if browser has at least one window
    
    
        

    # check if browser has at least one window
    windowCount = browser.windows.count()
    if windowCount == 0:
        currentTime = time.time()
        if currentTime - lastMessageTime >= 15:
            print("No windows/tabs found, please open a window")
            lastMessageTime = currentTime
        time.sleep(3)
        prevWindowCount = 0
        commandPromptPrinted = True  # reset the flag
    elif windowCount != prevWindowCount:
        prevWindowCount = windowCount
        commandPromptPrinted = False  # reset the flag

    # print command prompt if not already printed
    if not commandPromptPrinted:
        printy()
        commandPromptPrinted = True

    # Check tabs for keywords
    if browser.windows.count() > 0 and browser.windows.first.tabs.count() > 0:
        tabs = browser.windows.first.tabs()  # fetch latest tabs
        for keyword in keywords:
            for tab in tabs:
                if tab.exists():
                    try:
                        if keyword.lower() in tab.URL().lower():
                            tab.close()
                    except UnicodeEncodeError:
                        print("Error: UnicodeEncodeError occurred while checking tab URL")

    # Check for user input (non-blocking)
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    if ready:
        command = input("")
        if command == "exit":
            print("Exiting...")
            break
        elif command == "append": # Add a keyword to the list, if n
            listApp = input("Append the keyword: ").lower()
            if listApp == "":
                printy()
                continue
            elif listApp not in keywords:
                keywords.append(listApp)
            print(keywords)
            print(" ")
            printy()
        elif command == "remove": # Remove a keyword from the list
            print(keywords)
            print(" ")
            listRem = input("Remove the keyword: ").lower()
            if listRem == "":
                continue
            elif listRem in keywords:
                keywords.remove(listRem)
            print(keywords)
            print(" ")
            printy()
        elif command == "list":
            print(keywords)
            print(" ")
            printy()
        else:
            print("Invalid command")
            print(" ")
            printy()
    
    time.sleep(0.5)  # wait
