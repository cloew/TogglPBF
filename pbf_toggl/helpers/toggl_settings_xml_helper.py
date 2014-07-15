from pbf.helpers.configuration_helper import GetConfigurationsFilename
from pbf.helpers.XML.xml_helper import SaveEtreeXMLPrettily

from xml.etree.ElementTree import parse, Element, ElementTree

import os

__toggl_xml_tree__ = None

def GetTogglXMLFilename():
    """ Return the Toggl XML filename """
    return GetConfigurationsFilename("toggl.xml")

def GetTogglXMLTree():
    """ Return the Toggl XML Tree """
    global __toggl_xml_tree__
    togglFilename = GetTogglXMLFilename()
    if __toggl_xml_tree__ is None:
        if os.path.exists(togglFilename):
            __toggl_xml_tree__ = parse(togglFilename)
        else:
            __toggl_xml_tree__ = CreateConfigurationXML()
    return __toggl_xml_tree__
    
def CreateConfigurationXML():
    """ Create the Configuration XML """
    togglFilename = GetTogglXMLFilename()
    element = Element("toggl")
    tree = ElementTree(element)
    tree.write(togglFilename)
    return tree
    
def SaveTogglXML():
    """ Save the Project XML with the given tree """
    SaveEtreeXMLPrettily(__toggl_xml_tree__, GetTogglXMLFilename())