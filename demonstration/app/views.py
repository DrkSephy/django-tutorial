from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

def index(request):
	return HttpResponse('Hello World!')

def test(request):
	return HttpResponse('My second view!')

def profile(request):
	parsedData = []
	if request.method == 'POST':
		user = request.POST.get('user')
		jsonList = []
		req = requests.get('https://api.github.com/users/' + user)
		jsonList.append(json.loads(req.content))
		userData = {}
		for data in jsonList:
			userData['name'] = data['name']
			userData['blog'] = data['blog']
			userData['email'] = data['email']
			userData['public_gists'] = data['public_gists']
			userData['public_repos'] = data['public_repos']
			userData['avatar_url'] = data['avatar_url']
			userData['followers'] = data['followers']
			userData['following'] = data['following']
		parsedData.append(userData)
	return render(request, 'app/profile.html', {'data': parsedData})