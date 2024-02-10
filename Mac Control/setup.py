from setuptools import setup

APP = ['Mac Control.py']

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'img/icon/AppIcon.icns',
    'plist': {
        'CFBundleName': 'Mac Control',
        'CFBundleDisplayName': 'Mac Control',
        'CFBundleGetInfoString': 'Control your Mac with a gaming controller.',
        'CFBundleIdentifier': 'com.Tailspin96.MacControl',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleExecutable': 'Mac Control',
        'CFBundleIconFile': 'AppIcon.icns',
    },
    'packages': ['pyautogui', 'pygame'],  # packages
    'excludes': ['rubicon'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
