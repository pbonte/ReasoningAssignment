


query = '''
    SELECT ?work
        WHERE {
            ?work a <http://www.dbpedia.org/CreativeWork>.
        }
    '''
value = query.split('\n')[3].split('?')[1].split(' ')[2]
value = value[:-1]

print(value)