from django.shortcuts import render, redirect
from .models import CodeScan
import ast

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        code = request.POST.get('source_code')
        error_count = 0
        try:
            ast.parse(code)
        except Exception:
            error_count = 1
            
        scan = CodeScan.objects.create(title=title, source_code=code, detected_errors=error_count)
        return redirect('index')
        
    scans = CodeScan.objects.order_by('-created_at')
    return render(request, 'auditor/index.html', {'scans': scans})
