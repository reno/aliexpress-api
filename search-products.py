from aliexpress_api_client import AliExpress
from argparse import ArgumentParser

parser = ArgumentParser() 
parser.add_argument('query', type = str, help = 'Termo de busca')

aliexpress = AliExpress(
    app_key = process.env.YOUR_APP_KEY,
    app_secret = process.env.YOUR_APP_SECRET,
    redirect_uri = process.env.YOUR_REDIRECT_URI  # if applicable for OAuth2
)

def search_products(keyword, page=1, page_size=10):
    params = {
        'q': keyword,        
        'page': page,       
        'page_size': page_size,  
        # Add additional filters like price range, category, etc. if needed
    }
    response = aliexpress.get_product_list(params)
    
    if response.get('status') == 'success':
        return response.get('products')
    else:
        print("Error:", response.get('error_msg'))
        return None
    
args = parser.parse_args()

products = search_products(args.query)

# Print product details
if products:
    for product in products:
        print(f"Product: {product['product_title']}, Price: {product['price']}")
