import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Alert User!!",
            message="It's been one hour you are working on the pc... Take rest now!",
            app_icon=r"C:\Users\HPindia\Pictures\Saved Pictures\Shivesh\Python Examples\py apps\icon.ico",)
        time.sleep(60)
