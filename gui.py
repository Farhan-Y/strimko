import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def colormap(n):   
        '''returns a color depending on the given inputs'''
        return ['blue' , 'green' ,'red' ,'lime' ,'cyan' ,'orange' ,'silver' , 'tomato' ,'yellow'][n]


def Colormap(n):  
    if n==0:return 'blue'
    if n==1:return 'green'
    if n==2:return 'red'
    if n==3:return 'lime'
    if n==4:return 'cyan'
    if n==5:return 'orange'
    if n==6:return 'orcid'
    if n==7:return 'peru'
    if n==8:return 'yellow'

def draw(board , write_zeros=False):
    '''
    draw this strimko with given board, links and size 
    if write zero is false the empty cells will be empty otherwise they are written zero
    this only can draw square-like strimkos
    '''
    size = board.size
    links = board.links

    G = nx.Graph()
    mygrid=[]

    mygrid = [(i,j) for  i in range(size) for j in range(size)]                
    G.add_nodes_from(mygrid)
    # produce the coordinates -3*3 grid->([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)])
    
    # Each streamko node is a node in this graph which has its label color and position
    graphlabel={} 
    graphcolor=[]
    pos = {(x,y):(y,-x) for x,y in G.nodes()} # mapping coordiante to posititon of each node
    
    # Assigning colors and labels
    for i in range(size):
        for  j in range(size):

           # these line can possibly be simplified
            G.nodes[(i,j)]['color']=colormap(links[i,j])
            graphcolor.append(G.nodes[(i,j)]['color'])
            
            # If write_zero is false empty cells will remain empty
            if (str(board.board[i,j])!= '0' and not write_zeros):
                G.nodes[(i,j)]['label']=str(board.board[i,j])
                graphlabel[(i,j)]=G.nodes[i,j]['label']
                
            elif (write_zeros):
                  G.nodes[(i,j)]['label']=str(board.board[i,j])
                  graphlabel[(i,j)]=G.nodes[i,j]['label']
            
    nx.draw(G,labels=graphlabel ,pos=pos, node_color=graphcolor, with_labels=True)
    plt.show()
