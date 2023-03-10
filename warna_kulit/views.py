from distutils.sysconfig import customize_compiler
from django.db import connection
from django.shortcuts import redirect, render

# Create your views here.
def dictfetchall(cursor):
  "Returns all rows from a cursor as a dict"
  desc = cursor.description
  return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
  ]

def index(request):
  print("cek")
  if "pengguna" in request.session:
    isLogged = True
  else:
    isLogged = False

  if not isLogged:
    return redirect('main:home')

  with connection.cursor() as cursor:
    cursor.execute("set search_path to cims")
    cursor.execute(f"""SELECT * FROM WARNA_KULIT 
    WHERE KODE IN (SELECT KODE FROM WARNA_KULIT
    JOIN TOKOH ON WARNA_KULIT.KODE = TOKOH.WARNA_KULIT);""")
    result = dictfetchall(cursor)

    cursor.execute(f"""SELECT * FROM WARNA_KULIT
    WHERE KODE NOT IN (SELECT KODE FROM WARNA_KULIT
    JOIN TOKOH ON WARNA_KULIT.KODE = TOKOH.WARNA_KULIT);""")
    resultx = dictfetchall(cursor)

    print(result)
    print(resultx)
  #   row = dictfetchall(cursor)
  #   print(row)
  # context = {'row':row}
  return render(request, 'warnakulit.html', {'data':result, 'updateable':resultx})

def createWarnaKulit(request):
  return render(request, 'create_warna_kulit.html')