from PyQt5 import QtCore, QtGui, QtWidgets
import source_rc

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random
import time
import sys
import csv
import os

import db

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 653)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1114, 653))
        MainWindow.setMaximumSize(QtCore.QSize(1114, 653))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("voxviciblue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        
        self.YTLogo = QtWidgets.QLabel(self.centralwidget)
        self.YTLogo.setGeometry(QtCore.QRect(220, -20, 261, 241))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YTLogo.sizePolicy().hasHeightForWidth())
        
        self.YTLogo.setSizePolicy(sizePolicy)
        self.YTLogo.setStyleSheet("image: url(:/YTLogo/sm_5b321c9877382.png);")
        self.YTLogo.setText("")
        self.YTLogo.setObjectName("YTLogo")
        
        self.YTLogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.YTLogoLabel.setGeometry(QtCore.QRect(440, 30, 421, 141))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YTLogoLabel.sizePolicy().hasHeightForWidth())
        
        self.YTLogoLabel.setSizePolicy(sizePolicy)
        self.YTLogoLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
            "font: 25 36pt \"Segoe UI Light\";")
        self.YTLogoLabel.setObjectName("YTLogoLabel")
        
        self.ChooseLabel = QtWidgets.QLabel(self.centralwidget)
        self.ChooseLabel.setGeometry(QtCore.QRect(450, 230, 221, 71))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChooseLabel.sizePolicy().hasHeightForWidth())
        
        self.ChooseLabel.setSizePolicy(sizePolicy)
        self.ChooseLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
            "font: 25 36pt \"Segoe UI Light\";")
        self.ChooseLabel.setObjectName("ChooseLabel")
        
        self.MainInput = QtWidgets.QLineEdit(self.centralwidget)
        self.MainInput.setGeometry(QtCore.QRect(190, 320, 721, 71))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainInput.sizePolicy().hasHeightForWidth())
        
        self.MainInput.setSizePolicy(sizePolicy)
        self.MainInput.setStyleSheet("border: 2px solid;\n"
            "border-radius: 6px;\n"
            "border-color: rgb(255, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font: 24pt \"Segoe UI\";")
        self.MainInput.setObjectName("MainInput")
        
        self.ExtractButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExtractButton.setGeometry(QtCore.QRect(190, 405, 721, 71))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExtractButton.sizePolicy().hasHeightForWidth())
        
        self.ExtractButton.setSizePolicy(sizePolicy)
        self.ExtractButton.setStyleSheet("color: rgb(255, 255, 255);\n"
            "font: 24pt \"Segoe UI\";\n"
            "border-radius: 6px;\n"
            "background-color: rgb(255, 0, 0);")
        self.ExtractButton.setObjectName("ExtractButton")
        self.ExtractButton.clicked.connect(self.begin_extract)
        
        self.voxvici = QtWidgets.QLabel(self.centralwidget)
        self.voxvici.setGeometry(QtCore.QRect(10, 490, 151, 121))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voxvici.sizePolicy().hasHeightForWidth())
        
        self.voxvici.setSizePolicy(sizePolicy)
        self.voxvici.setStyleSheet("image: url(:/Voxvici/voxviciblue.png);")
        self.voxvici.setText("")
        self.voxvici.setObjectName("voxvici")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(190, 510, 721, 61))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet("QProgressBar{\n"
            "    border-radius: 6px;\n"
            "    text-align: center;    \n"
            "    color: rgb(255, 255, 255);\n"
            "    font: 25 12pt \"Segoe UI Light\";\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "    background-color: green;\n"
            "    width: 6px;\n"
            "    margin: 1.2px;\n"
            "    font: 25 12pt \"Segoe UI Light\";\n"
            "}")
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        
        self.frameLogin = QtWidgets.QFrame(self.centralwidget)
        self.frameLogin.setGeometry(QtCore.QRect(0, 0, 1111, 651))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameLogin.sizePolicy().hasHeightForWidth())
        
        self.frameLogin.setSizePolicy(sizePolicy)
        self.frameLogin.setStyleSheet("border: none;")
        self.frameLogin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLogin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLogin.setObjectName("frameLogin")
        
        self.pushButtonLogin = QtWidgets.QPushButton(self.frameLogin)
        self.pushButtonLogin.setGeometry(QtCore.QRect(300, 460, 491, 71))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLogin.sizePolicy().hasHeightForWidth())
        
        self.pushButtonLogin.setSizePolicy(sizePolicy)
        self.pushButtonLogin.setStyleSheet("color: rgb(255, 255, 255);\n"
            "font: 24pt \"Segoe UI\";\n"
            "border-radius: 6px;\n"
            "background-color: rgb(255, 0, 0);")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButtonLogin.clicked.connect(self.login_with_sql)

        self.pushButtonLoginNoSQL = QtWidgets.QPushButton(self.frameLogin)
        self.pushButtonLoginNoSQL.setGeometry(QtCore.QRect(300, 540, 491, 71))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLoginNoSQL.sizePolicy().hasHeightForWidth())

        self.pushButtonLoginNoSQL.setSizePolicy(sizePolicy)
        self.pushButtonLoginNoSQL.setStyleSheet("color: rgb(64, 64, 64);\n"
            "font: 24pt \"Segoe UI\";\n"
            "border-radius: 6px;\n"
            "background-color: rgb(156, 156, 156);")
        self.pushButtonLoginNoSQL.setObjectName("pushButtonLoginNoSQL")
        self.pushButtonLoginNoSQL.clicked.connect(self.login_without_sql)
        
        self.UserInput = QtWidgets.QLineEdit(self.frameLogin)
        self.UserInput.setGeometry(QtCore.QRect(300, 270, 491, 71))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserInput.sizePolicy().hasHeightForWidth())
        
        self.UserInput.setSizePolicy(sizePolicy)
        self.UserInput.setStyleSheet("border: 2px solid;\n"
            "border-radius: 6px;\n"
            "border-color: rgb(255, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font: 24pt \"Segoe UI\";")
        self.UserInput.setObjectName("UserInput")
        
        self.YTLogo_2 = QtWidgets.QLabel(self.frameLogin)
        self.YTLogo_2.setGeometry(QtCore.QRect(200, 10, 261, 241))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YTLogo_2.sizePolicy().hasHeightForWidth())
        
        self.YTLogo_2.setSizePolicy(sizePolicy)
        self.YTLogo_2.setStyleSheet("image: url(:/YTLogo/sm_5b321c9877382.png);")
        self.YTLogo_2.setText("")
        self.YTLogo_2.setObjectName("YTLogo_2")
        
        self.YTLogoLabel_2 = QtWidgets.QLabel(self.frameLogin)
        self.YTLogoLabel_2.setGeometry(QtCore.QRect(420, 60, 411, 141))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YTLogoLabel_2.sizePolicy().hasHeightForWidth())
        
        self.YTLogoLabel_2.setSizePolicy(sizePolicy)
        self.YTLogoLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 25 36pt \"Segoe UI Light\";")
        self.YTLogoLabel_2.setObjectName("YTLogoLabel_2")
        
        self.PasswordInput = QtWidgets.QLineEdit(self.frameLogin)
        self.PasswordInput.setGeometry(QtCore.QRect(300, 360, 491, 71))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PasswordInput.sizePolicy().hasHeightForWidth())
        
        self.PasswordInput.setSizePolicy(sizePolicy)
        self.PasswordInput.setStyleSheet("border: 2px solid;\n"
            "border-radius: 6px;\n"
            "border-color: rgb(255, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font: 24pt \"Segoe UI\";")
        self.PasswordInput.setObjectName("PasswordInput")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Scraper"))
        self.YTLogoLabel.setText(_translate("MainWindow", "Youtube Scraper"))
        self.ChooseLabel.setText(_translate("MainWindow", "Channel:"))
        self.ExtractButton.setText(_translate("MainWindow", "Extract"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Login With SQL"))
        self.pushButtonLoginNoSQL.setText(_translate("MainWindow", "Login Without SQL"))
        self.UserInput.setText(_translate("MainWindow", "Username"))
        self.YTLogoLabel_2.setText(_translate("MainWindow", "Youtube Scraper"))
        self.PasswordInput.setText(_translate("MainWindow", "Password"))

    def login_with_sql(self):

        username = self.UserInput.text()
        password = self.PasswordInput.text()

        data = (username, password)

        try:
            if username == '':
                self.UserInput.setText('Wrong Username')
            elif password == '':
                self.PasswordInput.setText('Wrong Password')
            else:
                validate = db.access_db(data)

                if validate:
                    self.frameLogin.hide()
                else:
                    self.UserInput.setText('Wrong Username')
                    self.PasswordInput.setText('Wrong Password')
                    self.frameLogin.show()
        except:
            self.UserInput.setText('Invalid')
            self.PasswordInput.setText('Invalid')

    def login_without_sql(self):
        self.frameLogin.hide()

    def begin_extract(self):

        self.Timer = random.randint(1,31)
        self.progressBar.setValue(self.Timer)

        if not os.path.exists('DATA'):
            os.mkdir('DATA')

        csvFile = open('DATA/data.csv', 'a', encoding='utf-8')
        csvWrite = csv.writer(csvFile)
        csvWrite.writerow(['CHANNEL', 'LOCATION', 'SUBSCRIBERS', 'DESCRIPTION', 'VIEWS'])

        userinput = self.MainInput.text() + ' channel'

        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.url = ('https://www.youtube.com/')

        self.driver.maximize_window()
        self.driver.get(self.url)

        try:
            self.driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/div/div[1]/input').send_keys(userinput)
            self.driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/a/div/div[2]').click()
            time.sleep(2.1)
            self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/app-toolbar/div/div/paper-tabs/div/div/paper-tab[6]/div').click()
            time.sleep(1.2)

            name = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string').text
            location = self.driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[4]/table/tbody/tr[2]/td[2]/yt-formatted-string')[0].text
            subscribers = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div/div[1]/yt-formatted-string').text
            description = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[1]/yt-formatted-string[2]').text
            views = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[2]/yt-formatted-string[3]').text

            csvWrite.writerow([name, location, subscribers, description, views])
            csvFile.close()

        except Exception:
            self.MainInput.setText('Invalid')

        self.driver.quit()

        self.MainInput.setText('Done -> Check DATA/data.csv')
        self.progressBar.setValue(100)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
