from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request,'htmlpages/home.html')
def displaySportsNews(request):
    return render(request,'htmlpages/sportsnews.html')
def displaypolicsnews(request):
    return render(request,'htmlpages/politcsnews.html')
