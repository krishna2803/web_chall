from django.shortcuts import render

def render_html(request):
    
    if request.method == 'POST':
        
        html_code = request.POST.get('html_code')
        
        blocked = ['script', 'svg', 'button', 'img', 'image']
        
        for b in blocked:
            if b in html_code:
                html_code = f"<h1>Trying XSS? Try harder!</h1>"
        
        return render(request, 'editor/index.html', {'html_code': html_code})
    return render(request, 'editor/index.html', {'html_code': ''})

def get_flag(request):
    flag = 'flag{congratulations_on_getting_the_WRONG_FLAG_lolololol}'
    
    origin = request.META.get('HTTP_REFERER', 'No referer')
    
    if request.method == 'GET':
        allowed = ['0.0.0.0', '127.0.0.1:8000']
        if origin in allowed:
            flag = open('flag.txt').read()
        else:
            flag = 'sorry! only server is allowed to access this :)'
        
    return render(request, 'editor/flag.html', {'flag': flag})