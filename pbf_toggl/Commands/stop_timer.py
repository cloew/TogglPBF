from pbf_toggl.helpers.toggl_project_helper import GetCurrentTogglProject

class StopTimerCommand:
    """ Represents command to stop the current timer """
    
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
