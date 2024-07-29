import webbrowser, sys
"""
يضهر بالمتصفح الموقع المكتوب ب args
"""
# نكتب في argv:
# الرياض+السعودية) بعد )place ليعطيك الموقع او
# (Riad+Saudi+Arabia) يعطي نفس النتيجة

# مثل https://www.google.com/maps/place/Riyadh+Saudi+Arabia
if len(sys.argv) > 1:
    # لانه ليست نبغا سترنج
    address = " ".join(sys.argv[1:])
    #الرابط الي يجي قبل احداثيات المكانhttps://www.google.com/maps/place/
    webbrowser.open("https://www.google.com/maps/place/"+ address)
else:
    print("Please Enter the address")
