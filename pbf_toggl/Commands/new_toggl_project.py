from pbf_project.helpers.project_helper import GetParentProjectFromDirectory
from pbf_toggl.Commands.add_toggl_settings import AddTogglSettings

import pbf_toggl.helpers.toggl_settings_helper as togglSettings

import pytoggl

class NewTogglProject:
    """ Command to create a New Toggl Project """
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('projectname', action='store', help='Toggl Project Name to connect to')
        parser.add_argument('connection', action='store', nargs='?', default=None, help='Toggl Connection to connect to')
        parser.add_argument('-s', '--store', action='store_true', help='Store this Toggl Project as the connection for this PBF Project')
        parser.add_argument('-w', '--workspace', action='store', help='The Workspace to add the project to')
    
    def run(self, arguments):
        """ Run the command """
        projectName = arguments.projectname
        workspaceName = arguments.workspace
        togglConnection = arguments.connection
            
        pbfProject = None
        if arguments.store:
            pbfProject = GetParentProjectFromDirectory()
            if pbfProject is None:
                print "No PBF project for current directory"
        
        if not arguments.store or pbfProject is not None:
            self.createTogglProject(projectName, togglConnection, pbfProject=pbfProject, workspaceName=workspaceName)
        
    def createTogglProject(self, projectName, togglConnection, pbfProject=None, workspaceName=None):
        """ Create the Toggl Project """
        toggl = togglSettings.GetTogglAPI(togglConnection)
        workspace = toggl.workspaces.findByName(workspaceName)
        togglProject = self.buildTogglProject(projectName, workspace=workspace)
        
        toggl.projects.create(togglProject)
        
        if pbfProject is not None:
            self.storeProjectSettings(projectName, togglConnection, pbfProject)
        
    def buildTogglProject(self, projectName, workspace=None):
        """ Build the Toggl Project """
        togglProject = pytoggl.Project(name=projectName)
        if workspace is not None:
            togglProject.wid = workspace.id
        return togglProject
        
    def storeProjectSettings(self, projectName, togglConnection, pbfProject):
        """ Store the Project Settings """
        addTogglSettings = AddTogglSettings()
        addTogglSettings.addTogglSettings(pbfProject, projectName, togglConnection)
