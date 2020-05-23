import networkx as nx
G2=nx.Graph()
for i in (range(10)):
    nodes = G2.add_node(i)
    
nodePos = nx.circular_layout(G2)
print("nodePos : \n" , nodePos)

# for i in range(G2.order()):
#     ii,jj = nodePos[i]
#     G2.nodes[i]['pos'] = (ii,jj)

ee = 2 
G2.nodes[2]['label'] = 's'
rr = [3,5]
G2.nodes[3]['label'] = 'd'
G2.nodes[5]['label'] = 'd'

xx=list(G2.nodes.data('s'))
# get_label = []
# for node in range(G2.order()):
#     if G2.nodes[node]['label'] == 's':
#         get_label.append(node)
            
# node_col = []
# for node in range(G2.order()):
#     if node==ee:
#         node_col.append('red')
        
#     elif node == (rr[j] for j in range(len(rr))):
#         node_col.append('yellow')
#     else:
#         node_col.append('blue')
    
# node_col = ['red' if node==ee else 'cyan' for node in range(G2.order())]
# so = 1 
# scc = []
# sc =''
# for node in G2.nodes():
#     if G2.nodes(i) == so:
#         sc = 1
#         scc.append(sc)
#     else:
#         sc == 0
#         scc.append(sc)




# nx.draw_networkx(G2, with_labels = True,pos=nodePos)

qq = nx.get_node_attributes(G2,'pos')
print ('\n\n',qq)
