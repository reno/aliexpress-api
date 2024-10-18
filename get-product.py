from aliexpress_api_client import AliExpress

parser = ArgumentParser() 
parser.add_argument('productId', type = str, help = 'Product id')

aliexpress = AliExpress(process.env.API_KEY, process.env.AFFILIATE_ID)

product = aliexpress.get_product_details(['productId', 'productTitle', 'salePrice', 'productUrl', 'imageUrl', 'allImageUrls'], product_id)
print(product)