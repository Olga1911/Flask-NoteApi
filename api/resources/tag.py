from api import auth, abort, db
from api.models.tag import TagModel
from api.schemas.tag import TagSchema, TagRequestSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, use_kwargs, doc
from webargs import fields


@doc(tags=['Tags'])
class TagResource(MethodResource):
    @marshal_with(TagSchema, code=200)
    @doc(summary="Get tag by id", description="Returns tag")
    @doc(responses={404: {"description": 'Tag not found'}})
    def get(self, tag_id):
        tag = TagModel.query.get(tag_id)
        if tag is None:
            abort(404, error=f"Tag with id={tag_id} not found")
        return tag, 200


@doc(tags=['Tags'])
class TagsListResource(MethodResource):
    @marshal_with(TagSchema(many=True), code=200)
    @doc(summary='Get ALL tags')
    def get(self):
        tags = TagModel.query.all()
        return tags, 200

    @doc(summary="Create new tag", description="Подробное описание метода POST")
    #@use_kwargs({"name": fields.String()}, location=('json'))
    @use_kwargs(TagRequestSchema, location='json')
    @marshal_with(TagSchema, code=201)
    def post(self, **kwargs):
        tag = TagModel(**kwargs)
        db.session.add(tag)
        db.session.commit()
        return tag, 201

