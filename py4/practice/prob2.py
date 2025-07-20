letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|> '''
print(letter.replace("<|Name|>", "Parth").replace("<|Date|>", "24 September"))