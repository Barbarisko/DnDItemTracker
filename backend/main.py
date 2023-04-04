from Loging import configure_logging
configure_logging()

from application import app

from APIHandlers.UserAPI import *
from APIHandlers.CharacterAPI import *
from APIHandlers.ArtifactAPI import *
from APIHandlers.SpellLevelAPI import *
from APIHandlers.SpecialPowerAPI import *
from APIHandlers.ConsumablesAPI import *
from APIHandlers.ItemsAPI import *

@app.route("/")
def index():
    return "Send Boobs"

# @app.route('/api/item/<int:id>plus_text', methods=['GET', 'POST'])
# def func_with_id(id):
#     return { "new_id": id}

# if __name__ == '__main__':
#     app.run(debug=True)