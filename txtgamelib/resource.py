import txtgamelib.resolver as resolver
import os.path as fs

class ResourceLoader(resolver.Resolver):
	def __init__(self,debug=False):
		super(ResourceLoader,self).__init__()
		if debug:
			self.addResolver(self.exactFile,10)
		self.addResolver(self.namespacedResource,9)
		self.addResolver(self.noNamespaceResource,8)

	"""Resolves only if the exact file exists. Debug only."""
	def exactFile(self,name):
		# Does the file exist?
		if fs.exists(name):
			return True,name # If so, that's the resource!
		return False,name

	"""Resolves namespaced assets. (i.e; "sonic25:scene1/script.txt")"""
	def namespacedResource(self,name):
		# Does the resource name have one and only one colon?
		if ":" not in name or name.count(":")!=1:
			return False,None # If not, it isn't a namespaced asset.
		abs = self.resourcePath(name)
		return self.exactFile(abs) # delegate file check to another resolver

	"""Alternatively, the resources may not be namespaced and may simply be in, for example, "assets/txt/scene1/script.txt"."""
	def noNamespaceResource(self,name):
		return self.namespacedResource(":"+name)

	"""Returns the full path of a resource, given a namespaced resource name."""
	def resourcePath(self,name):
		namespace,resource = name.split(":")
#		ext = fs.splitext(resource)[1]
		return fs.join("assets",namespace,resource).replace("//","/")

class Resource:
	def __init__(self,name,create_if_nonexistant=False):
		rl = ResourceLoader()
		path = rl.resolve(name)
		if path is None: # if the resource doesn't exist...
			if create_if_nonexistant: # and we should ignore it's lack of existence...
				path = rl.resourcePath(name) # get the raw path!
			else: # otherwise, throw an error
				raise Exception("Non-existant resource \"{}\"!".format(name))
		self.path = path

	def read(self,binary=False):
		with open(self.path,"r"+("b" if binary else "")) as f:
			return True,f.read()

	def write(self,callback,binary=False):
		with open(self.path,"w"+("b" if binary else "")) as f:
			callback(f)
		return True
