

import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QStandardItemModel

from GMPC_Tagger import *


class TagLineEdit(QLineEdit):
    def __init__(self):
        super(TagLineEdit, self).__init__()
        self.Old_Pos = 0

    def AutoComplete(self, pattern, pos, auto_val):
        if self.Old_Pos < pos:
            if pattern != '':
                if auto_val:
                    self.setText(auto_val[0])
                    self.cursorBackward(True, (self.cursorPosition() - pos))
            elif pos <= self.oldPos:
                self.setText(pattern)
        self.Old_Pos = pos



class TagList(QAbstractListModel):
    def __init__(self,  usr_tags, parent=None):
        super(TagList, self).__init__(parent)
        self.User_Tags = usr_tags

    def rowCount(self, parent=QModelIndex()):
        return len(self.User_Tags)

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.User_Tags[index.row()])
        else:
            return QVariant()

    def reset(self):
        self.beginResetModel()
        self.endResetModel()

    def setAvaliableTags(self, cut_list):
        self.User_Tags = cut_list
        self.reset()


class FileNameEdit(QLineEdit):

    def __init__(self):
        super(FileNameEdit, self).__init__()



class ImageUsrInterface(QWidget):
    # Create Layout for interface
    Layout = QVBoxLayout()

    # Setup information widgets (input prompt and Media_path)
    InputPrompt = QLabel("Type a tag, press tab to autocomplete and display previous tags")
    AcceptInput = QLabel("Press Enter to accept tag\n" +
                         "If a new Tag is requested an additional prompt will be shown")
    WidgetSize = QSize()
    FileName = ''
    Cut_List = []

    # Signals


    #CreateSignal for keypress

    def __init__(self, width, height, usr_tags: ImageTagDict):
        super(ImageUsrInterface, self).__init__()
        # Set Widget values
        self.Usr_Tags = usr_tags
        self.WidgetSize.setWidth(width)
        self.WidgetSize.setHeight(height)
        self.setBaseSize(self.WidgetSize)
        self.setMaximumSize(self.WidgetSize)

        # Create any Widgets that haven't been created yet

        self.UsrInputBox = TagLineEdit()
        self.UsrTagModel = TagList(self.Usr_Tags.getTagList(), self)
        self.UsrTagView = QListView()
        self.UsrTagView.setSelectionMode(QAbstractItemView.SingleSelection)
        #self.TagTest = QStandardItemModel(self.UsrTagView)

        self.UsrTagView.setModel(self.UsrTagModel)
        self.FileNameBox = FileNameEdit()

        #install EventFilters
        self.UsrInputBox.installEventFilter(self)
        self.UsrTagView.installEventFilter(self)
        self.FileNameBox.installEventFilter(self)

        # Add Widgets to layout and set it for this widget
        self.Layout.addWidget(self.InputPrompt)
        self.Layout.addWidget(self.UsrInputBox)
        self.Layout.addWidget(self.UsrTagView)
        self.Layout.addWidget(self.FileNameBox)
        self.Layout.addWidget(self.AcceptInput)
        self.setLayout(self.Layout)


        # Connections
        self.UsrInputBox.textEdited.connect(self.TextEntry)
        self.UsrTagView.selectionModel().currentChanged.connect(self.ListSelect)





    def CutTags(self, pattern):
        return [item for item in self.Usr_Tags.getTagList() if item.find(pattern) == 0]

    def TextEntry(self):
        pattern = str(self.UsrInputBox.text())
        pos = self.UsrInputBox.cursorPosition()
        if pattern != '':
            self.Cut_List = self.CutTags(pattern)
            self.UsrTagModel.setAvaliableTags(self.Cut_List)
            self.UsrInputBox.AutoComplete(pattern, pos, self.Cut_List)
        else:
            self.UsrTagModel.setAvaliableTags(self.Usr_Tags.getTagList())
            self.UsrInputBox.Old_Pos = 0

    def ListSelect(self, cur_tag, prev_tag):
        #print(cur_tag.data())
        self.UsrInputBox.setText(cur_tag.data())

    def UpdateFileName(self, filename):
        head, self.FileName = os.path.split(filename)
        self.FileNameBox.setText(self.FileName)

    def ReturnFileName(self):
        return self.FileNameBox.text()

    def ReturnCurTag(self):
        return self.UsrInputBox.text()

    def PullInput(self):
        return self.ReturnCurTag(), self.ReturnFileName()


def string_intersect(str1, str2):
    newlist = []
    for i, j in zip(str1, str2):
        if i == j:
            newlist.append(i)
        else:
            break
    return ''.join(newlist)