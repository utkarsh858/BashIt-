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

	
