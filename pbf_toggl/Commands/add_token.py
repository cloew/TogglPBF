from pbf.Commands import command_manager

import pbf_toggl.helpers.toggl_settings_helper as togglSettings

class AddToken:
    """ Represents COmmand to add api token to toggl settings """
    category = "add"
    command = "token"
    description = "Adds the given token to the Toggl Settings"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        token = args[0]
        name = None
        
        if len(args) > 1:
            name = args[1]
            
        self.addToken(token, name)
        
    def addToken(self, token, name=None):
        """ Add the Token to the Toggl Settings """
        togglSettings.AddToken(token, name=name)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [token] [name]".format(category=self.category, command=self.command)
        print "Adds the given token to the Toggl Settings with the specified name. If name is not provided"
        print "The given name can be used to specify to use this token"
        print "If no token is provided, the token is stored as the default"
    
command_manager.RegisterCommand(AddToken)