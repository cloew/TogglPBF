from pbf_project.helpers.project_helper import GetParentProjectFromDirectory
from pbf_toggl.helpers.toggl_project import TogglProject

def GetCurrentTogglProject():
    """ Get Toggl Project for the current directory """
    project = GetParentProjectFromDirectory()
    return TogglProject(project)