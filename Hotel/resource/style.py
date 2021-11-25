from flask_restful import Resource, reqparse, abort
from flask_jwt import jwt_required, current_identity
from Hotel.model.style import StyleModel


class StyleList(Resource):
    def get(self):
        styles = StyleModel.get_style_list()
        return [style.as_dict() for style in styles]

    @jwt_required()
    def post(self):
        if current_identity.from_admin is False:
            return {"message": "Please use the right token."}

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help="name is required.", required=True)
        data = parser.parse_args()

        style = StyleModel.get_by_name(data['name'])

        if style:
            abort(409, message="style exists.")
        style = StyleModel(name=data['name'])
        style.add()
        return style.as_dict(), 201
