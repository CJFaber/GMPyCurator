
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ImageViewer(QWidget):

    # Create variables specific to image display
    Img_Zoom = 0
    Img_Pix_Offset = 50  # Pixel offset for image resizing
    # Create Layout for this Widget
    Layout = QVBoxLayout()
    # Create Widgets in this layout
    Cur_Image = QImage()
    Media_Path = QLabel()
    Default_Size = QSize()
    Scene = QGraphicsScene()
    View = QGraphicsView(Scene)

    def __init__(self, width, height):
        super(ImageViewer, self).__init__()

        # create signals/Shortcuts for zoom in/out
        self.Zoom_In = QShortcut(self)
        self.Zoom_In.setKey(Qt.Key_F12)
        self.Zoom_Out = QShortcut(self)
        self.Zoom_Out.setKey(Qt.Key_F11)
        self.Zoom_In.activated.connect(self.ImageEventZoomIn)
        self.Zoom_Out.activated.connect(self.ImageEventZoomOut)

        # add Widgets to layout
        self.setGeometry(0, 0, width, height)
        self.Default_Size.setHeight(height - 70)
        self.Default_Size.setWidth(width)
        self.setBaseSize(self.Default_Size)
        self.Layout.addWidget(self.View)
        self.Layout.addWidget(self.Media_Path)
        self.setLayout(self.Layout)


    def OpenMedia(self, image_path):
        # Reset Img_Zoom
        self.Scene.clear()
        self.Img_Zoom = 0
        self.Cur_Image.load(image_path)
        temp_img = self.Cur_Image.scaled(self.Default_Size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Scene.addPixmap(QPixmap.fromImage(temp_img))
        self.Scene.update()
        self.Media_Path.setText(image_path)
        self.Media_Path.repaint()


    def ImageEventZoomIn(self):
        self.Img_Zoom += 1
        self.setFocus()
        if self.Img_Zoom > 0:
            self.View.scale(1.1, 1.1)
        elif self.Img_Zoom == 0:
            self.ImageResetSize()
        else:
            self.Img_Zoom = 0

    def ImageEventZoomOut(self):
        self.Img_Zoom -= 1
        self.setFocus()
        if self.Img_Zoom > 0:
            self.View.scale(.9, .9)
        elif self.Img_Zoom == 0:
            self.ImageResetSize()
        else:
            self.Img_Zoom = 0

    def ImageResetSize(self):
        self.Scene.clear()
        self.View.resetTransform()
        temp_image = self.Cur_Image.scaled(self.Default_Size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Scene.addPixmap(QPixmap.fromImage(temp_image))