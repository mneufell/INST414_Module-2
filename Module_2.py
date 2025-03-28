import json
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

with open("imdb_movies_2000to2022.prolific.json", "r") as IMDB_file:
    for obj in IMDB_file:
        movie = json.loads(obj)
        if 'Comedy' in movie.get('genres', []):
            actors = [actor[1] for actor in movie.get('actors', [])]
            for actor in actors:
                g.add_node(actor, name = actor)
            for i in range(len(actors)):
                for h in range(i + 1, len(actors)):
                    g.add_edge(actors[i], actors[h])
#degree_centrality
centrality_degree = nx.degree_centrality(g)
top_k = 50
top_actors = sorted(centrality_degree, key = centrality_degree.get, reverse = True)[:top_k]
top_graph = g.subgraph(top_actors)
plt.figure(figsize = (20, 8))
nx.draw(top_graph, nx.kamada_kawai_layout(top_graph), with_labels = True, node_size = 500, font_size = 13)
labels = {node:g.nodes[node]['name'] for node in top_graph.nodes()}
nx.draw_networkx_labels(top_graph, nx.kamada_kawai_layout(top_graph), labels, font_size = 13)
print(movie)



    
    

