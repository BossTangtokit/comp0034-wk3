from flask import current_app as app
from paralympics.schemas import RegionSchema, EventSchema
from paralympics.models import Event, Region
from paralympics import db
#from flask import request

# Flask-Marshmallow Schemas
regions_schema = RegionSchema(many=True)
region_schema = RegionSchema()
events_schema = EventSchema(many=True)
event_schema = EventSchema()

@app.route('/')
def hello():
    return f"Hello!"

# Use route and specify the HTTP method(s). If you do not specify the methods then it will default to GET.


@app.get("/regions")
def get_regions():
    """Returns a list of NOC regions and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all_regions = db.session.execute(db.select(Region)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = regions_schema.dump(all_regions)
    # Return the data
    return result

@app.get("/events")
def get_regions():
    """Returns a list of NOC regions and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all_events = db.session.execute(db.select(Event)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    results = regions_schema.dump(all_events)
    # Return the data
    return results