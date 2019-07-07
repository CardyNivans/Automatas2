def main():
    st = float (input("Introduce sueldo"))
    sf = float
    sf = 0
    if(st < 1000):
        sf = st*.15 + st
    elif(st > 1000):
        sf = st*.12 + st
    print ("El sueldo final es: ",sf)

if __name__ == "__main__":
    main()