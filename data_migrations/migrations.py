import pymongo
import pandas as pd
from collections import OrderedDict

# Importacion de ddbb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.db_sistems_2
pd.options.display.max_columns=None
pd.options.display.max_rows=None



def data_categoires_description():
	category = db.inv_categoria
	category_data = pd.DataFrame(category.find())
	description = category_data.columns
	return print(description)


category = db.inv_categoria
category_data = pd.DataFrame(category.find())
description = category_data.columns

print(description.iloc[:1])






def data_categoires_description(*args):
	category = db.inv_subcategoria
	category_data = pd.DataFrame(category.find())
	print(category_data)
	description = category_data.loc[:, args]
	return description


def data_categoires_description():
	category = db.inv_marca
	category_data = pd.DataFrame(category.find())
	return category_data



def data_categoires_description():
	category = db.inv_unidadmedida
	category_data = pd.DataFrame(category.find())
	return category_data




def data_categoires_description():
	category = db.inv_producto
	category_data = pd.DataFrame(category.find())
	return category_data



