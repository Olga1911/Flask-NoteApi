from api import db
import json
from api.schemas.user import UserRequestSchema
import click
from config import Config

from api.models.note import NoteModel
from api.models.user import UserModel


@click.command
@click.argument('file_name')
#@click.option('--count', default=1, help='Number of messages')
def load_data(file_name):
    with open(Config.PATH_TO_FIXTURES / file_name, "r", encoding="UTF-8") as f:
        file_data = json.load(f)
        model_name = file_data["model"]
        if model_name == "UserModel":
            model = UserModel
        elif model_name == "NoteModel":
            model = NoteModel

        for obj_data in file_data["data"]:
            obj = model(**obj_data)
            db.session.add(obj)
        db.session.commit()
    print(f"{len(file_data['data'])} notes created")
    #print(f"{len(file_data['data'])} users created")

#path_to_fixture = "fixtures/users.json"
# path_to_fixture = "fixtures/notes.json"
# load_data(path_to_fixture)

if __name__ == "__main__":
    load_data()
