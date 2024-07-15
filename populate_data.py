import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_api.settings')

django.setup()

from banks.models import Bank, Branch

def populate():
    bank1 = Bank.objects.create(name='State Bank of India', address='Mumbai, Maharashtra, India')
    bank2 = Bank.objects.create(name='HDFC Bank', address='Mumbai, Maharashtra, India')
    bank3 = Bank.objects.create(name='ICICI Bank', address='Mumbai, Maharashtra, India')
    bank4 = Bank.objects.create(name='Axis Bank', address='Mumbai, Maharashtra, India')

    Branch.objects.create(bank=bank1, name='Main Branch', ifsc_code='SBIN0000001', address='Mumbai, Maharashtra, India')
    Branch.objects.create(bank=bank1, name='Connaught Place Branch', ifsc_code='SBIN0000002', address='Connaught Place, New Delhi, India')
    Branch.objects.create(bank=bank2, name='Main Branch', ifsc_code='HDFC0000001', address='Mumbai, Maharashtra, India')
    Branch.objects.create(bank=bank2, name='Koramangala Branch', ifsc_code='HDFC0000002', address='Koramangala, Bengaluru, India')
    Branch.objects.create(bank=bank3, name='Main Branch', ifsc_code='ICIC0000001', address='Mumbai, Maharashtra, India')
    Branch.objects.create(bank=bank3, name='Nungambakkam Branch', ifsc_code='ICIC0000002', address='Nungambakkam, Chennai, India')
    Branch.objects.create(bank=bank4, name='Main Branch', ifsc_code='UTIB0000001', address='Mumbai, Maharashtra, India')
    Branch.objects.create(bank=bank4, name='Salt Lake Branch', ifsc_code='UTIB0000002', address='Salt Lake, Kolkata, India')

    print("Database populated with initial data.")

if __name__ == '__main__':
    populate()
