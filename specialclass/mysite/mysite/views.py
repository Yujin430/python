'''
Created on 2015. 12. 8.

@author: Yujin
'''
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')
