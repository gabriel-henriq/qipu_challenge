import json
import requests
from bs4 import BeautifulSoup
from test_list import icao_tests

"""
Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...) e imprima na tela:
As cartas disponíveis
Os horários de nascer e pôr do sol de hoje
A informação de TAF e METAR disponíveis
Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING. 
"""


def test_icaos() -> None:

    for test in icao_tests:
        url = f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={test}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        data = dict()

        try:
            validate(doc)
            data["sunrise_sunset"] = get_sunrise_sunset(doc)
            data["metar"] = get_metar(doc)
            data["taf"] = get_taf(doc)
            data["cards"] = get_cards(doc)
            with open(f"{test}.json", "w") as file:
                json.dump(data, file, indent=2)
                print(f"{test} salvo com sucesso.")
        except Exception as e:
            print(f"{e}: {test}")


def validate(doc: BeautifulSoup) -> None:
    bad_request = doc.find(text="We're sorry - An Error Occurred")
    not_found = doc.find(class_="alert alert-danger")
    if bad_request:
        raise Exception("\nO aeródromo não foi encontrado.")
    elif not_found:
        if not_found.text.strip() == "O aeródromo não foi encontrado.":
            raise Exception("\nO aeródromo não foi encontrado.")


def get_cards(doc: BeautifulSoup) -> dict:

    cards = doc.find("hr", id="cartas").find_next_siblings("h4")
    cards_len = len(cards)
    if cards_len > 3:
        cards = doc.find("hr", id="cartas").find_next_siblings("h4")[2:-1]
    else:
        return
    cards_list = []
    cards_text = []
    urls = []
    links = []

    for card in cards:
        ul = card.find_next_sibling("ul")
        url_list = []
        link_list = []
        for li in ul.find_all("li"):
            for link in li.find_all("a"):
                link_list.append(link.text.strip())
                url_list.append(link["href"].strip())
        urls.append(url_list)
        links.append(link_list)

    for i in range(len(cards)):
        cards_list.append(dict(zip(links[i], urls[i])))
        cards_text.append(cards[i].text.strip())

    return dict(zip(cards_text, cards_list))


def get_sunrise_sunset(doc: BeautifulSoup) -> dict:

    sunrise = doc.find("sunrise")
    sunset = doc.find("sunset")
    if sunrise and sunset:
        sunrise_sunset = {
            "sunrise": doc.find("sunrise").text.strip(),
            "sunset": doc.find("sunset").text.strip(),
        }
        return sunrise_sunset
    else:
        return


def get_metar(doc: BeautifulSoup) -> str:

    metar_header = doc.find("h5", class_="mb-0 heading-primary", text="METAR")
    if metar_header:
        metar = metar_header.find_next_siblings("p")
        if len(metar) == 2:
            metar = metar[1].text.strip()
        else:
            metar = metar_header.find_next_sibling("p").text.strip()

        return metar
    else:
        return


def get_taf(doc: BeautifulSoup) -> str:

    taf = doc.find("h5", class_="mb-0 heading-primary", text="TAF")
    if taf:
        return taf.find_next_sibling("p").text.strip()
    else:
        return


def print_data(data: dict) -> None:
    print(f"\nNascer do Sol: {data['sunrise_sunset']['sunrise']}\n")
    print(f"Por do Sol: {data['sunrise_sunset']['sunset']}\n")
    print(f"METAR: {data['metar']}\n")
    print(f"TAF: {data['taf']}\n")
    print("Cartas: ")
    if isinstance(data["cards"], dict):
        for card in data["cards"]:
            print(f"\t{card}:")
            for link in data["cards"][card]:
                print(f"\t\t{link}: {data['cards'][card][link]}")


if __name__ == "__main__":

    test_mode = False

    if test_mode:
        test_icaos()
    else:
        while True:
            icao = str(input("\nDigite um ICAO: "))
            url = f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={icao}"
            page = requests.get(url).text
            doc = BeautifulSoup(page, "html.parser")
            data = dict()

            try:
                validate(doc)
                data["sunrise_sunset"] = get_sunrise_sunset(doc)
                data["metar"] = get_metar(doc)
                data["taf"] = get_taf(doc)
                data["cards"] = get_cards(doc)
                print_data(data)
            except Exception as e:
                print(e)
