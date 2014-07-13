from pbf.Commands import command_manager

from pbf_toggl.helpers.toggl_project_helper import GetCurrentTogglProject

import pytoggl

class StartTimerCommand:
    """ Represents a command to start the Toggl timer """
    category = "start"
    command = "timer"
    description = "Start the Toggl Timer"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        description = args[0]
        
        self.startTimer(description)
        
    def startTimer(self, description):
        """ Start the Toggl Timer """
        pbfProject = GetCurrentTogglProject()
        timeEntry = pytoggl.TimeEntry(description=description, project=pbfProject.togglProject)
        pbfProject.togglAPI.timer.startTimer(timeEntry)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [description]".format(category=self.category, command=self.command)
        print "Start the Toggl timer for the project assoicated with this directory and the given description"
    
command_manager.RegisterCommand(StartTimerCommand)