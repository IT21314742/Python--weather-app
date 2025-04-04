import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70°F", self)
        self.emoji_label = QLabel(" ", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)   
        vbox.addWidget(self.temperature_label)   
        vbox.addWidget(self.emoji_label)   
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.initUI()

        def initUI(self):
            pass
    

        
        self.setStyleSheet("""
            QLabel, QPushButton{
            font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style:italic;
            }
            QlineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
             }

        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        
     def get_weather(self):
        
        api_key = "4313efec223625fa7c2f00619a717307"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city }&appid={api_key}"
        
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["cod"] == 200:
            self.display_weather(data)

    except requests.exceptions.HTTPError as http_error:
        match response.status_code:
            case 400:
                print("Bad request\nPlease check your input")
            case 401:
                print("Unauthorized\nInvalid API Key")
            case 403:
                print("Forbidden\nAccess is denied")
            case 404:
                print("Not Found\nCity not Found")
            case 500:
                print("Internal Server Error\nPlease try again later")
            case 502:
                print("Bad Gateway\nInvalid response from the server")
            case 503:
                print("Service Unavailable\nServer is down")
            case 504:
                print("Gateway Timeout\nNo responce from the server")
            case _:
                print(f"HTTP error occured\n{http_error}")
                
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.Timeout:
        pass
    except requests.exceptions.ConnectionError
                
    except requests.exceptions.RequestException:
        pass
    def display_error(self, message):
        pass

    def display_weather(self, data):
        print(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        