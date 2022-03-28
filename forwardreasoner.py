from rdflib import BNode
from rdflib.namespace import RDF, RDFS

class ForwardReasoner:
    def __init__(self, abox, tbox):
        self.abox = abox
        self.tbox = tbox
        self.blank_node = BNode()

    def execute_query(self, query):
        for assertion_triple in self.abox:
            subject_assertion, property_assertion, object_assertion = assertion_triple
            for terminology_triple in self.tbox:
                subject_terminology, property_terminology, object_terminology = terminology_triple

                if ((object_assertion != self.blank_node) and (subject_terminology != self.blank_node) and ((property_terminology == RDFS.subClassOf) or (property_assertion == RDF.type))):
                    if (subject_terminology == object_assertion):
                        self.abox.append(
                            (subject_assertion, RDF.type, object_terminology))
                    else:
                        pass
                else:
                    print('wrong format of ttl file entered, either modify it or add case in the code to satisty the requirements')
                    
        return self.abox
