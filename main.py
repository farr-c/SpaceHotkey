import keyboard
keyboard.add_hotkey('alt', lambda: keyboard.write(' ')) 
keyboard.add_abbreviation('silly', 'im flippn silly')
keyboard.wait()