from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


Division_choice = (
    ('', "Select division"),
    ('Dhaka', 'Dhaka'),
    ('Rangpur', 'Rangpur'),
    ('Rajshahi', 'Rajshahi'),
    ('Khulna', 'Khulna'),
    ('Barishal', 'Barishal'),
    ('Barishal', 'Barishal'),
    ('Chattogram', 'Chattogram'),
    ('Mymensingh ', 'Mymensingh '),
    ('sylhet', 'sylhet'),
)


District_choice = (
    ('', 'Select District'),
    ('Dhaka', 'Dhaka'),
    ('Bogra', 'Bogra'),
    ('Sirajganj', 'Sirajganj'),
    ('Brahmanbaria', 'Brahmanbaria'),
    ('Tangail', 'Tangail'),
    ('Pabna', 'Pabna'),
    ('Noakhali', 'Noakhali'),
    ('Mymensingh', 'Mymensingh'),
    ('Rajshahi', 'Rajshahi'),
    ('Gazipur', 'Gazipur'),
    ('Barisal', 'Barisal'),
    ('Jessore', 'Jessore'),
    ('Satkhira', 'Satkhira'),
    ('Narayanganj', 'Narayanganj'),
    ('Bandarban', 'Bandarban'),
    ('Natore', 'Natore'),
    ('Faridpur', 'Faridpur'),
    ('Khulna', 'Khulna'),
    ('Rangpur', 'Rangpur'),
    ('Comilla', 'Comilla'),
    ('Dinajpur', 'Dinajpur'),
    ('Munshiganj', 'Munshiganj'),
    ('Feni', 'Feni'),
    ('Narsingdi', 'Narsingdi'),
    ('Rangamati ', 'Rangamati '),
    ('Noakhali  ', 'Noakhali'),
    ('Panchagarh', 'Panchagarh'),
    ('Bhola', 'Bhola'),
    ('Chandpur', 'Chandpur'),
    ('Habiganj', 'Habiganj'),
    ('Lakshmipur', 'Lakshmipur'),
    ('Barguna', 'Barguna'),
    ('Jhalokati', 'Jhalokati'),
    ('Pirojpur', 'Pirojpur'),
    ('Jhenaidah', 'Jhenaidah'),
    ('Narail', 'Narail'),
    ('Magura', 'Magura'),
    ('Lalmonirhat', 'Lalmonirhat'),
    ('Kurigram', 'Kurigram'),
    ('Gaibandha', 'Gaibandha'),
    ('Thakurgaon', 'Thakurgaon'),
    ('Sherpur', 'Sherpur'),
    ('Gopalganj', 'Gopalganj'),
    ("Cox's Bazar", "Cox's Bazar"),
    ("Sunamganj", "Sunamganj"),
    ("Naogaon", "Naogaon"),
    ("Natore", "Natore"),
    ("Joypurhat", "Joypurhat"),
)


class AddressBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    province = models.CharField(max_length=250, choices=Division_choice)
    city = models.CharField(max_length=250, choices=District_choice)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    area = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)


Category_choice = (
    ('Dresses', 'Dresses'),
    ("Mens", "Men's Dresses"),
    ("Women", "Women's Dresses"),
    ("Baby", "Baby's Dresses"),
    ('Shirts', 'Shirts'),
    ('Jeans', 'Jeans'),
    ('Sweater', 'Sweater'),
    ('Sleepwear', 'Sleepwear'),
    ('Blazers', 'Blazers'),
    ('Jackets', 'Jackets'),
    ('Shoes', 'Shoes'),
    ('Accerssories', 'Accerssories'),
    ('Bags', 'Bags'),
)

sizes_choice = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
)


class Product(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(
        max_length=250, choices=Category_choice, null=True, blank=True)
    brand = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='image', null=True, blank=True)
    sizes = models.CharField(
        max_length=250, choices=sizes_choice, null=True, blank=True)
    win_collection = models.BooleanField(default=False, null=True, blank=True)
    spring_collection = models.BooleanField(
        default=False, null=True, blank=True)
    trandy_products = models.BooleanField(default=False, null=True, blank=True)
    just_arrived = models.BooleanField(default=False, null=True, blank=True)
    fashionable_dress = models.BooleanField(default=False, null=True, blank=True)
    reasonable_price = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def Cart_amount(self):
        return self.quantity*self.product.discount_price


class OrderPlacedFormModel(models.Model):
    Choice_month = (
        ('(01) Jan', '(01) Jan'),
        ('(02) Feb', '(02) Feb'),
        ('(03) Mar', '(03) Mar'),
        ('(04) Apr', '(04) Apr'),
        ('(05) May', '(05) May'),
        ('(06) Jun', '(06) Jun'),
        ('(07) Jul', '(07) Jul'),
        ('(08) Aug', '(08) Aug'),
        ('(09) Sep', '(09) Sep'),
        ('(10) Oct', '(10) Oct'),
        ('(11) Nov', '(11) Nov'),
        ('(12) Dec', '(12) Dec'),
    )
    
    Choice_year = (
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),
        ('2032', '2032'),
        ('2033', '2033'),
        ('2034', '2034'),
        ('2035', '2035'),
        ('2036', '2036'),
        ('2037', '2037'),
        ('2038', '2038'),
        ('2039', '2039'),
        ('2040', '2040'),
        ('2041', '2041'),
        ('2042', '2042'),
        ('2043', '2043'),
        ('2044', '2044'),
        ('2045', '2045'),
        ('2046', '2046'),
        ('2047', '2047'),
        ('2048', '2048'),
        ('2049', '2049'),
        ('2050', '2050'),
        ('2051', '2051'),
        ('2052', '2052'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=250, default='Unknown')
    month = models.CharField(max_length=15, default='01', choices=Choice_month)
    year = models.CharField(max_length=15, default='2023', choices=Choice_year)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    cvv_code = models.CharField(max_length=4, default='00')
    billing_address = models.CharField(max_length=250, default='N/A')

    def __str__(self):
        return str(self.id)


Status_choice = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)


class OrderPlacement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    addressbook = models.ForeignKey(AddressBook, on_delete=models.CASCADE)
    payment_info = models.ForeignKey(OrderPlacedFormModel, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250, choices=Status_choice, default='Pending')

    def __str__(self):
        return str(self.id)
    
    
    @property
    def total_amount(self):
        return self.quantity*self.product.discounted_price


class FAQ(models.Model):
    question_title = models.CharField(max_length=100, blank=True, null=True)
    question_description = models.CharField(
        max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.id)


Select_topic_choice = (
    ('Customer Service', 'Customer Service'),
    ('Online Orders', 'Online Orders'),
    ('My Rewards', 'My Rewards'),
    ('Club Taaga', 'Club Taaga'),
    ('Corporate Enquiry', 'Corporate Enquiry'),
    ('Partership opportunities', 'Partership opportunities'),
    ('General', 'General'),
)


class Help(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    select_topic = models.CharField(
        max_length=250, choices=Select_topic_choice)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    messages = models.TextField()

    def __str__(self):
        return str(self.id)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    your_rating = models.PositiveSmallIntegerField(unique=True, null=True)
    your_review = models.TextField()
    your_name = models.CharField(max_length=250)
    your_email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Subscribe(models.Model):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email


class NewsletterModel(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)
