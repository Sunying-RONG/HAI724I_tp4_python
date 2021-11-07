#! /usr/bin/env python3
# -*- coding: utf-8 -*-
print("Bonjour !")
import sys
print("il y a ", len(sys.argv), "parametres")
print("le premier parametre apres le nom de script est : ", sys.argv[1])
# for p in sys.argv :
    # print(p)
for p in sys.argv[1:] :
    print(p)