
class TogglConnection:
    """ Represents a Toggl Connection """
    
    def __init__(self, name=None, token=None, xml=None):
        """ Initialize the Toggl Connection """
        if xml is not None:
            self.name = xml.findtext('name')
            self.token = xml.findtext('token')
        else:
            self.name = name
            self.token = token