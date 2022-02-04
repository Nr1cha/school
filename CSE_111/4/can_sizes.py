import math




def main ():
    Name_list = ["#1 Picnic","#1 Tall","#2","#2.5","#3 Cylinder","#5","#6Z","#8Z short","#10","#211","#300","#303",]
    Radius_list = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10,]
    Height_list = [10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11,]
    Cost_per_can_list = [0,28,0.43,0.45,0.61,0.86,0.83,0.22,0.26,1.53,0.34,0.38,0.42,]

    for i, val in enumerate(Name_list):
        Volume = compute_volume(Radius_list[i], Height_list[i])
        surface_area = compute_surface_area(Radius_list[i], Height_list[i])
        storage_efficiency = compute_storage_efficiency(Volume, surface_area)
        print(f"{val} {storage_efficiency:.1f}")


    return    

def compute_volume (radius, height): # FUNCTION DONE

    volume = math.pi * radius**2 * height

    return volume

def compute_surface_area (radius, height): # FUNCTION DONE

    surface_area = 2 * math.pi * radius * (radius + height)

    return surface_area

def compute_storage_efficiency (volume, surface_area): # FUNCTION DONE

    storage_efficiency = volume / surface_area

    return storage_efficiency

main()
