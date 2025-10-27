import win32gui
import win32process
import psutil

def get_active_window():
    """
    Returns the name of the currently active process and its window title.
    Example: ("chrome.exe", "ChatGPT - Google Chrome")
    """
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        return process.name(), win32gui.GetWindowText(hwnd)
    except Exception:
        return None, None