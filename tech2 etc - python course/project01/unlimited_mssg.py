import pyautogui                 #importing module
mssg=10                          
while mssg>0:                     
    pyautogui.typewrite("hello")   #message you want to send
    pyautogui.press('enter')       #press enter to send 
    mssg=mssg-1			   #decrement	