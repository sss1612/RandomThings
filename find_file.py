import sys, os, platform
from difflib import SequenceMatcher as sm
from time import sleep, time


def match(a, b):
	return sm(None, a, b).ratio()



dest = ""

try:
	file = sys.argv[1]
except IndexError:
	print("Please provide the file as an argument.E.g. (python3 find_file \"hello.txt)\"")
	sys.exit()

blank_extensions = 0




def end_stage():
	global dest
	if not dest:
		dest = "File not found"
	print("Result: {}\nHandled exceptions: {}\nTime taken: {:2f} secs".format(dest, blank_extensions, time()-time_taken))
	sys.exit()

	
	#Needs refactoring
def f_bash(cwd, num):
	global file
	ls = os.listdir(cwd.strip())
	#print("\nCurrent directory: {}".format(cwd))

	for subdir in ls:
		if "." not in subdir:
			f_bash(cwd.strip() + "/" + subdir, num+1)
		if match(subdir, file) > .60:#if subdir == file:
			print("\nCurrent dicrectory: {}".format(cwd))
			#return

def f_cmd(cwd):
	global file, blank_extensions, dest
	try:
		ls = os.listdir(cwd.strip())
	except WindowsError:
		#print("Not a directory, skipping")
		blank_extensions += 1
		return
	#print("\nCurrent directory: {}".format(cwd))
	#print(ls)
	for subdir in ls:
		if "." not in subdir:
			f_cmd(cwd.strip() + "\\" + subdir)
		
		if subdir == file:
			dest = "\nFound at dicrectory: {} ({})".format(cwd, file)
			end_stage()
			return



if __name__ == "__main__":
	time_taken = time()
	
	if platform.system() == "Linux":
		pwd = os.popen("pwd").read()    #reads cwd (linux/bash)
		f_bash(pwd[:-1], 0)

	if platform.system() == "Windows":
		cd = os.popen("cd").read()		#Reads cwd (windows/cmd)
		f_cmd(cd[:-1].split("U")[0])
	end_stage()