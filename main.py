import keyboard
import pyautogui as auto
import time as wait


print("Press escape to start the farm")

while True:
    if keyboard.is_pressed('esc'):
        print("Farming now in progress, terminate this program to stop farming.")

        wait.sleep(0)
        enabled = True

        while enabled:
            fight = auto.locateCenterOnScreen('fight.png',region=(640,600,300,150), grayscale=False, confidence=0.95)
            run = auto.locateCenterOnScreen('run.png',region=(640,600,300,150), grayscale=False, confidence=0.95)
            elite = auto.locateCenterOnScreen('ELITE.PNG',region=(620,340,100,50), grayscale=False, confidence=0.6)
            forgetmove = auto.locateCenterOnScreen('forget.png',region=(960,540,100,50), grayscale=False, confidence=0.7)

            def clickFight():
                auto.click(fight)


            def clickRun():
                auto.click(run)

            def clickForget():
                auto.click(forgetmove)
            

            if elite:
                print(elite)
                clickRun()
                auto.leftClick()
                
            elif forgetmove:
                print(forgetmove)
                clickForget()
                auto.leftClick()

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
