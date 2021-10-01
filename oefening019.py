print("""<svg version="1.1"
    baseProfile="full"
    width="300" height="200"
    xmlns="http://www.w3.org/2000/svg">""")
for i in range (0,100):
    for j in range (0,100):
      print(f"""
    <circle cx="{i}" cy="{j}" r="80" fill="green" />""")
    
print("</svg>")