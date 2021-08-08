def paint_calc(height,width,cover):
    number_of_cans=round((height*width) / cover)
    area = number_of_cans*5
    print(f"{number_of_cans} cans will cover {area} square meter")



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
