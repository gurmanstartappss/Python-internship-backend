"""django then fast api

django=python web framework used to build secure scalable and maintainable web applications

build in
url rooting
views
templates
database model
orm
forms
authetications
admin panel 
security

mvt=model responsible for data base and data,view=applications/business logic and request handling,tempate=used for ui/html 

django admin=manage create your project
django-admin startproject config = creates a config folder and manage.py when directly in the directory
django-admin startproject school management = creates a config folder and manage.py in school management

wsgi server in config folder mainly used

manage.py=server create, migration,django admin,user create

python manage.py reserver = server run
python manage.py startapp.appname
python manage.py makemigrations = dtaabase update or fieled change
python manage.py migrate
python manage.py createuperuser = server super user create 
python manage.py shell=  orm related

add app name students
then migrate 
first create a super user
then runserver
#get, post, header, cookies, user, query , body

-------------------------DAY 2--------------------------

{% comment %} 
django template use {{variable}}

if condition
{% if is active %}
        <p>Student is active</P>
{% else %}
        <p>Student is inactive</p>
      
  {% end if%} 
{% endcomment %}
"""