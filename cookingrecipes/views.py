# A wiew for viewing recipes
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from cookingrecipes.models import Recipe


def home(request):
    return render(request, 'recipes/home.html')

def myRecipes(request):
    try:
        data = Recipe.objects.all()
    except:
        raise "You do not have any recipes"
    return render(request, 'recipes/recipes.html', {'myRecipes':data})

def viewRecipe(request, id):
    recipe = Recipe.objects.get(pk=id)
    return render(request, 'recipes/details.html', {"recipe":recipe})

def addRecipe(request):
    
    title = request.POST.get("title")
    description = request.POST.get("description")
    if title and description:
        
        newRecipe = Recipe(title=title,description=description)
        newRecipe.save()
        return HttpResponseRedirect('/myrecipes')
    
    return render(request, "recipes/addRecipe.html")

def updateRecipe(request, id):
    recipeUpd = Recipe.objects.get(pk=id)
    title = request.POST.get("title")
    description = request.POST.get("description")
    
    
    if title and description:
        
        recipeUpd.title = title
        recipeUpd.description = description
        recipeUpd.save()
        return HttpResponseRedirect(f'/myrecipes/{id}')
    
    return render(request, "recipes/updateRecipe.html", {"details":recipeUpd})

def deleteRecipe(request, id):
    try:
        recipetoDelete = Recipe.objects.get(pk=id)
    except:
        raise "recipe does not exist"
    recipetoDelete.delete()
    return HttpResponseRedirect('/myrecipes')
        
    
    
    