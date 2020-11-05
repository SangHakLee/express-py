from flask_restx import Namespace, Resource

router = Namespace("index", description="index")

@router.route("")
class Index(Resource):
    def get(self):
        return "index"