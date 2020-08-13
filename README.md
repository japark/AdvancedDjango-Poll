# AdvancedDjango-Poll
Improvement of "Poll" Tutorial in Django Official Docs. This is the First one in Advanced Django Series.

WARNING!!!
This repository does NOT contain SECRET_KEY item,  
so if you want to run the whole code,  
you need to generate your own SECRET_KEY and save it as "secret_key.json" file like below:

// AdvancedDjango-Poll/secret_key.json  
{  
  "SECRET_KEY": "<<<Enter your generated secret key here!!!>>>"  
}  

Or you can just copy the necessary code to your project.


After git clone, follow these:

  1) Enter the "Django-Board" directory.  
  2) Make virtual environment:  
    - virtualenv venv  
    - venv\Scripts\activate (Or "source venv/bin/activate" in Mac)  
    - pip install -r requirements.txt  
  3) python manage.py migrate  
  4) python manage.py createsuperuser  
    - Fill in username, email address, password, password(again).  
  5) python manage.py runserver  
    - Go to 127.0.0.1:8000/admin  
    - Login with superuser account made above.  
    - You can now control the admin site.  
  6) Go to 127.0.0.1:8000  
    - It's the "Django-Board" website, which is intended to show you.


The core modifications from original tutorial are following :  
  1) Create, Update, Delete polls without entering admin site.  
  2) Realize Add or Delete of choice forms with Javascript.
