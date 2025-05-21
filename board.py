import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class strimko:
    def __init__(self , size=5, type=None):
        '''initializing strimko, if the type equals soduko the links will be set just like a soduko'''

        if type == 'soduko':
            if size==9: # if the size isn't 9 nothing will be set 
                    
                    self.size=size
                    self.board=np.zeros(size*size).reshape(size,size).astype(int)
                    self.links = np.zeros(size*size).reshape(size,size).astype(int)
                    self.possiblities=np.full((size,size),set(np.arange(1,size+1))) # fill all the cells with all possible values
                    self.numberoflinks=0
                    self.new_link('00','01','02','10','11','12','20','21','22')
                    self.new_link('03','04','05','13','14','15','23','24','25')
                    self.new_link('06','07','08','16','17','18','26','27','28')

                    self.new_link('30','31','32','40','41','42','50','51','52')
                    self.new_link('33','34','35','43','44','45','53','54','55')
                    self.new_link('36','37','38','46','47','48','56','57','58')

                    self.new_link('60','61','62','70','71','72','80','81','82')
                    self.new_link('63','64','65','73','74','75','83','84','85')
                    self.new_link('66','67','68','76','77','78','86','87','88')
                    self.values_assigned = 0
                    return

        
        self.size=size # e.g if we have a 4*4 strimko size will be 4
        self.board = np.zeros(size*size).reshape(size,size).astype(int) # all values will be initialized to 0    

        self.links = np.zeros(size*size).reshape(size,size).astype(int) # all linkes are initialized to be the same link (link 0)
        self.possiblities=np.full((size,size),set(np.arange(1,size+1))) # each node can take values from 1 to 5
        self.numberoflinks=0
        self.values_assigned = 0
            
    def add_value(self ,posy ,posx ,value):  
        '''
        set value of a given node in board
        '''
        self.board[posy][posx]=value
        self.values_assigned += 1

    def new_link(self,*args): 
        """
        making a new link with the string it recives as arguments
        each string should be of length two 
        e.g for link of a square in soduko
        self.new_link('00','01','02','10','11','12','20','21','22')
        """
        for x in args :
            self.links[int(x[0])][int(x[1])] = self.numberoflinks
        self.numberoflinks+=1

    def rows_are_correct(self):
        '''
        return True if no rows breaks a constraint else returns False
        '''
        for i in range(self.size): 
            for j in range(1,self.size+1):
                if int(j in self.board[i])!=1:
                    return False 
        return True
    

    def cols_are_correct(self): 
        '''    
        return True if no rows breaks a constraint else returns False
        '''
        for i in range(self.size):
            for j in range(1,self.size+1):
                if int(j in self.board[:,i])!=1:
                    return False 
        return True
    
    def link_is_correct(self, number ): 
        '''
        given the number of the link check if it breaks a constraint 
        '''

        link=[]

        for i in range(self.size):
            for j in range(self.size):
                if(self.links[i,j]==number):
                    link.append(self.board[i,j])

        for i in range(1,self.size+1):
                if int(i in link)!=1:
                    return False            
        return True

    def links_are_correct(self):
        '''return True if all the links follow constraints else return False'''
        for i in range(self.size):
            if (self.link_is_correct(i)==False):
                return False
        return True    

    def is_solved(self):
        '''check all the constraints  return True if the board is solved else return False'''
        # worst case (all values are assigned runs in O(N^3)
        if self.values_assigned < self.size ** 2 : return False 
        else :return self.rows_are_correct() and self.cols_are_correct() and self.links_are_correct()
        


    def get_possibles(self , y , x):
        '''
        return the set of possible values for node in (y , x)
        '''

        poss =set({})
        for i in range(1, self.size +1):
            poss |= {i}

        # remove number from the set which are already present in the row          
        for i in self.board[y,:]:
            if( i != 0): 
                poss-={i}


        # remove number from the set which are alreay present in the column 
        for j in self.board[:,x]:
            if( j != 0):
                poss-={j}
                
        # remove number from the set which are alreay present in the link
        pos = self.links[y][x]   
        for i in range(self.size):
            for j in range(self.size):
                if(self.links[i][j]==pos):
                    poss-={self.board[i][j]} 

        return poss
    
    def set_unpacking(self ,s): 
        '''
        utility function to gest the only elemnt of a set 
        '''
        e, *_ = s 
        return e    

    def fill_possiblities(self):
        '''initialize the possiblitites for each node'''
        for i in range(self.size):
            for j in range(self.size):
                if (self.board[i,j]!=0):
                    self.possiblities[i,j] = set({})
                    continue
                self.possiblities[i,j] = self.get_possibles(i,j)
                


    def solver_csp(self):
   
        for _ in range(self.size*self.size - self.values_assigned): 
            self.fill_possiblities()       # Initialize the possibilities for each cell
            for y in range(self.size):       # These two loops iterate
                for x in range(self.size):   # all nodes in find the next number to write
                    
                    # if for board[y][x] only one value is possiblle
                    # add the value to the target position and move to the next node
                    if(len(self.possiblities[y,x])==1):
                        self.add_value(y ,x , self.set_unpacking(self.possiblities[y,x]))
                        continue

                    # now we check if one of poss for that is the only valid one. e.g no other value like it is in the same constraint
                    if(len(self.possiblities[y,x])>1):

                        # if thre is only one possible value in the row add it to target position
                        repeat={} # Constructing a dictionary to count the repetition of each possibility
                        
                        for i in range(1,self.size+1):
                            repeat[i]=0

                        for i in self.possiblities[y]:
                            for j in range(1,self.size+1):
                                repeat[j]+=int(j in i)

                        singlerepeat=0
                        for i in repeat.keys():
                            if(repeat[i]==1):
                                singlerepeat=i
                                break

                        for i ,counter in zip(self.possiblities[y],range(self.size)):
                            if (singlerepeat in i and (singlerepeat>0)):
                                self.add_value(y,counter,singlerepeat)
                                break

                        ################################
                        
                        # now the same thing for columns
                        repeat.clear()
                        # if thre is only one possible value in the column add it to target position
                        for i in range(1,self.size+1):
                            repeat[i]=0

                        for i in self.possiblities[:,x]:
                            for j in range(1,self.size+1):
                                repeat[j]+=int(j in i)

                        singlerepeat=0
                        for i in repeat.keys():
                            if(repeat[i]==1):
                                singlerepeat=i
                                break

                        for i ,counter in zip(self.possiblities[:,x],range(self.size)):
                            if (singlerepeat in i and (singlerepeat>0)):
                                self.add_value(counter,x,singlerepeat)
                                
                                break


                        ##################################
                        
                        # now same for links
                        repeat.clear()

                        lnk=self.links[y,x]
                        for i in range(1,self.size+1):
                            repeat[i]=0

                        for i in range(self.size):
                            for j in range(self.size):
                                if (self.links[i][j]==lnk):
                                
                                        for l in range(1,self.size+1):
                                            repeat[l]+=int(l in self.possiblities[i,j])
                                            

                        singlerepeat=0
                        for i in repeat.keys():
                            if(repeat[i]==1):
                                singlerepeat=i
                                break
                        for i in range(self.size):
                            for j in range(self.size):
                                if(self.links[i,j]==lnk):
                             
                                        if (({singlerepeat}&self.possiblities[i,j]=={singlerepeat}) and (singlerepeat>0)):
                                            self.add_value(i,j,singlerepeat)                  

        

    def __str__(self):
        return f'''
the main board is as follow
{self.board}

the links are 
{self.links}

puzzle is solved : {self.is_solved()}
'''



