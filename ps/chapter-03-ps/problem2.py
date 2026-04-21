letter = '''Dear <|name|>,
        You are selected!
          <|Date|>'''


print(letter.replace("<|name|>","Aminur").replace("<|Date|>", "18 April 2026"))