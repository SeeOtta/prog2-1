print("""<svg version="1.1"
    baseProfile="full"
    width="300" height="200"
    xmlns="http://www.w3.org/2000/svg">""")
for i in [0,1,2,3,4,5,6,7,8,9,10] :
    print(f"""
    <circle cx="{i}" cy="{i}" r="80" fill="green" />""")
    
print("</svg>")