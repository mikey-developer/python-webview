# pip install pywebview
import os
import webview

STORAGE_DIR = os.path.join(os.path.expanduser("~"), ".app_data")

if not os.path.exists(STORAGE_DIR):
    os.makedirs(STORAGE_DIR)

def run_app():
    window = webview.create_window(
        title="",
        url="",
        width=1200,
        height=800,
        resizable=True
    )
    webview.start(storage_path=STORAGE_DIR)

if __name__ == '__main__':
    run_app()
