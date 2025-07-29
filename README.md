# Walk Score MCP Server

## Overview

The Walk Score MCP (Microservices Communication Protocol) server is a powerful tool that provides Walk Score, Transit Score, and Bike Score for any location. This service is designed to help developers integrate location-based scoring into their applications, enhancing property listings, enabling search and sort functionalities, and much more.

## Features

- **Walk Score**: Understand the walkability of a location.
- **Transit Score**: Evaluate the accessibility to public transport.
- **Bike Score**: Gauge the bike-friendliness of an area.

## Usage

### Tool List

The Walk Score MCP server provides the following tool:

- **Walk Score**
  - **Function Name**: `walk_score`
  - **Description**: Get Walk Score for a specific location.

### Tool Declarations

The `walk_score` function requires the following parameters:

- **lat**: The latitude of the requested location (String, Required).
- **lon**: The longitude of the requested location (String, Required).
- **address**: The URL encoded address (String, Required).
- **wsapikey**: Your Walk Score API Key (String, Required).
- **format**: The format of the results, either XML or JSON (String, Optional).
- **transit**: Set to 1 to request the Transit Score (String, Optional).
- **bike**: Set to 1 to request the Bike Score (String, Optional).

## Getting Started

To start using the Walk Score MCP server, ensure you have a valid API key. The server will return detailed information about the walkability, transit options, and bikeability of the specified location.

### Response

The server will provide a response containing:

- **Status**: Status code of the result.
- **Walk Score**: The Walk Score of the location.
- **Description**: A description of the Walk Score.
- **Updated**: The timestamp of when the Walk Score was calculated.
- **Logo URL**: A link to the Walk Score logo.
- **More Info Icon**: A link to an icon for additional information.
- **More Info Link**: A URL for more detailed information.
- **WS Link**: A link to the detailed Walk Score page for the point.
- **Help Link**: A link to the help page explaining how Walk Score works.
- **Snapped Lat/Lon**: The adjusted latitude and longitude for the point.
- **Transit and Bike Scores**: If requested, these scores will be included with descriptions.

## Error Handling

The Walk Score MCP server handles various HTTP response status codes to indicate success or specific errors, such as invalid input or exceeded quotas. Contact technical support for assistance with error resolution.

---

This README provides an overview of the Walk Score MCP server's capabilities and usage. For developers looking to incorporate location-based scoring into their applications, this server offers a robust and flexible solution.