# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tV5j-DRcpPtoJGoMj8v2DSqR_9wyXeiE

**Task 07: Querying RDF(s)**
"""

#!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""
# TO DO
from rdflib.plugins.sparql import prepareQuery
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns = Namespace("http://somewhere#")

query = prepareQuery('''
    SELECT ?s
    WHERE{
        ?s rdfs:subClassOf ns:Person
    }
''', initNs={ "rdfs": RDFS, "ns" : ns})

# Visualize the results
for s, p, o in g:
  print(s,p,o)
for r in g.query(query):
  print(r)
"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**"""
# TO DO
query2 = prepareQuery('''
  SELECT ?p
  WHERE { 
    {
    ?p rdf:type ns:Person.
    } UNION {
      ?s rdfs:subClassOf ns:Person.
      ?p rdf:type ?p
    } 
  }
  ''',initNs = { "ns": ns}
)


# Visualize the results
for s, p, o in g:
  print(s,p,o)
for r in g.query(query2):
  print(r)
"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**"""
# TO DO

query3 = prepareQuery('''
 SELECT ?p ?prop ?c
  WHERE {
   {
    ?p rdf:type ns:Person.
    ?p ?prop ?o
    }UNION{ 
     ?p rdf:type ?s.
     ?p ?Prop ?o.
     ?s rdfs:subClassOf ns:Person
   }
  }
  ''', initNs = {"ns": ns, "rdf": RDF, "rdfs": RDFS})
# Visualize the results
for r in g.query(query3):
    print(r)