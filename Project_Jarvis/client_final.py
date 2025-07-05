import requests

API_KEY = "api_key" 


def ask_jarvis(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "jarvis"
        },
        json={
            # "model": "deepseek/deepseek-r1-0528:free",
            "model": "microsoft/mai-ds-r1:free",
            # "max_tokens": 500,  
            "messages": [
                {"role": "system", "content": "You are a helpful assistant named Jarvis like Alexa .Give answers in brief.That ia understanble for humans"},
                {"role": "user", "content": prompt}
            ]
        }
    )

    
    data = response.json()
    return data["choices"][0]["message"]["content"]