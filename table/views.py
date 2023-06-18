from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm
from django.db.models import Min, Avg, Max, Q, F
from django.http import HttpResponse
import openpyxl
import calendar
from django.utils.translation import gettext as _


# Create your views here.


def home(request):  # Функция представления /home
    records = Record.objects.all()  # Берем все записи из БД
    if request.method == 'POST':
        # Принимаем данные из полей ввода данных
        username = request.POST['username']
        password = request.POST['password']
        # Авторизируем
        user = authenticate(request, username=username, password=password)
        # Проверка на авторизацию, если все успешно, переводим на home, иначе на повторную авторизацию
        if user is not None:
            login(request, user)
            messages.success(request, "Вы вошли в аккаунт!")
            return redirect('home')
        else:
            messages.success(request, "Ошибка авторизации. Введите правильные логин и пароль")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):  # Функция представления logout
    logout(request)
    messages.success(request, "Вы вышли из аккаунта!")
    return redirect('home')


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Представления записей
        customer_record = Record.objects.get(id=pk)  # Получаем объекты по primary_key
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Войдите в аккаунт")
        return redirect('home')


def delete_record(request, pk):  # Функция представления удаления записи
    if request.user.is_authenticated:  # Проверяем залогирован пользователь или нет
        # Удаляем по primary_key
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Успешно удалено")
        return redirect('home')
    else:
        messages.success(request, "Войдите в аккаунт")
        return redirect('home')


@login_required  # Декоратор, требующий аутентификации пользователя
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            record = form.save(commit=False)
            record.employee_name = request.user.username  # Установка значения из залогиненного пользователя
            record.save()
            messages.success(request, "Запись добавлена")
            return redirect('home')
    return render(request, 'add_record.html', {'form': form})


# def add_record(request):  # Функция представления добавления записи
#     form = AddRecordForm(request.POST or None)
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             if form.is_valid():
#                 add_record = form.save()
#                 messages.success(request, "Запись добавлена")
#                 return redirect('home')
#         return render(request, 'add_record.html', {'form': form})
#     else:
#         messages.success(request, "Войдите в аккаунт")
#         return redirect('home')


def report(request):  # Функция представления отчёта
    month = request.GET.get('month')  # Получаем номер месяца из report.html
    records = Record.objects.all()  # Получаем все объекты записей
    month_number = None
    if month:
        month_number = int(month)  # Кладем целочисленное значение в month_number от month
        records = records.filter(created_at__month=month_number)  # Фильтруем записи поля created_at с помощью __month
    # Агрегирующие поля для нахождения Min, Avg, Max значений
    aggregation_fields = [
        'iron_concentration',
        'silicon_concentration',
        'aluminum_concentration',
        'calcium_concentration',
        'sulfur_concentration',
    ]
    field_names = {
        'iron_concentration': 'Содержание железа',
        'silicon_concentration': 'Содержание кремния',
        'aluminum_concentration': 'Содержание алюминия',
        'calcium_concentration': 'Содержание кальция',
        'sulfur_concentration': 'Содержание серы',
    }

    aggregation_data = {}
    for field in aggregation_fields:
        field_name = field_names.get(field)
        # Находим Min, Avg, Max значения
        field_data = records.aggregate(
            min_value=Min(field),
            avg_value=Avg(field),
            max_value=Max(field),
        )
        aggregation_data[field_name] = field_data
    # _ Нужно для перевода на русский
    # переводим в слово в нижнем регистре, иначе если не выбран месяц выводим 'все месяца'
    month_name = _(calendar.month_name[month_number]).lower() if month_number else _('все месяца')

    # Словарь из того что выводим после обработки, чтобы в последующем использовать в html, в частности month_name
    context = {
        'records': records,
        'aggregation_data': aggregation_data,
        'month_name': month_name
    }

    return render(request, 'report.html', context)


# Функция представления для импорта файла excel
def add_excel_file(request):
    if request.method == 'POST':
        # Читаем и записываем excel_file
        excel_file = request.FILES['excel_file']
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active
        # Проходимся по полям в excel
        for row in sheet.iter_rows(min_row=2, values_only=True):
            employee_name = row[0]
            raw_material_name = row[1]
            iron_concentration = row[2]
            silicon_concentration = row[3]
            aluminum_concentration = row[4]
            calcium_concentration = row[5]
            sulfur_concentration = row[6]
            # Записываем поля и сохраняем
            if employee_name:
                record = Record(
                    employee_name=employee_name,
                    raw_material_name=raw_material_name,
                    iron_concentration=iron_concentration,
                    silicon_concentration=silicon_concentration,
                    aluminum_concentration=aluminum_concentration,
                    calcium_concentration=calcium_concentration,
                    sulfur_concentration=sulfur_concentration
                )
                record.save()
                messages.success(request, "Запись добавлена")

        return redirect('home')

    return render(request, 'add_excel_file.html')
