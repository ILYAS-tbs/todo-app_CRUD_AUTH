## simple to do app - full CRUD

##  & authentication : Resigter , login && authorization for resources(permissions required)


## tailwind configuration to run with django templetes (no PIP package ..)
``` javascript 
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./backend/*/templates/*/*.html'],
  theme: {
    extend: {},
  },
  plugins: [],
  prefix :'tw-'
}

``` 
## tailwind run command & build 

``` bash 
npx tailwindcss -i ./backend/todo/static/css_input/input.css -o ./backend/todo/static/css/output.css  --watch

``` 
### how to run the app 

# 1.create virtual environment: 
 - insall requrements 
```bash 
  python -m venv venv
```

# 2.activate it : 
 - insall requrements 
```bash 
  source venv/bin/activate
```

# 3. install dependencies : 
```bash 
  pip install -r requirements.txt
``` 
# ur project structure should look like : 
  - backend/
  - venv/

# make sure the environment is activated  : 


# follow these commands : 

```bash 
   cd backend/
   python manage.py makemigrations && python manage.py migrate && python manage.py runserver
   
```


# links - webpages in this app are : 

## all are : localhost:8000/ ... ( or ur domain name with the port the app is in )
  - if you are using nginx configure ur reverse-proxy to port 8000 
  - or run the server with this command instead ( ex : i want port 8080)
  -  ``` bash 
       python manage.py runserver 0.0.0.0:8080
     

 - todo/ auth/ login/ [name='login']
 - todo/ auth/ logout/ [name='logout']

###  - - all below require u to be logged in (require authentication)
 - todo/todos : get the user todos
 - todo/create : create new one 
 - todo/ todos/ 
 - todo/ create/ 
 - todo/ get-todo/<int:pk> 
 - todo/ update-todo/<int:pk> 
 - todo/ delete-todo/<int:pk> 

