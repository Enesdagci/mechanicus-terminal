import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer  # Import the timer for real-time updates
from ui_dashboard import Ui_MainWindow 

class CogitatorDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Attach the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initial Boot Sequence
        self.log_message("Initializing Adeptus Mechanicus cogitator interface...")
        self.log_message("Establishing connection to Noosphere data repositories...")
        
        # --- 1. CONNECT BUTTONS (Signals & Slots) ---
        # When a button is clicked, trigger the corresponding function
        self.ui.pushButton.clicked.connect(self.engage_protocol)
        self.ui.pushButton_2.clicked.connect(self.emergency_scram)
        
        # --- 2. START TELEMETRY LOOP (QTimer) ---
        self.telemetry_timer = QTimer(self)
        self.telemetry_timer.timeout.connect(self.update_telemetry)
        self.telemetry_timer.start(500) # Triggers every 500 milliseconds (0.5 seconds)

    # --- CUSTOM FUNCTIONS ---

    def log_message(self, text):
        """Helper function to format and append text to the terminal."""
        self.ui.textEdit.append(f"[SYS] {text}")

    def engage_protocol(self):
        """Triggered by the green 'Engage' button."""
        self.log_message("PROTOCOL ENGAGED: Calibrating motive force...")
        self.log_message("Awaiting sensor fusion telemetry...")

    def emergency_scram(self):
        """Triggered by the red E-Stop button."""
        self.log_message("!!! EMERGENCY SCRAM INITIATED !!!")
        self.log_message("HALTING ALL ACTUATORS. CUTTING POWER.")
        
        # Instantly drain the power bar and stop the fake data loop
        self.ui.progressBar.setValue(0)
        self.telemetry_timer.stop() 

    def update_telemetry(self):
        """This function runs automatically every 500ms."""
        # 1. Simulate reactor/battery fluctuation
        current_val = self.ui.progressBar.value()
        
        # Add a random jump between -2 and +2 to simulate live data jitter
        fluctuation = random.randint(-2, 2) 
        new_val = max(0, min(100, current_val + fluctuation)) # Keep it between 0-100
        
        self.ui.progressBar.setValue(new_val)
        
        # Future integration point: 
        # This is exactly where you will eventually parse incoming data 
        # from your hardware sensors or ROS2 topics!

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = CogitatorDashboard()
    dashboard.show()
    sys.exit(app.exec())
