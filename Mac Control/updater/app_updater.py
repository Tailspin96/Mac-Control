import os
import shutil
import zipfile
import requests

from messages import notifications

def check_for_update():
    latest_release_url = "https://api.github.com/repos/Tailspin96/Mac-Control/releases/latest" #url here
    response = requests.get(latest_release_url)
    print("get repo url")
    if response.status_code == 200:
        latest_release = response.json()
        latest_version = latest_release
        current_version = "1.0.0"
        print("get latest and current verion of app")
        if latest_version > current_version:
            print("call d/i method")
            download_url = latest_release["assets"][0]["browser_download_url"]
            download_and_install_update(download_url)
            print("Update Check", "Downloading new update...")
            notifications.notificationBalloon("Mac Control Updater", "Downloading new update")
        else:
            print("Update Check", "You are running the latest version of the application.")
            notifications.notificationBalloon("Mac Control Updater", "You are running the latest version of Mac Control")
    else:
        print(response.status_code)
        print("Update Check", "Failed to check for updates. Please try again later.")
        notifications.notificationBalloon("Mac Control Updater", "Failed to check for updates")

def download_and_install_update(download_url):
    try:
        response = requests.get(download_url)
        with open("Mac Control.app.zip", "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile("Mac Control.app.zip", "r") as zip_ref:
            zip_ref.extractall("Mac Control")

        # Verify the path and move the updated application
        if os.path.exists("updated_app/Mac Control.app"):
            shutil.rmtree("Mac Control.app")
            shutil.move("updated_app/Mac Control.app", ".")
            print("The update has been successfully installed. Please restart the application.")
            notifications.notificationBalloon("Mac Control Updater", "Successfully installed update")
        else:
            print("Failed to find the updated application. Update may not have been properly downloaded.")
            notifications.notificationBalloon("Mac Control Updater", "Failed to find the updated application")

    except Exception as e:
        print("Failed to install the update:", str(e))
        notifications.notificationBalloon("Mac Control Updater", "Failed to install update")
    finally:
        # Clean up temporary files and directories
        if os.path.exists("Mac Control.app.zip"):
            os.remove("Mac Control.app.zip")
        if os.path.exists("Mac Control"):
            shutil.rmtree("Mac Control")
