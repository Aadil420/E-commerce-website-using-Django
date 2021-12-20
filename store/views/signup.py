from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class signup(View):
     def get(self , request):
           return render(request, 'signup.html')
     def post(self , request):
          postdata = request.POST
          first_name = postdata.get('firstname')
          last_name = postdata.get('lastname')
          phone = postdata.get('phone')
          email = postdata.get('email')
          password = postdata.get('password')
          # validation
      
          value = {
              'first_name': first_name,
              'last_name': last_name,
              'phone': phone,
              'email': email
          }
          error_message = None
        
      
               
                  
      
      
          customer = Customer(first_name=first_name,
                          last_name=last_name,
                          phone=phone,
                          email=email,
                          password=password)
      
          error_message = self.validateCustomer(customer)
      
      
          if not error_message:
               print(first_name, last_name, phone, email, password)
               customer.password = make_password(customer.password)
               customer.register()
               return redirect('homepage')
      
          else:
               data = {
              'error': error_message,
              'values': value
           }
               return render(request, 'signup.html', data)


     def validateCustomer(self , customer):
         error_message = None
         if (not customer.first_name):
             error_message = "First Name Required"
         elif len(customer.first_name) < 4:
             error_message = "First must be greater than 4 character"
         if(not customer.last_name):
             error_message = "Last Name Required"
         elif len(customer.last_name) < 4:
             error_message = 'Last Name must be 4 char long or more'
         elif (not customer.phone):
             error_message = 'Phone Number required'
         elif len(customer.phone) < 10:
             error_message = 'phone number be 10 char long'
         elif len(customer.password) < 6:
             error_message = 'password must be 6 char long'
         elif len(customer.email) < 5:
             error_message = 'Email must be 5 chr long'
         elif customer.isExits():
             error_message = 'Email Address Already Registered'
     
             return error_message
           
      