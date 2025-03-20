from django.http import JsonResponse


def home(request):
    return JsonResponse({'message': 'Welcome to LumaSphere API!'})


def articles(request):
    data = [
        {"id": 1, "title": "Introduction to AI", "description": "Learn AI basics", "category": "AI Basics"},
        {"id": 2, "title": "Machine Learning", "description": "Understand ML fundamentals", "category": "ML"},
        {"id": 3, "title": "NLP Explained", "description": "Explore NLP concepts", "category": "NLP"},
        {"id": 4, "title": "Computer Vision", "description": "Learn CV basics", "category": "CV"},
        {"id": 5, "title": "Deep Learning", "description": "Understand DL fundamentals", "category": "DL"},
        {"id": 6, "title": "Reinforcement Learning", "description": "Explore RL concepts", "category": "RL"},
    ]
    return JsonResponse(data, safe=False) 