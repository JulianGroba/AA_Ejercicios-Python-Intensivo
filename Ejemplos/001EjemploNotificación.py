# pip install win10toast --> desde cmd de windows para agregar librería
from win10toast import ToastNotifier
toaster = ToastNotifier() 
toaster.show_toast("Prueba Python","Notificación en Windows 10")