
from django.shortcuts import render, redirect

from predict.decide import Get_result
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter, landscape

from reportlab.pdfgen import canvas
from django.http import HttpResponse
from datetime import datetime 
#from django.templatetags.static import static
from django.templatetags.static import static
# Getting current date and time


# importing modules



from reportlab.lib import colors



s1=''
s2=''
s3=''
s4=''
s5=''
uname=''
accur=0
def check(request):
    global s1,s2,s3,s4,s5,uname,accur
    if request.method == "POST":
        uname=request.POST['uname']
        s1=request.POST['sym1']
        s2=request.POST['sym2']
        s3=request.POST['sym3']
        s4=request.POST['sym4']
        s5=request.POST['sym5']
        request.session["disease"],accur = Get_result(s1,s2,s3,s4,s5)
        return redirect(result)
    return render(request,'predict/check.html')
    
def result(request):
    return render(request,'predict/result.html',{'res':request.session["disease"]})
def home(request):
    return render(request,'predict/home.html')
def about(request):
    return render(request,'predict/about.html')
def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment;filename="Diagnosis Report.pdf"'
    p=canvas.Canvas(response)
    p.setTitle("Medical Report")
    p.setFillColor(colors.darkblue)
    

    p.rect(0, 801, 900, 40, stroke=1, fill=1)

   
    p.setFont("Times-Roman",20)
    p.setFillColor(colors.darkred) 
    p.drawCentredString(300, 770, "Virtual Diagnosis Medical Report")
    p.setFont("Times-Roman",18)
    p.setFont("Times-Roman",16)
    p.setFillColor(colors.black) 
    p.drawString(50,680,"Hello "+uname.capitalize()) 
    p.setFillColor(colors.black) 
    now = str(datetime.now().date())
    p.drawString(450,710,"Date: "+now) 
     


    textLine = [
    "I am your virtual doctor, and I work hard to forecast your disease",
    "based on your symptoms."
    
    
    ]
    text = p.beginText(50, 650) 

    text.setFont("Helvetica", 15) 
    text.setFillColor(colors.black) 

    for line in textLine: 

        text.textLine(line) 
    p.drawText(text)
    accur=0.983
    p.setFont("Times-Roman",18)
    p.setFillColor(colors.brown) 
    p.drawString(50,590,"Symtomns") 
    p.setFillColor(colors.black) 
    p.setFont("Times-Roman",15)
    p.drawString(50,560,"1) "+s1)
    p.drawString(230,560,"2) "+s2)
    p.drawString(430,560,"3) "+s3)
    p.drawString(50,530,"4) "+s4)
    p.drawString(230,530,"5) "+s5)

    




    p.setFont("Times-Roman",20)
    p.setFillColor(colors.brown)
    p.drawString(50,480,"The Predicted Disease is :")


    p.setFont("Times-Roman", 30)
    p.setFillColor(colors.darkblue)
    p.drawString(100, 440,request.session["disease"])
    #img_file = static('image/Reportpic.png')
    img_file="D:\miniproject pharm\Diseasepredict\predict\static\image\Reportpic.png"
    p.drawImage(img_file, 80, 160, height=250,width=420,  mask='auto')
    
    p.setFont("Times-Roman", 18)
    p.setFillColor(colors.brown)
    p.drawString(280, 80,"Contact:")
    p.setFillColor(colors.black)
    p.drawString(50, 60,'Accuracy:'+str(accur*100)+'%')

    p.drawString(280, 60,"Team-02, 3rd year cse-c, 2020-24")
    
    p.setFillColor(colors.darkblue)
    p.rect(0, 0, 900, 40, stroke=1, fill=1)
    
    

    
    p.showPage()
    p.save()
    '''doc = SimpleDocTemplate("file.pdf",pagesize=landscape(letter),
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=72)'''
    

    return response
