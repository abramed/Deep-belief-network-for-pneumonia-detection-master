from subprocess import run, PIPE
import sys

# 1. D'abord on cree une application
# 2. On l'ajoute dans settings.py
# 3. On cree une methode dans views.py
# 4. Creer un lien entre l'app et urls dans urls.py on appelon la methode
# 5. Creer le template (HTML..) et faire la liaison dans views.py
# 6. On recupere les variables depuis python grace au DTL {{}} dans le Html
from django.shortcuts import render




def button(request):
    return render(request, 'DbnSiteWeb/index.html')


def external(request):
    path = request.POST.get('upload')

    list_name = []
    list_mail = []

    f1 = open('output.txt', 'w')
    f1.write("")
    f1.close()

    filepath = 'list_users.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            name = line.strip()
            line = fp.readline()
            list_name.append(name)
            cnt += 1

    filepath1 = 'list_mails.txt'
    with open(filepath1) as fp1:
        line1 = fp1.readline()
        cnt1 = 1
        while line1:
            mail = line1.strip()
            line1 = fp1.readline()
            list_mail.append(mail)
            cnt1 += 1

    zipped_list = zip(list_name, list_mail)

    out = run([sys.executable, 'test_donner.py', path],
              shell=False, stdout=PIPE)

    output =out.stdout.decode('utf-8')
    if(len(output)>50):
        with open("output.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            # Append text at the end of file
            file_object.write("Presence d'une pneumonie")

    else:
        with open("output.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(output)




    return render(request, "DbnSiteWeb/index2.html", {'data1': out.stdout.decode('utf-8'), "context": zipped_list})


def index2(request):
    list_name = []
    list_mail = []

    filepath = 'list_users.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            name = line.strip()
            line = fp.readline()
            list_name.append(name)
            cnt += 1

    filepath1 = 'list_mails.txt'
    with open(filepath1) as fp1:
        line1 = fp1.readline()
        cnt1 = 1
        while line1:
            mail = line1.strip()
            line1 = fp1.readline()
            list_mail.append(mail)
            cnt1 += 1

    zipped_list = zip(list_name, list_mail)
    return render(request, 'DbnSiteWeb/index2.html', {"context": zipped_list})


def index(request):
    return render(request, 'DbnSiteWeb/index.html')


def signUP(request):
    name = request.POST.get('name')
    message = request.POST.get('message')
    email_user = request.POST.get('email')
    email_doc = request.POST.get('email_doc')

    # Open the file in append & read mode ('a+')
    with open("list_users.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(name)

    with open("list_mails.txt", "a+") as file_object1:
        # Move read cursor to the start of file.
        file_object1.seek(0)
        # If file is not empty then append '\n'
        data1 = file_object1.read(100)
        if len(data1) > 0:
            file_object1.write("\n")
        # Append text at the end of file
        file_object1.write(email_user)

    return render(request, 'DbnSiteWeb/index.html', {'name': name, 'mail': email_user})


def sendMail(request):

    f = open("output.txt", "r")
    x = f.read()

    filepath = 'list_users.txt'
    with open(filepath) as fp:
        line = fp.readline()
        name = line.strip()

    filepath1 = 'list_mails.txt'
    with open(filepath1) as fp1:
        line1 = fp1.readline()
        mail = line1.strip()

    list_name = []
    list_mail = []


    filepath2 = 'list_users.txt'
    with open(filepath2) as fp2:
        line2 = fp2.readline()
        cnt2 = 1
        while line2:
            name2 = line2.strip()
            line2 = fp2.readline()
            list_name.append(name2)
            cnt2 += 1

    filepath3 = 'list_mails.txt'
    with open(filepath3) as fp3:
        line3 = fp3.readline()
        cnt3 = 1
        while line3:
            mail3 = line3.strip()
            line3 = fp3.readline()
            list_mail.append(mail3)
            cnt3 += 1

    if name is not None:
        out = run(
            [sys.executable, 'SMTP_SSL.py', name, mail,x],
            shell=False, stdout=PIPE)

    if (len(list_name) >0):
        del list_mail[0]
        del list_name[0]


    f1 = open('list_users.txt', 'w')
    f1.write("")
    f1.close()

    f2 = open('list_mails.txt', 'w')
    f2.write("")
    f2.close()


    with open("list_users.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        i=0
        while(i<len(list_name)):

            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(list_name[i])

            i+=1


    with open("list_mails.txt", "a+") as file_object1:
        # Move read cursor to the start of file.
        j=0
        while (j < len(list_mail)):
            file_object1.seek(0)
            # If file is not empty then append '\n'
            data1 = file_object1.read(100)
            if len(data1) > 0:
                file_object1.write("\n")
            # Append text at the end of file
            file_object1.write(list_mail[j])

            j+=1

    zipped_list = zip(list_name, list_mail)

    return render(request, 'DbnSiteWeb/index2.html', {'data2': out.stdout.decode('utf-8'), "context": zipped_list})
