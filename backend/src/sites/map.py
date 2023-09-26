from flask import render_template
import folium
from folium import plugins
import branca
from src.models.databaselist import DatabaselistModel, DatabaselistSchema


def createMap():

    m = folium.Map(location=[35.683889, 139.774444], zoom_start=2)
    marker_layer = folium.plugins.MarkerCluster(
        name='DB-provider', 
        control=True).add_to(m)
    
    results = DatabaselistModel.query.all()
    databases_array = DatabaselistSchema(many=True).dump(results)

    loc_array = []
    for i in databases_array:

        creator_obj = i.get('creator')
        if creator_obj is not None:
            cre = i['creator']
            lon_obj = cre.get('lon')
            if lon_obj is not None:
                # coordinate
                point_arr = [float(cre['lat']), float(cre['lon'])]
                loc_array.append(point_arr)
                
                # 現状popupにHTMLを入れるとエラーがでる…
                #html=f"""
                #    <a href="{i['url']}" target="_blank">{i['title_ja']}</a>
                #    """
                pop_text = i['title_ja']
                popup = folium.Popup(pop_text, max_width=300)
                folium.Marker(location=point_arr, popup=popup, name=i['title_ja']).add_to(marker_layer)
                
        else: 
            continue
    
    folium.plugins.HeatMap(
        loc_array, 
        name='Heatmap',
        show=False,
        control=True).add_to(m)
    
    folium.plugins.Search(
                            layer=marker_layer,
                            search_label='name',
                            placeholder='Search database name in Japanese',
                            collapsed=False).add_to(m)
    folium.LayerControl().add_to(m)

    # set the iframe width and height
    m.get_root().width = '1000px'
    m.get_root().height = '800px'
    map = m.get_root()._repr_html_()
    return render_template('map.html', map=map)