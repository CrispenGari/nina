import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from api.app import app
from flask import make_response, jsonify, request
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from api.resolvers.queries import query
from api.resolvers.mutations import mutation
from api.blueprints import blueprint

type_defs = load_schema_from_path("schema/schema.graphql")
explorer_html = ExplorerGraphiQL().html(None)
schema = make_executable_schema(
    type_defs,
    [
        query,
        mutation,
    ],
)


class AppConfig:
    PORT = 3001
    DEBUG = True


app.register_blueprint(blueprint, url_prefix="/api")


@app.route("/", methods=["GET"])
def meta():
    meta = {
        "programmer": "@crispengari",
        "main": "Nice Intelligent Network Assistant (NINA)",
        "description": "Nice Intelligent Network Assistant (NINA) is a modern customer support chatbot framework powered by AI-driven intent recognition. Nina provides seamless integration through REST and GraphQL APIs, enabling businesses to automate and streamline customer interactions across platforms.",
        "language": "python",
        "libraries": ["pytorch", "googletrans"],
    }
    return make_response(jsonify(meta)), 200


@app.route("/api/v1/graphql", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200


@app.route("/api/v1/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value={"request": request}, debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(
        debug=AppConfig().DEBUG,
        port=AppConfig().PORT,
    )
