from FaceRecognition.FaceRecognition import Recognize
from Functions import *
from Inputs.Listen import *
from Outputs.Speak import *
import pyautogui
import os

def lis():
    a = input("USER:").lower()
    return a

if __name__ == '__main__':
    print("initiating systems")
    while True:
        print("started listening")
        q = lis()
        if "wake up" in q:
            if Recognize():
                while True:
                    q = lis()

                    if "sleep" in q:
                        speak_eng("Okay Sir please say wake up if you need me")
                        break

                    elif "search on youtube" in q:
                        YTSearch()
                        os.startfile("Automations\\YTAuto.py")

                    elif "search on google" in q:
                        GoogleSearch()

                    elif "open" and "website" in q:
                        speak_eng("Can you tell me the name of website to open?")
                        q = lis()
                        webbrowser.open(find_website_url(q))

                    elif "play" and "music" in q:
                        speak_eng("Can you tell me which one to play?")
                        q = lis()
                        PlayMusic(q)

                    # elif "send" and "whatsapp" and "message" in q:
                    #     speak_eng("Can you tell me whom to send?")
                    #     name  = lis()
                    #     speak_eng("Can you tell me what to send?")
                    #     msg = lis()
                    #     Whatsapp(name,msg,int(datetime.datetime.now().strftime("%H")),int(datetime.datetime.now().strftime("%M")))
                        
                    elif "take" and "screenshot" in q:
                        speak_eng("Taking screenshot")
                        ss = pyautogui.screenshot()    
                        ss.save("ScreenShots//"+str(datetime.datetime.now().strftime("%H%M%S%Y")+".png"))

                    elif "tell" and "joke" in q:
                        speak_eng(joke())

                    elif "repeat me" in q:
                        speak_eng(lis())

                    elif "dictionary" in q:
                        speak_eng("Opening Dictionary")
                        speak_eng("Pls tell me the problem:")
                        pr =  lis()
                        wd = DictionaryOP(pr)
                        defin = wd["definition"]
                        syno = wd["synonyms"]
                        oppo = wd["antonyms"]
                        speak_eng(f"The meaning of the word {pr} is {defin} and the synonym is {syno} and the antonyms is {oppo}")

                    elif "internet speed" in q:
                        d,u,p = run_speed_test()
                        speak_eng("The Download speed is " + str(d) + "MBPS and upload speed is " + str(u) + "MBPS" + str(p) + "is the pings")

                    elif "how" and ("can" or "to") in q:
                        q = q.replace("ARIA")
                        wikihow(q)
                    
                    elif "open vs code" in q:
                        os.startfile("C:\\Users\\IT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    elif "open chrome" in q:
                        os.startfile("shortcuts\\Google Chrome.lnk")
                    elif "open excel" in q:
                        os.startfile("shortcuts\\Excel.lnk")
                    elif "open unity hub" in q:
                        os.startfile("shortcuts\\Unity Hub.lnk")
                    elif "open powerpoint" in q:
                        os.startfile("shortcuts\\PowerPoint.lnk")
                    elif "open word" in q:
                        os.startfile("shortcuts\\Word.lnk")
                    elif "open edge" in q:
                        os.startfile("shortcuts\\Microsoft Edge.lnk")

                    elif "create" and "project" in q:
                        speak_eng("Which language do you want to?")
                        q = lis()
                        if "python" in q:
                            speak_eng("WHat is the name of the project?")
                            name = lis()
                            speak_eng(f"Creating a Python project named {name}")
                            parent_dir = "C:\\Users\\IT\\Desktop\\surynshu\\"
                            path = os.path.join(parent_dir,name)
                            os.makedirs(path)
                            speak_eng("Would you like to have main.py file?")
                            main = lis()
                            if "yes" in main:
                                pathof = path + "\\main.py"
                                os.system(f'type nul > {pathof}')
                            speak_eng("Would you like to have virtual environment?")
                            main = lis()
                            if "yes" in main:
                                venvpath = path+"\\"+name+"VENV"
                                os.system(f'python -m venv {venvpath}')
                            speak_eng("Would you like me to open it up in VS Code?")
                            q = lis()
                            if 'yes' in q:
                                os.system(f'code "C:\\Users\\IT\\Desktop\\surynshu\\{name}"')
                        if "html" in q:
                            speak_eng("WHat is the name of the project?")
                            name = lis()
                            speak_eng(f"Creating a Python project named {name}")
                            parent_dir = "C:\\Users\\IT\\Desktop\\surynshu\\"
                            path = os.path.join(parent_dir,name)
                            os.makedirs(path)
                            pathof = path + "\\index.html"
                            os.system(f'type nul > {pathof}')
                            pathof = path + "\\index.js"
                            os.system(f'type nul > {pathof}')
                            pathof = path + "\\style.css"
                            os.system(f'type nul > {pathof}')
                            speak_eng("Would you like me to open it up in VS Code?")
                            q = lis()
                            if 'yes' in q:
                                os.system(f'code "C:\\Users\\IT\\Desktop\\surynshu\\{name}"')
                    elif "make folder"  in q:
                        speak_eng("What is the name of the folder:")
                        nam = lis()
                        speak_eng("Where do you want to?")
                        path = lis()
                        # C:\\Users\\IT\\Desktop\\surynshu\\ARIA Beta Version\\main.py
                        if "surynshu" == path:
                            path = "C:\\Users\\IT\\Desktop\\surynshu\\"
                            path = os.path.join(path, nam)
                            os.makedirs(path)
                        else:
                            path = os.path.join(path,nam)
                            os.makedirs(path)

                
            else:
                speak_eng("Could not recognize face")
        elif "close" in q:
            pass