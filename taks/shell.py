from polls.models import User, Message
User.objects.all()
Message.objects.all()

#from django.utils import timezone
#q = Question(question_text="What's new?", pub_date=timezone.now())

q = User(cookie="What's new?")
q.save()

User.objects.all()


##########

Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')

from django.utils import timezone
current_year = timezone.now().year


Question.objects.get(pub_date__year=current_year)
Question.objects.get(id=2) #none

q = Question.objects.get(pk=1) # primary-key
q.was_published_recently()

q = Question.objects.get(pk=1)
q.choice_set.all()

q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
c.question
q.choice_set.all()
q.choice_set.count()

Choice.objects.filter(question__pub_date__year=current_year)
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()