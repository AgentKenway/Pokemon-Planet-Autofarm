
yeah = input("Type 'begin farming' to begin the autofarm ")
if yeah == "begin farming":
        print("Farming now in progress, terminate this program to stop farming.")
        import time as wait
        wait.sleep(1)
        enabled = True
        import pyautogui as auto
        while enabled:
                auto.keyDown('A')
                wait.sleep(1)
                auto.click(729, 639)
                auto.keyUp('A')
                wait.sleep(1)
                auto.click(729, 639)
                auto.keyDown('D')
                wait.sleep(1)
                auto.click(1010, 620)
                auto.keyUp('D')
                
