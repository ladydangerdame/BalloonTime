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

I've already done a little of the work for you, now it's time to write some models and views!
