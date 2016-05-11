from xml.dom.minidom import Document

class Output:
	def __init__(self, filename):
		self.filename = filename.replace(".", "_") + ".xml"
		self.doc = Document()
		self.rootNode = self.doc.createElement("package")
		self.doc.appendChild(self.rootNode)

	def insert(self, label, content = None, parent = None):
		item = self.doc.createElement(label)
		if content != None:
			item_content = self.doc.createTextNode(str(content))
			item.appendChild(item_content)
		if parent == None:
			parent = self.rootNode
		parent.appendChild(item)
		return item
	def get_rootNode(self):
		pass

	def write(self):
		file = open(self.filename, "a")
		file.write(self.doc.toprettyxml(indent="\t"))
		file.close()