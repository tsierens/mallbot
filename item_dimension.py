import pandas as pd
from datetime import datetime
    
class ItemDimension(object):
    
    def __init__(self):
        column_names = ["item number", "name", "descid", "image", "use", "access", "autosell", "plural"]
        self.df = pd.read_csv(
            "items.txt",
            sep = "\t",
            skiprows = 1,
            skip_blank_lines = True,
            header = None,
            comment = "#",
            names = column_names
        ).drop_duplicates("item number")
        
        
    @staticmethod
    def datetime_to_unix(dt):
        return int((dt - datetime(1970,1, 1)).total_seconds())

    
    def get_item_name_by_id(self, item_id):
        df = self.df[self.df["item number"] == item_id]
        if len(df) == 1:
            return df.iloc[0]["name"]
        else:
            return "unknown"

    def get_item_id_by_name(self, name):
        df = self.df[self.df["name"] == name]
        if len(df) == 1:
            return df.iloc[0]["item number"]
        else:
            return "unknown"