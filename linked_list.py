class Node():
	def __init__(self, ptr=None, item=None):
		self.ptr = ptr
		self.item = item

class LinkedList():

	def __init__(self):
		self.head = Node()

	"""return string representation of items in linked list on newlines"""
	def __str__(self):
		ptr = self.head
		lst = []
		try:
			while ptr.item != None:
				lst.append(str(ptr.item))
				ptr = ptr.ptr
		except:
			return "Unsupported string conversion for Linked list item"
		return "\n".join(lst) + "\n"

	"""Makes linked list iterable"""
	def __iter__(self):
		ptr = self.head
		while ptr.item != None:
			yield ptr.item
			ptr = ptr.ptr

	def add(self, item):
		self.head = Node(self.head, item)

	"""Removes latest item added"""
	def pop(self):
		self.head = self.head.ptr

	"""Returns number of items in linked list"""
	def count(self):
		ptr = self.head
		counter = 0
		while ptr.item != None:
			ptr = ptr.ptr
			counter += 1
		return counter

	"""Returns true if item is contained in linked list"""
	def contains(self, item):
		ptr = self.head
		while ptr.item != None:
			if ptr.item == item:return True
			ptr = ptr.ptr
		return False



def main():
	#test code
	ll = LinkedList()
	
	#test1-empty linked list
	print(ll.count() == 0)
	#test2-non empty linked list
	for x in range(10):
		ll.add(x)
	print(ll.count() == 10)
	#test3-linked list contains its' own items and iterable
	print(all([ll.contains(x) for x in ll ]))
	#test4-linked list popped
	ll.pop()
	print(ll.count() == 9)
	
	#print(ll)
	#for x in ll:print(x)

if __name__ == "__main__":
	main()