def get_label(label):
    class_dict = {
        "0": "Bacteriosis Vascular",
        "1": "Raya Parda",
        "2": "Ácaro Verde",
        "3": "Mosaico Común",
        "4": "Planta Sana"
    }
    return class_dict[str(label)]
