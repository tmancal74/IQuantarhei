# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager


def main():
    
    app = QtGui.QApplication(sys.argv)

    ipython_widget = qtconsole()
    ipython_widget.show()
    
    sys.exit(app.exec_())    
    
def qtconsole():
    
    
    #w = QtGui.QWidget()
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel(show_banner=False)
    kernel = kernel_manager.kernel
    kernel.gui = 'qt4'

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    ipython_widget = RichJupyterWidget()
    ipython_widget.kernel_manager = kernel_manager
    ipython_widget.kernel_client = kernel_client
    ipython_widget.show()
    
    #b = QtGui.QLabel(ipython_widget)
    #b.setText("Welcome to Quantarhei!")
    
    #ipython_widget.setGeometry(100,100,500,200)
    #b.move(40,20)
    
    ipython_widget.setWindowTitle("IQuantarhei ver. 0.0.1")
    return ipython_widget
    

    
    
if __name__ == '__main__':
    main()
    
    
