from pbf.Commands import command_manager

import pbf_toggl.helpers.toggl_settings_helper as togglSettings

class AddConnection:
    """ Represents Command to add toggl connection to toggl settings """
    category = "add"
    command = "connection"
    description = "Creates a connection for the given token in the Toggl Settings"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('token', action='store', help='Toggl API Token')
        parser.add_argument('name', action='store', nargs='?', default='default', help='Name for the new connection')
    
    def run(self, arguments):
        """ Run the command """
        token = arguments.token
        name = arguments.name
            
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