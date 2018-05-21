# Balloon Time!
CRUD Clown app


## Installation
```bash
git clone https://github.com/ladydangerdame/BalloonTime.git
cd BalloonTime
createdb balloontime
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
### It's party time! Let's say you are a party planner and clown wrangler.

You've got a lot of clowns to manage and parties to dispatch them to. We need to keep track of all that madness. Luckily we've got Django with its lovely built in ORM (Object-relational mapping) that is super sweet for us to store info about clowns and parties in our database.

I've already done some of the work for you! Have a look in ```settings.py``` to see that the database has been changed from the default sqlite to postgresql. There's some templates and styles (so pretty, am I right?) and stubbed out views.

All we need modify is ```views.py``` and ```models.py```

### Many to many relationships in Django

Flashback! Many to one relationship model:

```python
class Cat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    likes = models.IntegerField(default=0)
```

Our user model comes built in to Django, so for a user to have many cats we've given cats a foreign key for their user association. So how about many to many relationships? How might we do that?

Well, to define a many to many relationship in Django we use the ManyToManyField!

```python
class Party(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Clown(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    parties = models.ManyToManyField(Party)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
```

In the snippet above I have used the ManyToManyField on the Clown model, as parties can have many clowns. However, I could have put the ManyToManyField on the Party model! It does not really matter! You only need to define the relationship once!

If you'd like to read more about Many to Many relationships, you can do so [in the Django docs here!](https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/)


### Class-based views
