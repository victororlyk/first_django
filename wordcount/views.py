from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(req):
    return render(req, 'home.html',
                  {'greet': "hello gtetin"})  # to return html
    # file and dictionay to pass some stuff


def count(req):
    fulltext = req.GET['fulltext']
    word_list = fulltext.split(" ")
    words_count = {}
    for word in word_list:
        if word in words_count.keys():
            words_count[word] = words_count[word] + 1
        else:
            words_count[word] = 1
    print(words_count.items(), 'here')
    sorted_words = sorted(words_count.items(), key=operator.itemgetter(1),
                          reverse=True)
    options = {
        'text': fulltext,
        'length': len(word_list),
        'sorted_dictionary': sorted_words
    }
    return render(req, 'count.html', options)


def about(req):
    return render(req, 'about.html')
