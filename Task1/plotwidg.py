# Importing Packages
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from PyQt5.QtWidgets import QMessageBox
import pyqtgraph as pg
import startstop3 as ss
import pandas as pd
from scipy.io import loadmat
import sys
import os
import queue as Q
from sortedcontainers import SortedList
from pyqtgraph import PlotWidget


class myPlotWidget(PlotWidget):
    signal = pyqtSignal(int)  # Signal to send to other slots, containing int which identifies the exct type of the sent

    # data
    def __init__(self, parent, id, background='default', **kwargs):
        super(myPlotWidget, self).__init__(parent=parent, background=background, **kwargs)
        self.id = id
        self.clicked = False
        self.sceneObj.sigMouseClicked.connect(self.select_event)

    def select_event(self):
        """
        the sender function which is connected to the clicking event of the plotwidget
        :emit: id of the last clicked widget
        """
        # print("The Current Selected widget is: ", self.id )
        self.clicked = True
        self.signal.emit(self.id)



# MainClass of the application
class signalViewer(ss.Ui_MainWindow):
    # counter represents the chunks size of data to be loaded
    i = 0

    # Dictionaries for files configuration
    # Contains file path (key) and extension (value)
    filenames = dict()

    # Contains file path (key) and DataFrame of the file
    channels = dict()

    # Contains file path (key) and
    chunks = dict()

    # Contains file path (key) and data lines of plotItem
    graphs = dict()

    # Current Channel to start from 0 when adding one in the first time
    channel = -1

    # Number of Panels, start from 0 at the start
    numOfPanels = 0

    # Queues for tracing the available and shown panels
    AvPanels = Q.PriorityQueue(5)
    ShownPanels = Q.PriorityQueue(5)

    # Sorted list, used in queue operations
    LsShownPanels = SortedList()

    # Contains keys of the channels (1 - 5) and the file path for each channel
    CurUsedFile = dict()

    # Current selected widget by the user
    currentSelected = 0

    def __init__(self, mainwindow, speed):
        '''
        Main loop of the UI
        :param mainwindow: QMainWindow Object
        '''
        super(signalViewer, self).setupUi(mainwindow)
        # Speed of changing the rows of the data
        self.speed = speed

        # Reset filename if existed already
        self.filename, self.format = None, None

        # Initialize the widgets to be none
        self.widget_2 = myPlotWidget(self.centralwidget, id=2).close()
        self.widget_3 = myPlotWidget(self.centralwidget, id=3).close()
        self.widget_4 = myPlotWidget(self.centralwidget, id=4).close()
        self.widget_5 = myPlotWidget(self.centralwidget, id=5).close()
        self.widget = myPlotWidget(self.centralwidget, id=1)

        # list of the widgets
        self.widgets = [self.widget, self.widget_2, self.widget_3, self.widget_4, self.widget_5]
        self.checkBoxes = [self.channel1_chk, self.channel2_chk, self.channel3_chk, self.channel4_chk, self.channel5_chk]

        # Setup Queues
        self.AvPanels.put(2)
        self.AvPanels.put(3)
        self.AvPanels.put(4)
        self.AvPanels.put(5)
        self.ShownPanels.put(1)

        # pens configurations
        self.pens = [pg.mkPen(color=(255, 0, 0)), pg.mkPen(color=(0, 255, 0)),
                     pg.mkPen(color=(0, 0, 255)), pg.mkPen(color=(200, 87, 125)),
                     pg.mkPen(color=(123, 34, 203))]

        # Plot Configurations
        self.plot_conf()

        # Load Button connector checked
        self.actionAdd.triggered.connect(self.addNewPanel)

        self.checkBoxes[0].toggled.connect(lambda: self.hideChannel(0))
        self.checkBoxes[1].toggled.connect(lambda: self.hideChannel(1))
        self.checkBoxes[2].toggled.connect(lambda: self.hideChannel(2))
        self.checkBoxes[3].toggled.connect(lambda: self.hideChannel(3))
        self.checkBoxes[4].toggled.connect(lambda: self.hideChannel(4))

        self.actionReset.triggered.connect(self.resetAllPanels)
        self.actionDelete.triggered.connect(self.delete)
        self.actionStop.triggered.connect(self.stopSignal)
        self.actionLoad.triggered.connect(self.load_file)
        # Timer Configurations
        # self.timer()
        self.view = self.widget.plotItem.getViewBox()

        # Connector slot to the signal from myplotwidget
        self.widget.signal.connect(self.hi)


        # Zoom Buttons Configuration
        self.actionZoomIn.triggered.connect(self.zoomin)
        self.actionZoomOut.triggered.connect(self.zoomout)

    def hi(self, data):
        """
        testing function to demonstrate how two classes can communicate with each other
        :param data: sent from myplotwidget
        :return:  None
        """
        print('This is the data sent', data)
        signalViewer.currentSelected = data

    # Zoom in Configurations
    def zoomin(self):
        if signalViewer.currentSelected == 0:
            pass
        else:
            self.widgets[signalViewer.currentSelected - 1].plotItem.getViewBox().scaleBy(0.3)

    def zoomout(self):
        if signalViewer.currentSelected == 0:
            pass
        else:
            self.widgets[signalViewer.currentSelected - 1].plotItem.getViewBox().scaleBy(1 / 0.3)

    # Load File
    def load_file(self):
        """
        Load the File from User and add it to files dictionary
        :return:
        """

        if signalViewer.currentSelected == 0:
            self.show_popup('No Selected Pannel', 'First Select a Panel by clicking on it')
            pass
        else:
            signalViewer.i = 0

            # Stop timer for waiting to upload new file
            # self.timer.stop()

            # Open File
            self.filename, self.format = QtWidgets.QFileDialog.getOpenFileName(None, 'Load Signal', '/home', "*.csv;;"
                                                                                                             " *.txt;;"
                                                                                                             "*.mat")
            if self.filename == '':
                pass
            else:
                # signalViewer.channel += 1
                #
                # if signalViewer.channel > 4:
                #     signalViewer.channel = 0
                #     if not self.find(signalViewer.channel):
                #         signalViewer.channel += 1
                #
                # # Check if the channel is found in the ShownPanel Queue
                # if (not self.find(signalViewer.channel+1)):
                #     signalViewer.channel -= 1
                #     self.show_popup('Error','Add a new channel first')
                #     pass
                # else:
                if self.filename in signalViewer.filenames:
                    self.show_popup("File Existed", "You already uploaded this file before")
                else:
                    signalViewer.filenames[self.filename] = self.format
                    signalViewer.CurUsedFile[signalViewer.channel] = self.filename
                    self.checkFileExt(signalViewer.filenames)

    def plot_conf(self):
        """
        Sets the plotting configurations
        :return:
        """
        # Channel 1
        # Setting ranges of the x and y axis
        self.widget.setXRange(min=0, max=4000)
        self.widget.setMinimumSize(QtCore.QSize(500, 200))
        self.widget.plotItem.setTitle("Channel 1")
        # self.legend = pg.LegendItem(size=(2, 3), offset=(80, 80))
        # self.legend.setParentItem(self.widget.plotItem.graphicsItem())
        # self.legend.addItem(self.widget.plotItem, "Plot111")
        self.widget.plotItem.addLegend(size=(2, 3))
        self.widget.plotItem.showGrid(True, True, alpha=0.8)
        self.widget.plotItem.setLabel('bottom', text='Time (ms)')
        self.widget.plotItem.enableAutoScale()
        self.widget.plotItem.getViewBox().setAutoPan(x=True)
        self.verticalLayout.addWidget(self.widget)



    # Reading Files Functions
    def load_csv_data(self, file_name):
        """
        load the data from user if the file format is a .csv format
        :param file_name: file path ... string
        :return:
        """
        if file_name in signalViewer.channels:
            print("You Already Loaded this file1")
        else:
            # Return dataFrame (data)
            signalViewer.channels[file_name] = pd.read_csv(file_name)

            # Return y chunk (data line)
            signalViewer.chunks[file_name] = signalViewer.channels[file_name].iloc[:, 1]

            self.deletePreviousSignal()

            # Plot chunk
            self.plot(file_name, signalViewer.chunks[file_name])

    def load_mat_data(self, file_name):
        """
        load the data from user if the file format is a .mat format
        :param file_name: file path ... string
        :return:
        """
        if file_name in signalViewer.channels:
            print("You already loaded this file2")
        else:
            mat_file = loadmat(file_name)
            signalViewer.channels[file_name] = pd.DataFrame(mat_file['F'])
            signalViewer.chunks[file_name] = signalViewer.channels[file_name].iloc[:, 1]
            self.deletePreviousSignal()
            self.plot(file_name, signalViewer.chunks[file_name])

    def load_txt_data(self, file_name):
        """
        load the data from user if the file format is a .txt format
        :param file_name: file path ... string
        :return:
        """
        if file_name in signalViewer.channels:
            print("You already loaded this file3")
        else:
            signalViewer.channels[file_name] = pd.read_csv(file_name, skiprows=[i for i in range(1500, 7657)])
            signalViewer.chunks[file_name] = signalViewer.channels[file_name].iloc[:, 2]
            self.deletePreviousSignal()
            self.plot(file_name, signalViewer.chunks[file_name])

    def plot(self, file_name, chunk):
        '''
        main plotting function
        :return:
        '''
        # File name
        name = file_name.split('/')[-1]
        signalViewer.graphs[file_name] = self.widgets[signalViewer.currentSelected-1].plotItem.plot(chunk, name=name,
                                                                                          pen=self.pens[signalViewer.currentSelected-1])


    def update_plot_data(self):
        '''
        update function .... add chunks to self.y from loaded data self.data
        :return:
        '''
        # Iterate over keys (chunk) in chnuks dictionary
        for chunk in signalViewer.chunks:
            signalViewer.i += 30
            signalViewer.chunks[chunk] = pd.concat([signalViewer.chunks[chunk],
                                                    signalViewer.channels[chunk].iloc[
                                                    signalViewer.i:signalViewer.i + self.speed, 1]],
                                                   axis=0, sort=True)
            # graph ->> file_name is the key
            signalViewer.graphs[chunk].setData(signalViewer.chunks[chunk])

    # def timer(self):
    #     """
    #     Timer function that executes the data updating for every n ms
    #     :return:
    #     """
    #     self.timer = QtCore.QTimer()
    #     self.timer.setInterval(50)
    #     self.timer.timeout.connect(self.update_plot_data)
    #     self.start_timer()
    #     self.pause_timer()
    #
    # def start_timer(self):
    #     '''
    #     Event of clicking the start button which starts the signal plotting
    #     :return:
    #     '''
    #     self.actionStart.triggered.connect(self.timer.start)
    #
    # def pause_timer(self):
    #     '''
    #     Event of clicking the stop button which stops the signal plotting
    #     :return:
    #     '''
    #     self.actionPause.triggered.connect(self.timer.stop)

    def stopSignal(self):
        signalViewer.i = 0
        signalViewer.chunks = dict()
        # self.show_popup("Signal has stopped", "You have terminated the signal.. upload it again to view it")

    def checkFileExt(self, file):
        """
        Checks the file format loaded by the user and maps to appropriate function
        :param file: File dictionary updated by the load function
        :return:
        """
        for i in file.items():
            if i[1] == '*.csv':
                self.load_csv_data(i[0])
            elif i[1] == '*.txt':
                self.load_txt_data(i[0])
            elif i[1] == '*.mat':
                self.load_mat_data(i[0])

    def resetAllPanels(self):

        """
        Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function.
        """
        print("Deleting panels...")
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def delete(self):
        print('the current is ', signalViewer.currentSelected)
        num = signalViewer.currentSelected
        signalViewer.LsShownPanels.clear()
        while not signalViewer.ShownPanels.empty():
            signalViewer.LsShownPanels.add(signalViewer.ShownPanels.get())
        # if not signalViewer.LsShownPanels.__contains__(num):
        #     print("No plots to delete")
        #     self.show_popup("Channel doesn't exist","Choose an existing panel")
        if signalViewer.currentSelected == 0:
            self.show_popup("No Channel Selected", "Choose an existing panel")
        else:
            # signalViewer.numOfPanels = signalViewer.ShownPanels.get()
            signalViewer.AvPanels.put(num)
            # signalViewer.LsShownPanels.remove(num)
            num -= 1
            self.widgets[num].close()
            self.checkBoxes[num].setEnabled(False)
            self.widgets[num] = None
            if num in signalViewer.CurUsedFile:
                del signalViewer.filenames[signalViewer.CurUsedFile[num]]
                del signalViewer.channels[signalViewer.CurUsedFile[num]]
                del signalViewer.CurUsedFile[num]
            self.stopSignal()
            for x in range(signalViewer.LsShownPanels.__len__()):
                signalViewer.ShownPanels.put(signalViewer.LsShownPanels.pop())

            # Return currentSelected to normal state
            signalViewer.currentSelected = 0

    def find(self, num):
        while not signalViewer.ShownPanels.empty():
            signalViewer.LsShownPanels.add(signalViewer.ShownPanels.get())
        found = signalViewer.LsShownPanels.__contains__(num)
        for x in range(signalViewer.LsShownPanels.__len__()):
            signalViewer.ShownPanels.put(signalViewer.LsShownPanels.pop())
        return found

    def addNewPanel(self):
        if signalViewer.AvPanels.empty():
            print("No more than 5 plots")
            self.show_popup("Maximum number of channels is 5",
                            "You can't add more than 5 channels, you have to delete one first")
        else:
            # signalViewer.numOfPanels += 1
            # if not signalViewer.AvPanels.empty() :
            # Adjusting Queues
            signalViewer.numOfPanels = signalViewer.AvPanels.get()
            signalViewer.ShownPanels.put(signalViewer.numOfPanels)
            signalViewer.numOfPanels -= 1

            signalViewer.channel = signalViewer.numOfPanels - 1

            # Setup Plot Configuration
            self.widgets[signalViewer.numOfPanels] = myPlotWidget(self.centralwidget, id=signalViewer.numOfPanels + 1)
            self.widgets[signalViewer.numOfPanels].setEnabled(True)
            self.widgets[signalViewer.numOfPanels].setMinimumSize(QtCore.QSize(500, 200))
            self.widgets[signalViewer.numOfPanels].setXRange(min=0, max=4000)
            self.widgets[signalViewer.numOfPanels].setYRange(min=-1, max=1)
            self.widgets[signalViewer.numOfPanels].plotItem.setTitle("Channel " + str(signalViewer.numOfPanels + 1))
            self.widgets[signalViewer.numOfPanels].plotItem.addLegend(size=(2, 3))
            self.widgets[signalViewer.numOfPanels].plotItem.showGrid(True, True, alpha=0.8)
            self.widgets[signalViewer.numOfPanels].plotItem.setLabel('bottom', text='Time (ms)')
            self.widgets[signalViewer.numOfPanels].plotItem.enableAutoScale()
            self.widgets[signalViewer.numOfPanels].plotItem.getViewBox().setAutoPan(x=True)
            self.widgets[signalViewer.numOfPanels].signal.connect(self.hi)
            self.verticalLayout.addWidget(self.widgets[signalViewer.numOfPanels])
            self.checkBoxes[signalViewer.numOfPanels].setEnabled(True)

    def hideChannel(self, checkNumber):
        if self.widgets[checkNumber] is None:
            self.show_popup("Channel Doesn`t exist", "You didn`t add this channel")
            self.checkBoxes[checkNumber].setChecked(True)
        else:
            self.widgets[checkNumber].setHidden(not self.widgets[checkNumber].isHidden())

    def show_popup(self, message, info):
        msg = QMessageBox()
        msg.setWindowTitle("Popup Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText(info)
        # msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def startDeletingProcess(self):
        self.showDeleteList("Delete a channel", "Choose the channel you want to delete")

    def showDeleteList(self, message, info):
        msg = QMessageBox()
        msg.setWindowTitle("Popup Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setInformativeText(info)

        # Custome btns
        msg.setWindowModality(QtCore.Qt.NonModal)
        panel1 = msg.addButton("1", msg.ActionRole)
        panel2 = msg.addButton("2", msg.ActionRole)
        panel3 = msg.addButton("3", msg.ActionRole)
        panel4 = msg.addButton("4", msg.ActionRole)
        panel5 = msg.addButton("5", msg.ActionRole)

        # msg.buttonClicked.connect(self.deletePanel)
        msg.buttonClicked.connect(self.delete)
        x = msg.exec_()


    def deletePreviousSignal(self):
        # clear the previous data line
        self.widgets[signalViewer.currentSelected - 1].plotItem.clear()

        # Remove the legend and add the new one
        # print(self.widgets[signalViewer.currentSelected - 1].getPlotItem().legend.items)
        # self.widgets[signalViewer.currentSelected - 1].getPlotItem().legend.items = []
        # print(self.widgets[signalViewer.currentSelected - 1].getPlotItem().legend.items)


def main():
    '''
    the application startup functions
    :return:
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signalViewer(MainWindow, speed=50)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
