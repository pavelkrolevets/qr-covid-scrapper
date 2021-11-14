from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"qr код ковид, ковид кодб сертификат о вакцинации","limit":10000,"print_urls":True, "chromedriver": "/Users/pavelkrolevets/Downloads/chromedriver"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
# print(paths)   #printing absolute paths of the downloaded images
