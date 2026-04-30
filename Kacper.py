import time

time_to_explode = 10

print("\nOh god!!! There is a bomb! We must escape! Aaaaaaaaaaaaaa!!!!")

while time_to_explode > 0:
    time.sleep(1)
    time_to_explode-=1
    print(time_to_explode)
else:
    print("Ka BOOM!")
    time.sleep(2)
    print("""
     _ ._  _ , _ ._
    (_ ' ( `  )_  .__)
  ( (  (    )   `)  ) _)
 (__ (_   (_ . _) _) ,__)
     `~~`\ ' . /`~~`
          |   |
          |   |
          |   |
          /   |
""")