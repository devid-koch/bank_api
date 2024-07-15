from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Bank, Branch

class BankAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.bank1 = Bank.objects.create(name='State Bank of India', address='Mumbai, Maharashtra, India')
        self.bank2 = Bank.objects.create(name='HDFC Bank', address='Mumbai, Maharashtra, India')

        self.branch1 = Branch.objects.create(bank=self.bank1, name='Main Branch', ifsc_code='SBIN0000001', address='Mumbai, Maharashtra, India')
        self.branch2 = Branch.objects.create(bank=self.bank1, name='Connaught Place Branch', ifsc_code='SBIN0000002', address='Connaught Place, New Delhi, India')
        self.branch3 = Branch.objects.create(bank=self.bank2, name='Main Branch', ifsc_code='HDFC0000001', address='Mumbai, Maharashtra, India')
        self.branch4 = Branch.objects.create(bank=self.bank2, name='Koramangala Branch', ifsc_code='HDFC0000002', address='Koramangala, Bengaluru, India')

    def test_get_bank_list(self):
        response = self.client.get('/api/banks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'State Bank of India')
        self.assertEqual(response.data[1]['name'], 'HDFC Bank')

    def test_get_branch_details(self):
        response = self.client.get(f'/api/branches/{self.branch1.ifsc_code}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Main Branch')
        self.assertEqual(response.data['ifsc_code'], 'SBIN0000001')

        response = self.client.get(f'/api/branches/{self.branch2.ifsc_code}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Connaught Place Branch')
        self.assertEqual(response.data['ifsc_code'], 'SBIN0000002')

    def test_get_branch_details_invalid_ifsc(self):
        response = self.client.get('/api/branches/INVALID_IFSC/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
