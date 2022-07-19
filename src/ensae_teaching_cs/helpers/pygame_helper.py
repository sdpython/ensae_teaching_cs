"""
@file
@brief pygame helpers

The module pygame is not imported in this module but sent
to every function as a parameter to avoid importing
the module if not needed.
"""
import math


MOUSE = "mouse"
KEY = "key"


def wait_event(pygame):
    """
    The function waits for an event, a

    @param      pygame      module pygame
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                return (MOUSE, event.button, event.pos[0], event.pos[1])
            elif event.type == pygame.KEYUP:
                if event.key == 27:
                    return None
                else:
                    return (KEY, event.key)
            elif event.type == pygame.QUIT:
                return None


def empty_main_loop(pygame, msg=None):
    """
    Removes all events in the main loop,
    a mouse click make the program halt,
    another click makes it start again.

    @param      pygame      module pygame
    @return                 event ``pygame.QUIT``?
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP:
            if msg is not None:
                print(msg())
            wait_event(pygame)
    return True


def get_pygame_screen_font(h, size, flags=0):
    """
    Creates a surface with :epkg:`pygame`, initialize the module,
    creates font.

    @param      h       size of the main font
    @param      size    screen size
    @param      flags   see `pygame.display.set_mode <https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode>`_
    @return             pygame, screen, dictionary of fonts

    The dictionary of fonts contains three fonts of size *h*,
    *3h/4*, *5h/6*.

    This function leaves file still opened and generates warnings.
    Parameter *flag* can be useful if you run the function just
    to test that it is working and the result does not need to be seen.
    """
    import pygame
    pygame.init()
    font = pygame.font.Font("freesansbold.ttf", h)
    font_small = pygame.font.Font("freesansbold.ttf", 3 * h // 4)
    try:
        screen = pygame.display.set_mode(size, flags)
    except pygame.error as e:
        raise Exception(
            f"Unable to create a screen, flags={flags}") from e
    font = pygame.font.Font("freesansbold.ttf", h)
    font_small = pygame.font.Font("freesansbold.ttf", 3 * h // 4)
    font_half = pygame.font.Font("freesansbold.ttf", 5 * h // 6)
    return pygame, screen, dict(font=font, font_half=font_half, font_small=font_small)


def build_diff_image(pygame, screen, h, maxw, seq1=None, seq2=None, diff=None, fonts=None,
                     bars=None, colors=None, progress=None, prev_bars=None):
    """
    Builds an image to show a difference between two lists,
    we assume these list contain distinct items.

    @param      pygame      module pygame
    @param      screen      screen (pygame surface)
    @param      h           height of a line
    @param      maxw        width of the screen
    @param      seq1        list 1 (can be None)
    @param      seq2        list 2 (cannot be None)
    @param      diff        difference (object `SequenceMatcher <https://docs.python.org/3.5/library/difflib.html#sequencematcher-objects>`_)
    @param      fonts       dictionary of fonts with keys ``'font'``, ``'font_small'``, ``'font_half'``
    @param      bars        each item of sequence 2 can be associated to a width (in [0, 1])
    @param      colors      dictionary of colors (see below)
    @param      progress    draws the progress between two list
    @param      prev_bars   previous width

    Colors:

    * black: no change
    * blue: new
    * red: deleted
    * green: vert
    * yellow: bars

    When *progress* is not None, the picture is a kind of average
    between the previous position and the new one. When a suggestion moves
    from *p1* to *p2*, it defines a circle.
    The result looks like this.

    .. raw:: html

        <video autoplay=" controls="" loop="" height="250">
        <source src="http://www.xavierdupre.fr/enseignement/complements/diff.mp4" type="video/mp4" />
        </video>

    """
    font = fonts.get('font', None)
    font_small = fonts.get('font_small', None)
    font_half = fonts.get('font_half', None)
    if font is None:
        raise ValueError("font cannot be None")
    if font_small is None:
        raise ValueError("font_small cannot be None")
    if font_half is None:
        raise ValueError("font_half cannot be None")
    if seq2 is None:
        raise ValueError("seq2 cannot be None")

    if colors is None:
        colors = {}
    set_seq1 = {} if seq1 is None else set(seq1)
    set_seq2 = set(seq2)
    width = h // 3
    color_bar = colors.get('yellow', (240, 240, 0))
    pos = 0
    if diff is not None:
        if progress is None:
            # just the diff
            opcodes = []
            for opcode in diff.get_opcodes():
                if opcode[0] in {'delete', 'equal', 'insert'}:
                    opcodes.append(opcode)
                elif opcode[0] == "replace":
                    opcodes.append(
                        ('delete', opcode[1], opcode[2], None, None))
                    opcodes.append(
                        ('insert', None, None, opcode[3], opcode[4]))
                else:
                    raise ValueError(f"unexpected: {opcode}")

            for opcode in opcodes:
                if opcode[0] == "delete":
                    for i in range(opcode[1], opcode[2]):
                        text = seq1[i]
                        if text not in set_seq2:
                            color = colors.get('red', (200, 0, 0))
                            text = font_small.render(text, True, color)
                            screen.blit(text, (10, h * pos + h // 6))
                            pos += 1
                        else:
                            # we skip, it is going to be display by the other
                            # part of the loop
                            pass
                elif opcode[0] == "equal":
                    color = colors.get('black', (0, 0, 0))
                    for i in range(opcode[3], opcode[4]):
                        if bars is not None:
                            y = h * pos + (h - width) // 2 + width
                            pygame.draw.line(
                                screen, color_bar, (0, y), (int(bars[i] * maxw), y), width)
                        text = seq2[i]
                        text = font.render(text, True, color)
                        screen.blit(text, (10, h * pos))
                        pos += 1
                else:
                    for i in range(opcode[3], opcode[4]):
                        if bars is not None:
                            y = h * pos + (h - width) // 2 + width
                            pygame.draw.line(
                                screen, color_bar, (0, y), (int(bars[i] * maxw), y), width)
                        text = seq2[i]
                        if text in set_seq1:
                            color = colors.get('green', (0, 120, 0))
                            text = font.render(text, True, color)
                            screen.blit(text, (10, h * pos))
                            pos += 1
                        else:
                            color = colors.get("blue", (0, 120, 120))
                            text = font.render(text, True, color)
                            screen.blit(text, (10, h * pos))
                            pos += 1
        else:
            # animation
            positions = []
            opcodes = []
            for opcode in diff.get_opcodes():
                if opcode[0] in {'delete', 'equal', 'insert'}:
                    opcodes.append(opcode)
                elif opcode[0] == "replace":
                    opcodes.append(
                        ('delete', opcode[1], opcode[2], None, None))
                    opcodes.append(
                        ('insert', None, None, opcode[3], opcode[4]))
                else:
                    raise ValueError(f"unexpected: {opcode}")

            for opcode in opcodes:
                if opcode[0] == "delete":
                    for i in range(opcode[1], opcode[2]):
                        row = (seq1[i], i, seq2.index(seq1[i]) if seq1[i] in seq2 else None,
                               prev_bars[i] if prev_bars is not None else None)
                        positions.append(row)
                elif opcode[0] == "equal":
                    for i in range(opcode[3], opcode[4]):
                        row = (seq2[i], seq1.index(seq2[i]), i,
                               bars[i] if bars is not None else None)
                        positions.append(row)
                else:
                    for i in range(opcode[3], opcode[4]):
                        row = (seq2[i], seq1.index(seq2[i]) if seq2[i] in seq1 else None, i,
                               bars[i] if bars is not None else None)
                        positions.append(row)
            for text, p1, p2, bar_ in positions:
                if p1 is None:
                    # new
                    x = maxw * (1 - progress)
                    y = p2 * h
                    color = colors.get('blue', (0, 120, 120))
                elif p2 is None:
                    # deleted
                    x = maxw * progress
                    y = p1 * h
                    color = colors.get('green', (0, 120, 0))
                else:
                    # moved or equal
                    if p1 == p2:
                        x = 0.0
                        y = p1 * h
                    else:
                        x = math.sin(progress * math.pi) * maxw / 2 * \
                            abs(p2 - p1) / len(seq2)
                        y = (p1 + p2) * h / 2 - (p2 - p1) * \
                            h * math.cos(progress * math.pi) / 2
                    color = colors.get('black', (0, 0, 0))

                x = int(x)
                y = int(y)
                if bar_ is not None:
                    y2 = y + (h - width) // 2 + width
                    pygame.draw.line(screen, color_bar, (x, y2),
                                     (x + int(bar_ * maxw), y2), width)
                text = font.render(text, True, color)
                screen.blit(text, (x, y))

    else:
        color = colors.get('black', (0, 0, 0))
        for i in range(0, len(seq2)):
            text = seq2[i]
            text = font.render(text, True, color)
            screen.blit(text, (10, h * pos))
            pos += 1
