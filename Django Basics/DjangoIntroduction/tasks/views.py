from django import http

from django.shortcuts import render

from tasks.models import Task


# Create your views here.
# FBV
# A function that has one or more params
# Returns a response


# Взима един параметър
#def index(request):
    ##Трябва да връща response
   # content = "<h1>IT works!</h1>" + \
      #  "<p>You are welcome to my project</p>" + \
      #  "<ul></ul>"

   # return http.HttpResponse(content)


def index(request):

    title_filter = request.GET.get('filter', None)
    tasks = Task.objects.all()

    if not tasks:
        return http.HttpResponse('<h1> No tasks!</h1>')

    result = []

    #If there is filter
    if title_filter:
        tasks = tasks.filter(title__contains=filter.lower()) #<-- Case Sensitive

    for task in tasks:
        result.append(f"""
        <li>
        <h2>{task.title}</h2>
        <p>{task.description}</p>
        </li>
        """)

        ul = f"<ul>{''.join(result)}</ul>"

        content = f"""
        <h1>{len(tasks)} Tasks </h1>
        {ul}"""


        return http.HttpResponse(content)