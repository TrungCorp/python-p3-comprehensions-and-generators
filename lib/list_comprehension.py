#!/usr/bin/env python3

def return_evens(num_list):
    list_obj = [ k for k in num_list if (k%2 ==0)]
    return list_obj

def make_exclamation(sentence_list):
    new_list = [k +"!" for k in sentence_list ]
    return new_list