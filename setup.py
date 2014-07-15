from distutils.core import setup

setup(name='pbf_toggl',
      version='.1',
      description="Programmer's Best Friend Utility Extension for Toggl",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_toggl', 'pbf_toggl.Commands', 'pbf_toggl.helpers', 'pbf_toggl.templates'],
      #package_data = {'pbf_toggl.templates':[]}, # Add template files
     )