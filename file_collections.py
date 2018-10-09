import os, sys


class File():
	def __init__(self, name, path):
		"""	String : name
			String : path
		"""
		self.name = name
		self.path = path

		"""string representation of File object"""
	def __str__(self):
		return "\n[Filename: {}\n 	path: {}]".format(self.name, self.path)

	def get_info(self):
		return self.name, self.path


class Files(object):
	TEST_MARK = "rec_dir_test_dir:"
	TEST_DIR_NAMES = "abcde"

	"""Creates obect that holds file objects"""
	def __init__(self, cwd=None):
		try:
			self.lst = list()
			if cwd != None:
				self.find_files(cwd)
			else:
				self.find_files(os.getcwd())
		except:
			print("No such directory")

	"""helper"""
	def __str__(self):
		return "use 	.get_items()"

	"""Allows iterating over File objects"""
	def __iter__(self):
		for file in self.lst:
			yield file 


	"""Adds non-directory to File collection"""
	def add(self, fileobj):
		self.lst.append(fileobj)


	def get_items(self):
		return self.lst
	"""Scans current directory and subdirectories for files"""
	def find_files(self, path):
		for item in os.listdir(path):
			new_path = path + "\\" + item
			if os.path.isdir(new_path):
				self.find_files(new_path)
			elif item != "file_collections.py":	#this file
				self.add(File(item, path))


	"""testing purposes"""
	def rec_dir(self, path, depth=3):
		if depth == 0:
			return

		for char in self.TEST_DIR_NAMES:
			new_path = "{}\\{}".format(path, self.TEST_MARK + char)
			try:
				os.mkdir(new_path)
			except:
				pass	#dir exists
		
			rec_dir(new_path, depth-1)
			if depth == 3:
				print("DO NOT STORE ANYTHING WORTH LOSING INSIDE THE TEST DIRECTORIES\n<del_dir deletes all test directories and contents>")


	"""testing purposes"""
	def del_dir(self):
		for char in self.TEST_DIR_NAMES:
			try:
				os.system("rmdir {} /s /q".format(self.TEST_MARK + char))
			except:
				pass
		print("Directories deleted")



#testing purposes only
def main():
	print("""
usage:
	-Create a FileCollections() instance (option to pass in path name or use current default path)
	-Can iterate over files ("for loop")
	-Contain file objects
	-File objects can get printed out
	-File.get_info()	returns name and path tuple
		""")



if __name__ == '__main__':
	main()