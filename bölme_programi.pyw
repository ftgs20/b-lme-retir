from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Pencere(QWidget):
    def __init__ (self):
        super().__init__()
        self.islem="/"
        self.setUI()
        
    def setUI(self):
        self.setWindowTitle("Bölme Öğren")
        self.yazı1=QLabel("Bölünen sayı:  ")
        self.yazı2=QLabel("Bölen  sayı   :  ")
        self.sonuc=QLabel("")
        self.sonuc.setAlignment(Qt.AlignCenter)
        self.bölünen=QLabel("")
        self.bölünen.setAlignment(Qt.AlignCenter)
        self.bölen=QLabel("")
        self.bölen.setAlignment(Qt.AlignCenter)
        self.kalan=QLabel("")
        self.kalan.setAlignment(Qt.AlignCenter)
        bölünen1=QLabel("Bölünen")
        bölen1=QLabel("Bölen")
        bölüm1=QLabel("Bölüm")
        kalan1=QLabel("Kalan")
        
        self.giris1=QLineEdit()
        self.giris2=QLineEdit()
        
        self.button1=QPushButton("hesapla")
        self.temizle=QPushButton("temizle")
        self.cikalim=QPushButton("Çıkış")
        
        self.temizle.setFont(QFont("Comic Sans MS",25))
        self.button1.setFont(QFont("Comic Sans MS",25))
        self.giris2.setFont(QFont("Comic Sans MS",25))
        self.giris1.setFont(QFont("Comic Sans MS",25))
        self.kalan.setFont(QFont("Comic Sans MS",25))
        self.bölen.setFont(QFont("Comic Sans MS",25))
        self.bölünen.setFont(QFont("Comic Sans MS",25))
        self.sonuc.setFont(QFont("Comic Sans MS",25))
        self.yazı2.setFont(QFont("Comic Sans MS",25))
        self.yazı1.setFont(QFont("Comic Sans MS",25))
        self.cikalim.setFont(QFont("Comic Sans MS",25))
        bölünen1.setFont(QFont("Comic Sans MS",25))
        bölen1.setFont(QFont("Comic Sans MS",25))
        bölüm1.setFont(QFont("Comic Sans MS",25))
        kalan1.setFont(QFont("Comic Sans MS",25))
        
        izgara=QGridLayout()
        #QLabel("kalan   : ")
        izgara.addWidget(bölünen1,1,1)
        izgara.addWidget(QLabel("                                 "),1,3)
        izgara.addWidget(self.bölünen,1,2)
        izgara.addWidget(bölen1,2,1)
        izgara.addWidget(self.bölen,2,2)
        izgara.addWidget(bölüm1,3,1)
        izgara.addWidget(self.sonuc,3,2)
        izgara.addWidget(kalan1,4,1)
        izgara.addWidget(self.kalan,4,2)
                     
        h_box1=QHBoxLayout()
        h_box2=QHBoxLayout()
                
        h_box1.addWidget(self.yazı1)
        h_box1.addWidget(self.giris1)
        
        h_box2.addWidget(self.yazı2)
        h_box2.addWidget(self.giris2)
        
        v_box=QVBoxLayout()
        
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addStretch()
        v_box.addLayout(izgara)
        v_box.addStretch()
        v_box.addWidget(self.button1)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.cikalim)
        
        
        self.cikalim.clicked.connect(self.cikis)       
        self.button1.clicked.connect(self.uygula)
        self.temizle.clicked.connect(self.temiz)
        
        self.setLayout(v_box)
        self.show()
        
    def cikis(self):
        sys.exit()
        
    def temiz(self):
        self.giris1.clear()
        self.giris2.clear()
        
           
    def uygula(self):
       if self.islem == "/":
            try:
                bölünen=int(self.giris1.text())
                bölen=int(self.giris2.text())
                sonuc=bölünen//bölen
                kalan=bölünen % bölen
                self.sonuc.setText(str(sonuc))
                self.bölünen.setText(str(bölünen))
                self.bölen.setText(str(bölen))
                self.kalan.setText(str(kalan))
                
            except ValueError and ZeroDivisionError:
                self.giris1.clear()
                self.giris2.clear()
                
        

        
        
           
        

if __name__ ==  "__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
    