'''
Created on 2012-03-16

@author: William Panting
@TODO: should check for exceptions and log errors for missing files/sections etc., we'll need to accept a logger
'''
import ConfigParser

class Islandora_configuration(object):
    '''
EXAMPLE:

[Fedora]
url:http://localhost:8080/fedora
username: fedoraAdmin
password: islandora
[Solr]
url:http://localhost:8080/solr
[Drupal]
url:http://localhost/drupal
[logging]
directory:./logs
[alerts]
medium:mailx
emails:willy@domain.ca wonka@notadomian.com
[miscellaneous]
ingest_name:name_of_ingest
temporary_directory:./tmp
default_fedora_pid_namespace:packers_plus
[cron]
when_last_ran:timestamp_here

    '''

    def __init__(self, configuration_file_path):
        '''
        Constructor
        @param configuration_file_path: the path to the configuration file 
        '''
        #get config
        self._configuration_parser = ConfigParser.SafeConfigParser()
        self._configuration_parser.read(configuration_file_path)
        self._configuration_dictionary = {}
        self._configuration_file_path = configuration_file_path
        #loop through he configuration file sections and dump the config to a dictionary
        self.sections = self._configuration_parser.sections()
        for section in self.sections:
            self._configuration_dictionary[section] = {}
            options = self._configuration_parser.options(section)
            for option in options:
                self._configuration_dictionary[section][option] = self._configuration_parser.get(section, option)

    @property
    def configuration_parser(self):
        '''
        This will return the configuration parser object that self is using
        '''
        return self._configuration_parser
    
    @property
    def configuration_file_write_handle(self):
        '''
        This will return a file handle pointing to the file used to set the configuration.
        '''
        file_handle = open(self._configuration_file_path, 'w')
        return file_handle
    
    @property
    def configuration_dictionary(self):
        '''
        The dictionary version of my configuration.
        '''
        return self._configuration_dictionary