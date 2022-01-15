import pyautogui
import time
from datetime import datetime
import sys

def myexcepthook(type, value, traceback, oldhook=sys.excepthook):
    oldhook(type, value, traceback)
    input("Press RETURN. ")

sys.excepthook = myexcepthook

workersInterval = 60 * 50
lastWorkingTime = time.time()
repositionInterval = 60 * 5 
lastRepositionTime = time.time()
today = datetime.now().strftime('%d/%m/%Y %H:%M')

def sleep(seconds):
    time.sleep(seconds)

def connectWallet():
    print(':::::: [' + datetime.now().strftime('%d/%m/%Y %H:%M') + '] : Connecting wallet.')
    connectWalletClicked = False
    signInMetamaskClicked = False
    treasureHuntClicked = False

    finished = False
    while not finished:
        if(not connectWalletClicked):
            connectWalletClicked = waitForNextImageAndClick('./images/connect-wallet.png', './images/sign-metamask.png', 6)
        if(not signInMetamaskClicked and connectWalletClicked):
            signInMetamaskClicked = waitForImageAndClick('./images/sign-metamask.png', 4, False)
        if(not treasureHuntClicked and signInMetamaskClicked):
            treasureHuntClicked = waitForImageAndClick('./images/treasure-hunt.png', 4, False)

        if (connectWalletClicked and signInMetamaskClicked):
            finished = True
            print(':::::: [' + datetime.now().strftime('%d/%m/%Y %H:%M') + '] : Wallet connected.')
            work()

def waitForImageAndClick(imageUrl, seconds, skipVerify):
    founded = False
    while not founded:
        image = pyautogui.locateOnScreen(imageUrl, confidence=0.7)
        
        if (image is not None):
            pyautogui.click(image)
            sleep(seconds)
            if (pyautogui.locateOnScreen(imageUrl, confidence=0.7) is None) or skipVerify:
                founded = True

    return founded

def waitForNextImageAndClick(imageUrl, nextImageUrl, seconds):
    founded = False
    while not founded:
        image = pyautogui.locateOnScreen(imageUrl, confidence=0.7)
        
        if (image is not None):
            pyautogui.click(image)
            sleep(seconds)
            if (pyautogui.locateOnScreen(nextImageUrl, confidence=0.7) is not None):
                founded = True

    return founded

def waitForAllImageAndClick(imageUrl, seconds):
    founded = False
    while not founded:
        images = list(pyautogui.locateAllOnScreen(imageUrl, confidence=0.7))
        
        if (len(images) > 0):

            for image in images:
                pyautogui.click(image)
                sleep(seconds)

            founded = True

    return founded

def work():

    if (pyautogui.locateOnScreen('./images/back.png', confidence=0.7) is None):
        return False

    print(':::::: [' + datetime.now().strftime('%d/%m/%Y %H:%M') + '] : Putting heroes to work.')
    backClicked = False
    heroesClicked = False
    allClicked = False
    closeClicked = False
    treasureClicked = False

    finished = False

    while not finished:
        if(not backClicked):
            backClicked = waitForImageAndClick('./images/back.png', 1, False)
        if(not heroesClicked and backClicked):
            heroesClicked = waitForImageAndClick('./images/heroes-work.png', 2, False)
        if(not allClicked and heroesClicked):
            allClicked = waitForAllImageAndClick('./images/all-work.png', 3)
        if(not closeClicked and allClicked):
            closeClicked = waitForImageAndClick('./images/close-work.png', 2, False)
        if(not treasureClicked and closeClicked):
            treasureClicked = waitForImageAndClick('./images/treasure-hunt.png', 1, False)

        if (backClicked and heroesClicked and allClicked and closeClicked and treasureClicked):
            finished = True
            print(':::::: [' + datetime.now().strftime('%d/%m/%Y %H:%M') + '] : Heroes working.')
    
    return True

def reposition():
    if (pyautogui.locateOnScreen('./images/back.png', confidence=0.7) is None):
        return False

    print(':::::: [' + datetime.now().strftime('%d/%m/%Y %H:%M') + '] : Repositioning heroes.')
    backClicked = False
    treasureClicked = False

    finished = False

    while not finished:
        if(not backClicked):
            backClicked = waitForImageAndClick('./images/back.png', 1, False)
        if(not treasureClicked and backClicked):
            treasureClicked = waitForImageAndClick('./images/treasure-hunt.png', 1, False)

        if (backClicked and treasureClicked):
            finished = True
            print(':::::: [' + datetime.now().strftime('%d/%m/%Y %H:%M') + '] : Heroes have been repositioned.')
    
    return True

banner ="""
PPPPPPPPPPPPPPPPP                                                     dddddddd                 
P::::::::::::::::P                                                    d::::::d                 
P::::::PPPPPP:::::P                                                   d::::::d                 
PP:::::P     P:::::P                                                  d:::::d                  
  P::::P     P:::::Prrrrr   rrrrrrrrr     aaaaaaaaaaaaa       ddddddddd:::::d     ssssssssss   
  P::::P     P:::::Pr::::rrr:::::::::r    a::::::::::::a    dd::::::::::::::d   ss::::::::::s  
  P::::PPPPPP:::::P r:::::::::::::::::r   aaaaaaaaa:::::a  d::::::::::::::::d ss:::::::::::::s 
  P:::::::::::::PP  rr::::::rrrrr::::::r           a::::a d:::::::ddddd:::::d s::::::ssss:::::s
  P::::PPPPPPPPP     r:::::r     r:::::r    aaaaaaa:::::a d::::::d    d:::::d  s:::::s  ssssss 
  P::::P             r:::::r     rrrrrrr  aa::::::::::::a d:::::d     d:::::d    s::::::s      
  P::::P             r:::::r             a::::aaaa::::::a d:::::d     d:::::d       s::::::s   
  P::::P             r:::::r            a::::a    a:::::a d:::::d     d:::::d ssssss   s:::::s 
PP::::::PP           r:::::r            a::::a    a:::::a d::::::ddddd::::::dds:::::ssss::::::s
P::::::::P           r:::::r            a:::::aaaa::::::a  d:::::::::::::::::ds::::::::::::::s 
P::::::::P           r:::::r             a::::::::::aa:::a  d:::::::::ddd::::d s:::::::::::ss  
PPPPPPPPPP           rrrrrrr              aaaaaaaaaa  aaaa   ddddddddd   ddddd  sssssssssss"""

bannerBreakLine = """
===============================================================================================
"""

print(bannerBreakLine + banner + bannerBreakLine)
print(':::::: Bomb Crypto Bot')
print(':::::: Bot started at: ' + today)
print()
print(':::::: Develop by Leandro Pradal')
print(':::::: 2021 - v1.0.0')
print(bannerBreakLine)
print(':::::: [EN] It works correctly with a 67% Chrome zoom at 1920x1080 resolution.')
print(':::::: [EN] Heroes will work whenever wallet is connected/reconnected or every 50 min.')
print(':::::: [EN] Press "Ctrl + C" on console to exit program.')
print()
print(':::::: [PT] Funciona corretamente com um zoom de 67% do Chrome e na resolução de 1920x1080.')
print(':::::: [PT] Os heróis irão trabalhar sempre que a carteira for conectada/reconectada ou a cada 50 min.')
print(':::::: [PT] Pressione "Ctrl + C" no console para sair do programa.')
print(bannerBreakLine)

while True:
    try:
        if (time.time() > lastWorkingTime + workersInterval):
            worked = work()
            if worked:
                lastWorkingTime = time.time()

        if (time.time() > lastRepositionTime + repositionInterval):
            repositioned = reposition()
            if repositioned:
                lastRepositionTime = time.time()

        connectWalletButton = pyautogui.locateOnScreen('./images/connect-wallet.png', confidence=0.7)
        if (connectWalletButton is not None):
            connectWallet()

        treasureHunt = pyautogui.locateOnScreen('./images/treasure-hunt.png', confidence=0.7)
        if (treasureHunt is not None):
            pyautogui.click(treasureHunt)
            sleep(2)

        disconnected = pyautogui.locateOnScreen('./images/disconnected-ok.png', confidence=0.7)
        if (disconnected is not None):
            pyautogui.click(disconnected)
            sleep(2)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise