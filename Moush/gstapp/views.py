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
