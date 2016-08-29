from django.db import models
from django.core.urlresolvers import reverse


class Message(models.Model):
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email


# *******************************************************************
#                              PROFILE
# *******************************************************************

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(default='default/project.png', upload_to='avatar')

    send_email_messages = models.BooleanField(blank=True, default=True)

    @property
    def full_name(self):
        return '%s %s ' % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


class Link(models.Model):
    profile = models.ForeignKey(Profile, related_name='link_list')
    name = models.CharField(max_length=120)
    url = models.CharField(max_length=250)
    icon_class = models.CharField(max_length=20)


class SkillDescription(models.Model):
    profile = models.ForeignKey(Profile, related_name='skill_description_list')
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title


# *******************************************************************
#                              PROJECT
# *******************************************************************

class Skill(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Project(models.Model):
    slug = models.CharField(unique=True, max_length=50)
    title = models.CharField(max_length=120)
    body = models.TextField()
    skill_list = models.ManyToManyField(Skill)
    picture = models.ImageField(default='default/project.png', upload_to='p_img_preview')

    created_at = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:project-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']


class BlockOfSkill(models.Model):
    project = models.ForeignKey(Project, related_name='block_skill_list')
    skill_list = models.ManyToManyField(Skill)

    def __str__(self):
        return ', '.join([str(s) for s in self.skill_list.all()])


class Picture(models.Model):
    project = models.ForeignKey(Project, related_name='pic_list')
    title = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='p_img')

    def __str__(self):
        return 'Picture: %s; %s' % (str(self.project), self.title[:15])
