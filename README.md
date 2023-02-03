## Weather module for polybar

This is a python3 script that queries [OpenWeatherApi](https://openweathermap.org) to fetch the current weather data. 
The temp is in metric.

You'll have to set your **[API_KEY](https://openweathermap.org/api)** and **CITY** in the `$HOME/.config/polybar/data/cred.json`

Clone this repo in `$HOME/.config/polybar/modules/weather/`

```
- SSH: git clone git@github.com:SushiJ/polybar-weather-module.git 
- HTTPS: git clone https://github.com/SushiJ/polybar-weather-module.git
```

The follow snippet shows an example for integrating this script with polybar.

```ini
[module/weather]
type = custom/script

exec = "python3 $HOME/.config/polybar/modules/weather/app.py"
; Call every 15 minutes
interval = 900

format = <label>
format-prefix-foreground = ${colors.foreground}

label = %output:0:50%
```
follow [polybar](https://github.com/polybar/polybar/wiki/Module:-script) for more info on running custom scripts
