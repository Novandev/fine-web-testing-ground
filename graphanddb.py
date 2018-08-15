from py2neo import Graph, Node, Relationship
#  the access to the db is at http://localhost:7474/ password is...well ya know
#
#

practice_graph_db_conn = Graph("http://localhost:7474")
print("\n\t\tDatabase has the configuration settings:\n {}\n\n".format(practice_graph_db_conn.database))
practice_graph = practice_graph_db_conn.begin()


def random_sampler():
    '''This function takes in a string file name and fills nodes with the pertinent information'''
