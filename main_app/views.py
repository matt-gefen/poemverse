from django.shortcuts import render
from django.http import HttpResponse
from .models import Poem
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
import requests
import json
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def poems_index(request):
  linecount = 0

  while int(linecount) >= 30 or int(linecount) == 0:
    response = requests.get('https://poetrydb.org/random').json()
    response = response[0]
    linecount = response['linecount']
  
  s = "\n"
  response['lines'] = s.join(response['lines'])

  user = request.user
  try:
    print(Poem.objects.get(title=response["title"], user=user))
  except:
    print("Does not exist")
  finally:
    return render(request, 'poems/index.html', {'poem':response} )

  
def user_index(request):
  poems = Poem.objects.filter(user=request.user).order_by("-pk")
  for poem in poems:
    s = "\n"
    poem.lines = poem.lines.replace("<br>", s)
  return render(request, 'poems/user_index.html', { 'poems': poems })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('poems_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class PoemCreate(CreateView):
  model = Poem
  fields = ['title', 'author', 'lines']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/poems/myverse'

def poems_add(request):
  form = request.POST
  form.user = request.user
  new_poem = Poem.objects.create(title=form["title"],author=form["author"],lines=form["lines"], user=form.user)
  new_poem.save()
  return redirect('user_index')

class PoemDelete(DeleteView):
  model = Poem
  success_url = '/poems/myverse'