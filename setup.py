setup(
    name="Roblox Studio Presence",
    version="1.0.0",
    description="A Discord Rich Presence for Discord.",
    license="MIT",
    url="https://github.com/realpython/reader",
    long_description=README.md,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["rs2disc"],
    include_package_data=True,
    install_requires=[
        "pywinauto", "pyautogui", "discordrp", "sys"
    ],
    console=False,
    icon='app.ico'
)