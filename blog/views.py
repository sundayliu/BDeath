from django.shortcuts import render

# Create your views here.
from mcbv.list_custom import DetailListCreateView
from mcbv.list import ListView
from blog.models import Post,Comment
from blog.forms import CommentForm
import time
from calendar import month_name

class PostView(DetailListCreateView):
    detail_model = Post
    list_model = Comment
    modelform_class = CommentForm
    related_name = "comments"
    fk_attr = "post"
    template_name = "blog/post.html"
    
class Main(ListView):
    list_model = Post
    paginate_by = 10
    template_name = "blog/list.html"
    
    def months(self):
        if not Post.obj.count():
            return list()
        
        current_year,current_month = time.localtime()[:2]
        first = Post.obj.order_by("created")[0]
        first_year = first.created.year
        first_month = first.created.month
        months = list()
        
        for year in range(current_year,first_year-1,-1):
            start = 12
            end = 0
            if year == current_year:
                start = current_month
            if year == first_year:
                end = first_month - 1
            
            for month in range(start,end,-1):
                if Post.obj.filter(created__year=year,created__month=month):
                    months.append((year,month,month_name[month]))
        return months

class ArchiveMonth(Main):
    paginate_by = None
    def get_list_queryset(self):
        year,month = self.args
        return Post.obj.filter(created__year=year,created__month=month).order_by("created")
        
        