from pbf.Commands import command_manager

from pbf_toggl.helpers.toggl_project_helper import GetCurrentTogglProject

class StopTimerCommand:
    """ Represents command to stop the current timer """
    category = "stop"
    command = "timer"
    description = "Stop the current timer for Toggl"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        pass # No arguments
    
    def run(self, arguments):
        """ Run the command """
        self.stopTimer()
        
    def stopTimer(self):
        """ Stop the Toggl Timer """
        pbfProject = GetCurrentTogglProject()
        timeEntry = pbfProject.togglAPI.timer.current()
        pbfProject.togglAPI.timer.stopTimer(timeEntry)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command}".format(category=self.category, command=self.command)
        print "Stop the current Toggl Timer"
    
command_manager.RegisterCommand(StopTimerCommand)