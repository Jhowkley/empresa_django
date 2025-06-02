from django.shortcuts import render
from .models import AboutSection, HomeSection, TeamMember, ContactMessage,ImageSlider, Servico, Depoimento


def home(request):
  sliders = ImageSlider.objects.all()
  sections = HomeSection.objects.all()
  return render(request,'home.html',{'sliders':sliders,'sections':sections})

def about(request):
  sections = AboutSection.objects.all()
  return render(request,'about.html',{'sections':sections})

def team(request):
  team_members = TeamMember.objects.all()
  return render(request,'team.html',{'team_members':team_members})

def contact(request):
  if request.method == 'POST':
    ContactMessage.objects.create(
      name = request.POST['name'],
      email = request.POST['email'],
      #subject = request.POST['subject'],
      message = request.POST['message']
    )
    return render(request,'contact.html',{'message': 'Mensagem enviada com sucesso!'})
  return render(request, 'contact.html')

def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})

def testimonials_view(request):
    depoimentos = Depoimento.objects.order_by('-data')
    return render(request, 'testimonials.html', {'depoimentos': depoimentos})