# Ex.04 Design a Website for Server Side Processing
## Date:07.03.2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
gst.html
<html>
    <head>
        <title>Bill</title>
        <style>
            body{
                text-align: center;
                background: rgb(19, 83, 83);
            }
            .box{
                width:500px;
                margin: 150px auto;
                padding: 20px;
                background: lightcoral;
                color:black;
                border: dashed 4px maroon;
            }
            h1{color: rgb(5, 28, 84);}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>TOTAL GST AMOUNT</h1>
            <form method="POST">
                {% csrf_token %}
                Price:
                <input type="number" name="Price" required>
                <br>
                <br>
                GST%:
                <input type="number" name="GST" required>
                <br>
                <br>
                <button type="submit">Calculate</button>
                <br>
                <br>
                TOTAL:
                <input type="number" value="{{Total}}">
            </form>
        </div>
    </body>
</html>

views.py
from django.shortcuts import render

def calculate_Total(request):

    P = 0
    GST = 0
    Total = 0

    if request.method == "POST":
        P = float(request.POST.get('Price', 0))
        GST = float(request.POST.get('GST', 0))
        Total = P + (P * GST / 100)

        print("Price =", P)
        print("GST =", GST)
        print("Total =", Total)

    return render(request, 'gstapp/gst.html', {'P': P, 'GST': GST, 'Total': Total})

    urls.py
    from django.urls import path
from gstapp import views
urlpatterns = [path('', views.calculate_Total, name='Total')]

```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (32).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (31).png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
