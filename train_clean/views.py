from datetime import datetime, timedelta

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Line, Train, CleanRecords


def index(request):
    lines = Line.objects.all().order_by('name')
    line_trains_list = []
    for line in lines:
        trains_data = []
        for train in line.trains.all().order_by("number"):
            last_front_record = None
            last_side_record = None
            front_queryset = train.records.filter(clean_front=True).order_by('-clean_date')
            if front_queryset.exists():
                last_front_record = front_queryset[0]
            side_queryset = train.records.filter(clean_front=False).order_by('-clean_date')
            if side_queryset.exists():
                last_side_record = side_queryset[0]
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            trains_data.append(
                {
                    "number": train.number,
                    "clean_front_date": last_front_record.clean_date.strftime("%Y-%m-%d") if last_front_record else "",
                    "clean_side_date": last_side_record.clean_date.strftime("%Y-%m-%d") if last_side_record else "",
                    "clean_front_days_passed":
                        int((today-last_front_record.clean_date.replace(hour=0, minute=0, second=0, microsecond=0))
                            / timedelta(days=1)) if last_front_record else 0,
                    "clean_side_days_passed":
                        int((today-last_side_record.clean_date.replace(hour=0, minute=0, second=0, microsecond=0))
                            / timedelta(days=1)) if last_side_record else 0,
                }
            )

        line_trains_list.append(
            {
                "name": line.name,
                "trains_data": trains_data
            }
        )
    return render(request, 'train_clean/dashboard.html', {"line_trains_list": line_trains_list})


def clean(request):
    lines = Line.objects.all()
    return render(request, 'train_clean/tables.html', {"lines": lines, "today": datetime.now().strftime("%Y-%m-%d")})


@csrf_exempt
def line_trains(request):
    line_id = request.POST['line']
    trains = list(Train.objects.filter(line__id=line_id).order_by('number').values())
    return JsonResponse(trains, safe=False)


@csrf_exempt
def save(request):
    clean_type = request.POST['clean_type']
    date_str = request.POST['date']
    print(date_str)
    train_id_list = request.POST.getlist('train')
    for train_id in train_id_list:
        train = Train.objects.get(id=train_id)
        CleanRecords.objects.create(train=train, clean_front=(clean_type=="true"), clean_date=datetime.strptime(date_str, "%Y-%m-%d"))
    return render(request, 'train_clean/success.html')
