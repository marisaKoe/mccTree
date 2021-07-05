'''
Created on 21.05.2019

@author: marisakoe
'''

import dendropy

def read_single_file(test_file):
    '''
    read one file from one mr bayes run. get the number of generations/500+1 to get the number of trees in the file
    the number of trees are the same for all runs
    0.25*number of trees = the remaining 75% of the trees after burn-in (burn-in at 25% = 25% of the trees need to be disjected)
    '''
    ##read the tree file
    with open(test_file,'r') as file1:
        ##read lines
        data = file1.readlines()
        ##get the last line including a tree, the line before the last one
        line = data[-2].split()
        ##get the number of generations
        numGen = line[1].split(".")[1]
        ##compute the number of trees from the generations
        numTrees = int(numGen)/500+1
        ##get the tree offset (number of trees after 25% tree from the burn-in are disjected)
        tree_offset = int(0.25*numTrees)
        ##return the tree offset
        return tree_offset

def compute_mcc(list_of_files):
    '''
    compute the mcct using dendropy, get the mcc tree for the sample, compute the mcc score, write both to file
    :param list_of_files:list of tree files
    '''
    offset = read_single_file(list_of_files[0])
    trees = dendropy.TreeList()
    for tree_file in list_of_files:
        trees.read(path=tree_file, schema='nexus',tree_offset=offset)
    
    mcct = trees.maximum_product_of_split_support_tree()
    mcc_score = mcct.log_product_of_split_support
    
    print mcc_score
    return mcct, mcc_score



if __name__ == '__main__':
    pass

    
    
    
    
    
    