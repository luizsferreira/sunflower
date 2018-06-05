import RPi.GPIO as GPIO
import curses

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(18, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 20, "Up")
        print "UP pressed"
        GPIO.output(22, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
    elif key == curses.KEY_DOWN:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH) 
        stdscr.addstr(3, 20, "Down")
        print "DOWN pressed"
    elif key == ord('q'):
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
curses.endwin()
