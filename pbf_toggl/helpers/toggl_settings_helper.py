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
    
def GetAPIToken(connectionName=None):
    """ Return the API Token for the requested Connection """
    tokenXML = FindTokenXML(connectionName)
    return tokenXML.findtext('api-token')
    
def FindTokenXML(connectionName=None):
    """ Find the requested Token XML """
    if connectionName is None:
        connectionName = 'default'
        
    tokensXML = GetTokensXML()
    tokenElements = tokensXML.findall('token')
    
    matchingTokens = [tokenElement for tokenElement in tokenElements if tokenElement.findtext('name') == connectionName]
    if len(matchingTokens) == 0:
        return None
    else:
        return matchingTokens[0]
        
def GetTokensXML():
    """ Return the tokens xml """
    tree = GetTogglXMLTree()
    tokensXML = tree.getroot().find('tokens')
    if tokensXML is None:
        tokensXML = SubElement(tree.getroot(), 'tokens')
        
    return tokensXML