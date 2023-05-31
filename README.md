"# online_marketplace" 

# Install all [requirements.txt] on your environment

# import _postman collection_

# Create Seller and Buyer Account
 Example:
  # POST `http://127.0.0.1:8000/backend/register`
    {
        "username":"Tagline",
        "email":"info@taglineinfotech.com",
        "password":"Tagline@123"
    }

# Login account
 Example:
  # POST `http://127.0.0.1:8000/backend/login`
    {
        "email":"info@taglineinfotech.com",
        "password":"Tagline@123"
    }
    or
    {
        "username":"Tagline",
        "password":"Tagline@123"
    }

# LogOut account
 Example:
  # POST `http://127.0.0.1:8000/backend/logout`

# Product
 `Add Product`
  Example:
  # POST `http://127.0.0.1:8000/backend/product/`
    {
        "name":"boAt Stone 352",
        "discription":"boAt Stone 352 Bluetooth Speaker with 10W RMS Stereo Sound, IPX7 Water Resistance, TWS Feature, Up to 12H  Total Playtime, Multi-Compatibility Modes and Type-C Charging(Raging Black)",
        "price":"1699",
        "image_url":"https://m.media-amazon.com/images/I/61K8FS335JL._SX522_.jpg",
        "seller_user":1
    }

 `Get all data`
   # GET `http://127.0.0.1:8000/backend/product/`  
 `Get for Seller data`
   # GET `http://127.0.0.1:8000/backend/product/?seller_user=<seller_id>`  

# Purchase
  `Purchase Product`
  Example:
  # POST `http://127.0.0.1:8000/backend/purchase/`
    {
        "tracking":1,
        "product_name":1,
        "purches_price":"1690",
        "seller_user":1,
        "buyer_user":2
    }

 `Get all Purchase`
   # GET `http://127.0.0.1:8000/backend/purchase/`  

 `Get for Seller data`
   # GET `http://127.0.0.1:8000/backend/purchase/?seller_user=<seller_id>` 

 `Get for Buyer data`
   # GET `http://127.0.0.1:8000/backend/purchase/?buyer_user=<buyer_id>`    
