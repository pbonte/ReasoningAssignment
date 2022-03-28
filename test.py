
query = '''
    SELECT ?work
        WHERE {
            ?work a <http://www.dbpedia.org/CreativeWork>.
        }
    '''

index = query.rindex('}') + 1
# print(query_two.split('?')[2].split('<')[1].split('>')[0].split('/')[3])
# print(query_two.split('?')[1].split('\n')[0])
# print(query_two.split('/')[-1].split('>')[0])

# print(query_two.split('?')[-1].rsplit('/',1)[0])

# print('?' + query.split('?')[-1].rsplit('/',1)[0] + '>.')

# print(query_two.split('?')[2].split('/', 1)[0])

# print(query.split('/')[-1].split('>')[0])

# print(len(query) - 5)
# print(query[:index])

# print(query[:102] + 'UNION { ?work a <http://www.dbpedia.org/' + 'something' + '> . }')

# print(query.split('?')[2].split('}'))
value = query.split('/')[-1].split('>')[0]
print(value)