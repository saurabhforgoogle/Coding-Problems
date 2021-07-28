class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None
		

class binary_search_tree:
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root==None:
			self.root=node(value)
		else:
			self._insert(value,self.root)
	def _insert(self,value,cur_node):
		if value<cur_node.value:
			if cur_node.left_child==None:
				cur_node.left_child=node(value)
				cur_node.left_child.parent=cur_node # set parent
			else:
				self._insert(value,cur_node.left_child)
		elif value>cur_node.value:
			if cur_node.right_child==None:
				cur_node.right_child=node(value)
				cur_node.right_child.parent=cur_node # set parent
			else:
				self._insert(value,cur_node.right_child)
		else:
			print("Value already in tree!")

	def Delete(self,value):
		if self.root!=None:
			if self.root==value:
				self._delete(value,self.root,parent=None)
			elif self.root!=value:
				self._delete(value,self.root,parent=None)
		else:
			return False
	def _delete(self,value,curr_node,parent=None):
		def min_value_node(n):#Find Min in SubTree
			current=n
			while current.left_child!=None:
				current=current.left_child
			return current

		##FIND FUNC
		if value<curr_node.value:
			if curr_node.left_child!=None:
				self._delete(value,curr_node.left_child,curr_node)
			else:
				return False
		elif value>curr_node.value:
			if curr_node.right_child!=None:
				self._delete(value,curr_node.right_child,curr_node)
			else:
				return False

		##DELETE FUNC 				
		elif value==curr_node.value:
		#CASE 1
			if curr_node.left_child==None and curr_node.right_child==None:
				if parent!=None:
					if parent.left_child==curr_node:
						parent.left_child=None
						#print("Deleted",value)
					elif parent.right_child==curr_node:
						parent.right_child=None
						#print("Deleted",value)
				else:
					self.root=None
		#CASE  2
			elif curr_node.left_child==None and  curr_node.right_child!=None:
				curr_node.value=curr_node.right_child.value
				curr_node.right_child=None
				#print("Deleted",value)
			elif curr_node.left_child!=None and  curr_node.right_child==None:
				curr_node.value=curr_node.left_child.value
				curr_node.left_child=None
				#print("Deleted",value)
		#CASE 3
			elif curr_node.left_child!=None and curr_node.right_child!=None:
				successor=min_value_node(curr_node.right_child)
				curr_node.value=successor.value
				self._delete(curr_node.value,curr_node.right_child,curr_node)



	

	def Minimum(self):
		if self.root!=None:
			self._Minimum(self.root)
	def _Minimum(self,curr_node):
		if curr_node.left_child!=None:
			self._Minimum(curr_node.left_child)
		else:
			print (curr_node.value)

	def print_tree(self):
		if self.root!=None:
			self._print_tree(self.root)
	def _print_tree(self,cur_node):
		if cur_node!=None:
			self._print_tree(cur_node.left_child)
			print (str(cur_node.value))
			self._print_tree(cur_node.right_child)


import random
def WholeInsert(n):
	for i in range(n):
		bst.insert(40)
		bst.insert(random.randint(1,1000))
		bst.insert(20)


bst=binary_search_tree()
#WholeInsert(4)
bst.insert(40)
bst.insert(30)
bst.insert(50)
bst.insert(15)
bst.insert(35)
bst.insert(45)
bst.insert(37)
bst.insert(55)

print("Minimum Digit")
bst.Minimum()

print("InOrder Traversal:")
bst.print_tree()

bst.Delete(40)

print("InOrder Traversal:")
bst.print_tree()



