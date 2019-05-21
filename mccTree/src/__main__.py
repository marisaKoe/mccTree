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
    test_file="../../../../Dropbox/EVOLAEMP/projects/Project-MaximumCladeCredibility/MCC_testscripts/bayes/dataMatrix_Berg::N.nex.nex.run2.t"
    test_list=[test_file]
