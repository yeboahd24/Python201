import pyqrcode 

qr=pyqrcode.create('@PythonTestUz')
qr.png('rasm.png',scale=8)