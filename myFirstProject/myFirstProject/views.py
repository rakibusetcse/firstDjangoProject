from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

    #return HttpResponse("Home")

def analyze(request):
    djtext=request.GET.get('text', 'default')
    removepunc= request.GET.get('removepunc','off')
    fullcaps= request.GET.get('fullcaps','off')
    newlineremove= request.GET.get('newlineremove','off')
    extraspaceremover= request.GET.get('extraspaceremover','off')
    charactercounter= request.GET.get('charactercounter','off')
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+ char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed= analyzed+ char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremove=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extraspaceremover=="on":
        analyzed= ""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed=analyzed +char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charactercounter=="on":
        analyzed = 0
        for char in djtext:
            if char !=" ":
                analyzed= analyzed+1
        params = {'purpose': 'Count the Character', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
