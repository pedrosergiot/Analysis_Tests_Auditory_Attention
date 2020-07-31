from __future__ import division, print_function
from scipy.io import loadmat, savemat

import os

import numpy as np

# Junta dados dados das diferentes sessoes em um unico arquivo para melhor manuseio

path = "/media/pedrosergiot/Windows/Users/pedro_000/Documents/Livros/PPGEL/Projeto_HD/Dados Pedro/todos_exames/"

sessions_list = os.listdir(path)

exams = []
target  = []
base_exams = []

for session in sessions_list:
    
    exam0 = loadmat(path + session + "/exame_0.mat")
    exam1 = loadmat(path + session + "/exame_1.mat")
    base = loadmat(path + session + "/dadosBasais.mat")
    
    # descarta aproximadamente o primeiro segundo de sinal para evitar o transitorio
    exams.append(exam0['dadosREJEICAO'][10*64:6144, 0:19]) #retira as 10 primeiras janenas de 64 pontos
    target.append(exam0['ladoAT'])
    exams.append(exam1['dadosREJEICAO'][10*64:6144, 0:19]) #retira as 10 primeiras janelas de 64 pontos
    target.append(exam1['ladoAT'])
    
    base_exams.append(base['dadosREJEICAO'][10*64:6144, 0:19]) #retira as 10 primeiras janelas de 64 pontos
    
exams = np.asarray(exams)
target = np.asarray(target)
base_exams = np.asarray(base_exams)

savemat('exames_sem1segundo.mat',{'exams':exams, 'target':target})
savemat('base_exames_sem1segundo.mat',{'base_exams':base_exams})
