# istifadeci melumatlarinin istehsal olunmasi ve bir yere toplanilmasi
# istifadecilerin bir yere toplanmasi ucun lazim olan data struktur(list)
users=[]
# istifadenin istehsal olunmasi lazm olan class diger adi ile eskiz
class User:
    def __init__(self,_ad,_soyad,_username,_password):
        self.ad=_ad
        self.soyad=_soyad
        self.username=_username
        self.password=_password