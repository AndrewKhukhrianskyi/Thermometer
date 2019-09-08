 scale = [' ' for _ in range (8)]
def draw_gradus(scale):
        print("\n\t", "-----")
        print("\t", "|",scale[0], "| ",  ">300")
        print("\t", "|",scale[1], "| ",  "201-250")
        print("\t", "|",scale[2], "| ",  "151-200")
        print("\t", "|",scale[3], "| ",  "101-150")
        print("\t", "|",scale[4], "| ",  "51-100")
        print("\t", "|",scale[5], "| ",  "1-50")
        print("\t", "|",scale[6], "| ",  "0")
        print("\t", "|",scale[7], "| ",  ">-50")
        print("\n\t", "-----")

                
celsium = int(input(" Celsium: "))
farenheit = celsium*1.8+32
kelvin = celsium+273.15
print(" Farenheit: ", farenheit )
print(" Kelvin: ", round(kelvin,2))




def celsium_move(celsium,scale):
        if celsium<=-50:
                scale[7] = "C"
        elif celsium == 0:
                scale[6] = "C"
        elif celsium>0 and celsium<=50:
                scale[5] = "C"
        elif celsium>50 and celsium<=100:
                scale[4] = "C"
        elif celsium>100 and celsium<=150:
                scale[3] = "C"
        elif celsium>150 and celsium<=200:
                scale[2] = "C"
        elif celsium>200 and celsium<=250:
                scale[1] = "C"
        elif celsium>250:
                scale[0] = "C"

def farenheit_move(farenheit,scale):
        if farenheit<=-50:
                scale[7] = "F"
        elif farenheit == 0:
                scale[6] = "F"
        elif farenheit>0 and farenheit<=50:
                scale[5] = "F"
        elif farenheit>50 and farenheit<=100:
                scale[4] = "F"
        elif farenheit>100 and farenheit<=150:
                scale[3] = "F"
        elif farenheit>150 and farenheit<=200:
                scale[2] = "F"
        elif farenheit>200 and farenheit<=250:
                scale[1] = "F"
        elif farenheit>250:
                scale[0] = "F"

def kelvin_move(kelvin,scale):
        if kelvin<=-50:
                scale[7] = "K"
        elif kelvin == 0:
                scale[6] = "K"
        elif kelvin>0 and kelvin<=50:
                scale[5] = "K"
        elif kelvin>50 and kelvin<=100:
                scale[4] = "K"
        elif kelvin>100 and kelvin<=150:
                scale[3] = "K"
        elif kelvin>150 and kelvin<=200:
                scale[2] = "K"
        elif kelvin>200 and kelvin<=250:
                scale[1] = "K"
        elif kelvin>250:
                scale[0] = "K"

def main(celsium,farenheit,kelvin):
        celsium_move(celsium,scale)
        farenheit_move(farenheit,scale)
        kelvin_move(kelvin,scale)                
        draw_gradus(scale)

main(celsium,farenheit,kelvin)
