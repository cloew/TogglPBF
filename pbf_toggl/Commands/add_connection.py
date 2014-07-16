from pbf.Commands import command_manager

import pbf_toggl.helpers.toggl_settings_helper as togglSettings

class AddConnection:
    """ Represents Command to add toggl connection to toggl settings """
    category = "add"
    command = "connection"
    description = "Creates a connection for the given token in the Toggl Settings"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        token = args[0]
        name = None
        
        if len(args) > 1:
            name = args[1]
            
        self.addConnection(token, name)
        
    def addConnection(self, token, name=None):
        """ Add the Connection to the Toggl Settings """
        togglSettings.AddConnection(token, name=name)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [token] [name]".format(category=self.category, command=self.command)
        print "Creates a Toggl Connection with the given token and name"
        print "If no name is provided, the token is stored as the default connection"
    
command_manager.RegisterCommand(AddConnection)