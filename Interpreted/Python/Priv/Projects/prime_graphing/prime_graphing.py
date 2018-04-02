import curses

def is_prime(number):
        if number == 1:
            return False
        for x in range(2, int(number/2)+1):
            if not number % x:
                return False
        return True


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.start_color()
    limit = 5000
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()
    y,x = stdscr.getmaxyx()
    i = 0
    gap = 5

    for x_cor in range(0, 55*gap, gap):
        if i <= limit:
            for y_cor in range(0, 100):
                i += 1
                if is_prime(i):
                    try:
                        stdscr.addstr(y_cor, x_cor, '{}'.format(i), curses.color_pair(2))
                    except:
                        pass
                else:
                    try:
                        stdscr.addstr(y_cor, x_cor, '{}'.format(i))
                    except:
                        pass

    stdscr.refresh()
    stdscr.getkey()

main()
