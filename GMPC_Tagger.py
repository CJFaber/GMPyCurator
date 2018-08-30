'''

GMPC_Tagger

Contains classes associated with tags

'''

import csv
import os

class ImageTag:
    def __init__(self, tag: str, suptag: str, lookup: str):
        self.ImageTagName = tag             #The actual folder the image will be stored under
        self.ImageSuperTag = suptag         #The super tag the ImageTagName is catagorigezed under, Takes the name of
                                            #   ImageTagIndex for its given supertag
        self.ImageTagIndex = lookup         #The lookup name of this given tag, used in autocomplete / tag search

    def getIndex(self):
        return self.ImageTagIndex

    def getSupTag(self):
        return self.ImageSuperTag

    def getTagName(self):
        return self.ImageTagName


class ImageTagDict():
    def __init__(self):
        self.ImageTagDictionary = {}       # Dictionary of tags
        self.ImageTagList = []             # List of Indexes

    #Load tags from CSV
    def LoadTags(self, database_src):
        os.path.isfile(database_src)
        with open(database_src) as csvfile:
            tagreader = csv.reader(csvfile, delimiter=',')
            for row in tagreader:
                if not self.AddTag(row[0], row[1], row[2]):
                    print("Error!: Subtag found before supertag")



    def AddTag(self, tag: str, suptag: str, lookup: str):
        if lookup not in self.ImageTagList:
            if(suptag == 'ROOT') or (suptag in self.ImageTagList):
                newtag = ImageTag(tag, suptag, lookup)
                self.ImageTagDictionary[lookup] = newtag
                self.ImageTagList.insert(0, lookup)
                return True
            else:
                return False
        else:
            return False

    def getTagList(self):
        return sorted(self.ImageTagList, key=str.lower)

    def getImageTag(self, key):
        return self.ImageTagDictionary[key]

    def getTagPath(self, key):
        curkey = key
        path = '/'
        while(curkey != 'ROOT'):
            path = '/' + ImageTagDict[curkey].getTagName() + path
            curkey = ImageTagDict[curkey].getIndex()
        return path
