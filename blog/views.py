from django.http import HttpResponse
from django.shortcuts import render
from .forms import LinkForm
from .myutils import csgo

adam_posts = []
for i in reversed(range(296, 500)):
    i = 'adam24live/' + str(i)
    adam_posts.append({'post_id': i})


def contact(request):
    context = {
        #smth
    }
    return render(request, 'blog/contact.html', context)


def test(request):
    return render(request, 'blog/testing_stuff.html')


def stuff(request):
    return render(request, 'blog/stuff.html')


def hire_me(request):
    return render(request, 'blog/hire-me.html')


def bunq(request):
    return render(request, 'blog/bunq.html')


# ----------> CS GO
def csgo_stats(request):
    if request.method == 'POST':
        print('got post request here boi')
        form = LinkForm(request.POST)
        if form.is_valid():
            game_data = csgo.get_match_stats(form.cleaned_data['link_to_game'])
            match_started_at = csgo.epoch_to_string(game_data['started_at'])
            results = {
                'game_data': game_data,
                'match_start': match_started_at
            }
            return csgo_results(request, results)
    form = LinkForm()
    return render(request, 'blog/csgo_stats.html', {'form': form})


def csgo_results(request, results):
    game_results = {
        'results': results
    }
    return render(request, 'blog/csgo_results.html', game_results)
# ----------> CS GO


def blog_home(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/blog-related/blog-home.html', context)


def blog_contribute(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/blog-related/blog-contribute.html', context)


def blog_interviews(request):
    return render(request, 'blog/blog-related/blog-interviews.html')


def code_hello(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/code-related/code-hello.html', context)


def crash_courses(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/crash-courses.html', context)


def blog_tg_stuff(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/blog-related/blog-tg-stuff.html', context)


# ----------------- adam section
def ams_adam24live(request):
    context = {
        'adam_posts': adam_posts
    }
    return render(request, 'blog/amsterdam/ams-adam24live.html', context)


def ams_guide(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/amsterdam/ams_guide.html', context)


def ams_quick_facts(request):
    return render(request, 'blog/amsterdam/ams-quick-facts.html')


def ams_map(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/amsterdam/ams_map.html', context)


def ams_stuff(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/amsterdam/ams_stuff.html', context)


def ams_hello(request):
    return render(request, 'blog/amsterdam/ams_main.html')


def ams_contribute(request):
    return render(request, 'blog/amsterdam/ams-contribute.html')


# --------------- hello page
def hello(request):
    context = {
        'ayy': 'lmao'
    }
    return render(request, 'blog/hello.html', context)


def rat(request):
    return render(request, 'blog/full-metal-rat.html')


# --------------- CODE SECTION
def javascript_clock(request):
    return render(request, 'blog/code-related/javascript-code-timer.html')


def javascript_intro(request):
    return render(request, 'blog/code-related/intro-to-javascript.html')


def python_first_steps(request):
    return render(request, 'blog/code-related/python-first-steps.html')


def python_intro(request):
    return render(request, 'blog/code-related/intro-to-python.html')


def java_intro(request):
    return render(request, 'blog/code-related/intro-to-java.html')


def java_first_steps(request):
    return render(request, 'blog/code-related/java-first-steps.html')


def code_vcs_git(request):
    return render(request, 'blog/code-related/version-control-and-git.html')


def code_common(request):
    return render(request, 'blog/code-related/common-knowledge.html')


def code_project_ideas(request):
    return render(request, 'blog/code-related/project-ideas.html')


def code_useful_links(request):
    return render(request, 'blog/code-related/useful-links.html')


def code_howto(request):
    return render(request, 'blog/code-related/how-to-start.html')


def code_language(request):
    return render(request, 'blog/code-related/choose-your-programming-language.html')


def html_css_stuff(request):
    return render(request, 'blog/code-related/html-css-frontend.html')


def javascript_first_steps(request):
    return render(request, 'blog/code-related/javascript-first-steps.html')
