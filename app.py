from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.indice import IndiceList, IndiceItem
from resources.comic import ComicList, ComicItem, ComicItemCreate

app = Flask(__name__)
CORS(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(IndiceItem, '/indice-item-delete')
api.add_resource(IndiceList, '/indices')
api.add_resource(ComicItem, '/comics/<string:item_id>')
api.add_resource(ComicItemCreate, '/comics')
api.add_resource(ComicList, '/comics')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
