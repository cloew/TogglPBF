from pbf.Commands import command_manager
from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf_toggl.Commands.add_toggl_settings import AddTogglSettings

import pbf_toggl.helpers.toggl_settings_helper as togglSettings

import pytoggl

class NewTogglProject:
    """ Command to create a New Toggl Project """
    category = "new"
    command = "toggl-project"
    description = "Create a new Toggl Project"
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('projectname', action='store', help='Toggl Project Name to connect to')
        parser.add_argument('connection', action='store', nargs='?', default='default', help='Toggl Connection to connect to')
        parser.add_argument('-s', '--store', action='store_true', help='Store this Toggl Project as the connection for this PBF Project')
    
    def run(self, arguments):
        """ Run the command """
        projectName = arguments.projectname
        togglConnection = arguments.connection
            
        pbfProject = None
        if arguments.store:
            pbfProject = GetParentProjectFromDirectory()
            if pbfProject is None:
                print "No PBF project for current directory"
        
        if not arguments.store or pbfProject is not None:
            self.createTogglProject(projectName, togglConnection, pbfProject=pbfProject)
        
    def createTogglProject(self, projectName, togglConnection, pbfProject=None):
        """ Create the Toggl Project """
        togglProject = pytoggl.Project(name=projectName)
        toggl = togglSettings.GetTogglAPI(togglConnection)
        toggl.projects.create(togglProject)
        
        if pbfProject is not None:
            self.storeProjectSettings(projectName, togglConnection, pbfProject)
        
    def storeProjectSettings(self, projectName, togglConnection, pbfProject):
        """ Store the Project Settings """
        addTogglSettings = AddTogglSettings()
        addTogglSettings.addTogglSettings(pbfProject, projectName, togglConnection)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command}".format(category=self.category, command=self.command) # ADD ADITIONAL PACKAGE ARGUMENTS
        print "" # ADD DETAILED DESCRIPTION 
    
command_manager.RegisterCommand(NewTogglProject)