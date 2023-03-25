#Import the necessay module(s)
import qrcode

message = "Click to subscribe"

imag = qrcode.make(message)

imag.save('C:/Users/USER/Desktop/Coding/Python/Projects/Basic stuff/Qr Code Encoding, Decoding/new.png')