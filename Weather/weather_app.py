while True:
    import requests

    api_key = '30d4741c779ba94c470ca1f63045390a'

    user_input = input("Masukkan Nama Kota : ")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("Eror Kota Tidak Ditemukan")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp_fahrenheit = round(weather_data.json()['main']['temp'])
        
        # Konversi suhu dari Fahrenheit ke Celsius
        temp_celsius = round((temp_fahrenheit - 32) * 5/9)

        print(f"Cuaca Di {user_input} Adalah: {weather}")
        print(f"Suhu Di {user_input} Adalah: {temp_fahrenheit}ºF")
        print(f"Suhu Di {user_input} Adalah: {temp_celsius}ºC")
        
    back =input("Ingin Mencari Lagi (yes/no) :").strip().lower()
    if back != 'yes':
        print ("TERIMA KASIH :3")
        break