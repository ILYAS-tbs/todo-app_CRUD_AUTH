from django.shortcuts import redirect, render


from .models import Todo
from .forms  import TodoForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def get_todos_view(request):

    
    print(request.user)

    user = request.user
    
    todos = Todo.objects.filter(owner = user).order_by("-updated","-created")
   # todos = Todo.objects.all()


    for todo in todos : 
         print(str(todo))

    data = { 
        'todos':todos
    }

    return render(request , 'todo/todos.html', data)


@login_required(login_url='login')
def create_todo_view(request ):
      
    #  form = TodoForm()
      #! we can get the use r easily 
      user = request.user 

      if(request.method =="POST"): 
           form = TodoForm(request.POST)

           if(form.is_valid()):
                todo = form.save(commit=False)
                #! set user (one-to-many {foreign key relationship})
                todo.owner = user
                todo.save()

                print("done ...")
                return redirect('get-todos_url')
           else:
                print("error  ...")
               


      
      else:
           form = TodoForm()
    


      return render(request , 'todo/create-todo.html',{"form":form})

@login_required(login_url='login')
def get_todo_view(request,pk):
         
     #! if todo even exist in the databaese 
     try : 
          todo =Todo.objects.get(id=pk)    
     except Todo.DoesNotExist : 
          print('Not found')
          return render(request, 'todo/not-found.html')

      #* (todo) and  ( todo.owner == request.user)
     #! if todo even exist in the databaese and u have to be the user
     if( todo.owner == request.user  ):
          todo = todo
          return  render(request , 'todo/get-todo.html', { "todo":todo})

     else:
          return redirect('get-todos_url')
          
    


@login_required(login_url='login')
def update_todo_view(request , pk):
     

     todo = Todo.objects.get(id=pk)


     form =TodoForm(instance=todo)
     
     #!! check if the todo in the pk belong to this user --- one can only update his
     if(todo.owner == request.user): 
         
        if (request.method =="POST" ):
            form =TodoForm(instance=todo , data= request.POST)
            if (form.is_valid()): 
                
                form = form.save()
                
                print(" valid --  updated")

                return redirect('get-todos_url')


            else :
                print( ' not valid  - not updated')
        

        else: #! Get 
            
            return render(request,'todo/update-todo.html',{'form':form})
   
     else :      #!! not his todos  --- error 404 

          return render(request,'todo/todos.html')
     

@login_required(login_url='login')
def delete_todo_view(request,pk):
     
     todo = Todo.objects.get(id=pk)

     if( todo.owner == request.user):

          todo = todo.delete() 

          return redirect('get-todos_url')
     
     
     return  redirect('get-todos_url')




def register_user_view(request):
     
     
     if (request.method =="POST"):
          form =UserCreationForm(request.POST)
          if(form.is_valid()):
               
               user = form.save()
               print('form valid --- user added')
               
               return redirect('login')
          else :
               print(f'form - invalied -- will not register user {form.error_messages}')
               return render(request,'registration/register.html' , {"form":form})
     else:
          form =UserCreationForm()

          return render(request,'registration/register.html' , {"form":form})




