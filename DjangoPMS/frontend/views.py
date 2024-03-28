from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.views import generic
from django.views.decorators.http import require_GET, require_http_methods
from django.http import HttpRequest
from .forms import ReserveForm
import folium
import geocoder

# Create your views here.


def index(request):
    return render(request, "frontend/Home/init.html")


@require_GET
def signup(request):
    form = UserCreationForm()
    return render(request, "frontend/signup.html", {"form": form})


@require_GET
def login(request):
    form = AuthenticationForm()
    return render(request, "frontend/login.html", {"form": form})


@require_GET
def index_reserve(request):
    form = ReserveForm()
    return render(request, "frontend/Reserve/form.html", {"form": form})


# LEAFLET_CONFIG = {
#         "DEFAULT_CENTER": (52.62301,1.24069),
#         "DEFAULT_ZOOM": 16
#         }


# This function uses Guard Statement for early returns, be aware
@require_http_methods(["GET", "POST"])
def reserve(request: HttpRequest):
    form = ReserveForm(request.POST)
    map = folium.Map(location=[52.62301, 1.24069], zoom_start=16)
    # making Iframe fit the parent container
    map.get_root().width = "100%"
    map.get_root().height = "100%"

    if request.method == "GET":
        return render(
            request, "frontend/Reserve/init.html", {"form": form, "map": map._repr_html_()}
        )
    # Rest of the code is dealing as if it a POST REQUEST
    if not form.is_valid():
        raise Exception("WTF")

    destination_osm = geocoder.osm(form.cleaned_data["location"])

    if destination_osm.error:
        raise Exception("WTF")
    # print(destination_osm.__dict__)
    # print(dir(destination_osm))

    folium.Marker(
        location=destination_osm.latlng,
        tooltip="Destination",
        popup=destination_osm.current_result,
        icon=folium.Icon(icon="car", prefix="fa"),
    ).add_to(map)
    return render(
            request, "frontend/Reserve/init.html", {"form": form, "map": map._repr_html_()}
    )
