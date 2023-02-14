import time
import appscript
import select
import sys

safari = appscript.app("Safari")
list = ["twitter", "facebook", "reddit", "youtube", "instagram", "tumblr", "pinterest", "imgur", "9gag"]
print("Enter 'append', 'remove', 'list' or 'exit': ")
def printy():
    print("Enter 'append', 'remove', 'list' or 'exit': ")

wait_for_delay = True  # start by waiting for the 3s delay
while True:
    # check if safari is running
    while not safari.isrunning():
        time.sleep(3)
    # Check tabs for keywords
    tabs = safari.windows.first.tabs()  # fetch latest tabs
    for keyword in list:
        for tab in tabs:
            if tab.exists() and keyword in tab.URL():
                tab.close()

    # Check for user input (non-blocking)
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    if ready:
        wait_for_delay = False  # don't wait for delay if user entered a command
        command = input("")
        if command == "exit":
            print("Exiting...")
            break
        elif command == "append": # Add a keyword to the list, if n
            listApp = input("Append the keyword: ")
            if listApp == "":
                printy()
                continue
            elif listApp not in list:
                list.append(listApp)
            print(list)
            print(" ")
            printy()
        elif command == "remove": # Remove a keyword from the list
            print(list)
            print(" ")
            listRem = input("Remove the keyword: ")
            if listRem == "":
                continue
            elif listRem in list:
                list.remove(listRem)
            print(list)
            print(" ")
            printy()
        elif command == "list":
            print(list)
            print(" ")
            printy()
        else:
            print("Invalid command")
            print(" ")
            printy()
    else:
        if wait_for_delay:
            time.sleep(3)  # wait for 3 seconds before checking Safari tabs again
        wait_for_delay = True  # reset the flag so that we wait for delay next time
