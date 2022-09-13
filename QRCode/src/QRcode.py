import qrcode
from os import chdir

def  generate_qrcode(text = "Somethings wrong with input", name = "SomethingsWrongWithWnput"):

	qr = qrcode.QRCode(
		version = 1,
		error_correction = qrcode.constants.ERROR_CORRECT_L,
		box_size = 10,
		border = 4,
	)

	qr.add_data(text)
	qr.make(fit=True)

	img = qr.make_image(fill_color = "black", back_color = "white")
	img_name = name + ".png"
	chdir("../image")
	img.save(img_name)


def main():

	text = input("Enter message to encode to QR: ")
	name = input("Enter name of QR: ")
	generate_qrcode(text = text, name = name)

if __name__ == "__main__":
	main()