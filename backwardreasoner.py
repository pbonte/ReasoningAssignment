from rdflib.namespace import RDF

class BackwardReasoner:
    def __init__(self, abox, tbox):
        self.abox = abox
        self.tbox = tbox

    def execute_query(self, query):

        query_object = query.split('\n')[3].split('?')[1].split(' ')[2]
        query_object = query_object[:-1]

        values = []

        for terminology_triple in self.tbox:
            subject_terminology, property_terminology, object_terminology = terminology_triple
            if object_terminology == query_object:
                values.append(subject_terminology)
            else:
                print('test')





        # dbpedia_resource =  query.split('?')[2].split('<')[1].split('>')[0].split('/')[3]

        # dbpedia_resource = query.split('?')[2].split('<')[1].split('>')[0].split('/')[3]
        # variable = query.split('?')[1].split('\n')[0]
        # query_inside_where = '?' + query.split('?')[-1].rsplit('/',1)[0] + '>.'
        # property = RDF.type
        # query_length = len(query)
        # length_to_add_union = query_length - 5
        

        # resources = []
        # resources.append(dbpedia_resource)


        # for value in resources:
        #     for terminology_triple in self.tbox:
        #         subject_terminology, property_terminology, object_terminology = terminology_triple 
        #         # print(object_terminology)
        #         query_new =  query[:length_to_add_union] + 'UNION { ?work a <' + object_terminology + '>.}' 
        #         # return query_new





    
