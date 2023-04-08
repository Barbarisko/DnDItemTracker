from Application.Loging import configure_logging
configure_logging()

from Application.application import app

from APIHandlers.UserAPI import app
from APIHandlers.CharacterAPI import app
from APIHandlers.ArtifactAPI import app
from APIHandlers.SpellLevelAPI import app
from APIHandlers.SpecialPowerAPI import app
from APIHandlers.ConsumablesAPI import app
from APIHandlers.ItemsAPI import app

@app.route("/")
def index():
    return "Send Boobs"

# @app.route('/api/item/<int:id>plus_text', methods=['GET', 'POST'])
# def func_with_id(id):
#     return { "new_id": id}

# if __name__ == '__main__':
#     app.run(debug=True)