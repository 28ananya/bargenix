## Created a flask application
1. We created a mock_db a dictonary which stores all the coupons and log_requests. Log requests are called before any api call and it stores all the entries like data,http method(post ,get), timestamp and end point.
## clone the project
it runs on the local host http://127.0.0.1:5000
base_url = "http://127.0.0.1:5000"
## It has 3 end points
Use any application like postman to run
The end points are:-
## 1. http://127.0.0.1:5000/generate_coupon 
It is a post api. i.e the user has to give product_id: from body
it returns a coupon,product_id and expiration date(which is 7 days from current date)
## 2. http://127.0.0.1:5000/validate_coupon
It is also post api. i,e the user has to give product_id and coupoun from the body
It returns if coupon is valid or expired or invalid.
## 3. http://127.0.0.1:5000/mock_db
It is a get api. i.e it doesnot take anything from body but returns all the coupons and request logs from the mock db.
