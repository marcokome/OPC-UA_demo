from PyQt5 import QtWidgets, uic
#from PyQt5.QtGui import QPainter, QBrush, QPen, QPalette
from PyQt5.QtGui import *
#from PyQt5.QtCore import Qt
from PyQt5.QtCore import *

from view.untitled import Ui_MainWindow  # importing our generated file

import sys, random, math, json, time

from opcua import Client
import threading

class mywindow(QtWidgets.QMainWindow):

    ultrasonValueChanged = pyqtSignal(float)
    lumiereValueChanged = pyqtSignal(float)
    ultrasonValueChanged = pyqtSignal(float)
    ledValueChanged = pyqtSignal(bool)

    def __init__(self, ip):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.button_ultrason.clicked.connect(self.button_ultrason_clicked)
        self.ui.button_lumiere.clicked.connect(self.button_lumiere_clicked)
        self.ui.button_led.clicked.connect(self.button_led_clicked)


        self.widget_ultrason = self.ui.widget_ultrason
        self.widget_lumiere = self.ui.widget_lumiere
        self.widget_led = self.ui.widget_led

        self.label_ultrason = self.ui.label_ultrason
        self.label_lumiere = self.ui.label_lumiere

        self.label_infos = self.ui.label_infos

        self.valueUltrason = 1.0
        self.valueLumiere = 1.0

        self.state_ultrason = True
        self.state_lumiere = True
        self.state_led = True

        self.margins = 10

        self.url = "opc.tcp://{}:4840".format(ip)

    def start(self):
        threading.Thread(target=self.startClient, daemon=True).start()

    def button_ultrason_clicked(self):
        if self.state_ultrason:
            self.ui.button_ultrason.setText('Activer')
            self.state_ultrason = False
        else:
            self.ui.button_ultrason.setText('Désactiver')
            self.state_ultrason = True
        '''
        val = round(random.random(), 1)*math.pi*10
        self.valueUltrason = round(val, 2)
        print("New angle value {}".format(self.valueUltrason))

        self.ultrasonValueChanged.emit(self.valueUltrason)
        '''

    def button_lumiere_clicked(self):
        if self.state_lumiere:
            self.ui.button_lumiere.setText('Activer')
            self.state_lumiere = False
        else:
            self.ui.button_lumiere.setText('Désactiver')
            self.state_lumiere = True
        '''
        val = round(random.random(), 1)*math.pi*10
        self.valueLumiere = round(val, 2)
        print("New angle value {}".format(self.valueLumiere))

        self.lumiereValueChanged.emit(self.valueLumiere)
        '''

    def button_led_clicked(self):
        if self.state_led:
            self.ui.button_led.setText('Activer')
            self.state_led = False
            self.led_img = 'imgs/light_off.png'
        else:
            self.ui.button_led.setText('Désactiver')
            self.state_led = True
            self.led_img = 'imgs/light_on.png'

        #self.ledValueChanged.emit(self.state_led)

    def on_event_received(self):
        self.update()

    def drawNeedle(self, painter, widget, angle):
       painter.save()
       # Première gauge
       pic = QPixmap("imgs/gauge_back.png")
       #painter.drawPixmap(self.widget.rect(), pic)
       painter.translate(widget.pos().x(), widget.pos().y())
       painter.drawPixmap(widget.rect(), pic)

       #painter.translate(widget.width()/2 - 10, widget.height()-10)
       painter.translate(widget.width()/2 - 5, widget.height() - 5)
       painter.rotate(angle*1.80)

       scale = min((widget.width() - self.margins)/120.0,
                   (widget.height() - self.margins)/120.0)

       # Première aiguille

       painter.scale(scale, scale)
       painter.setPen(QPen(Qt.NoPen))
       painter.setBrush(self.palette().brush(QPalette.Shadow))

       '''
       painter.drawPolygon(
           QPolygon([QPoint(-10, 0), QPoint(0, -45), QPoint(10, 0),
                     QPoint(0, 45), QPoint(-10, 0)])
           )

           '''
       painter.setBrush(self.palette().brush(QPalette.Highlight))
       '''
       painter.drawPolygon(
           QPolygon([QPoint(-5, -25), QPoint(0, -45), QPoint(5, -25),
                     QPoint(0, -30), QPoint(-5, -25)])
           )
           '''
       pen = QPen()
       pen.setWidth(0)
       pen.setColor(QColor('blue'))
       painter.setPen(pen)
       painter.drawLine(QPoint(0, -6), QPoint(-90, -6))
       #painter.drawRoundedRect(QRect(-1.0, -95.0, 5.0, 90.0), 1.0, 15.0)

       #p1 = [QPoint(0,0),QPoint(0,-10),QPoint(-100,-5)]
       p1 = [QPoint(-5,0),QPoint(-5,-10),QPoint(-100,-5)]
       painter.drawPolygon(QPolygon(p1))

       #painter.translate(self.widget_ultrason.width()/2, self.widget_ultrason.height())
       painter.drawEllipse(10, 10, -30, -30)

       #painter.rotate(angle*1.80)

       painter.restore()

    def drawLed(self, painter, widget):
        painter.save()

        pic = QPixmap('imgs/light_on.png') if self.state_led else QPixmap('imgs/light_off.png')
        painter.translate(widget.pos().x(), widget.pos().y())
        painter.drawPixmap(widget.rect(), pic)

        painter.translate(widget.width()/2, widget.height())
        scale = min((widget.width() - self.margins)/120.0,
                   (widget.height() - self.margins)/120.0)
        painter.scale(scale, scale)

        painter.restore()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black,  5, Qt.DotLine))
        # Première gauge
        self.drawNeedle(painter, self.widget_ultrason, self.valueUltrason)
        # Deuxième gauge
        self.drawNeedle(painter, self.widget_lumiere, self.valueLumiere)
        #painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        #painter.drawRect(40, 40, 400, 200)
        self.drawLed(painter, self.widget_led)

    def startClient(self):
        print("Connecting to server {}".format(self.url))
        client = Client(self.url)
        try:
            client.connect()
            print("Client connected !")
            while True:
                Ultrasound = client.get_node("ns=2;i=2").get_value()
                Luminosity = client.get_node("ns=2;i=3").get_value()
                Led = client.get_node("ns=2;i=4").get_value()

                message = json.dumps({"ultrasound":Ultrasound, "luminosity":Luminosity, "led":Led})
                print(message)
                self.valueUltrason = Ultrasound
                self.valueLumiere = Luminosity
                self.state_led = True if Led == 1 else False

                self.label_ultrason.setText(str(Ultrasound))
                self.label_lumiere.setText(str(Luminosity))

                self.ultrasonValueChanged.emit(self.valueUltrason)
                self.lumiereValueChanged.emit(self.valueLumiere)
                self.ledValueChanged.emit(self.state_led)
                '''
                self.updateView(self.ultrason_image, Ultrasound)
                self.updateView(self.lumiere_image, Luminosity)
                self.updateView(self.led_image, Led)
                self.updateView(self.info_button, message)
                '''
                time.sleep(2)

        except Exception as e:
            print("Problem on the network")
            self.label_infos.setText("Problème de réseau ! Le client n'est pas connecté au server OPCUA.")


if __name__=='__main__':
    if len(sys.argv) < 2:
        print("You need an ip adress !")
    elif len(sys.argv) == 2:
        app = QtWidgets.QApplication([])
        application = mywindow(sys.argv[1])
        application.ultrasonValueChanged.connect(application.on_event_received)
        application.lumiereValueChanged.connect(application.on_event_received)
        application.ledValueChanged.connect(application.on_event_received)
        application.start()
        application.show()

        sys.exit(app.exec())
