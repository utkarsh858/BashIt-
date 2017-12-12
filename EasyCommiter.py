import sublime
import sublime_plugin
import os


class AddCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		currentWindow = self.view.window()
		currentDir = currentWindow.folders()[0]
		os.chdir(currentDir)		
		bashCommand = "git add -A"
		process = os.system(bashCommand)
		bashCommand = "mkdir pop"
		os.system(bashCommand)
		
class InitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		currentWindow = self.view.window()
		currentDir = currentWindow.folders()[0]
		os.chdir(currentDir)		
		bashCommand = "git init"
		process = os.system(bashCommand)

class PullCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		currentWindow = self.view.window()
		currentDir = currentWindow.folders()[0]
		os.chdir(currentDir)		
		bashCommand = "git pull"
		process = os.system(bashCommand)




class CommitCommand(sublime_plugin.TextCommand):
	commitmessage ="first"
	currentDir=""

	def on_change(self,string):
		return

	def on_done(self,string):
		CommitCommand.commitmessage=string
		os.chdir(self.currentDir)		

		bashCommand = "git commit -m '"+self.commitmessage+"'"
		process = os.system(bashCommand)

	def on_cancel(self):
		exit()

	def run(self, edit):
		currentWindow = self.view.window()
		CommitCommand.currentDir = currentWindow.folders()[0]
		currentWindow.show_input_panel("Commit message","Minor changes", self.on_done,self.on_change, self.on_cancel)

class CheckoutCommand(sublime_plugin.TextCommand):
	branch ="first"
	currentDir=""

	def on_change(self,string):
		return

	def on_done(self,string):
		CheckoutCommand.branch=string
		os.chdir(self.currentDir)		

		bashCommand = "git checkout "+self.branch
		process = os.system(bashCommand)

	def on_cancel(self):
		exit()

	def run(self, edit):
		currentWindow = self.view.window()
		CheckoutCommand.currentDir = currentWindow.folders()[0]
		currentWindow.show_input_panel("Commit message","Minor changes", self.on_done,self.on_change, self.on_cancel)

class CheckoutbCommand(sublime_plugin.TextCommand):
	branch ="first"
	currentDir=""

	def on_change(self,string):
		return

	def on_done(self,string):
		CheckoutbCommand.branch=string
		os.chdir(self.currentDir)		

		bashCommand = "git checkout -b "+self.branch
		process = os.system(bashCommand)

	def on_cancel(self):
		exit()

	def run(self, edit):
		currentWindow = self.view.window()
		CheckoutbCommand.currentDir = currentWindow.folders()[0]
		currentWindow.show_input_panel("Commit message","Minor changes", self.on_done,self.on_change, self.on_cancel)


class RaddCommand(sublime_plugin.TextCommand):
	remotename ="first"
	url ="first"
	currentDir=""
	currentWindow=None

	def on_change(self,string):
		return

	def on_done(self,string):
		RaddCommand.remotename=string
		os.chdir(self.currentDir)		
		self.currentWindow.show_input_panel("URL of remote","http://github.com/", self.on_done2,self.on_change, self.on_cancel)

	def on_done2(self,string):
		RaddCommand.url=string
		bashCommand = "git remote add "+self.remotename+" "+self.url
		process = os.system(bashCommand)


	def on_cancel(self):
		exit()

	def run(self, edit):
		RaddCommand.currentWindow = self.view.window()
		RaddCommand.currentDir = self.currentWindow.folders()[0]
		self.currentWindow.show_input_panel("Remote name","origin", self.on_done,self.on_change, self.on_cancel)


class PushCommand(sublime_plugin.TextCommand):
	remotename ="first"
	branch ="first"
	currentDir=""
	currentWindow=None

	def on_change(self,string):
		return

	def on_done(self,string):
		PushCommand.remotename=string
		os.chdir(self.currentDir)		
		self.currentWindow.show_input_panel("branch","master", self.on_done2,self.on_change, self.on_cancel)

	def on_done2(self,string):
		PushCommand.branch=string
		bashCommand = "git push "+self.remotename+" "+self.branch
		process = os.system(bashCommand)


	def on_cancel(self):
		exit()

	def run(self, edit):
		PushCommand.currentWindow = self.view.window()
		PushCommand.currentDir = self.currentWindow.folders()[0]
		self.currentWindow.show_input_panel("Remote name","origin", self.on_done,self.on_change, self.on_cancel)


