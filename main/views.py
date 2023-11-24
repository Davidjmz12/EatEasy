import datetime
from math import ceil

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from login.models import Restaurant, User
from main.models import Dish, Rating

from Levenshtein import distance as distanceLev


def are_strings_similar(str1, str2, threshold=3):
    distance = distanceLev(str1.lower(), str2.lower())
    return distance <= threshold


# Create your views here.
def index(request):
    if not request.user.is_superuser:
        if request.method == "POST":
            price = ceil(getMax(Restaurant.objects.all()))
            loc = request.POST.get("location", " ")
            location = loc if loc != "" else "all"
            return HttpResponseRedirect(
                reverse(
                    "main:search",
                    kwargs={
                        "locationEntry": location,
                        "priceEntry": price,
                        "veganEntry": "False",
                        "vegetEntry": "False",
                        "celEntry": "False",
                        "nutsEntry": "False",
                        "lactoseEntry": "False",
                    },
                )
            )
        else:
            return render(request, "main/index.html")
    else:
        return HttpResponseRedirect(reverse("super:index"))


def subsetPreferences(rest, veget, cel, vegan, nuts, lactose):
    return [
        oneRest
        for oneRest in rest
        if any(
            [
                (veget and item.vegetarian or not veget)
                and (cel and item.celiac or not cel)
                and (vegan and item.vegan or not vegan)
                and (nuts and item.nuts_free or not nuts)
                and (lactose and item.lactose_free or not lactose)
                for item in oneRest.my_dishes.all()
            ]
        )
    ]


def subsetCity(rest, loc):
    return (
        rest
        if loc == "all"
        else [oneRest for oneRest in rest if are_strings_similar(oneRest.city, loc)]
    )


def avg(v):
    return 0 if len(v) == 0 else sum(v) / len(v)


def max0(v):
    if len(v) == 0:
        return 0
    else:
        return max(v)


def subsetPrice(rest, price):
    return [
        oneRest
        for oneRest in rest
        if avg([item.price for item in oneRest.my_dishes.all()]) <= price
    ]


def queryRestaurants(cel, vegan, veget, nuts, lactose, loc, price):
    rest = Restaurant.objects.all()
    rest = subsetPreferences(rest, veget, cel, vegan, nuts, lactose)
    rest = subsetCity(rest, loc)
    rest = subsetPrice(rest, price)
    return rest


def getMax(restaurants):
    avg_prices = []
    for oneRest in restaurants:
        my_dishes = [item.price for item in oneRest.my_dishes.all()]
        avg_prices.append(sum(my_dishes) / len(my_dishes)) if len(my_dishes) != 0 else 0
    return max0(avg_prices)


def search(
    request,
    locationEntry,
    celEntry,
    vegetEntry,
    veganEntry,
    nutsEntry,
    lactoseEntry,
    priceEntry,
):
    if request.method == "POST":
        cel = request.POST.get("celiac", "off") == "on"
        veget = request.POST.get("vegetarian", "off") == "on"
        vegan = request.POST.get("vegan", "off") == "on"
        nuts = request.POST.get("nuts", "off") == "on"
        lactose = request.POST.get("lactose", "off") == "on"
        loc = request.POST.get("location")
        loc = loc if loc != "" else "all"
        price = int(request.POST.get("sliderPrice", 0))
        return HttpResponseRedirect(
            reverse(
                "main:search",
                kwargs={
                    "locationEntry": loc,
                    "celEntry": cel,
                    "vegetEntry": veget,
                    "veganEntry": vegan,
                    "nutsEntry": nuts,
                    "lactoseEntry": lactose,
                    "priceEntry": price,
                },
            )
        )
    else:
        restaurants = Restaurant.objects.all()
        maxPrice = ceil(getMax(restaurants))
        restaurants = queryRestaurants(
            celEntry == "True",
            veganEntry == "True",
            vegetEntry == "True",
            nutsEntry == "True",
            lactoseEntry == "True",
            locationEntry,
            int(priceEntry),
        )
        locationEntry = locationEntry if locationEntry != "all" else ""
        return render(
            request,
            "main/search.html",
            {
                "restaurants": restaurants,
                "max": maxPrice,
                "location": locationEntry,
                "cel": celEntry,
                "veget": vegetEntry,
                "vegan": veganEntry,
                "price": priceEntry,
                "nuts": nutsEntry,
                "lactose": lactoseEntry,
            },
        )


def filter_preferences(dishes, cel, veget, vegan, nuts, lactose):
    return [
        dish
        for dish in dishes
        if (dish.vegetarian and veget or not veget)
        and (dish.celiac and cel or not cel)
        and (dish.vegan and vegan or not vegan)
        and (dish.nuts_free and nuts or not nuts)
        and (dish.lactose_free and lactose or not lactose)
    ]


def filter_dish_price(dishes, price):
    return [item for item in dishes if item.price <= price]


def filter_dishes(dishes, cel, veget, vegan, nuts, lactose, price):
    dishes = filter_preferences(dishes, cel, veget, vegan, nuts, lactose)
    dishes = filter_dish_price(dishes, price)
    return dishes


def getMaxPriceRest(res):
    return max([dish.price for dish in res.my_dishes.all()])


def restaurant(
    request,
    user_id,
    celEntry,
    vegEntry,
    veganEntry,
    nutsEntry,
    lactoseEntry,
    priceEntry,
):
    res = Restaurant.objects.get(user_id=user_id)
    dishes = res.my_dishes.all()

    if request.method == "POST":
        cel = request.POST.get("celiac", "off") == "on"
        veget = request.POST.get("vegetarian", "off") == "on"
        vegan = request.POST.get("vegan", "off") == "on"
        nuts = request.POST.get("nuts", "off") == "on"
        lactose = request.POST.get("lactose", "off") == "on"
        price = int(request.POST.get("price", 0))
        return HttpResponseRedirect(
            reverse(
                "main:restaurant",
                kwargs={
                    "user_id": user_id,
                    "celEntry": cel,
                    "veganEntry": vegan,
                    "vegEntry": veget,
                    "nutsEntry": nuts,
                    "lactoseEntry": lactose,
                    "priceEntry": price,
                },
            )
        )
    else:
        maxPrice = ceil(getMaxPriceRest(res))
        priceEntry = priceEntry if priceEntry != "-1" else str(maxPrice)
        dishes = filter_dishes(
            dishes,
            celEntry == "True",
            vegEntry == "True",
            veganEntry == "True",
            nutsEntry == "True",
            lactoseEntry == "True",
            int(priceEntry),
        )
        return render(
            request,
            "main/restaurant.html",
            {
                "restaurant": res,
                "dishes": dishes,
                "celiac": celEntry,
                "vegetarian": vegEntry,
                "vegan": veganEntry,
                "nuts": nutsEntry,
                "lactose": lactoseEntry,
                "max_price": maxPrice,
                "price": priceEntry,
            },
        )


def restaurant_info(request, user_id):
    res = Restaurant.objects.filter(user_id=user_id).first()
    return render(request, "main/restaurant-info.html", {"restaurant": res})


def filters(request):
    return render(request, "main/layout-filters.html")


def menu(request, rest, menuid):
    myRestaurant = Restaurant.objects.filter(rest_name=rest).first()
    myDish = Dish.objects.filter(name=menuid, restaurant=myRestaurant).first()
    myIngredients = myDish.ingredients.all()
    ratingOfDish = Rating.objects.filter(dish_id=myDish.id).all()
    mean_rating = avg([item.rate for item in ratingOfDish])

    if (
        request.user.is_authenticated
        and request.user.role == User.Role.CLIENT
        and request.method == "POST"
    ):
        rating_v = request.POST.get("rating")
        comment = request.POST.get("comment")
        if not rating_v or not comment:
            return render(
                request,
                "main/menu.html",
                {
                    "menu": menuid,
                    "ingredients": myIngredients,
                    "ratings": ratingOfDish,
                    "rest": rest,
                    "mean_ratings": mean_rating,
                    "i_am_client": request.user.role == User.Role.CLIENT,
                    "err": True,
                },
            )
        else:
            rating_v = int(rating_v)
            my_new_rating = Rating(comment=comment, rate=rating_v, client=request.user, dish=myDish, date=datetime.datetime.now())
            my_other_ratings = Rating.objects.filter(client_id=request.user.id, dish_id=myDish.id).all()
            if len(my_other_ratings) > 0:
                for oneRate in my_other_ratings:
                    oneRate.delete()
            my_new_rating.save()
            return HttpResponseRedirect(
                reverse("main:menu", kwargs={"rest": rest, "menuid": menuid})
            )
    else:
        return render(
            request,
            "main/menu.html",
            {
                "menu": menuid,
                "ingredients": myIngredients,
                "ratings": ratingOfDish,
                "rest": rest,
                "mean_ratings": mean_rating,
                "i_am_client": request.user.role == User.Role.CLIENT,
            },
        )

