# class DemoCenter(models.Model):
#     # server, hostname, ip adress, domain, username, password, console username, password,
#     server = models.CharField(max_length=100)
#     hostname = models.CharField(max_length=100)
#     ip_address = models.CharField(max_length=100)
#     domain = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     console_username = models.CharField(max_length=100)
#     console_password = models.CharField(max_length=100)


# class Project(models.Model):
#     title = models.CharField(max_length=100)
#     product = models.CharField(max_length=100)
#     information = models.CharField(max_length=100)
#     notes = models.TextField()
#     status = models.BooleanField(default=False)
#     customer = models.ForeignKey(Customer)
#     partner = models.ForeignKey(Partner)
#     vendor = models.ForeignKey(Vendor)
