import logging

from .geocode import GeocodeCityName
from .fetch_openmeteo import FetchWeatherForecast
from .fetch_jua import FetchJuaForecast
from .plot import WeatherPlot
from .to_text import WeatherToText
from .extract import ExtractWeatherVariable
from .load_grib2 import LoadGRIB2
from .heatmap import WeatherHeatmap
from .preview_grid import PreviewWeatherGrid
from .latlon_collector import LatLonCollector
from .grid_collector import GridCollector
from .set_api_key import SetOpenMeteoAPIKey, SetJuaAPIKey
from .preview_data import PreviewWeatherData
from .preview_grid_dual import PreviewWeatherGridDual

logger = logging.getLogger(__name__)

NODE_CLASSES = [
    GeocodeCityName,
    FetchWeatherForecast,
    FetchJuaForecast,
    WeatherPlot,
    WeatherToText,
    ExtractWeatherVariable,
    LoadGRIB2,
    WeatherHeatmap,
    PreviewWeatherGrid,
    PreviewWeatherGridDual,
    PreviewWeatherData,
    LatLonCollector,
    GridCollector,
    SetOpenMeteoAPIKey,
    SetJuaAPIKey,
]

try:
    from .load_weather_model import LoadWeatherModel

    NODE_CLASSES.append(LoadWeatherModel)
except Exception as exc:
    logger.warning("Weather optional node LoadWeatherModel unavailable: %s", exc)

try:
    from .predict_weather import PredictWeather

    NODE_CLASSES.append(PredictWeather)
except Exception as exc:
    logger.warning("Weather optional node PredictWeather unavailable: %s", exc)
