import pytoggl

def FindProjectByName(projectName, apiToken=None):
    """ Find a project from its name """
    toggl = pytoggl.TogglAPI(apiToken=apiToken)
    workspaces = toggl.workspaces.getAll()
    
    project = None
    for workspace in workspaces:
        projects = toggl.workspaces.getProjects(workspace)
        
        projectsWithMatchingName = [project for project in projects if project.name == projectName]
        if len(projectsWithMatchingName) > 0:
            project = projectsWithMatchingName[0]
            break
    return project