import os, time, subprocess

string = "[www.MP3Fiber.com]"
path = "C:\\Users\\sss1612\\Downloads\\"  #my chosen path
#WINDOWS RENAME COMMAND SYNTAX ---> RENAME C:/PATH/file.mp3 sample.mp3 (just an fyi)

def read_dir():
   global string, path

   for file in os.listdir(path):
      if string in file:
         return True
   return False

def run_command(command):
   #nifty anti-cmd popup
   si = subprocess.STARTUPINFO()
   si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
   #si.wShowWindow = subprocess.SW_HIDE # default
   subprocess.call(command, startupinfo=si, shell=True)


def remove_duplicate(file, files):
   global path, string
   
   if file in files and file.replace(string, "") in files:
      run_command("del {}".format(path+file.replace(string, "")))


def rename():
   global path, string 
   
   files = os.listdir(path)
   for file in files:
      if string in file:
         remove_duplicate(file, files)
         run_command("REN {} {}".format(path+file, file.replace(string, "")))  #replace word



while True:
   if read_dir():
      rename()

   time.sleep(10)