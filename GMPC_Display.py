
import sys
from GMPC_Images import *
from GMPC_UsrInterface import *
from GMPC_Tagger import *
import pprint
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter


class MediaDisplay(QMainWindow):
    Screen_x = 30  # inital x location on screen
    Screen_y = 100  # initial y location on screen
    Width = 1850  # Window width    Image/media = 1150 | UserTagLayout = 700
    Height = 900  # Window Height
    Img_Pix_Offset = 50  # Pixel offset for image resizing
    Title = 'GMPC - '
    WindowDim = QSize(Width, Height)

    MediaW = 1150
    MediaH = 900
    InterfaceW = 500
    InterfaceH = 900
    TagLibrary = None
    # create a text box for image path and name, Used for all media


    def __init__(self, mode, usr_tags):
        # Mode is string selected by user
        super(MediaDisplay, self).__init__()
        self.MainWindow = QWidget()
        self.MainWindowLayout = QHBoxLayout()
        self.UserTagLayout = QVBoxLayout()
        self.MediaLayout = QVBoxLayout()
        self.Title += mode



        # SetWindow properties
        self.setGeometry(self.Screen_x, self.Screen_y, self.Width, self.Height)
        self.setWindowIcon(QIcon.fromTheme('view-sort-ascending'))
        self.setWindowTitle(self.Title)

        #Depending on the mode create Media Widget and Interface Widget
        if mode == 'Images':
            self.MediaViewer = ImageViewer(self.MediaW, self.MediaH)
            self.UsrInterface = ImageUsrInterface(self.InterfaceW, self.InterfaceH, usr_tags)
            self.TagLibrary = usr_tags
        elif mode == 'Movies':
            # self.MediaViewer = MovieViewer()
            # self.UsrInterface = ImageUsrInterface()
            print ("hello!")
        else:
            # self.MediaViewer = ImageViewer()
            # self.UsrInterface = ImageUsrInterface()
            print ("Hello!")

        # Set up Layouts and set central QWidget
        self.MainWindowLayout.addWidget(self.MediaViewer)
        self.MainWindowLayout.addWidget(self.UsrInterface)
        self.MainWindow.setLayout(self.MainWindowLayout)
        self.setCentralWidget(self.MainWindow)


    # ------------------------------
    # Widget Initializer functions
    #   Updates the window with the necessary widgets/variables given what type of
    #   curation we are preforming
    # ------------------------------


    # Turns the window into an image display with path shown

    def StartCuration(self, file_list):
        self.MediaViewer.OpenMedia(file_list[0])
        self.UsrInterface.UpdateFileName(file_list[0])

    def GetTag(self):
        tag, filename = self.UsrInterface.PullInput()
        if tag not in self.TagLibrary.getTagList():
            self.UsrTagPrompt()





    def UsrTagPrompt(self):
        # OpenDialog box to input new tag and pass new libary to UsrInterface
        Dialog = QDialog()
        prompt = QLabel("Tag not found! Please enter tag information:")
        T1 = QLabel("Tag index (What you want to show in the tag display")
        T2 = QLabel("Super tag (What you would like tag to be categorized under, \
                                Must be an existing index tag or type \"ROOT\" if none")
        T3 = QLabel("Tag name (What you would like the final folder destination to be)")
        L1 = QLineEdit()
        L2 = QLineEdit ()
        L3 = QLineEdit ()
        Layout = QVBoxLayout()
        Layout.addWidget(prompt)
        Layout.addWidget(T1)
        Layout.addWidget(L1)
        Layout.addWidget(T2)
        Layout.addWidget(L2)
        Layout.addWidget(T3)
        Layout.addWidget(L3)
        ok = QPushButton("OK", Dialog)
        cancel = QPushButton("Cancel", Dialog)
        ButtonLayout = QHBoxLayout()
        ButtonLayout.addWidget(ok)
        ButtonLayout.addWidget(cancel)
        Layout.addLayout(ButtonLayout)
        Dialog.setWindowTitle("New Tag Entry")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.setLayout(Layout)
        Dialog.exec_()
        #ok.clicked.connect(self.NewTagCheck(L3, L2, L1))
        #cancel.clicked.connect(sys.exit())



    def NewTagCheck(self, tag, suptag, lookup):
        print( self.TagLibrary.AddTag(tag.text, suptag.text, lookup.text))
            #raise Exception("Incorrect supertag or lookup tag already exists")

    def Curate(self):
        print("HELLO")



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if (event.key() == Qt.Key_Return) or (event.key() == Qt.Key_Enter):
            self.GetTag()
            self.Curate()

#    def displayMovie(self):

#    def displayMusic(self):







