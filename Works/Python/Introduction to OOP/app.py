class book:
    def __init__(self,_name,_price,_author):
        self.ad=_name
        self.qiymet=_price
        self.yazar=_author
    def showBook(self):
        print(f'{self.ad}|{self.qiymet}'|{self.yazar})
    def changePrice(self):
        self.qiymet+=1000
        return self.qiymet
book01=book('The Secret Adversary', 200,'Agatha Christie')

print(book01.changePrice())