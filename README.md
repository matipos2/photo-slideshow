# Photo SlideShow

## Overview

1. [Description](#description)
2. [Main features](#main-features-)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Possible errors](#possible-errors)
5. [About](#about)

## Description

It's simple and easy tool to make a slideshow on your computer with your photos.
![photo-slideshow window](resources/photo-slideshow_window.png)

## Main features:

1. Read all photos / images from current directory and from all subdirectories
2. Possibility to choose what file types should be presented
3. Fullscreen option
4. Possibility to run the slideshow in a random order
5. It's python based so it should run everywhere where python is present

## Installation

The fastest and easiest way is to install it via `pip`. `pip` is a command line program provided with [python](https://www.python.org/downloads/).
```
pip install photo-slideshow
```
Installing from the source. Download this project. Unpack it. Go to the folder with source files. Open the main folder. Execute that command:
```
pip3 install .
```

## Usage

Run the application with command:
```
photo-slideshow
```
Application window will show up.

Browse the folder where your pictures are stored. In the settings you may configure:

- background color if the picture doesn't fit to your screen
- the time for showing current picture before switching to next one
- turn on/off random order
- select file types to be read

Select the fullscreen checkbox if you want that mode and push the start button. If you want to stop, simply push the stop button. In the fullscreen mode, push the <esc> button.

## Possible errors
If you get error:
```
ModuleNotFoundError: No module named 'tkinter'
```
It tells that you have to install pythong GUI framework (Tcl/Tk). Depends on the operating systems the instruction may differ, for example:
1. In windows open `python installer -> modify -> select tcl/tk and IDLE`, go next and finalize installation.
2. Ubuntu / debian: `sudo apt-get install python3-tk`
3. Fedora: `sudo dnf install python3-tkinter`
4. CentOS: `sudo yum install python3-tkinter`
5. MacOS: `brew install python-tk@3.10`
6. For other, just check hot to install.

When tkinter is installed you can run photo-slideshow.

## License

MIT License.

## About
Author: Mateusz Poślednik. Experienced data engineer, but also photographer. I was missing an easy, light software to make a slideshow on my photos. Most of the applications can make the slideshow only for current directory, but my photos are organized in many subdirectories.

My other projects: [https://github.com/matipos](https://github.com/matipos) and [https://github.com/matipos2](https://github.com/matipos2)

Contact: [https://matpos.pythonanywhere.com/](https://matpos.pythonanywhere.com/)
