
import pbf_toggl.helpers.toggl_settings_helper as togglSettings

class AddConnection:
    """ Represents Command to add toggl connection to toggl settings """
    
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
