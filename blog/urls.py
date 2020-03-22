from django.urls import include, path

from . import views

urlpatterns = [
    # main page
    path('', views.hello, name='hello-home'),
    path('full-metal-rat/', views.rat, name='hello-rat'),
    path('test/', views.test, name='hello-test'),
    # one-offs
    path('bunq/', views.bunq, name='bunq'),
    path('contact/', views.contact, name='contact'),
    path('faceit/', views.csgo_stats, name='csgo-stats'),
    path('hire-me/', views.hire_me, name='hire-me'),
    # blog
    path('blog/', views.blog_home, name='blog-welcome'),
    path('blog/main/', include('posts.urls')),
    path('blog/tg-stuff', views.blog_tg_stuff, name='blog-tg-stuff'),
    path('blog/interviews', views.blog_interviews, name='blog-interviews'),
    path('blog/contribute', views.blog_contribute, name='blog-contribute'),
    # path('crash-courses', views.crash_courses, name='blog-crash-courses'),
    # Amsterdam
    path('amsterdam/', views.ams_hello, name='ams-hello'),
    path('amsterdam/guide', views.ams_guide, name='ams-guide'),
    path('amsterdam/quick-facts-about-Amsterdam', views.ams_quick_facts, name='ams-quick-facts'),
    path('amsterdam/map', views.ams_map, name='ams-map'),
    path('amsterdam/stuff', views.ams_stuff, name='ams-stuff'),
    path('amsterdam/adam24live', views.ams_adam24live, name='ams-adam24live'),
    path('amsterdam/contribute', views.ams_contribute, name='ams-contribute'),
    # General code stuff
    # main
    path('code/', views.code_hello, name='code-hello'),
    # starter pack
    path('code/how-to-start-coding', views.code_howto, name='code-howto'),
    path('code/choose-your-language', views.code_language, name='code-language'),
    # general knowledge
    path('code/every-coder-should-know', views.code_common, name='code-common'),
    path('code/html-css', views.html_css_stuff, name='code-html-css'),
    path('code/vcs-git', views.code_vcs_git, name='code-vcs-git'),
    # further reading
    path('code/project-ideas', views.code_project_ideas, name='code-project-ideas'),
    path('code/useful-links', views.code_useful_links, name='code-links'),
    # JS
    path('code/javascript/intro', views.javascript_intro, name='js-intro'),
    path('code/javascript/first-steps', views.javascript_first_steps, name='js-intro'),
    path('code/javascript/examples/js-clock', views.javascript_clock, name='js-clock'),
    # Python
    path('code/python/intro', views.python_intro, name='python-intro'),
    path('code/python/first-steps', views.python_first_steps, name='python-first-steps'),
    # Java
    path('code/java/intro', views.java_intro, name='java-intro'),
    path('code/java/first-steps', views.java_first_steps, name='java-first-steps')
]
