from course.htmltutorial.database import Database
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
    
db = Database("cars.db")

def get_dropdown_values():


    carbrands = db.fetch_brand()
    myDict =  {}
    for brand in carbrands:
        key = brand[1]
        brand_id = brand[0]

        fetched_model = db.fetch_model(brand_id)
    
        car_model = []
        for model in fetched_model:
            car_model.append( model[2] )
        myDict[key] = car_model
    
    
    class_entry_relations = myDict
                        
    return class_entry_relations


@app.route('/update_dropdown')
def update_dropdown():

    # the value of the first dropdown (selected by the user)
    selected_class = request.args.get('selected_class', type=str)

    # get values for the second dropdown
    updated_values = get_dropdown_values()[selected_class]

    # create the value sin the dropdown as a html string
    html_string_selected = ''
    for entry in updated_values:
        html_string_selected += '<option value="{}">{}</option>'.format(entry, entry)

    return jsonify(html_string_selected=html_string_selected)


@app.route('/process_data')
def process_data():
    selected_class = request.args.get('selected_class', type=str)
    selected_entry = request.args.get('selected_entry', type=str)

    # process the two selected values here and return the response; here we just create a dummy string

    return jsonify(random_text="You selected the car brand: {} and the model: {}.".format(selected_class, selected_entry))




@app.route('/')
def index():

    """
    initialize drop down menus
    """

    class_entry_relations = get_dropdown_values()

    default_classes = sorted(class_entry_relations.keys())
    default_values = class_entry_relations[default_classes[0]]

    return render_template('index.html',
                       all_classes=default_classes,
                       all_entries=default_values)


if __name__ == '__main__':

    app.run(debug=True)