from django.shortcuts import render

from app.blog.models import Post


def school_list(request):
    posts = Post.objects.order_by(id=school_list)
    context = {
        'schools': school_list,
    }

    return render(
        request=request,
        context=context,
    )


def school_detail(request, school_id):
    post = Post.objects.get(id=school_id)
    context = {
        'student': student,
    }

    return render(request, 'blog/school_detail.html', context)
