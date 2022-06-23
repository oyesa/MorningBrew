## Generating database diagram(ERD) with Django Extensions Automatically For FnD Project.

>  pygraphviz is a Python interface to the GrapthViz grapph layout and visualization package
 * sudo apt install python3-pygraphviz or pip3 install pygraphviz

> installing django-extensions
 * pip3 install django-extensions

> add django-extensions to the installed apps of your django project settings.py.

 * # Application definition
```
INSTALLED_APPS = 
[
    'django.contrib.admin',
     .....

    'django_extensions', # add this line
        
]

```

> To install pydot you need to run this command:

*  pip install pyparsing pydot

> The option GRAPH_MODELS = {} can be used in the settings file to specify default options:

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

> Create a dot file

* ./manage.py graph_models -a > my_project.dot

> Create a PNG image file called my_project_visualized.png with application grouping

* ./manage.py graph_models -a -g -o my_project_visualized.png

> explicit selection of pygraphviz or pydot

* ./manage.py graph_models --pygraphviz -a -g -o my_project_visualized.png
* ./manage.py graph_models --pydot -a -g -o my_project_visualized.png

> Create a dot file for only the 'foo' and 'bar' applications of your project
* ./manage.py graph_models foo bar > my_project.dot

> Create a graph excluding certain models
* $ ./manage.py graph_models -a -X Foo,Bar -o my_project_sans_foo_bar.png

> Create a graph including models matching a given pattern and excluding some of them
> It will first select the included ones, then filter out the ones to exclude
* $ ./manage.py graph_models -a -I Product* -X *Meta -o my_project_products_sans_meta.png

> Create a graph without showing its edges' labels
* $ ./manage.py graph_models -a --hide-edge-labels -o my_project_sans_foo_bar.png

> Create a graph with 'normal' arrow shape for relations
* $ ./manage.py graph_models -a --arrow-shape normal -o my_project_sans_foo_bar.png



### other Setup
> To Group all the application and output into a .png file

* $ python3 manage.py graph_models -a -g -o imagefile_name.png


> Include only some applications

* $ python3 manage.py graph_models app1 app2 -o app1_app2.png

> Include only some specific models

* $ python3 manage.py graph_models -a -I Foo,Bar -o foo_bar.png

> OR exclude certain models

* $ python3 manage.py graph_models -a X Foo,Bar -o no_foo_bar.png 