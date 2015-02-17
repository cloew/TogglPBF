from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf.helpers.Project.project_xml_helper import SaveProjectXML


from pbf_toggl.helpers.toggl_helper import FindProjectByName
import pbf_toggl.helpers.toggl_settings_helper as togglSettings

from xml.etree.ElementTree import SubElement

class AddTogglSettings:
    """ Represents command to add Toggl Settings to the current Project """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('projectname', action='store', help='Toggl Project Name to connect to')
        parser.add_argument('connection', action='store', nargs='?', default='default', help='Toggl Connection to connect to')
    
    def run(self, arguments):
        """ Run the command """
        projectName = arguments.projectname
        togglConnection = arguments.connection
            
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
