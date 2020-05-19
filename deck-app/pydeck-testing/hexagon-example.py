# Hexagon Example
# From here: https://deckgl.readthedocs.io/en/stable/layer.html#pydeck.bindings.layer.Layer

import pydeck

MAPBOX_API_KEY = None
UK_ACCIDENTS_DATA = ('https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv')

layer = pydeck.Layer(
     'HexagonLayer',
     UK_ACCIDENTS_DATA,
     get_position=['lng', 'lat'],
     auto_highlight=True,
     elevation_scale=50,
     pickable=True,
     elevation_range=[0, 3000],
     extruded=False,
     coverage=1)

view_state = pydeck.ViewState(
   longitude=-1.415,
   latitude=52.2323,
   zoom=6,
   min_zoom=5,
   max_zoom=15,
   bearing=-27.36)

r = pydeck.Deck(layers=[layer],
               initial_view_state=view_state,
               map_style='mapbox://styles/mapbox/dark-v10',
               mapbox_key=MAPBOX_API_KEY)

r.to_html('hexagon-example-dark.html', notebook_display=False)

r = pydeck.Deck(layers=[layer],
                initial_view_state=view_state,
                map_style='mapbox://styles/mapbox/light-v10',
                mapbox_key=MAPBOX_API_KEY)

r.to_html('hexagon-example-light.html', notebook_display=False)
