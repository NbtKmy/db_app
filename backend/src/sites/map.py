from flask import render_template
import folium
from folium import plugins
from src.models.map import MapModel, MapSchema


def createMap():

    results = MapModel.query.all()
    databases_array = MapSchema(many=True).dump(results)
    

    m = folium.Map()

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    map = m.get_root()._repr_html_()
    return render_template('map.html', map=map)