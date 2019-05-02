from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()
    #공백 기준 나누기
    word_dictionary = {}
    #빈 사전형 객체

    for word in word_list:
        if word in word_dictionary:
            # 한번 등장했던(사전 안에 있는) 단어 
            word_dictionary[word] += 1
        else:
            # 새로운 (사전 안에 없는) 단어
            word_dictionary[word] = 1
            # 해당하는 word를 key값 삼아서 value를 1로 해라.

    return render(request, 'result.html', {'fulltext': full_text, 'total': len(word_list)})