# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PINS_CONFIG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import  QMessageBox
import sys
import os
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
#importing xmltodict module
import xmltodict


class Ui_Form(object):
    SelPINS_DECT={}
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(788, 871)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 85, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PIN_DIR = QGroupBox(Form)
        self.PIN_DIR.setObjectName(u"PIN_DIR")
        self.PIN_DIR.setGeometry(QRect(70, 170, 161, 201))
        font = QFont()
        font.setPointSize(10)
        self.PIN_DIR.setFont(font)
        self.OUTPUT = QRadioButton(self.PIN_DIR)
        self.OUTPUT.setObjectName(u"OUTPUT")
        self.OUTPUT.setGeometry(QRect(20, 60, 95, 20))
        self.OUTPUT.setFont(font)
        self.OUTPUT.setAutoFillBackground(False)
        self.INPUT = QRadioButton(self.PIN_DIR)
        self.INPUT.setObjectName(u"INPUT")
        self.INPUT.setGeometry(QRect(20, 120, 95, 20))
        self.INPUT.setFont(font)
        self.INPUT_CONFIG = QGroupBox(Form)
        self.INPUT_CONFIG.setObjectName(u"INPUT_CONFIG")
        self.INPUT_CONFIG.setGeometry(QRect(280, 290, 301, 91))
        self.INPUT_CONFIG.setFont(font)
        self.PULL_UP = QRadioButton(self.INPUT_CONFIG)
        self.PULL_UP.setObjectName(u"PULL_UP")
        self.PULL_UP.setGeometry(QRect(20, 40, 95, 20))
        self.PULL_UP.setFont(font)
        self.HIGH_IMP = QRadioButton(self.INPUT_CONFIG)
        self.HIGH_IMP.setObjectName(u"HIGH_IMP")
        self.HIGH_IMP.setGeometry(QRect(130, 40, 161, 21))
        self.HIGH_IMP.setFont(font)
        self.OUTPUT_CONFIG = QGroupBox(Form)
        self.OUTPUT_CONFIG.setObjectName(u"OUTPUT_CONFIG")
        self.OUTPUT_CONFIG.setGeometry(QRect(280, 170, 301, 91))
        self.OUTPUT_CONFIG.setFont(font)
        self.HIGH = QRadioButton(self.OUTPUT_CONFIG)
        self.HIGH.setObjectName(u"HIGH")
        self.HIGH.setGeometry(QRect(20, 40, 95, 20))
        self.HIGH.setFont(font)
        self.LOW = QRadioButton(self.OUTPUT_CONFIG)
        self.LOW.setObjectName(u"LOW")
        self.LOW.setGeometry(QRect(150, 40, 95, 20))
        self.LOW.setFont(font)
        self.GENERATE = QPushButton(Form)
        self.GENERATE.setObjectName(u"GENERATE")
        self.GENERATE.setGeometry(QRect(400, 530, 231, 41))
        self.GENERATE.setFont(font)
        self.PATH = QTextEdit(Form)
        self.PATH.setObjectName(u"PATH")
        self.PATH.setGeometry(QRect(520, 440, 211, 41))
        self.PATH.setFont(font)
        self.PIN_SELECTION = QComboBox(Form)
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.addItem("")
        self.PIN_SELECTION.setObjectName(u"PIN_SELECTION")
        self.PIN_SELECTION.setGeometry(QRect(630, 190, 81, 41))
        self.PIN_SELECTION.setFont(font)
        self.PIN_SELECTION.setAutoFillBackground(False)
        self.ADD = QPushButton(Form)
        self.ADD.setObjectName(u"ADD")
        self.ADD.setGeometry(QRect(60, 420, 181, 31))
        self.ADD.setFont(font)
        self.LOAD = QPushButton(Form)
        self.LOAD.setObjectName(u"LOAD")
        self.LOAD.setGeometry(QRect(60, 540, 181, 31))
        self.LOAD.setFont(font)
        self.SAVE = QPushButton(Form)
        self.SAVE.setObjectName(u"SAVE")
        self.SAVE.setGeometry(QRect(60, 480, 181, 31))
        self.SAVE.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 440, 171, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setAcceptDrops(False)

        self.retranslateUi(Form)
        
        
        
        QObject.connect(self.OUTPUT,SIGNAL("clicked(bool)"),self.INPUT_CONFIG.setDisabled)
        QObject.connect(self.INPUT,SIGNAL("clicked(bool)"),self.OUTPUT_CONFIG.setDisabled)
        QObject.connect(self.OUTPUT,SIGNAL("clicked(bool)"),self.OUTPUT_CONFIG.setEnabled)
        QObject.connect(self.INPUT,SIGNAL("clicked(bool)"),self.INPUT_CONFIG.setEnabled)
        self.GENERATE.clicked.connect(self.GenerateFunction)
        self.ADD.clicked.connect(self.Add_Handle)
        self.PIN_SELECTION.currentTextChanged.connect(self.ComboBox_Handle)
        self.SAVE.clicked.connect(self.Save_Handle)
        self.LOAD.clicked.connect(self.Load_Handle)

        
      

        QMetaObject.connectSlotsByName(Form)
        
    def  GenerateInterfaceFile(self):
        Output_Path = self.PATH.toPlainText() + r'\Dio_INTERFACE.h'
        File_Handler = open(Output_Path ,'w')
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("*******************************   Author  : Taqwa Hamed     *****************************\n")
        File_Handler.write("*******************************   SWC     : Dio_Interface.h *****************************\n")
        File_Handler.write("*******************************   Version : Version 01      *****************************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("#ifndef _DIO_INTERFACE_H_\n")
        File_Handler.write("#define _DIO_INTERFACE_H_\n")
        File_Handler.write("\n\n")
        File_Handler.write("#include \"std_types.h\"\n\n")
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("************** Don't Change The following MACROS *******************\n")
        File_Handler.write("****************************************************************************************/\n")
        for i in range(self.PIN_SELECTION.count()):
            File_Handler.write("#define " + self.PIN_SELECTION.itemText(i)+"       ((u8)"+str(i) + ")\n")  
        File_Handler.write("\n\n")
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("************** Don't Change The following MACROS   *******************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("\n")
        File_Handler.write("#define DIO_INIT_TO_ZERO    ((u8)0)\n")
        File_Handler.write("#define DIO_INIT_TO_ONE     ((u8)1)\n")
        File_Handler.write("#define DIO_OK              ((u8)1)\n")
        File_Handler.write("#define DIO_NOT_OK          ((u8)0)\n")
        File_Handler.write("#define DIO_TRUE            ((u8)1)\n")
        File_Handler.write("#define DIO_FALSE           ((u8)0)\n")
        File_Handler.write("\n\n")
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("************** Don't Change The following MACROS   *******************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("\n\n")
        File_Handler.write("#define DIOA                 ((u8)0)\n")
        File_Handler.write("#define DIOB                 ((u8)1)\n")
        File_Handler.write("#define DIOC                 ((u8)2)\n")
        File_Handler.write("#define DIOD                 ((u8)3)\n")
        File_Handler.write("\n\n")
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("******************* Add Your Implementation here   *******************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("\n\n")
        File_Handler.write("#endif /*_DIO_INTERFACE_H_*/\n")  

    def GenerateConfigFile(self):
        Output_Path = self.PATH.toPlainText() + r'\Dio_CONFIG.h'
        File_Handler = open(Output_Path ,'w')
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("*******************************   Author  : Taqwa Hamed    ******************************\n")
        File_Handler.write("*******************************   SWC     : Dio_Config.h   ******************************\n")
        File_Handler.write("*******************************   Version : Version 01     ******************************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("#ifndef _DIO_CONFIG_H\n")
        File_Handler.write("#define _DIO_CONFIG_H\n")
        File_Handler.write("\n\n")
        File_Handler.write("#include \"std_types.h\"\n")
        File_Handler.write("#include \"Dio_INTERFACE.h\"  \n\n")
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("************** Don't Change The following MACROS *******************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("#define  OUTPUT_HIGH     ((u8)0)\n")
        File_Handler.write("#define  INPUT_PULL_UP   ((u8)1)\n")
        File_Handler.write("#define  INPUT_HIGH_IMP  ((u8)2)\n")
        File_Handler.write("#define  OUTPUT_LOW      ((u8)3)\n")
        File_Handler.write("\n\n")
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("************** Don't Change The following MACROS   *******************\n")
        File_Handler.write("************** MicroController Pins Configurations *******************\n")
        File_Handler.write("****************************************************************************************/\n\n")
        File_Handler.write("#define NUM_OF_PINS     ((u8)"+ str(len(self.SelPINS_DECT)) + ")\n\n")
        for Pin_Name in self.SelPINS_DECT.keys():
          Pin_Config = list(self.SelPINS_DECT[Pin_Name])
          File_Handler.write("#define "+Pin_Name+"_CONFIG"+ "        ((u8)"+Pin_Config[0]+"_"+Pin_Config[1] + ")")
          File_Handler.write("\n")

        File_Handler.write("\n\n")
        File_Handler.write("DIO_Pin_Configurations_ST DIO_PINS_arr[NUM_OF_PINS] = { \n")
        PINS_Configured = list(self.SelPINS_DECT.keys())
        for Pin_Number in range(len(PINS_Configured) - 1):
            File_Handler.write("                   {" + PINS_Configured[Pin_Number] + ", "+ PINS_Configured[Pin_Number]+ "_CONFIG"+ "},\n")
        
        File_Handler.write("                   {" + PINS_Configured[len(PINS_Configured)-1] + ", "+ PINS_Configured[len(PINS_Configured)-1]+ "_CONFIG"+ "}\n")
        File_Handler.write(("};\n").rstrip('\n'))
        File_Handler.write("\n")
        File_Handler.write("#endif /*_DIO_CONFIG_H*/\n")    

    def Generate_StandardTypes(self):
        Output_Path = self.PATH.toPlainText() + r'\std_types.h'
        File_Handler = open(Output_Path ,'w')
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("*******************************   Author  : Taqwa Hamed    ******************************\n")
        File_Handler.write("*******************************   SWC     : std_types.h   ******************************\n")
        File_Handler.write("*******************************   Version : Version 01     ******************************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("#ifndef _STD_TYPES_H_\n")
        File_Handler.write("#define _STD_TYPES_H_\n")
        File_Handler.write("\n\n")
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("************** Don't Change The following MACROS *******************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("typedef unsigned char            u8;\n")
        File_Handler.write("typedef signed char              s8;\n")
        File_Handler.write("typedef unsigned short           u16;\n")
        File_Handler.write("typedef signed short             s16;\n")
        File_Handler.write("typedef unsigned long            u32;\n")
        File_Handler.write("typedef signed long              s32;\n")
        File_Handler.write("typedef unsigned long long       u64;\n")
        File_Handler.write("typedef signed long long         s64;\n")
        File_Handler.write("typedef float                    f32;\n")
        File_Handler.write("typedef double                   f64;\n")
        File_Handler.write("\n\n")
        File_Handler.write("#endif /*_STD_TYPES_H_*/\n") 


    def GeneratePrivateFile(self):
        Output_Path = self.PATH.toPlainText() + r'\Dio_PRIVATE.h'
        File_Handler = open(Output_Path ,'w')
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("*******************************   Author  : Taqwa Hamed    ******************************\n")
        File_Handler.write("*******************************   SWC     : Dio_Private.h  ******************************\n")
        File_Handler.write("*******************************   Version : Version 01     ******************************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("#ifndef _DIO_PRIVATE_H_\n")
        File_Handler.write("#define _DIO_PRIVATE_H_\n")
        File_Handler.write("\n\n")
        File_Handler.write("#include \"std_types.h\"\n\n")
        File_Handler.write("/****************************************************************************************\n")
        File_Handler.write("************** Don't Change The following MACROS *******************\n")
        File_Handler.write("****************************************************************************************/\n")
        File_Handler.write("typedef struct { \n")
        File_Handler.write("                u8 Pin_Number; \n")
        File_Handler.write("                u8 Pin_Configs; \n")
        File_Handler.write("}DIO_Pin_Configurations_ST; \n")
        File_Handler.write("\n\n")
        File_Handler.write("#endif /*_DIO_PRIVATE_H_*/\n")   



    def GenerateFunction(self):
      if os.path.exists(self.PATH.toPlainText()):
        self.GenerateInterfaceFile()
        self.GenerateConfigFile()
        self.Generate_StandardTypes()
        self.GeneratePrivateFile()
      else:
        msgBox = QMessageBox()
        msgBox.setText("You Enterd a Wrong Path")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec()
        
    def Save_Handle(self):
      if os.path.exists(self.PATH.toPlainText()):
        Output_Path = self.PATH.toPlainText() +"\Pins_Configs.xml"
        My_Pins = {}
        for key, item in self.SelPINS_DECT.items(): # .items >> return key and the value
            #print(key)
            #print(item)
            #print("=========================")
            PINS_XML_Dict = {}
            for K , i in item.items(): # looping on the config of each pin
                #print(K)
                #print(i)
                #print("++++++++++++++++++++++")
                if K in ["INPUT" , "OUTPUT"]:
                    PINS_XML_Dict["Pin_Direction"] = K
                else:
                    PINS_XML_Dict["Pin_State"] = K
            My_Pins[key] = PINS_XML_Dict
            #print(My_Pins[key])
        xml = dicttoxml(My_Pins, attr_type=False)
        parsed_xml = parseString(xml)
        with open(Output_Path, 'w') as file:
            file.write(parsed_xml.toprettyxml())
      else:
        msgBox = QMessageBox()
        msgBox.setText("You Enterd a Wrong Path")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec()
    

    def Load_Handle(self):
      Group_list=[self.PIN_DIR,self.OUTPUT_CONFIG,self.INPUT_CONFIG]
      Loaded_Pins_Dict = {}
      if os.path.exists(self.PATH.toPlainText()):
        Output_Path = self.PATH.toPlainText() +"\Pins_Configs.xml"
        with open(Output_Path, 'r', encoding='utf-8') as file:
            my_xml = file.read()  
            # Use xmltodict to parse and convert 
            # the XML document
            my_xml_dict = xmltodict.parse(my_xml)
            # Print the dictionary
            for key , item in my_xml_dict["root"].items():
                Pin_Config_Dict = {}
                for sub_key , value in item.items():
                    Pin_Config_Dict[value] = True
                Loaded_Pins_Dict[key] = Pin_Config_Dict

        self.SelPINS_DECT = Loaded_Pins_Dict
        if self.PIN_SELECTION.currentText()in self.SelPINS_DECT.keys():  
          for group in Group_list:
            for radioButton in group.findChildren(QRadioButton):
              Rad_Name= radioButton.objectName()
              Pin_Name=self.PIN_SELECTION.currentText()
              if Rad_Name in self.SelPINS_DECT[Pin_Name].keys():
                radioButton.setChecked(True)
          
      else:
        msgBox = QMessageBox()
        msgBox.setText("You Enterd a Wrong Path")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec()
        
        
    # setupUi
    def Add_Handle(self):
      Group_list=[self.PIN_DIR,self.OUTPUT_CONFIG,self.INPUT_CONFIG]
      PINS_DECT={}
      for group in Group_list:
        for radioButton in group.findChildren(QRadioButton):
          if radioButton.isChecked():
            PINS_DECT[radioButton.objectName()]=radioButton.isChecked()
      self.SelPINS_DECT[self.PIN_SELECTION.currentText()]=PINS_DECT      
      #print(list(PINS_DECT))
      #print(self.SelPINS_DECT)

          
    def ComboBox_Handle(self):
      Group_list=[self.PIN_DIR,self.OUTPUT_CONFIG,self.INPUT_CONFIG]
      for group in Group_list:
        group.setEnabled(True)
        for radioButton in group.findChildren(QRadioButton):
          radioButton.setAutoExclusive(False)
          radioButton.setChecked(False)
          radioButton.setAutoExclusive(True)
      if self.PIN_SELECTION.currentText()in self.SelPINS_DECT.keys():  
        for group in Group_list:
          for radioButton in group.findChildren(QRadioButton):
            Rad_Name= radioButton.objectName()
            Pin_Name=self.PIN_SELECTION.currentText()
            if Rad_Name in self.SelPINS_DECT[Pin_Name].keys():
              radioButton.setChecked(True)
              
            
        
        
            
      
      
        
        
        
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PIN_DIR.setTitle(QCoreApplication.translate("Form", u"PIN DIRECTON", None))
        self.OUTPUT.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.INPUT.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.INPUT_CONFIG.setTitle(QCoreApplication.translate("Form", u"INPUT CONFIGURATIONS", None))
        self.PULL_UP.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.HIGH_IMP.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.OUTPUT_CONFIG.setTitle(QCoreApplication.translate("Form", u"OUTPUT CONFIGURATIONS", None))
        self.HIGH.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.LOW.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.GENERATE.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.PIN_SELECTION.setItemText(0, QCoreApplication.translate("Form", u"PIN0", None))
        self.PIN_SELECTION.setItemText(1, QCoreApplication.translate("Form", u"PIN1", None))
        self.PIN_SELECTION.setItemText(2, QCoreApplication.translate("Form", u"PIN2", None))
        self.PIN_SELECTION.setItemText(3, QCoreApplication.translate("Form", u"PIN3", None))
        self.PIN_SELECTION.setItemText(4, QCoreApplication.translate("Form", u"PIN4", None))
        self.PIN_SELECTION.setItemText(5, QCoreApplication.translate("Form", u"PIN5", None))
        self.PIN_SELECTION.setItemText(6, QCoreApplication.translate("Form", u"PIN6", None))
        self.PIN_SELECTION.setItemText(7, QCoreApplication.translate("Form", u"PIN7", None))
        self.PIN_SELECTION.setItemText(8, QCoreApplication.translate("Form", u"PIN8", None))
        self.PIN_SELECTION.setItemText(9, QCoreApplication.translate("Form", u"PIN9", None))
        self.PIN_SELECTION.setItemText(10, QCoreApplication.translate("Form", u"PIN10", None))
        self.PIN_SELECTION.setItemText(11, QCoreApplication.translate("Form", u"PIN11", None))
        self.PIN_SELECTION.setItemText(12, QCoreApplication.translate("Form", u"PIN12", None))
        self.PIN_SELECTION.setItemText(13, QCoreApplication.translate("Form", u"PIN13", None))
        self.PIN_SELECTION.setItemText(14, QCoreApplication.translate("Form", u"PIN14", None))
        self.PIN_SELECTION.setItemText(15, QCoreApplication.translate("Form", u"PIN15", None))
        self.PIN_SELECTION.setItemText(16, QCoreApplication.translate("Form", u"PIN16", None))
        self.PIN_SELECTION.setItemText(17, QCoreApplication.translate("Form", u"PIN17", None))
        self.PIN_SELECTION.setItemText(18, QCoreApplication.translate("Form", u"PIN18", None))
        self.PIN_SELECTION.setItemText(19, QCoreApplication.translate("Form", u"PIN19", None))
        self.PIN_SELECTION.setItemText(20, QCoreApplication.translate("Form", u"PIN20", None))
        self.PIN_SELECTION.setItemText(21, QCoreApplication.translate("Form", u"PIN21", None))
        self.PIN_SELECTION.setItemText(22, QCoreApplication.translate("Form", u"PIN22", None))
        self.PIN_SELECTION.setItemText(23, QCoreApplication.translate("Form", u"PIN23", None))
        self.PIN_SELECTION.setItemText(24, QCoreApplication.translate("Form", u"PIN24", None))
        self.PIN_SELECTION.setItemText(25, QCoreApplication.translate("Form", u"PIN25", None))
        self.PIN_SELECTION.setItemText(26, QCoreApplication.translate("Form", u"PIN26", None))
        self.PIN_SELECTION.setItemText(27, QCoreApplication.translate("Form", u"PIN27", None))
        self.PIN_SELECTION.setItemText(28, QCoreApplication.translate("Form", u"PIN28", None))
        self.PIN_SELECTION.setItemText(29, QCoreApplication.translate("Form", u"PIN29", None))
        self.PIN_SELECTION.setItemText(30, QCoreApplication.translate("Form", u"PIN30", None))
        self.PIN_SELECTION.setItemText(31, QCoreApplication.translate("Form", u"PIN31", None))

        self.ADD.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.LOAD.setText(QCoreApplication.translate("Form", u"LOAD", None))
        self.SAVE.setText(QCoreApplication.translate("Form", u"SAVE", None))
        self.label.setText(QCoreApplication.translate("Form", u"    ENTER THE PATH", None))
    # retranslateUi

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()

Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())
