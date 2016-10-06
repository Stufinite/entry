from django.shortcuts import render

def entry(request):
		return render(request, 'entry/entry.html')
