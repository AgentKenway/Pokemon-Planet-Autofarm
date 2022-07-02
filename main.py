import keyboard
print("Press escape to start the farm")

while True:
    if keyboard.is_pressed('esc'):
        print("Farming now in progress, terminate this program to stop farming.")
        import time as wait

        wait.sleep(0)
        enabled = True
        import pyautogui as auto

        while enabled:
            fight = auto.locateCenterOnScreen('fight.png')
            run = auto.locateCenterOnScreen('run.png')
            elite = auto.locateCenterOnScreen('ELITE.PNG')


            def clickFight():
                auto.click(fight)


            def clickRun():
                auto.click(run)


            if elite:
                print(elite)
                clickRun()
            elif fight:
                print(fight)
                clickFight()
                wait.sleep(0.3)
                auto.leftClick()
                wait.sleep(0.3)
                auto.leftClick()
                auto.moveTo(960, 540)

            else:
                auto.keyDown('A')
                wait.sleep(0.5)
                auto.keyUp('A')
                auto.keyDown('D')
                wait.sleep(0.5)
                auto.keyUp('D')
