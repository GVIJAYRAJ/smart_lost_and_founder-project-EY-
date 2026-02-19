from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import json

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")

        # Simple AI Logic (You can upgrade later)
        if "hello" in user_message.lower():
            bot_reply = "Hello 👋 How can I help you today?"
        elif "help" in user_message.lower():
            bot_reply = "Sure 😊 Tell me what you need help with."
        else:
            bot_reply = "I'm here to assist you! 🤖"

        ChatMessage.objects.create(
            user_message=user_message,
            bot_response=bot_reply
        )

        return JsonResponse({"response": bot_reply})
