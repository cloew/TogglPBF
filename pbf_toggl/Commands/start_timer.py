from pbf.Commands import command_manager

from pbf_toggl.helpers.toggl_project_helper import GetCurrentTogglProject

import pytoggl

class StartTimerCommand:
    """ Represents a command to start the Toggl timer """
    category = "start"
    command = "timer"
    description = "Start the Toggl Timer"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('description', action='store', help='Toggl time entry description')
    
    def run(self, arguments):
        """ Run the command """
        description = arguments.description
        
        self.startTimer(description)
        
    def startTimer(self, description):
        """ Start the Toggl Timer """
        pbfProject = GetCurrentTogglProject()
        timeEntry = pytoggl.TimeEntry(description=description, pid=pbfProject.togglProject.id, created_with="TogglPBF")
        pbfProject.togglAPI.timer.startTimer(timeEntry)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [description]".format(category=self.category, command=self.command)
        print "Start the Toggl timer for the project assoicated with this directory and the given description"
    
command_manager.RegisterCommand(StartTimerCommand)