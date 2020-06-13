from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html')

def count(request):
    data = request.GET['fulltextarea']
    convert = data.title()
    word_list = convert.split()
    list_length = len(word_list)
    
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    
    sorted_list = sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'Yourtext':data,'Length':list_length,'worddictionary':sorted_list})


def about(request):
    return render(request,'about.html')