from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .forms import IndexForms
from datetime import datetime, timedelta


class IndexView(View):
    index_form = IndexForms

    def get(self, request):
        form = self.index_form()
        return render(request, 'cal_time/index.html', {'form': form})

    def post(self, request):
        form = self.index_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            exit_time = self.cal_time(cd['entry_time'], int(cd['holidays']),  int(cd['two_days_weekend']))
            return JsonResponse({'response': exit_time}, status=200)
        else:
            return JsonResponse({'response': 'ورودی اشتباه'}, status=422)

    def cal_time(self, entry_time, holidays, two_days_weekend):
        lunch_time = 30
        hour, minute, second = str(entry_time).split(":")
        days_of_week = 5 - holidays if two_days_weekend else 5
        regular_day_minutes = 480
        minutes_for_th = 240

        ent = datetime.now().replace(
            hour=int(hour),
            minute=int(minute),
            second=int(second)
        )



        exit_time = ent + timedelta(minutes=regular_day_minutes + lunch_time + (minutes_for_th/days_of_week if two_days_weekend else 0))
        return f'زمان خروج شما ------>>   {exit_time.hour}:{exit_time.minute}'
