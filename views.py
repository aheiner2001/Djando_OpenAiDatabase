from django.shortcuts import render

# Create your views here.

from .forms import QueryForm
from .utils import generate_sql_query
from django.db import connection
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")  # Add this view

def contact(request):
    return render(request, "contact.html")  # Add this view

def slammmy(request):
    return render(request, "biggo.html")

def query_view(request):
      results = None
      if request.method == 'POST':
          form = QueryForm(request.POST)
          if form.is_valid():
              prompt = form.cleaned_data['prompt']
            #   prompt2 = form.cleaned_data['preset_idea']
              sql_query = generate_sql_query(prompt)
              with connection.cursor() as cursor:
                  cursor.execute(sql_query)
                  results = cursor.fetchall()
      else:
          form = QueryForm()
      return render(request, 'query.html', {'form': form, 'results': results})
