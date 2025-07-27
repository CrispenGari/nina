from ariadne import QueryType
from api.types import Meta

query = QueryType()
@query.field("meta")
def meta_resolver(obj, info):
   return Meta(
      programmer = "@crispengari",
      main = "Nice Intelligent Network Assistant (NINA)",
      description = "Nice Intelligent Network Assistant (NINA) is a modern customer support chatbot framework powered by AI-driven intent recognition. Nina provides seamless integration through REST and GraphQL APIs, enabling businesses to automate and streamline customer interactions across platforms.",
      language = "python",
      libraries = ["pytorch","googletrans"],
   ).to_json()
   