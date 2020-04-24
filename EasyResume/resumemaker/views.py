from django.shortcuts import render

# Create your views here.
def Home(request):
	template_name="resume/Home.html"
	return render(request,template_name,{})

def resumebuilder(request):
	template_name="resume/builder.html"
	return render(request,template_name,{})