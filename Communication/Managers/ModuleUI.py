import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Notebook
import datetime
from Modules.Config import Configuration as MainConfig

""" Liad Kashanovsky - Module UI for loaded and arrived Protobuf messages, display

    Create UI tab and sub tabs for each Protobuf loaded module (Classes and attributes)
    Each Tab (Frame) title = topic (Protobuf class name)
    Each Protobuf attribute can be defined to be displayed or not using config.message (per specific protobuf)
    Aggregate ChainResponsibility for Protobuff arrived messages callback as defined in config.messages"""

from Communication.Managers.ModuleManager import *

class Tabs:
    def __init__(self, oModuleUI, parent):
        self.selected_tab = None
        self.tab_top_flag = False
        self.oModuleUI = oModuleUI
        self.oConfig = MainConfig()
        self.oTKRoot = oModuleUI.oTKRoot
        self.notebook = Notebook(parent)  # Create the program notebook
        self.notebook.pack(padx=0, pady=0, fill='both', expand = 1)
        
        self.oFrames={}
    
    def addFrame(self, title):
        oFrame = Frame(self.notebook, width=self.oConfig.tab_width, height=self.oConfig.form_height)
        self.oFrames[title] = oFrame
        if self.tab_top_flag == False:
            self.tab_top_flag = True
            self.notebook.add(oFrame, text=title, compound=TOP)
        else:
            self.notebook.add(oFrame, text=title)
        return oFrame


class TModuleUIForm:
    #__slots__ = ('__dict__')
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(TModuleUIForm, cls).__new__(cls)
            cls.instance.initialize()
        return cls.instance

    def initialize(self):
        self.tab_top_flag = False
        self.oGenericProtoManager = GenericProtoManager()
        self.rdr_id = 0  # radar id received from
        self.engine_state = 0  # on off
        self.radar_state = 3
        self.record_state = 6
        self.current_preset = 1
        self.preset_response_msg = None
        self.proto = None
        self.oModulesManager = ModuleManager()
        self.oChainResponsibility = ChainResponsibility()
        self.oChainResponsibility.oModuleUI = self # Aggregation for ChaonResponsibility Updating UI when Protobuf message arrives
        self.oConfig = MainConfig()
        self.oModulesFrames = {}
        self.tk = tk
        self.oTKRoot = tk.Tk()
        self.oTKRoot.title(self.oConfig.gatewayID)
        self.font_3 = Font(family='Arial', size=12, weight='normal', slant='roman', underline=0, overstrike=0)
        self.font_4 = Font(family='Arial', size=12, weight='bold', slant='roman', underline=0, overstrike=0)

        window_width = self.oConfig.form_width
        window_height = self.oConfig.form_height

        # get the screen dimension
        screen_width = self.oTKRoot.winfo_screenwidth()
        screen_height = self.oTKRoot.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.oTKRoot.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.oTKRoot.configure(background='DimGray')

        self.oTKRoot.resizable(width=False, height=False)

        # create a notebook
        oTabs = Tabs(self, self.oTKRoot)
        # create frames
        modules = self.oGenericProtoManager.modules
        postfix = '_pb2'
        index = 0
        """ Create UI tab for each Protobuf loaded module (Class and attributes)
            Each Tab (Frame) title = topic (Protobuf class name)
            Each Protobuf attribute can be defined to be displayed or not using config.message (per specific protobuf)"""
        for module_name in modules:
           if postfix in module_name:
             module_name_short = module_name.replace(postfix, '')
             oFrame = oTabs.addFrame(module_name_short)
             oTabChildren = Tabs(self, oFrame)
             oTopics = modules[module_name]
             for topic in oTopics:
                 oFrameChild = oTabChildren.addFrame(topic)
                 oMsg = oTopics[topic]
                 for attr in oMsg:
                     index += 1
                     self.__add_attribute(oFrameChild, attr, module_name+topic+attr, index)

        self.oTKRoot.title = "Protobuf Monitor"
        self.oTKRoot.protocol("WM_DELETE_WINDOW", self.__on_closing)# Clean exit
        # run form main loop
        self.__execute()

    def __execute(self):
        self.oTKRoot.mainloop()

    def __add_attribute(self, frame, label, attName, index):
       # fields Labels
       tk.Label(frame, font=self.font_4, text=str(label + ": "), anchor=tk.W).grid(row=index, column=0,
                                                                                        sticky=tk.W + tk.E)
       # fields
       self.__dict__[attName] = tk.StringVar()
       tk.Entry(frame, width=250, font=self.font_3, text="", textvariable=self.__dict__[attName]).grid(row=index,column=1,sticky=tk.W + tk.E)

       return index + 1

    def __on_bthCloseComm_Clicked(self):
        self.__on_closing()

    # Main Form Close Event
    # Clean exit
    def __on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # logging.info("Explicit Close Port and Handlers (User clicked on Exit button)")
            self.oModulesManager.stop()
            th = threading.Thread(target=self.oTKRoot.destroy, daemon=True)
            th.start()

    def __set_time_stamp(self, messageTime):
        oDate = datetime.datetime.now()
        seconds_since_epoch = oDate.replace(tzinfo=datetime.timezone.utc).timestamp()
        messageTime.seconds = int(seconds_since_epoch)
        messageTime.nanos = self.__sec_fraction_to_nano(seconds_since_epoch)

    # retrieves offset for seconds fraction since epoch time
    def __sec_fraction_to_nano(self, seconds_since_epoch):
        sSec = str(seconds_since_epoch)
        nPos = sSec.find(".")
        if nPos == -1:
            return 0
        sSecFrac = sSec[nPos:sSec.__len__()]
        return int(float(sSecFrac) * 1000000000)
