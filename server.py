import json
import requests
from datetime import datetime
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")
from pydantic import BaseModel, Field
from typing import Union
from typing import Annotated
import xmltodict

__rapidapi_url__ = 'https://rapidapi.com/theapiguy/api/walk-score'

mcp = FastMCP('walk-score')

@mcp.tool()
def walk_score(lat: Annotated[str, Field(description='The latitude of the requested location.')],
               address: Annotated[str, Field(description='The URL encoded address.')],
               wsapikey: Annotated[Union[str, None], Field(description='Your Walk Score API Key. https://www.walkscore.com/professional/api-sign-up.php')],
               lon: Annotated[str, Field(description='The longitude of the requested location.')],
               format: Annotated[Union[str, None], Field(description='Type of result to return: (movie, series, episode)')] = None,
               bike: Annotated[Union[str, None], Field(description='Set bike=1 to request Bike Score (if available).')] = None,
               transit: Annotated[Union[str, None], Field(description='Set transit=1 to request Transit Score (if available).')] = None) -> dict: 
    '''Get Walk Score'''
    url = 'https://walk-score.p.rapidapi.com/score'
    headers = {'x-rapidapi-host': 'walk-score.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'address': address,
        'wsapikey': wsapikey if wsapikey is not None else 'e1d98b47417b46a654874a20b710bea2',
        'lon': lon,
        'format': format,
        'bike': bike,
        'transit': transit
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)

    data_dict = xmltodict.parse(response.text)

    # 如果你需要返回 JSON 字符串
    data_json = json.dumps(data_dict, indent=2, ensure_ascii=False)

    # 如果你只想返回字典格式
    return data_dict


if __name__ == "__main__":
    mcp.run(transport="stdio")