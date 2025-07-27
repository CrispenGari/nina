from flask import Blueprint, make_response, jsonify, request
from random import choice
from api.models import predict_intent, device, responses
from api.models.pytorch import bilstm
from api.utils import translate_text,detect_languages

blueprint = Blueprint("blueprint", __name__)

@blueprint.route('/v1/ask', methods=["POST"]) 
async def askBot():
    data = {"success": False}
    if request.method == "POST":
        try:
            if request.is_json:
                json_data = request.get_json(force=True)
                if json_data.get("message"):
                    lang = await detect_languages(json_data.get("message"))
                    if lang == 'en':
                        msg = json_data.get('message')
                    else:
                        msg = await translate_text('en', json_data.get('message'))
                    res = predict_intent(bilstm, msg, device)
                    top = res.get('top').get('class')
                    botResponse = choice(responses.get(top))
                    # Translate response back to user's language
                    botResponse = await translate_text(lang, botResponse) if lang != 'en' else botResponse
                    data = {
                        'success': True,
                        'prediction': res,
                        'lang': lang,
                        "response": botResponse
                    }  
                else:
                    data['error']  = "You should pass the 'message' in your JSON body while making this request."
            else:
                raise Exception("There is no JSON data in your request.")
        except Exception:
            data['error'] = 'Something went wrong on the server'
    else:
        data['error']  = "The request method should be POST only."        
    return make_response(jsonify(data)), 200
