from toggl_settings_xml_helper import GetTogglXMLTree, SaveTogglXML
from toggl_connection import TogglConnection

from xml.etree.ElementTree import SubElement

def AddConnection(token, name=None):
    """ Add the given token to the Toggl settings """
    if name is None:
        name = 'default'
        
    connectionsXML = GetConnectionsXML()
    connectionXML = SubElement(connectionsXML, 'connection')
    
    nameElement = SubElement(connectionXML, 'name')
    nameElement.text = name
    apiTokenElement = SubElement(connectionXML, 'api-token')
    apiTokenElement.text = token
    SaveTogglXML()
    
def FindTogglConnection(connectionName=None):
    """ Find the Toggl Connection for the given Connection Name """
    connection = None
    connectionXML = FindConnectionXML(connectionName)
    if connectionXML is not None:
        connection = TogglConnection(connectionXML)
    return conenction
    
def GetAPIToken(connectionName=None):
    """ Return the API Token for the requested Connection """
    connectionXML = FindConnectionXML(connectionName)
    return connectionXML.findtext('api-token')
    
def FindConnectionXML(connectionName=None):
    """ Find the requested Connection XML """
    if connectionName is None:
        connectionName = 'default'
        
    connectionsXML = GetConnectionsXML()
    connectionElements = connectionsXML.findall('connection')
    
    matchingTokens = [connectionElement for connectionElement in connectionElements if connectionElement.findtext('name') == connectionName]
    if len(matchingTokens) == 0:
        return None
    else:
        return matchingTokens[0]
        
def GetConnectionsXML():
    """ Return the connections xml """
    tree = GetTogglXMLTree()
    connectionsXML = tree.getroot().find('connections')
    if connectionsXML is None:
        connectionsXML = SubElement(tree.getroot(), 'connections')
        
    return connectionsXML