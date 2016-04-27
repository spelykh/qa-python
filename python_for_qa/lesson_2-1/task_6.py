__author__ = 'Stepan_Pelykh'
# Connection database properties

db_properties = ('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')
prod_config={'dialect':db_properties[0],'host':db_properties[1],'port':db_properties[2],'database name':db_properties[3],'user name':db_properties[4],'password':db_properties[5]}
stag_config=prod_config.copy()
stag_config['host']='semantic.amazonaws-staging.com'
stag_config['password']='root'

connection_str_prod = "{}://{}:{}@{}:{}/{}".format(prod_config['dialect'],prod_config['user name'],prod_config['password'],prod_config['host'],prod_config['port'],prod_config['database name'])
print "connection string for production: \n", connection_str_prod

connection_str_stag="{}://{}:{}@{}:{}/{}".format(stag_config['dialect'],stag_config['user name'],stag_config['password'],stag_config['host'],stag_config['port'],stag_config['database name'])
print "connection string for staging: \n", connection_str_stag
