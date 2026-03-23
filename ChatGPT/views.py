# # views.py

# from django.shortcuts import render
# from groq import Groq
# from django.http.response import StreamingHttpResponse
# from django.views.decorators.csrf import csrf_exempt

# client = Groq()

# def home(request):
#     return render(request, 'home.html', {'name': 'Yash'})


# def generate_response(question):
#     context = """
#     You are a gen-Z chat-bot who uses trending slangs in your each response whith slightly sarcastic but friendly tone. Your reply do not need to be very long.
#     """

#     stream = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "developer",
#                 "content": "You must answer ONLY according to the provided context."
#             },
#             # {"role": "user", "content": question}
#             {
#                 "role": "user",
#                 "content": f"""
#                 Context:
#                 {context}

#                 Question:
#                 {question}
#                 """
#             }
#         ],
#         model="llama-3.1-8b-instant",
#         stream=True
#     )

#     for chunk in stream:
#         if chunk.choices[0].delta.content is not None:
#             yield chunk.choices[0].delta.content


# @csrf_exempt
# def answer(request):

#     if request.method == "POST":
#         question = request.POST.get("message")

#         return StreamingHttpResponse(
#             generate_response(question),
#             content_type="text/plain"
#         )

import os
from django.shortcuts import render
from groq import Groq
from django.http.response import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv


from .rag_engine import retrieve_context

load_dotenv()
# client = Groq() If environment variable API KEY
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def home(request):
    return render(request, 'home.html', {'name': 'Yash'})


def generate_response(question):

    context = retrieve_context(question)
    if not context.strip():
        context = "No relevant context found."

    stream = client.chat.completions.create(

        messages=[
            {
            "role": "developer",
            "content": """
            You are a helpful AI assistant.

            Guidelines:
            1. Use the provided context ONLY if it is relevant to the question.
            2. If the context is not relevant, answer normally as a general assistant.
            3. Format responses using Markdown.
            4. Use headings, bullet points, and code blocks when appropriate.
            5. If the question asks specifically about the document but the answer is not in the context, say:
            "I could not find this information in the document."
            """
            },
            {
            "role": "user",
            "content": f"""
            Context:
            {context}

            Question:
            {question}
            """
            }
        ],

        model="llama-3.1-8b-instant",
        temperature=0.2,
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content


@csrf_exempt
def answer(request):

    if request.method == "POST":

        question = request.POST.get("message")

        return StreamingHttpResponse(
            generate_response(question),
            content_type="text/plain"
        )