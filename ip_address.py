import re, os, platform
from json import load
from urllib.request import urlopen

"""
WINDOWS ONLY
"""

class Get_ip():
	
	IPV4_PATTERN = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}[ \n]")
	IPV6PATTERN = re.compile("([a-f0-9]{0,4})(:[a-f0-9]{0,4}){3,7}%\d+")
	OS_TYPE = {
		"Linux":"ip addr",
		"Windows":"ipconfig"
	}

	"""
	Windows lineup	(Linux unknown)
	Link-local IPv6 Address . . . . . : fe80::80c7:43d2:7fd:cc64%17
	--assorted address index 0, 1, 2 respectively--
	IPv4 Address. . . . . . . . . . . : 192.168.42.122	
	Subnet Mask . . . . . . . . . . . : 255.255.255.0
	Default Gateway . . . . . . . . . : 192.168.42.129
	"""
	def __init__(self):
		self.ipv4, self.subnet_mask, self.default_gateway, self.ipv6 = self.assort_addresses()
		self.public_ip = self.obtain_public()

	def __str__(self):
		return "ipv4: {}\nipv6: {}\nSubnet mask: {}\nDefault gateway: {}\nPublic ip: {}\n".format(self.ipv4, self.ipv6, self.subnet_mask, self.default_gateway, self.public_ip)


	def obtain_public(self):
		return load(urlopen('http://httpbin.org/ip'))['origin']


	@classmethod
	def assort_addresses(cls):
		string =  os.popen(cls.OS_TYPE[platform.system()]).read()
		matches = re.findall(cls.IPV4_PATTERN, string)
		ipv6 = re.search(cls.IPV6PATTERN, string).group()	#used brackets so must use group method
		return [x.strip() for x in matches] + [ipv6]	#remove newline and add ipv6


def main():
	ip = Get_ip()
	print(ip)



if __name__ == '__main__' and platform.system() == "Windows":
	main()
else:
	print("This works only for windows")
