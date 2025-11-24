from .kilbel import KilbelExtractor


EXTRATORS = {
    "Kilbel": KilbelExtractor
}


def get_extractor(site_name):
    return EXTRATORS[site_name]()