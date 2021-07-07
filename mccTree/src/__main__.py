'''
Created on 21.05.2019

@author: marisakoe
'''

import mbTrees


def write_languageTree(list_of_files):
    '''
    write the mcc tree to a file
    write the mcc score to a file
    '''
    mcct, mcc_score = mbTrees.compute_mcc(list_of_files)
    mcct.write(path="mccTree.tre", schema='nexus')
    
    f = open("mccScore.csv","w")
    f.write(mcc_score)
    f.close()



if __name__ == '__main__':
    ##please use the output files from your analysis computed by Mr.Bayes, IQTree or another method computing tree replicates (e.g. bootstrap method or bootstrapping with noise)
    input_file= "please insert your tree file"
    input_list=[input_file]
