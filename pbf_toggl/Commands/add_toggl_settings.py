from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf.helpers.Project.project_xml_helper import SaveProjectXML

from pbf.Commands import command_manager

from pbf_toggl.helpers.toggl_helper import FindProjectByName
import pbf_toggl.helpers.toggl_settings_helper as togglSettings

from xml.etree.ElementTree import SubElement

class AddTogglSettings:
    """ Represents command to add Toggl Settings to the current Project """
    category = "add"
    command = "toggl-settings"
    description = "Add Toggl settings to the current project"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        projectName = args[0]
        togglConnection = None
        
        if len(args) > 1:
            togglConnection = args[1]
            
        pbfProject = GetParentProjectFromDirectory()
        if pbfProject is None:
            print "No PBF project for current directory"
        else:
            self.addTogglSettings(pbfProject, projectName, togglConnection)
            
    def addTogglSettings(self, pbfProject, projectName, togglConnection):
        """ Add Toggl Settings to the project XML """
        connection = togglSettings.FindTogglConnection(togglConnection)
        
        if connection is not None:
            togglProject = FindProjectByName(projectName, apiToken=connection.token)
            
            togglElement = SubElement(pbfProject.projectXML, "toggl")
            connectionElement = SubElement(togglElement, "connection")
            connectionElement.text = connection.name
            projectIdElement = SubElement(togglElement, "project-id")
            projectIdElement.text = str(togglProject.id)
            
            SaveProjectXML()
        else:
            print "No Toggl Connection:", togglConnection
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [Project Name] [Toggl Connection]".format(category=self.category, command=self.command)
        print "Stores the Toggl Settings in the current project with the given Project Name from the default Toggl connection or the one specified"
    
command_manager.RegisterCommand(AddTogglSettings)