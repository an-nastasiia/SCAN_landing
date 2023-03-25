from django.shortcuts import render


def main(request):
    template = 'base.html'
    return render(request, template)
