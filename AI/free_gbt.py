from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


# الآن يمكنك استخدام driver للتنقل والتفاعل مع الصفحات


"""
استخراج رسائل شات جي بي تي مبني على:
    عند استخراج اول رساله يكون السلكتور بهذا الاسم
     .markdown
     عند استخراج ثاني رساله يكون السلكتور بهذا الاسم مع ملاحضة ان الرقم 5 يزيد 2 كل رساله جديدية
     div.w-full:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)
     div.w-full:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)
     div.w-full:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)
     div.w-full:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)

ارسال رساله يكون نفس السلكتور دائما
    prompt-textarea

    نفحص السيليكتور 
    محدد السي اس اس لزر ارسال النص بشانت جي بي تي تختلف حسب حاله النص

    - عند ادخال رساله 
       svg.text-white > path:nth-child(1)
    - تحميل
       .h-2 > path:nth-child(1)
    - باهت(لم اكتب اي رساله)
       svg.text-white > path:nth-child(1)

      نقوم بانتضار الزر حتى ينتهي من التحميل 

     الزر يختلف شكله بوقت مبكر قبل اكتمال النص كاملا فنقوم بالتاخير 0.2 ثانية قبل استخراج النص
     
     ملاحضة:
     هذا الكود كان يعمل بالسابق ربما بسبب تحديث شات جي بي تي 
"""
def connect_to_gbt(): 
    #اخفائ المتصفح لم تضبط
    browser = webdriver.Firefox()

    browser.get('https://chat.openai.com/')
    num = 3

    # send_intoduction(browser, "hello")
    while True:
        massage = input("\n>>")
        send_massage(browser, massage)
        get_massage(browser, num)
        num += 2

#ارسال رساله لشات جي بي تي 
def send_massage(browser, massage):
    web2 = browser.find_element(By.CSS_SELECTOR, "#prompt-textarea")
    web2.send_keys(massage)

    web2 = browser.find_element(By.CSS_SELECTOR, "svg.text-white > path:nth-child(1)")
    web2.click()
    

#سحب ساله الواردة منه
def get_massage(browser, num):
    #تحقق من الزر
    q = 0
    #الانتضار حتى ينتهي من الكتابة
    while True:
        if q ==0 :
            try:
                web2 = browser.find_element(By.CSS_SELECTOR, ".h-2 > path:nth-child(1)")
                q = 1
            except:
                pass

        else:
            try:
                web2 = browser.find_element(By.CSS_SELECTOR, "svg.text-white > path:nth-child(1)")
                break
            except:
                pass
    #ننتضر 0.2 ثواني اضافية
    sleep(0.2)



    #سحب الاجابة
    while True:
        if num == 3:
            slog1 = browser.find_element(By.CSS_SELECTOR, ".markdown")
        else:
            slog1 = browser.find_element(By.CSS_SELECTOR, f"div.w-full:nth-child({num}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")

        print(slog1.text)
        ## يمكن المرور حرف حرف
        # res = slog1.text
        # for letters in range(len(res)) :
        #     print(res[letters], end = "", flush = True)
        #     sleep(0.03)
        break

        
    

connect_to_gbt()