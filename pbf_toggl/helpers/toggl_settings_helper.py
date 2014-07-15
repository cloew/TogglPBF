from toggl_settings_xml_helper import GetTogglXMLTree, SaveTogglXML

from xml.etree.ElementTree import SubElement

def AddToken(token, name=None):
    """ Add the given token to the Toggl settings """
    if name is None:
        name = 'default'
        
    tokensXML = GetTokensXML()
    tokenElement = SubElement(tokensXML, 'token')
    
    nameElement = SubElement(tokenElement, 'name')
    nameElement.text = name
    apiTokenElement = SubElement(tokenElement, 'api-token')
    apiTokenElement.text = token
    SaveTogglXML()
        
def GetTokensXML():
    """ Return the tokens xml """
    tree = GetTogglXMLTree()
    tokensXML = tree.getroot().find('tokens')
    if tokensXML is None:
        tokensXML = SubElement(tree.getroot(), 'tokens')
        
    return tokensXML