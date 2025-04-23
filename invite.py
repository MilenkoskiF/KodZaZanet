import base64

def run():
    data = b"VG9kYXkgZmVlbHMgbGlrZSBhIGRheSBmb3Igc29tZXRoaW5nIHNhdm9yeeKAnC4uLiBhbmQgSSdtIG5vdCBqdXN0IHRhbGtpbmcgbW9sZWN1bGVzLiBRdWljayBleHBlcmltZW50PyBZb3UgKyBtZSArIGZvb2QgPSBwb3NzaWJsZSByZWFjdGlvbi4g8Jiln/CfkYk="
    output = base64.b64decode(data).decode('utf-8')
    print(output)

run()
