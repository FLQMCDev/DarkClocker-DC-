Darkling Clicker - Customizable Auto-Clicker

Darkling Clicker is a Python-based auto-clicker developed by FLQMZECLIENT. This project enables users to automate mouse clicks with customizable settings for interval, button selection, and click count. Designed over a span of three months, Darkling Clicker aims to provide a straightforward yet powerful tool for automating repetitive clicking tasks.

-----------------------------------------------------
Features
-----------------------------------------------------

- **Customizable Click Interval:** Adjust the time interval between each click in seconds.
- **Choice of Mouse Button:** Select between left, right, or middle mouse button for clicking.
- **Number of Clicks:** Specify the exact number of clicks to perform.
- **Start/Stop Control:** Initiate and halt clicking sessions with easy-to-use console commands.
- **Progress Feedback:** Real-time display of click progress to monitor task completion.
- **Engaging ASCII Art:** Welcoming ASCII art and custom messages for an interactive user experience.

-----------------------------------------------------
Installation
-----------------------------------------------------

### Prerequisites
- Python 3.x
- `pyautogui` library

### Installation Steps
1. **Install Python 3.x:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install `pyautogui`:**
   - Open a terminal or command prompt.
   - Run the following command:
     ```
     pip install pyautogui
     ```

3. **Clone the Repository:**
   - Open a terminal or command prompt.
   - Clone the repository using Git:
     ```
     git clone https://github.com/yourusername/darkling-clicker.git
     cd darkling-clicker
     ```

-----------------------------------------------------
Usage
-----------------------------------------------------

### Running Darkling Clicker
1. **Navigate to the Darkling Clicker directory:**

2. **Execute the script:**

3. **Follow on-screen prompts to configure:**
- Enter the click interval (in seconds).
- Choose the mouse button (left, right, middle).
- Specify the number of clicks.

4. **Control the Clicking Session:**
- To start: Press Enter after entering the configuration.
- To stop: Enter 'stop' in the console prompt.

-----------------------------------------------------
Creating an Executable
-----------------------------------------------------

### Creating a Standalone Executable
- If you prefer not to run the script using Python directly, you can create a standalone executable file.

1. **Install `pyinstaller`:**
- Open a terminal or command prompt.
- Run the following command:
  ```
  pip install pyinstaller
  ```

2. **Generate the executable:**
- Navigate to the Darkling Clicker directory.
- Run the following command:
  ```
  pyinstaller --onefile --windowed darkling_clicker.py
  ```

3. **Locate the executable:**
- The standalone executable will be found in the `dist` directory within the Darkling Clicker project folder.

=====================================================
