#convert distant given in feet and inches into meter and centimeter

feet=float(input("Enter the feet :"))
inch=float(input("Enter the inch :"))
meter=(feet*0.3048)+(inch*0.0254)
centimeter=meter*100

print(f"meter is {meter} centimeter is {centimeter}")