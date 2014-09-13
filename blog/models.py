from django.db.models import *
from shared.utils import *
from django.core.mail import send_mail

# Create your models here.
notify = False

class Post(BaseModel):
    title = CharField(max_length=60)
    body = TextField()
    created = DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    def __unicode__(self):
        return self.title
    
class Comment(BaseModel):
    author = CharField(max_length=60,blank=True)
    body = TextField()
    post = ForeignKey(Post,related_name="comments",blank=True,null=True)
    created = DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u"%s: %s" % (self.post,self.body[:60])
    def save(self,*args,**kwargs):
        if notify:
            tpl = "Comment was added to '%s' by '%s':\n\n%s"
            message = tpl % (self.post,self.author,self.body)
            from_addr = "no-reply@sundayliu.com"
            recipient_list = ["admin@sundayliu.com"]
            send_mail("New comments added",message,from_addr,recipient_list)
        super(Comment,self).save(*args,**kwargs)