import qrcode
import webbrowser

address = input("Sisesta aadress: ")
maps_link = "https://www.google.com/maps/place/" + address.replace(' ', '+')
qr_code = qrcode.make(maps_link)
qr_code.save("maps_link.png")
webbrowser.open("maps_link.png")
