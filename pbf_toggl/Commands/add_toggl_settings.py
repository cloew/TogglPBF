from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf.helpers.Project.project_xml_helper import SaveProjectXML

from pbf.Commands import command_manager

from pbf_toggl.helpers.toggl_helper import FindProjectByName

from xml.etree.ElementTree import SubElement

class AddTogglSettings:
    """ Represents command to add Toggl Settings to the current Project """
    category = "add"
    command = "toggl-settings"
    description = "Add Toggl settings to the current project"
    minimumNumberOfArguments = 2
    
    def run(self, args):
        """ Run the command """
        projectName = args[0]
        apiToken = args[1]
        pbfProject = GetParentProjectFromDirectory()
        
        if pbfProject is None:
            print "No PBF project for current directory"
        else:
            self.addTogglSettings(pbfProject, apiToken, projectName)
            
    def addTogglSettings(self, pbfProject, apiToken, projectName):
        """ Add Toggl Settings to the project XML """
        togglProject = FindProjectByName(projectName, apiToken=apiToken)
        
        togglElement = SubElement(pbfProject.projectXML, "toggl")
        apiTokenElement = SubElement(togglElement, "api-token")
        apiTokenElement.text = apiToken
        projectIdElement = SubElement(togglElement, "project-id")
        projectIdElement.text = str(togglProject.id)
        
        SaveProjectXML()
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [Project Name] [Toggl API Token]".format(category=self.category, command=self.command)
        print "Stores the Toggl Settings in the current project with the given API Token and Project Name"
    
command_manager.RegisterCommand(AddTogglSettings)