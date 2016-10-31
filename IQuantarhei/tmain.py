# -*- coding: utf-8 -*-
import signal
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager

class MainWindow(QMainWindow):
   count = 0
	
   def __init__(self, parent = None):
      super().__init__(parent)
      self.mdi = QMdiArea()
      self.setCentralWidget(self.mdi)
      
      
      bar = self.menuBar()
      #bar.setNativeMenuBar(False)      
      
      file = bar.addMenu("File")
      file.addAction("New project ...")
      file.addAction("Open project ...")
      file.addAction("Save")
      file.addAction("Save all")
      file.addAction("Save as ...")
      file.addSeparator()
      file.addAction("Close")
      file.addAction("Close all")
      file.addSeparator()
      file.addAction("Quit")
      file.addSeparator()
      file.addAction("Quantarhei Preferences ...")
      file.addAction("IQuantarhei Preferences ...")
      file.triggered[QAction].connect(self.file_action)
      
      view = bar.addMenu("View")
      view.addAction("Cascade")
      view.addAction("Tiled")
      view.triggered[QAction].connect(self.view_action)
      
      console = bar.addMenu("Consoles")
      console.addAction("Open Inprocess Qt Console")
      console.addAction("Open Qt Console with Kernel")
      console.addSeparator()
      console.addAction("PYTHONPATH Manager ...")
      console.triggered[QAction].connect(self.console_action)
      
      qntr = bar.addMenu("Quantarhei")
      qntr.addAction("Quantarhei Path/Select version ...")
      qntr.addAction("Version info")
      qntr.triggered[QAction].connect(self.qntr_action)
      
      hlp = bar.addMenu("Help")
      hlp.addAction("Quantarhei Documentation")
      hlp.triggered[QAction].connect(self.view_action)
      
      self.setWindowTitle("IQuantarhei ver. 0.0.1")
		
   def file_action(self, q):
		
      if q.text() == "New":
          MainWindow.count = MainWindow.count+1
          sub = QMdiSubWindow()
          sub.setWidget(QTextEdit())
          sub.setWindowTitle("subwindow"+str(MainWindow.count))
          self.mdi.addSubWindow(sub)
          sub.show()

      if q.text("Quantarhei Preferences ..."):
          pass
       
   def view_action(self, q):
		
      if q.text() == "Cascade":
          self.mdi.cascadeSubWindows()
		
      if q.text() == "Tiled":
          self.mdi.tileSubWindows()
          
   def qntr_action(self, q):
       
       if q.text() == "Version info":
           pass
       
   def console_action(self, q):
       
       if q.text() == "Open Inprocess Qt Console":
          MainWindow.count = MainWindow.count+1
          sub = QMdiSubWindow()
          qtc = inprocess_qtconsole()
          sub.setWidget(qtc)
          sub.setWindowTitle("Inprocess Jupyter Qt Console (IPython)")
          self.mdi.addSubWindow(sub)
          sub.show()

   def closeEvent(self, event):

        quit_msg = "Are you sure you want to exit IQuantarhei?"
        reply = QMessageBox.question(self, 'Message', 
                     quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def inprocess_qtconsole():
    
    
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

    return ipython_widget


def sigint_handler(*args):
    """Handler for the SIGINT signal."""
    sys.stderr.write('\r')
    if QMessageBox.question(None, '', "Are you sure you want to quit?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No) == QMessageBox.Yes:
        QApplication.quit()


def main():
    
    signal.signal(signal.SIGINT, sigint_handler)
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()
