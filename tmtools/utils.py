#!/usr/bin/env python3
## INFO ##
## INFO ##


#------------------------------------------------------------------------------#
# HSBA Color Object
class hsba:

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, hue        : '0 .. 360',
                       saturation : '0.0 .. 1.0',
                       brightness : '0.0 .. 1.0',
                       alpha      : '0.0 .. 1.0' = 1.0):
        # Store static values
        self._hue = hue
        self._saturation = saturation
        self._brightness = brightness
        self._alpha = alpha

        # Convert and store RGBA values too
        self._to_rgba()


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def _to_rgba(self):
        # Get local references
        h = self._hue
        s = self._saturation
        b = self._brightness
        a = self._alpha

        i = h // 60
        f = h / 60.0 - i
        p = b * (1.0 - s)
        q = b * (1.0 - f * s)
        t = b * (1.0 - (1.0 - f) * s)

        if i == 0:
            rgb = b, t, p
        elif i == 1:
            rgb = q, b, p
        elif i == 2:
            rgb = p, b, t
        elif i == 3:
            rgb = p, q, b
        elif i == 4:
            rgb = t, p, b
        elif i == 5:
            rgb = b, p, q

        # Store converted values
        self._rgba = rgb + (a,)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def to_hex(self):
        # Convert to hexadecimal string representation
        alpha = '' if self._alpha >= 1.0 else f'{int(self._alpha*255):02X}'
        return '#{:02X}{:02X}{:02X}{a}'.format(
            *(int(c*255) for c in self._rgba[:3]), a=alpha)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def to_rgba(self):
        # Convert to CSS's rgba() string representation
        return 'rgba({}, {}, {}, {:.2f})'.format(*self._rgba)



#------------------------------------------------------------------------------#
# Generate section captions
def separator(*captions):
    for caption in captions:
        print('#{:-<78}#'.format(f'-- {caption.upper()} '))
