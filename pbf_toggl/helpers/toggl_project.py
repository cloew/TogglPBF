import pbf_toggl.helpers.toggl_settings_helper as togglSettings
import pytoggl

class TogglProject:
    """ Represents a Toggl Project """
    
    def __init__(self, project):
        """ Initialize the Toggl Project """
        self.project = project
        self.togglXML = self.project.projectXML.find('toggl')
        
    @property
    def togglAPI(self):
        """ Return the Toggl API """
        return pytoggl.TogglAPI(apiToken=self.apiToken)
        
    @property
    def apiToken(self):
        """ Return the Project Username """
        connection = self.togglXML.findtext('connection')
        return togglSettings.GetAPIToken(connection)
        
    @property
    def togglProject(self):
        """ Return the Toggl Project """
        return pytoggl.Project(id=self.projectId)
        
    @property
    def projectId(self):
        """ Return the Toggl Project Id """
        return int(self.togglXML.findtext('project-id'))