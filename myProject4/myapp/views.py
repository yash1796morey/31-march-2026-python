from django.shortcuts import render


def search(request):
    return render(request, 'app/search.html')

# def about(request):
#    portfolio = [
#     {
#         "name": "Yash",
#         "age": 30,
#         "profession": "Engineer",
#         "city": "Pune"
#     },
#     {
#         "name": "Harsh",
#         "age": 26,
#         "profession": "Engineer",
#         "city": "Mumbai"
#     }
# ]
#    return render(request, 'app/about.html',{'portfolio':portfolio})

portfolio_list = []

def about(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        if name:
            portfolio_list.append({"name": name})
        if age:
            portfolio_list.append({"age": age})    

    return render(request, 'app/about.html', {'portfolio': portfolio_list})

def career(request):
    jobs = ["Python Developer", "Django Developer", "Backend Developer","Java Developer"]
    return render(request, 'app/career.html', {'jobs': jobs})