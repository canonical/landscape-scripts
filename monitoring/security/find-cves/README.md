# Find CVEs in Landscape
Simple script that finds a specified CVE within an estate in Landscape

## Requirements:
- JWT token is in an environment variable
  - ex. `export JWT_TOKEN_LANDSCAPE=<insert jwt token here>`
  - ***Note:*** If help is needed obtaining JWT token follow steps [here](https://ubuntu.com/landscape/docs/make-rest-api-requests)

## Example Usage:
`python3 cve_script.py --url 'https://landscape.canonical.com' --cve 'CVE-2024-47814' --jwt_token $JWT_TOKEN_LANDSCAPE`

From here you should see log info regarding what is going on. Script may take a while to run so pay attention to log info
