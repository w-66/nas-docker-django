from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.

# 我们的投票应用中，我们需要下列几个视图：
#     问题索引页——展示最近的几个投票问题。
#     问题详情页——展示某个投票的问题和不带结果的选项列表。
#     问题结果页——展示某个投票的结果。
#     投票处理器——用于响应用户为某个问题的特定选项投票的操作。

def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, 'polls/index.html', context)

    ### v1 start 更简单的写法如上
    # from django.template import loader
    # return HttpResponse(template.render(context, request))

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # return HttpResponse("Hello, world. You're at the polls index.")
    ### v1 end

def detail(request, question_id):
    ### v2 start  相比于v1的更快捷的方式实现相同的效果
    from django.shortcuts import get_object_or_404, render
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    ### v2 end

    # ## v1 start  对于不存在的信息，抛出404
    # from django.http import Http404
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question does not exist")
    #     # pass
    # return render(request, 'polls/detail.html', {'question': question})
    # ## v1 end

    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    ### v2 当有人对 Question 进行投票后， vote() 视图将请求重定向到 Question 的结果界面
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

    ### v1
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # question = get_object_or_404(Question, pk=question_id) 
            # how old are you? 
        # request.POST['choice'] 
            # 6 
        # selected_choice 
            # 20

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:
        # 使用 F() 避免竞争条件 
        from django.db.models import F
        selected_choice.votes = F('votes') + 1
        # selected_choice.votes += 1,
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))