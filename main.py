from rdflib import Graph
from rdflib.namespace import RDF, RDFS

from backwardreasoner import BackwardReasoner
from forwardreasoner import ForwardReasoner
from queryengine import QueryEngine


def load_data(path):
    g = Graph()
    g.parse(path)
    return g

def extract_abox_and_tbox(rdf_graph):
    abox = []
    tbox = []
    for (s,p,o) in rdf_graph:
        if p == RDFS.subClassOf:
            tbox.append((s,p,o))
        if p == RDF.type and o != RDFS.Class:
            abox.append((s,p,o))
    return abox, tbox

def print_results(qres):
    for row in qres:
        print(row)

def forward_reasoning(path, query):
    rdf_graph = load_data(path)
    abox, tbox = extract_abox_and_tbox(rdf_graph)
    reasoner = ForwardReasoner(abox, tbox)
    result = reasoner.execute_query(query)
    return result

def backward_reasoning(path, query):
    rdf_graph = load_data(path)
    abox, tbox = extract_abox_and_tbox(rdf_graph)
    reasoner = BackwardReasoner(abox, tbox)
    result = reasoner.execute_query(query)
    return result



if __name__ == '__main__':

    path = 'data/ontology.ttl'

    query_forward = '''
    SELECT ?novel
        WHERE {
            ?novel a <http://www.dbpedia.org/LightNovel>.
        }
    '''


    query_backward = '''
    SELECT ?work
        WHERE {
            ?work a <http://www.dbpedia.org/CreativeWork>.
        }
    '''

    # query_result = forward_reasoning(path, query_forward)

    # for subject, property, object in query_result:
    #     print(subject, property, object)


    query_result = backward_reasoning(path, query_backward)
    print(query_result)