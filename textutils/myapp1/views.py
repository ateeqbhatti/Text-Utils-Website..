from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request): 
    return render(request,'index.html')
def index2(request): 
    return render(request,'index2.html')
    
def analyze(request):
    antext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newline=request.POST.get('newline','off')
    extraspace=request.POST.get('extraspace','off')
    counter=request.POST.get('counter','off')
    
    if removepunc=="on":
        analyzed=""
        punctuations='''! " # $ % & ' ( ) * + , - . / : ; ? @ [ \ ] ^ _ ` { | } ~ '''
        for char in antext:
            if char not in punctuations:
                analyzed=analyzed+char
        params= {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        antext=analyzed        
    
    if(uppercase=="on"):
        analyzed=""
        for char in antext:
            analyzed=analyzed+char.upper()
        params= {'purpose':'Upper Case', 'analyzed_text':analyzed}
        antext=analyzed 
        
    if(newline=="on"):
        analyzed=""
        for char in antext:
            if char !="\n" and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'New line remover', 'analyzed_text':analyzed}
        antext=analyzed 
        
    if(extraspace=="on"):
        analyzed=""
        for index, char in enumerate (antext):
            if antext[index] == "" and antext[index+1]=="":
                pass
            else:
                 analyzed=analyzed+char
        params={'purpose':'Extra Space remover', 'analyzed_text':analyzed}
        antext=analyzed 
        
    if(counter=="on"):
        analyzed=""
        for index, char in enumerate (antext):
            index=index+1
        analyzed=index
        params={'purpose':'Words Counter', 'analyzed_text':analyzed}
        
    
            
        
        
    if(counter!="on" and extraspace!="on" and newline != "on" and uppercase!="on" and removepunc!="on"):
        return HttpResponse("Please select the Desired Operation")
    return render(request,'analyze.html',params)
    
