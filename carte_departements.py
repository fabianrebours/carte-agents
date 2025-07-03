import folium
import geopandas as gpd
import webbrowser

geo_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson"
departements = gpd.read_file(geo_url)

carte = folium.Map(location=[46.6, 2.5], zoom_start=6)

for _, row in departements.iterrows():
    nom = row["nom"]
    code = row["code"]
    folium.GeoJson(
        row["geometry"],
        name=nom,
        tooltip=f"{nom} ({code})",
        style_function=lambda x: {
            "fillColor": "#0077cc",
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.4,
        }
    ).add_to(carte)

output_file = "carte_departements.html"
carte.save(output_file)
webbrowser.open(output_file)
