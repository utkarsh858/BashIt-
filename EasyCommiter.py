import sublime
import sublime_plugin
import subprocess


class AddCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		bashCommand = "cd "+currentDir+";git add -A;"
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()

class CommitCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		bashCommand = "cd "+currentDir+";git commit -m \""+commitmessage+"\";"
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()

