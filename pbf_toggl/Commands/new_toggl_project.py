from pbf.Commands import command_manager
# from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory

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
        parser.add_argument('connection', action='store', default='default', help='Toggl Connection to connect to')
    
    def run(self, arguments):
        """ Run the command """
        projectName = arguments.projectname
        togglConnection = arguments.connection
            
        # pbfProject = GetParentProjectFromDirectory()
        # if pbfProject is None:
            # print "No PBF project for current directory"
        # else:
        self.createTogglProject(projectName, togglConnection)
        
    def createTogglProject(self, projectName, togglConnection):
        """ Create the Toggl Project """
        togglProject = pytoggl.Project(name=projectName)
        toggl = togglSettings.GetTogglAPI(togglConnection)
        toggl.projects.create(togglProject)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command}".format(category=self.category, command=self.command) # ADD ADITIONAL PACKAGE ARGUMENTS
        print "" # ADD DETAILED DESCRIPTION 
    
command_manager.RegisterCommand(NewTogglProject)