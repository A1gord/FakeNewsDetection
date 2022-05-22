import os


def generate_rdf(name, rules):
    os.system("java -jar rmlmapper.jar -m " + str(rules) + ' -o ' + str(name))
    return


if __name__ == '__main__':
    generate_rdf('news.rdf', 'rules.rml.ttl')
