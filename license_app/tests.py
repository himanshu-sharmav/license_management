from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import License, LicenseRevocation

class LicenseManagementTest(TestCase):
    
    def setUp(self):
        # Create a regular user and an admin user
        self.user = User.objects.create_user(username='regular_user', password='password123')
        self.admin = User.objects.create_superuser(username='admin_user', password='adminpass123')

    def test_user_registration(self):
         # Test user registration process
         response = self.client.post(reverse('register'), {
             'username': 'new_user',
             'password1': 'testpass123',
             'password2': 'testpass123',  # Include password confirmation
         })

         # Check if the registration redirects after success
         self.assertEqual(response.status_code, 200)  # Expecting redirect to create_license



    def test_create_license_view(self):
        # Test creating a license by a logged-in user
        self.client.login(username='regular_user', password='password123')
        response = self.client.post(reverse('create_license'), {
            'license_key': '1234-5678-9101-1121'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to view_licenses
        self.assertTrue(License.objects.filter(owner=self.user).exists())  # Check license exists

    def test_license_list_view(self):
        # Test viewing licenses for a logged-in user
        self.client.login(username='regular_user', password='password123')
        License.objects.create(license_key='1234-5678', owner=self.user)
        response = self.client.get(reverse('view_licenses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1234-5678')

    def test_license_revocation_by_admin(self):
        # Test revoking a license by an admin user
        license = License.objects.create(license_key='1234-5678', owner=self.user)
        self.client.login(username='admin_user', password='adminpass123')
        response = self.client.post(reverse('revoke_license', args=[license.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to view_licenses
        license.refresh_from_db()
        self.assertFalse(license.is_active)  # License should now be inactive

    def test_unauthorized_license_revocation(self):
        # Test revoking a license by a regular (non-admin) user
        license = License.objects.create(license_key='1234-5678', owner=self.user)
        self.client.login(username='regular_user', password='password123')
        response = self.client.post(reverse('revoke_license', args=[license.id]))
        self.assertEqual(response.status_code, 403)  # Should return Forbidden

    
