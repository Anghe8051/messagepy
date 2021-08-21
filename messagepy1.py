#LINK PARA ACTIVAR LA OPCION DE APPS MENOS SEGURAS EN GMAIL
# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MuniZd1vuLsoy0wZ1yS2rmK2_jkYmqHBsy3i5uYgjiSjA5w_zIP_MmrsXP9Q69PMVU9VEdnwtl-glXbUMpi48P1tf54g


#****************************************** HERRAMIENTA 1 ******************************************
def spam():
  #IMPORTAR LIBRERIAS
  import smtplib
  import time
  
  #DEFINICION DE VARIABLES
  a=float()
  n=float()
  a=1
  
  #VARIABLES DE CORREOS
  user="---" # <-- AQUI VA TU DIRRECCION DE CORREO "GMAIL"
  passw="---" # <-- AQUI VA TU CONTRASEA DEL CORREO
  
  #INGRESO DE DATOS
  rec=input("INGRESE EL CORREO DEL RECEPTOR: ")
  n=float(input("INGRESE EL NUMERO DE CORREOS POR MANDAR: "))
  time.sleep(1)
  print("\n")
  print(" INICIANDO SPAM ".center(50,"="))
  
  #iNICIO DE SESION E INICIO DEL SERVIDOR
  server=smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(user,passw)
  
  #BULCE SPAM
  while a<=n :
    #MENSAJE DEL CORREO 
    mess1=(f"PRUEBA DE CORREO {n}")
    mess2=(f"\n HOLA: {rec}")
    mess3=("\n COMO ESTAS, ESTO ES UNA PRUEBA DE SPAM AUTOMATICO CON PYTHON.... ")
    
    subject=(f"CORREO {n}")
    mess=(f"subject: {subject} \n\n {mess1} \n{mess2} \n\n{mess3} ")
    server.sendmail(user,rec,mess)
    print(f"\n MENSAJE {n} ENVIADO CON EXITO!")

    n=n-1
    time.sleep(2) #RETARDO ENTRE MENSAJES
  #FIN DEL BUCLE

  #SALIDA DEL SERVIDOR
  server.quit()
  print("\n")
  print("SPAM TERMINADO".center(50,"="))


#****************************************** FIN HERRAMIENTA 1 ******************************************


#****************************************** HERRAMIENTA 2 ******************************************
def whats():
  # IMPORTAR EL MODULO
  import pywhatkit
  
  #INGRESO DE DATOS
  num=input(str("INGRESE EL NUMERO DE TELEFONO CON EL CODIGO DEL PAIS: ")) #CODIGO DE ECUADOR "+593"
  mesw=input(str("INGRESE EL MENSAJE: "))
  hor=int(input("INGRESE LA HORA EN FORMATO 24 HORAS: "))
  min=int(input("INGRESE EL MINUTO: "))
  print("".center(100,"="))
  
  try:
    # ENVIAR MENSAJE
    pywhatkit.sendwhatmsg(num,mesw,hor,min)
    print("\nMENSAJE ENVIADO CON EXITO \n")
  
  except:
    print("\nOCURRIO UN ERROR \n")

#****************************************** FIN HERRAMIENTA 2 ******************************************

#HERRAMIENTA DE MENSAJERIA Messagepy VERSION: 1.0
print("\n")
print(" HERRAMIENTA DE MENSAJERIA Messagepy ".center(50,"="))
print("\n")
print("by AngheCh \n")
print("1) SPAM CORREO ELECTRONICO \n\n2) WHATSAPP MESSAGE \n")

#ELEGIR LA HERRAMIENTA
her=int(input("ESCOGA LA HERRAMIENTA QUE DESEE: "))
print("\n")

if her==1:
  print("ESCOGIO LA OPCION 1 ----- SPAM POR CORREO \n")
  spam()
elif her==2:
  print("ESCOGIO LA OPCION 2 ----- WHATSAPP MESSAGE \n")
  whats()
else:
  print("ERROR \n")

#SALIDA DE LA HERRAMIENTA
sal=input(str("\nPRESIONE INTRO PARA FINALIZAR... "))
print("\n")
print(" GRACIAS POR USAR MI HERRAMIENTA ".center(50,"="))

#Messagepy Version: 1.0 by AngheCh.
