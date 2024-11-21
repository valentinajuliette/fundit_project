from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, SubscriptionForm
from .models import CausaSocial, ODS

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        subscription_form = SubscriptionForm(request.POST)
        
        if user_form.is_valid() and subscription_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            subscription = subscription_form.save(commit=False)
            subscription.user = user
            subscription.save()
            
            subscription_form.save_m2m()  # Guardar selección de ODS
            login(request, user)
            return redirect('index')
    else:
        user_form = UserRegistrationForm()
        subscription_form = SubscriptionForm()
    
    return render(request, 'register.html', {
        'user_form': user_form,
        'subscription_form': subscription_form,
    })

def causas(request):
    # Recupera todas las causas y ODS para mostrar en la página
    ods_list = ODS.objects.all()
    causas = CausaSocial.objects.all()

    # Verifica si hay un filtro aplicado por ODS
    ods_id = request.GET.get('ods')
    if ods_id:
        causas = causas.filter(ods_relacionados=ods_id)

    return render(request, 'causas.html', {
        'causas': causas,
        'ods_list': ods_list,
    })
