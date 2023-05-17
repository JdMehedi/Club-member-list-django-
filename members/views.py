from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('member_list.html')
    context = {'members': members, }
    return HttpResponse(template.render(context, request))

def details(request, id):
  members = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))


