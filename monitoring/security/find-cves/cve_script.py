import argparse
import json
import logging
import os
import requests


def main():
    parser = argparse.ArgumentParser(description="Parse for URL, CVE and JWT token")

    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="URL to landscape deployment. (e.g., https://landscape.canonical.com)",
    )
    parser.add_argument(
        "--cve",
        type=str,
        required=True,
        help="CVE to find on computers",
    )
    parser.add_argument(
        "--jwt_token",
        type=str,
        required=True,
        help="Name of environment variable JWT token is in for landscape server",
    )

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    url = args.url
    cve_to_find = args.cve

    jwt_token = get_jwt_token(args.jwt_token)
    computer_ids = get_computer_ids(url, jwt_token)
    usns = get_usns(url, jwt_token, computer_ids)
    computers_with_cve = get_computers_with_cve(usns, cve_to_find)

    if len(computers_with_cve) != 0:
        logging.info(f"IDs of computers with {cve_to_find}: {computers_with_cve}")
        return

    logging.info(f"No computers with {cve_to_find}")


def get_jwt_token(env_variable: str) -> str:
    """
    retrieves the jwt token from an environment variable

    env_variable - the name of the environment variable containing jwt token
    """
    logging.info("Attempting to get jwt token from env")
    jwt_token = os.getenv(env_variable)
    if not jwt_token:
        logging.error("Invalid JWT token provided")
        raise ValueError("JWT token not found in environment variables")
    return jwt_token


def get_computer_ids(url: str, jwt_token: str) -> list[int]:
    """
    uses api of provided url to obtain computer ids of all computers in landscape

    url       - domain of landscape server
    jwt_token - jwt_token to use landscape api
    """
    logging.info("Attempting to get all computer ids")
    url = url + "/api/v2/computers"

    computers = request_get_helper(url, jwt_token)
    computer_ids = [res["id"] for res in computers["results"]]

    logging.info("Retrieved all computer ids")
    return computer_ids


def get_usns(url: str, jwt_token: str, ids: list[int]) -> dict:
    """
    retrieves all usns for every computer, along with package information
    to identify which computer has the obtained usns

    url       - domain of landscape server
    jwt_token - jwt_token to use landscape api
    ids       - list of all computer ids in landscape
    """
    logging.info("Attempting to obtain usns for all computers")
    url = url + "/api/v2/usns?computer_ids="

    ids_str = ",".join(map(str, ids))
    url = url + ids_str

    url = url + "&show_packages=true&limit=10000"

    usns = request_get_helper(url, jwt_token)
    usn_results = usns["results"]

    logging.info("Retrieved all usns")
    return usn_results


def get_computers_with_cve(usns: dict, cve: str) -> set:
    """
    finds which computers have the cve we are looking for within the usns

    usns - usns for all computers in landscape
    cve  - the cve we are looking for
    """
    computers = set()

    for usn in usns:
        cur_cves = usn["cves"]
        for cur_cve in cur_cves:
            if cur_cve["cve"] == cve:
                for package in usn["packages"]:
                    computers.update(package["computer_ids"])
    return computers


def request_get_helper(url: str, jwt_token: str):
    """
    helper for making get requests

    url       - url to make request to
    jwt_token - token for authorization
    """
    headers = {"Authorization": f"Bearer {jwt_token}"}
    retval = {}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            retval = response.json()
        else:
            logging.error(f"Received status code {response.status_code}")
            logging.error(response.text)

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")

    return retval


if __name__ == "__main__":
    main()
