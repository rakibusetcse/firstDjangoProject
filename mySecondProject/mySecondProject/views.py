from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremove= request.POST.get('newlineremove','off')
    extraspaceremover= request.POST.get('extraspaceremover','off')
    charactercounter= request.POST.get('charactercounter','off')
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+ char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext= analyzed
        #return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed= analyzed+ char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremove=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("No")
        print("pre",analyzed)
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover=="on":
        analyzed= ""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed=analyzed +char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if charactercounter=="on":
        analyzed = 0
        for char in djtext:
            if char !=" ":
                analyzed= analyzed+1
        params = {'purpose': 'Count the Character', 'analyzed_text': analyzed}
        #djtext = analyzed
        #return render(request, 'analyze.html', params)
    #else:
        #return HttpResponse("Error")
    if(removepunc!="on" and fullcaps!="on" and newlineremove!="on" and extraspaceremover!="on" and charactercounter!="on"):
        return HttpResponse("Please select any operation and Try again")

    return render(request, 'analyze.html', params)