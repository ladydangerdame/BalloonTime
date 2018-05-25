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

Go ahead into ```models.py``` and add the ManyToManyField to whichever model you prefer.

If you'd like to read more about Many to Many relationships, you can do so [in the Django docs here!](https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/)


### Class-based views

[Introduction to Class-based views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/intro/)

"Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences and advantages when compared to function-based views:

- Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
- Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components."

This is an example of imperative versus declarative programming! I can spell out each step of what I want a view to do with functions (imperative), or I can use a Class view to handle HTTP requests (GET, POST, etc...) in just a few elegant lines of code. Let's take a peek at the differences:

```python
  def post_party(request):
    form = PartyForm(request.POST)
    if form.is_valid():
        party = form.save(commit = False)
        party.save()
    return HttpResponseRedirect('/')
```

Above is an example of writing an imperative view, and it will get the job done. But we're spelling out each step. Use this form, check if it is valid, then save the input and redirect. Not too bad, but I think we can do better.

```python
class PartyCreate(CreateView):
    model = Party
    fields = ["title","location","description"]
    success_url = reverse_lazy("party_list")
```

We cut down to 4 lines from 6. Not that drastic, but cleaner, clearer, and does the same work. With other views, using a class can really cut down the lines you write more drastically.

Using the stubbed out views, and the [documentation](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/), complete the views in your ```views.py```!

### Your Task:

Create CRUD views (see note below), form fields, and URLs for creating clowns and assigning them to parties. (You already can do this through the Django admin panel since you used the ManyToManyField! It's a matter of mapping that to your front end the same way as Parties!)

(*Note*: Django, on its own doesn't support full CRUD - no PUT or DELETE methods. Go ahead an just use GET/POST to approximate these for now, as shown in the `completed` branch of this repo)

#### BONUS

As noted above, your Django app doesn't support PUT and DELETE methods by default. This is a common problem that other developers are well aware of. Read up on the [Django REST framework](http://www.django-rest-framework.org/#example) if you'd like to see a way to implement legit full CRUD!

#### Hot tip:

There is a `completed` branch for this code if you should get stuck. However, it doesn't include the bonus work!
