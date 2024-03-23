from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from web.models import Users

from web.forms import RegisterForm, Balancee

from web.models import Tea

from web.models import Balance

from web.forms import BasketA


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = BasketA(request.POST)
        tea_id = request.POST['tea_id']
        print(tea_id)
        db = Balance.objects.get(user_id=request.user.id)
        if int(db.money) > int(tea_id):
            db.money = int(db.money) - int(tea_id)
            db.save()
        else:
            print('лох')

    try:
        profile_balance = int(str(Balance.objects.filter(user_id=request.user.id)[0]))
    except:
        profile_balance = 0

    tea_cards = Tea.objects.all()
    return render(request, 'web/main.html', {'tea_cards': tea_cards, 'bal': profile_balance}, )
# Create your views here.

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/reg.html'
    success_url = reverse_lazy("web:profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def balance_view(request):


    if request.method == 'POST':

        if request.POST['number'] == '' or request.POST['people'] == '' or request.POST['cvv'] == '' or request.POST['money'] == '' :
            print('hui')
        else:

            form = Balancee(request.POST)
            if Balance.objects.filter(user_id=request.user.id):
                inp = request.POST.get('money')
                db = Balance.objects.get(user_id=request.user.id)

                db.money = int(str(Balance.objects.filter(user_id=request.user.id)[0])) + int(str(inp))
                db.save()

                return redirect('web:profile')

            elif form.is_valid():
                obj = form.save(commit=False)
                obj.user_id = request.user.id
                obj.save()
                form.save()
                return redirect('web:profile')
            else:
                print('err')

    return render(request, 'web/add.html')


def busket_view(request):
    bal = Balance.objects.filter(user_id=request.user.id)[0]



    return render(request, 'web/korzina.html', {'bal': bal})
